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

- **Nome completo:**  
- **GitHub:**  

---

## 1️⃣ Visão Geral da Solução

O projeto implementa um **Sensor de Proximidade Reativo** (inspirado em radares de ré automotivos). Ele utiliza ondas ultrassônicas para calcular a distância física em tempo real, fornecendo feedback visual através de um display OLED e feedback auditivo dinâmico, cuja pulsação sonora acelera à medida que se aproxima do obstáculo, culminando em um alarme intermitente de colisão com suporte a desativação manual.

## 2️⃣ Arquitetura do Sistema Embarcado

A solução foi projetada com foco em programação não-bloqueante e concorrência no Super Loop:

1. **Gestão de Tarefas (Ticks):** Em vez de paralisar o microcontrolador com funções de `sleep()`, o firmware agenda a leitura do sensor e as pulsações PWM do buzzer avaliando deltas de tempo via `time.ticks_ms()`. Isso garante que o display não trave enquanto o alarme soa.
2. **Máquina de Estados de Risco:** O fluxo é dividido nos estados `STATE_SAFE` (>100cm), `STATE_PROXIMITY` (<=100cm) e `STATE_COLLISION` (<= 2.0cm).
3. **Mapeamento Dinâmico por Degraus:** No estado de proximidade, o intervalo de tempo entre as interrupções sonoras não é linear. Ele utiliza fatores multiplicativos que diminuem em degraus (a cada 20cm inicialmente, e a cada 5cm na reta final), criando uma curva exponencial de aceleração rítmica.


## 3️⃣ Componentes Utilizados na Simulação

- **Microcontrolador:** ESP32 (DevKitC V4).
- **Sensor HC-SR04 (Pinos 5 e 18):** Envio de pulso de Trigger e leitura não-bloqueante do tempo do Echo.
- **Display OLED SSD1306 (I2C - Pinos 21/22):** Interface Homem-Máquina para telemetria da distância e status da máquina de estados.
- **Buzzer Piezoelétrico (Pino 13 - PWM):** Atuador sonoro. Modula tanto o *duty cycle* (liga/desliga) quanto a frequência (Hz) para criar tons distintos.
- **Push Button (Pino 12 - IRQ):** Interface de desarmamento vinculada à interrupção de hardware por borda de descida.


## 4️⃣ Decisões Técnicas Relevantes

- **Uso do time_pulse_us:** O cálculo de distância evitou bibliotecas externas, utilizando a função nativa do MicroPython com um timeout de 30.000 microssegundos para evitar que o código ficasse preso esperando um eco de um ambiente vazio.
- **Articulação Sonora (Estacato):** Para simular a precisão de um radar automotivo real, o pulso sonoro do bip foi fixado no tempo mínimo audível do simulador (10 milissegundos), garantindo ataques curtos e secos que não se atropelam em altas velocidades.
- **Efeito Sirene (Ambulância):** No estado crítico de colisão, o PWM alterna suas frequências entre 800Hz e 1200Hz a cada 100ms de forma autônoma para causar desconforto acústico e gerar um alerta assertivo, até ser interrompido pelo usuário.
- **Precedência de Hardware (IRQ):** A função de silenciar o alarme (`btn_isr`) acontece via interrupção. Isso significa que, independentemente da carga processual do momento, o comando do operador desliga o som no exato milissegundo do acionamento.
- **Roteamento de Circuito (Bus Routing):** O diagrama `diagram.json` foi editado a nível de código para garantir que as trilhas de dados e força (VCC/GND) contornassem o ESP32 de forma ortogonal e sem sobreposições, simulando o design limpo de uma placa de circuito impresso (PCB) real.


## 5️⃣ Resultados Obtidos

A simulação no ambiente Wokwi demonstra a eficiente execução do projeyo. Ao alterar a distância do HC-SR04 no simulador:
- De 400cm até 101cm: O sistema permanece silencioso no estado `SEGURO` e atualiza o painel visualmente.
- Ao cruzar o limiar de 100cm: O estado muda para `ATENCAO`. Os bipes iniciam compassados. Conforme a distância cai pelas faixas de 80, 60, 40, 20 e 15cm, o ritmo do buzzer acelera vertiginosamente.
- Em 2.0cm (Limite físico do HC-SR04): O estado `COLISAO!` é ativado. Uma margem de absorção de float no código (2.2cm) garante que a precisão matemática do simulador acione o alarme de dupla frequência sem falhas. 
- Pressionar o botão aciona a interrupção, que altera instantaneamente a tela para "SILENCIADO" e corta o sinal PWM, que só é rearmado caso o objeto se afaste da zona de perigo.
De maneira geral, o sistema apresentou-se como um ótimo protótipo de sensor reativo.



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
