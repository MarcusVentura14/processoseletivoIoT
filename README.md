# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---

### 👤 Identificação do Candidato

- **Nome completo: Marcus Vinicius Oliveira Ventura**  
- **GitHub: https://github.com/MarcusVentura14**  

---

## 1️⃣ Visão Geral da Solução

O projeto implementa um Sensor de Proximidade Reativo (inspirado em radares de ré automotivos) utilizando um ESP32. Seu mecanismo utiliza ondas ultrassônicas para calcular a distância física em tempo real, fornecendo feedback visual através de um display OLED e feedback auditivo dinâmico. A lógica de controle do buzzer utiliza interpolação matemática para replicar o padrão comercial, acelerando a pulsação sonora de forma progressiva e linear à medida que o obstáculo se aproxima. O sistema conta também com um alarme de colisão com suporte a desativação manual via interrupções de hardware (IRQ) e uma camada de conectividade IoT que utiliza protocolos MQTT e NTP para sincronização de tempo, telemetria de dados e registro remoto de incidentes.

## 2️⃣ Arquitetura do Sistema Embarcado

### Fluxo Principal do Programa

Antes de iniciar o monitoramento, o sistema chama a função `setup_conexoes()`. Neste momento, o ESP32 conecta-se à rede Wi-Fi, sincroniza o relógio interno via NTP e estabelece a conexão com o broker MQTT. O display OLED informa o status visual de cada uma dessas etapas de boot.

Finalizada a inicialização, o sistema entra em um While True executando dois blocos de verificação de maneira assíncrona:

**Sensoriamento, Estado e Nuvem:** A cada 60ms, o código lê o sensor ultrassônico e avalia a distância. Baseado nessa leitura, ele atualiza a máquina de estados (em `STATE_COLLISION`, `STATE_PROXIMITY` ou `STATE_SAFE`). Caso detecte a entrada no estado de Colisão, o sistema formata a data/hora exata do incidente e publica o alerta no servidor MQTT. Ao fim desta etapa, o display OLED é atualizado.

**Motor de Áudio:** Logo em seguida, o loop avalia o estado atual para comandar o pino PWM do Buzzer. Se estiver na zona de proximidade, ele calcula o intervalo dinâmico e dispara pulsos curtos de 60ms (ou sinal contínuo, caso atinja a zona crítica inferior a 30cm), se estiver em colisão, alterna as frequências da sirene.

Ao final do ciclo principal, há apenas um micro-atraso estrutural de 2 milissegundos (`time.sleep_ms(2)`), implementado para estabilizar o processador e o watchdog timer do microcontrolador, evitando travamentos no simulador ou no hardware físico.

### Estrutura de Estados e Temporizações

O projeto implementa temporização Não-Bloqueante ao evitar a função `sleep()` e gerir todo o agendamento de tarefas (leitura do sensor, bipes e atualização da tela) pelo `time.ticks_ms()`. Isso impede que o display trave ou a rede caia enquanto o alarme sonoro é processado.

Quanto à Estrutura de Estados, o sistema reage ao ambiente baseando-se em três estados definidos pela distância:

**STATE_SAFE (> 200cm):** Sistema em monitoramento passivo.

**STATE_PROXIMITY (2.2cm a 200cm):** Utiliza uma interpolação matemática linear para definir os alertas. O pulso do buzzer é fixo em 60ms (padrão comercial), mas o intervalo de silêncio cai progressivamente de 1500ms para 300ms conforme a aproximação. Ao atingir 30cm, o som torna-se contínuo.

**STATE_COLLISION (<= 2.2cm):** Colisão detectada. Aciona a sirene de emergência e a telemetria.

### Interação entre Componentes

O fluxo de dados do sistema opera em quatro vias de comunicação:

**Entrada (Sensoriamento):** O HC-SR04 mede a distância física e atualiza o estado interno do ESP32.

**Saída (Atuação):** Em resposta, o ESP32 modula imediatamente o som do Buzzer (via PWM) e atualiza os dados visuais no Display OLED (via I2C).

**Controle (Intervenção):** O botão tátil atua sob uma interrupção de hardware (IRQ), sobrepondo-se ao fluxo principal para silenciar o alarme de forma instantânea.

**Nuvem (Telemetria):** Exclusivamente no estado de colisão, o sistema captura a hora exata (via NTP) e despacha o alerta para o servidor remoto (via MQTT).

## 3️⃣ Componentes Utilizados na Simulação

- **Microcontrolador:** ESP32 (DevKitC V4). Atua como o cérebro da operação e fornece o módulo Wi-Fi nativo para a telemetria via rede.
- **Sensor HC-SR04 (Pinos 5 e 18):** Envio de pulso de Trigger e leitura não-bloqueante do tempo do Echo.
- **Display OLED SSD1306 (I2C - Pinos 21/22):** Interface Homem-Máquina para telemetria da distância e status da máquina de estados.
- **Buzzer Piezoelétrico (Pino 13 - PWM):** Atuador sonoro. Modula tanto o *duty cycle* (liga/desliga) quanto a frequência (Hz) para criar tons distintos.
- **Push Button (Pino 12 - IRQ):** Interface de desarmamento vinculada à interrupção de hardware por borda de descida.


## 4️⃣ Decisões Técnicas Relevantes

Visando a manutenibilidade, legibilidade e a eficiência do processador, o projeto utilizou as seguintes estratégias: 

**Uso de Constantes Nominais:** Pinos e limiares físicos foram definidos como constantes globais nominais, facilitando a leitura e futuras calibrações de hardware.

**Modularidade:** As rotinas de boot e rede (Wi-Fi, NTP e MQTT) foram isoladas em uma função dedicada (`setup_conexoes()`), mantendo o bloco main() focado exclusivamente no Super Loop.

**Redução de Complexidade:** A interpolação matemática linear substituiu longas cadeias de if/else no motor de áudio, otimizando o processamento e a memória do ESP32.

**Resiliência contra Latência:** O uso de interrupção de hardware (IRQ) para o botão garante o silenciamento instantâneo do alarme, não sendo afetado por eventuais gargalos de rede durante envios MQTT.


## 5️⃣ Resultados Obtidos

As simulações realizadas no ambiente Wokwi validaram a eficiência do código, que atendeu a todos os requisitos arquiteturais e de conectividade propostos. O resultado final é um protótipo funcional de nível comercial, destacando-se pela validação dos seguintes comportamentos:

**Feedback Audiovisual em Tempo Real:** A leitura da distância no sensor, a atualização do display OLED e a resposta do buzzer operam de forma fluida e simultânea. A ausência de travamentos no simulador comprova o sucesso da arquitetura não-bloqueante.

**Transição de Estados:** O sistema obedece rigorosamente aos limites estabelecidos. A aceleração rítmica do alarme sonoro ocorre progressivamente na zona de proximidade e muda corretamente para a sirene de emergência ao cruzar a marca de 2.2cm.

**Controle de Interrupção:** O acionamento do botão físico no Wokwi corta o som do buzzer imediatamente, validando o funcionamento prioritário da rotina de IRQ (Hardware Interrupt).

**Telemetria IoT Validada:** O fluxo de comunicação com a nuvem foi testado com êxito. Ao simular uma colisão no Wokwi (arrastando o controle de distância para ≤ 2.2cm), o sistema formata o pacote com a hora exata (NTP) e o despacha. A recepção íntegra desses dados foi monitorada e confirmada em tempo real através do aplicativo MQTT Dashboard Client.



> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
