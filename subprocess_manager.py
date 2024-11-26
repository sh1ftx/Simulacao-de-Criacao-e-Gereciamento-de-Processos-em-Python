# ---------------------------------------------------------------------------------
# Módulo subprocess_manager
# Gerencia os subprocessos e realiza as operações definidas
# ---------------------------------------------------------------------------------

import os
import multiprocessing
import time
from datetime import datetime
from term_colors import TermColors

def subProcessTask(number, color):
    """
    Função executada por cada subprocesso. Realiza um cálculo e exibe
    informações detalhadas com uma cor específica para cada subprocesso.
    
    Args:
        number (int): Número base para o cálculo.
        color (str): Cor associada ao subprocesso.
    """
    try:
        # Obter informações sobre o processo
        pid = os.getpid();
        ppid = os.getppid();
        initTime = datetime.now().strftime("%H:%M:%S");
        
        # Exibir informações iniciais do subprocesso
        print(f"\n{'='*40}\n{color}[SUBPROCESSO] Iniciando subprocesso\n"
              f"PID: {pid} | Pai: {ppid} | Início: {initTime}{TermColors.RESET}");
        print(f"{color}[SUBPROCESSO] PID: {pid} | Tarefa: Calculando {number}³\n{'='*40}{TermColors.RESET}");
        
        # Simulação de execução com pausa
        time.sleep(3);
        result = number ** 3;
        
        # Exibir o resultado do cálculo
        endTime = datetime.now().strftime("%H:%M:%S");
        print(f"{color}[SUBPROCESSO] PID: {pid} | Resultado: {number}³ = {result}{TermColors.RESET}");
        print(f"{color}[SUBPROCESSO] PID: {pid} | Finalizando subprocesso | Fim: {endTime}\n{'='*40}{TermColors.RESET}");
    except Exception as e:
        print(f"{color}[SUBPROCESSO] PID: {os.getpid()} | ERRO: {e}{TermColors.RESET}");

def manageSubProcesses(numSubProcesses):
    """
    Gerencia a criação e execução de subprocessos com cores diferenciadas.

    Args:
        numSubProcesses (int): Número de subprocessos a serem criados.
    """
    print(f"\n{'#'*50}\n{TermColors.BLUE}[PRINCIPAL] PID: {os.getpid()} | Criando {numSubProcesses} subprocessos\n{'#'*50}{TermColors.RESET}");
    processes = [];
    colors = [TermColors.RED, TermColors.GREEN, TermColors.YELLOW, TermColors.MAGENTA, TermColors.CYAN, TermColors.ORANGE];

    try:
        # Criar subprocessos
        for i in range(1, numSubProcesses + 1):
            print(f"{TermColors.BLUE}[PRINCIPAL] Criando subprocesso {i}...{TermColors.RESET}");
            color = colors[i-1];
            process = multiprocessing.Process(target=subProcessTask, args=(i, color));
            processes.append(process);
            process.start();
            print(f"{TermColors.BLUE}[PRINCIPAL] Subprocesso {i} iniciado | PID: {process.pid}{TermColors.RESET}");
        
        print(f"\n{TermColors.BLUE}[PRINCIPAL] Todos os subprocessos foram criados. Aguardando finalização...\n{'-'*50}{TermColors.RESET}");
        
        # Aguardar a conclusão de todos os subprocessos
        for process in processes:
            process.join();
            print(f"{TermColors.BLUE}[PRINCIPAL] Subprocesso concluído | PID: {process.pid}{TermColors.RESET}");
        
    except Exception as e:
        print(f"{TermColors.BLUE}[PRINCIPAL] ERRO durante execução: {e}{TermColors.RESET}");
    finally:
        print(f"{'#'*50}\n{TermColors.BLUE}[PRINCIPAL] Todos os subprocessos foram finalizados.\n{'#'*50}{TermColors.RESET}");
