### **Documentação Completa do Programa Python: Gerenciamento de Subprocessos**

---

### **Índice**
- [**Documentação Completa do Programa Python: Gerenciamento de Subprocessos**](#documentação-completa-do-programa-python-gerenciamento-de-subprocessos)
- [**Índice**](#índice)
- [**1. Visão Geral** ](#1-visão-geral-)
- [**2. Objetivos do Programa** ](#2-objetivos-do-programa-)
- [**3. Estrutura do Projeto** ](#3-estrutura-do-projeto-)
- [**4. Descrição de Arquivos e Funções** ](#4-descrição-de-arquivos-e-funções-)
  - [**4.1. Arquivo `main.py`** ](#41-arquivo-mainpy-)
  - [**4.2. Arquivo `term_colors.py`** ](#42-arquivo-term_colorspy-)
  - [**4.3. Arquivo `legend.py`** ](#43-arquivo-legendpy-)
  - [**4.4. Arquivo `subprocess_manager.py`** ](#44-arquivo-subprocess_managerpy-)
- [**5. Fluxo de Execução** ](#5-fluxo-de-execução-)
- [**6. Configurações e Execução** ](#6-configurações-e-execução-)
  - [**Requisitos**](#requisitos)
  - [**Passo a Passo**](#passo-a-passo)
- [**7. Exemplo de Saída** ](#7-exemplo-de-saída-)
- [**8. Detalhes Técnicos** ](#8-detalhes-técnicos-)
- [**9. Apresentação do Código** ](#9-apresentação-do-código-)

---

### **1. Visão Geral** <a id="visao-geral"></a>

Este programa simula a criação e o gerenciamento de **subprocessos** utilizando o módulo `multiprocessing` do Python. Ele organiza as tarefas em subprocessos distintos, cada um responsável por realizar cálculos (o cubo do número correspondente). O programa utiliza **cores** e uma **legenda detalhada** para facilitar a identificação dos subprocessos.

---

### **2. Objetivos do Programa** <a id="objetivos"></a>

- Demonstrar o uso de **múltiplos subprocessos** em Python.
- Apresentar o conceito de gerenciamento de subprocessos, como criação, execução e sincronização.
- Utilizar **diferenciação visual (cores)** para tornar a saída mais compreensível.
- Oferecer uma estrutura de projeto modular e organizada para fácil manutenção.

---

### **3. Estrutura do Projeto** <a id="estrutura"></a>

O projeto está organizado em arquivos separados, garantindo **modularidade** e **reuso de código**:

```plaintext
project/
│
├── main.py               # Ponto de entrada do programa
├── term_colors.py        # Definição de cores para o terminal
├── legend.py             # Função para exibir a legenda explicativa
└── subprocess_manager.py # Lógica de criação e gerenciamento de subprocessos
```

---

### **4. Descrição de Arquivos e Funções** <a id="descricao-arquivos"></a>

#### **4.1. Arquivo `main.py`** <a id="arquivo-main"></a>
- **Função principal do programa.**
- Chamadas principais:  
  - **`printLegend()`**: Exibe a legenda com cores e funções de cada subprocesso.
  - **`manageSubProcesses()`**: Inicia o processo principal e os subprocessos.

Exemplo de trecho funcional:  
```python
print("\n==== INÍCIO DO GERENCIAMENTO DE SUBPROCESSOS ====\n");
printLegend();  # Exibe a legenda
manageSubProcesses(6);  # Cria 6 subprocessos
```

---

#### **4.2. Arquivo `term_colors.py`** <a id="arquivo-term_colors"></a>
Define as **sequências ANSI** para aplicar cores no terminal:
- **Azul**: Processo principal.
- **Vermelho**: Subprocesso 1.
- **Verde**: Subprocesso 2.
- **Amarelo**: Subprocesso 3.
- **Magenta**: Subprocesso 4.
- **Ciano**: Subprocesso 5.
- **Laranja**: Subprocesso 6.

Exemplo:  
```python
class TermColors:
    BLUE = "\033[94m";
    RED = "\033[91m";
    GREEN = "\033[92m";
    YELLOW = "\033[93m";
    MAGENTA = "\033[95m";
    CYAN = "\033[96m";
    ORANGE = "\033[33m";  # Laranja
    RESET = "\033[0m";    # Reseta para cor padrão
```

---

#### **4.3. Arquivo `legend.py`** <a id="arquivo-legend"></a>
Exibe a legenda que associa **cores às tarefas dos subprocessos**.  
**Exemplo de legenda exibida no terminal**:  
```plaintext
Azul: Processo Principal
Vermelho: Subprocesso 1 - Calcula o cubo de 1
Verde: Subprocesso 2 - Calcula o cubo de 2
Amarelo: Subprocesso 3 - Calcula o cubo de 3
Magenta: Subprocesso 4 - Calcula o cubo de 4
Ciano: Subprocesso 5 - Calcula o cubo de 5
Laranja: Subprocesso 6 - Calcula o cubo de 6
```

---

#### **4.4. Arquivo `subprocess_manager.py`** <a id="arquivo-subprocess_manager"></a>
Contém duas funções principais:

1. **`subProcessTask(number, color)`**: Executa a lógica de cada subprocesso.
   - Exibe informações do PID, pai, cálculo e horários.
   - Adiciona cores às mensagens para fácil identificação.

2. **`manageSubProcesses(numProcesses)`**:  
   - Cria, executa e sincroniza os subprocessos.
   - Exibe mensagens detalhadas do processo principal.

Exemplo da criação de subprocessos:
```python
for i in range(1, numProcesses + 1):
    color = colors[i-1];  # Atribui cor a cada subprocesso
    process = multiprocessing.Process(target=subProcessTask, args=(i, color));
    process.start();
    processes.append(process);
```

---

### **5. Fluxo de Execução** <a id="fluxo"></a>

1. O programa principal (`main.py`) inicia a execução.  
2. A legenda é exibida com explicações sobre as cores e funções.  
3. O processo principal (`manageSubProcesses`) cria os subprocessos.  
4. Cada subprocesso executa sua tarefa e exibe informações detalhadas (PID, cálculo, tempo de início e término).  
5. O processo principal aguarda a finalização de todos os subprocessos e encerra o programa.  

---

### **6. Configurações e Execução** <a id="configuracoes"></a>

#### **Requisitos**
- **Python 3.6 ou superior**.
- Módulo `multiprocessing` (nativo do Python).

#### **Passo a Passo**
1. **Baixe os arquivos do projeto** para uma pasta local.
2. **Execute o programa** a partir do terminal:
   ```bash
   python3 main.py
   ```

---

### **7. Exemplo de Saída** <a id="exemplo"></a>

```plaintext
==== INÍCIO DO GERENCIAMENTO DE SUBPROCESSOS ====

Legenda:
Azul: Processo Principal
Vermelho: Subprocesso 1 - Calcula o cubo de 1
Verde: Subprocesso 2 - Calcula o cubo de 2
Amarelo: Subprocesso 3 - Calcula o cubo de 3
Magenta: Subprocesso 4 - Calcula o cubo de 4
Ciano: Subprocesso 5 - Calcula o cubo de 5
Laranja: Subprocesso 6 - Calcula o cubo de 6

--------------------------------------------------

##################################################
[PRINCIPAL] PID: 12345 | Criando 6 subprocessos
##################################################

[PRINCIPAL] Criando subprocesso 1...
[PRINCIPAL] Subprocesso 1 iniciado | PID: 12346

========================================
[SUBPROCESSO] PID: 12346 | Tarefa: Calculando 1³
========================================
[SUBPROCESSO] PID: 12346 | Resultado: 1³ = 1
========================================

...

##################################################
[PRINCIPAL] Todos os subprocessos foram finalizados.
##################################################
==== PROGRAMA ENCERRADO ====
```

---

### **8. Detalhes Técnicos** <a id="detalhes-tecnicos"></a>

- **Subprocessos**: Gerenciados pelo módulo `multiprocessing`, garantindo **execução paralela**.  
- **PID e PPID**: Identificadores dos subprocessos e seus pais.  
- **Sincronização**: O processo principal aguarda a finalização dos subprocessos usando `join()`.  
- **Cores**: Sequências ANSI aplicadas diretamente às mensagens.
