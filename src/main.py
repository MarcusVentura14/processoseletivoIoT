print('Teste', flush=True)
import machine
import time
import network
import ntptime
import ssd1306
from umqtt.simple import MQTTClient

print("Inicializando Sistema...")

# ------- Configurações de Rede e Nuvem -------

WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""
MQTT_CLIENT_ID = "pnaat-marcus-esp32"
MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_PUBLISH_TOPIC_ALERTA = "pnaat/industrial/marcus/alerta"


# ------- Configuração de Pinos, Sensor, Atuador e Display -------

PIN_TRIG, PIN_ECHO = 5, 18
PIN_SDA, PIN_SCL = 21, 22
PIN_BUZZER, PIN_BTN = 13, 12

trig = machine.Pin(PIN_TRIG, machine.Pin.OUT)
echo = machine.Pin(PIN_ECHO, machine.Pin.IN)
i2c = machine.SoftI2C(sda=machine.Pin(PIN_SDA), scl=machine.Pin(PIN_SCL))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
buzzer = machine.PWM(machine.Pin(PIN_BUZZER), duty=0)
btn = machine.Pin(PIN_BTN, machine.Pin.IN, machine.Pin.PULL_UP)


# ------- Variáveis de Estado e Temporização -------

STATE_SAFE = 0
STATE_PROXIMITY = 1
STATE_COLLISION = 2
current_state = STATE_SAFE

last_sensor_read = 0
last_buzzer_toggle = 0
buzzer_active = False
sirene_high = True
alarme_silenciado = False
distancia_atual = 400.0
mqtt_client = None

contador_colisoes = 0
historico_colisoes = []


# ------- Lógica do Botão (Interrupção) -------

def btn_isr(pin):
    global alarme_silenciado
    if current_state == STATE_COLLISION:
        alarme_silenciado = True
        buzzer.duty(0)

btn.irq(trigger=machine.Pin.IRQ_FALLING, handler=btn_isr)


# ------- Funções de Conectividade -------

def display_boot_msg(linha1, linha2=""):
    oled.fill(0)
    oled.text("INICIANDO...", 16, 0)
    oled.text(linha1, 0, 25)
    oled.text(linha2, 0, 40)
    oled.show()

def setup_conexoes():
    global mqtt_client
    display_boot_msg("Conectando WiFi")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
    
    # Adicionamos um "Timeout" de 10 segundos (20 tentativas de 0.5s)
    tentativas = 0
    while not sta_if.isconnected() and tentativas < 20:
        time.sleep(0.5)
        tentativas += 1
        
    # Se conectou, segue a vida. Se não conectou, os blocos 'try/except' 
    # abaixo vão proteger o código de quebrar, e ele continuará rodando.
        
    display_boot_msg("WiFi OK!", "Ajustando Hora")
    try:
        ntptime.settime()
    except Exception as e:
        pass
        
    display_boot_msg("Conectando MQTT")
    try:
        mqtt_client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
        mqtt_client.connect()
        display_boot_msg("MQTT OK!", "Sistema Pronto")
        time.sleep(1)
    except Exception as e:
        display_boot_msg("Erro MQTT", str(e))
        time.sleep(2)
        
    

def formatar_data_hora():
    t_local = time.localtime(time.time() - 10800) 
    data = "{:02d}/{:02d}/{:04d}".format(t_local[2], t_local[1], t_local[0])
    hora = "{:02d}:{:02d}:{:02d}".format(t_local[3], t_local[4], t_local[5])
    return data, hora


# ------- Funções do Sistema ------- 

def ler_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    pulso = machine.time_pulse_us(echo, 1, 30000)
    return 400.0 if pulso < 0 else (pulso * 0.0343) / 2

def atualizar_oled(dist, estado):
    oled.fill(0)
    oled.text("SENSOR DE RE", 16, 0)
    oled.text("Dist: {:.1f} cm".format(dist), 0, 25)
    
    if estado == STATE_SAFE:
        oled.text("STATUS: SEGURO", 0, 50)
    elif estado == STATE_PROXIMITY:
        oled.text("STATUS: ATENCAO", 0, 50)
    elif estado == STATE_COLLISION:
        msg = "SILENCIADO" if alarme_silenciado else "COLISAO!"
        oled.text("STATUS: " + msg, 0, 50)
        
    oled.show()


# ------- Lógica Principal -------

def main():
    global current_state, alarme_silenciado, distancia_atual, contador_colisoes, historico_colisoes
    global last_sensor_read, last_buzzer_toggle, buzzer_active, sirene_high
    
    setup_conexoes()

    print('Teste')
    
    while True:
        agora = time.ticks_ms()
        
        # Leitura do Sensor
        if time.ticks_diff(agora, last_sensor_read) >= 60:
            distancia_atual = ler_distancia()
            last_sensor_read = agora
            
            novo_estado = current_state
            
            if distancia_atual <= 2.2: 
                novo_estado = STATE_COLLISION
            elif distancia_atual <= 200.0:
                novo_estado = STATE_PROXIMITY
            else:
                novo_estado = STATE_SAFE
                
            # Trata a mudança de estado
            if novo_estado != current_state:
                
                # Integração MQTT com histórico e NTP forçado
                if novo_estado == STATE_COLLISION and mqtt_client is not None:

                    # Força a atualização do relógio com o mundo real na hora da batida
                    try:
                        ntptime.settime()
                    except:
                        pass
                        
                    contador_colisoes += 1
                    data, hora = formatar_data_hora()
                    
                    # Monta a string desta batida específica
                    nova_batida = "Registro de Incidente #{}: Colisão detectada às {} do dia {}".format(contador_colisoes, hora, data)
                    
                    # Adiciona à lista de memória
                    historico_colisoes.append(nova_batida)
                    
                    # Limita a memória a 10 itens para não estourar a RAM do ESP32 e a tela do app
                    if len(historico_colisoes) > 10:
                        historico_colisoes.pop(0)

                    # Junta todas as batidas com uma quebra de linha (\n)    
                    payload_final = "\n".join(historico_colisoes)
                    
                    print(">> ENVIANDO NUVEM:")
                    print(payload_final)
                    try:
                        # Envia o pacote de texto contendo todas as linhas
                        mqtt_client.publish(MQTT_PUBLISH_TOPIC_ALERTA, payload_final.encode())
                    except Exception as e:
                        print("Erro ao enviar MQTT:", e)
                
                current_state = novo_estado
                buzzer.duty(0)
                buzzer_active = False
                last_buzzer_toggle = agora
                
                if current_state != STATE_COLLISION:
                    alarme_silenciado = False
            
            atualizar_oled(distancia_atual, current_state)

        
        # Motor de Áudio
        if current_state == STATE_SAFE or alarme_silenciado:
            buzzer.duty(0)
            
        elif current_state == STATE_PROXIMITY:
            if distancia_atual <= 30.0:
                # Zona Crítica (30cm a 2.2cm): Som contínuo de alerta 
                if not buzzer_active or time.ticks_diff(agora, last_buzzer_toggle) >= 50:
                    buzzer.freq(1000)
                    buzzer.duty(512)
                    buzzer_active = True
                    last_buzzer_toggle = agora
            else:
                # Mapeamento baseado em especificações comerciais reais
                if distancia_atual >= 80.0:
                    # 80cm a 200cm: Mapeia de 1500ms a 2000ms (Afastado)
                    intervalo_silencio = int(1500 + ((distancia_atual - 80) / 120.0) * 500)
                elif distancia_atual >= 50.0:
                    # 50cm a 80cm: Mapeia de 1200ms a 1500ms (Transição intermediária)
                    intervalo_silencio = int(1200 + ((distancia_atual - 50) / 30.0) * 300)
                else:
                    # 30cm a 50cm: Mapeia de 300ms a 1200ms (Aproximação rápida)
                    intervalo_silencio = int(300 + ((distancia_atual - 30) / 20.0) * 900)
                    
                duracao_bip = 60 
                
                if not buzzer_active:
                    if time.ticks_diff(agora, last_buzzer_toggle) >= intervalo_silencio:
                        buzzer.freq(1000)
                        buzzer.duty(512)
                        buzzer_active = True
                        last_buzzer_toggle = agora
                else:
                    if time.ticks_diff(agora, last_buzzer_toggle) >= duracao_bip:
                        buzzer.duty(0)
                        buzzer_active = False
                        last_buzzer_toggle = agora
                    
        elif current_state == STATE_COLLISION:
            # Zona de Impacto (< 2.2cm): Sirene de duas frequências
            if time.ticks_diff(agora, last_buzzer_toggle) >= 100:
                sirene_high = not sirene_high
                last_buzzer_toggle = agora
                buzzer.freq(1200 if sirene_high else 800)
                buzzer.duty(512)
        
        time.sleep_ms(2)

if __name__ == "__main__":
    main()