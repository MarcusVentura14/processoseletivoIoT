import machine
import time
import ssd1306

# ==========================================
# Configuração de Pinos e Objetos
# ==========================================
PIN_TRIG, PIN_ECHO = 5, 18
PIN_SDA, PIN_SCL = 21, 22
PIN_BUZZER, PIN_BTN = 13, 12

trig = machine.Pin(PIN_TRIG, machine.Pin.OUT)
echo = machine.Pin(PIN_ECHO, machine.Pin.IN)
i2c = machine.SoftI2C(sda=machine.Pin(PIN_SDA), scl=machine.Pin(PIN_SCL))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
buzzer = machine.PWM(machine.Pin(PIN_BUZZER), duty=0)
btn = machine.Pin(PIN_BTN, machine.Pin.IN, machine.Pin.PULL_UP)

# ==========================================
# Variáveis de Estado e Temporização
# ==========================================
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

# ==========================================
# Lógica do Botão (Interrupção)
# ==========================================
def btn_isr(pin):
    global alarme_silenciado
    # Só silencia se estiver de fato no estado de colisão
    if current_state == STATE_COLLISION:
        alarme_silenciado = True
        buzzer.duty(0) # Corta o som imediatamente

btn.irq(trigger=machine.Pin.IRQ_FALLING, handler=btn_isr)

# ==========================================
# Funções do Sistema
# ==========================================
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

# ==========================================
# Fluxo Principal
# ==========================================
def main():
    global current_state, alarme_silenciado, distancia_atual
    global last_sensor_read, last_buzzer_toggle, buzzer_active, sirene_high
    
    while True:
        agora = time.ticks_ms()
        
        # 1. Leitura do Sensor
        if time.ticks_diff(agora, last_sensor_read) >= 60:
            distancia_atual = ler_distancia()
            last_sensor_read = agora
            
            # Análise do Novo Estado
            novo_estado = current_state
            
            # Margem de 2.2cm absorve o erro de float do simulador garantindo o acionamento em 2cm
            if distancia_atual <= 2.2: 
                novo_estado = STATE_COLLISION
            elif distancia_atual <= 100.0:
                novo_estado = STATE_PROXIMITY
            else:
                novo_estado = STATE_SAFE
                
            # Se o estado mudou, reseta as variáveis sonoras para transição limpa
            if novo_estado != current_state:
                current_state = novo_estado
                buzzer.duty(0)
                buzzer_active = False
                last_buzzer_toggle = agora
                if current_state != STATE_COLLISION:
                    alarme_silenciado = False # Destrava o botão ao sair da colisão
            
            atualizar_oled(distancia_atual, current_state)

        # 2. Motor de Áudio Conciliado
        if current_state == STATE_SAFE or alarme_silenciado:
            buzzer.duty(0)
            
        elif current_state == STATE_PROXIMITY:
            # Aceleração em degraus solicitada (20cm em 20cm -> 5cm em 5cm)
            if distancia_atual > 80: fator = 8
            elif distancia_atual > 60: fator = 6
            elif distancia_atual > 40: fator = 4
            elif distancia_atual > 20: fator = 2
            elif distancia_atual > 15: fator = 1.5
            elif distancia_atual > 10: fator = 1.0
            else: fator = 0.5
            
            intervalo_silencio = int(distancia_atual * fator)
            duracao_bip = 10 # Pulso sonoro ultra-curto de 10ms
            
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
            # Alarme sonoro ininterrupto alternando frequência (Ambulância)
            if time.ticks_diff(agora, last_buzzer_toggle) >= 100:
                sirene_high = not sirene_high
                last_buzzer_toggle = agora
                buzzer.freq(1200 if sirene_high else 800)
                buzzer.duty(512)
        
        time.sleep_ms(2) # Resolução extrema para capturar os 10ms de bip sem atrasos

if __name__ == "__main__":
    main()