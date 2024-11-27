# ---------------------------------------------------------------------------------
# Módulo subprocess_manager
# Gerencia a criação e execução de subprocessos
# ---------------------------------------------------------------------------------
import os
import multiprocessing
import time
from datetime import datetime
from term_colors import TermColors

def subProcessTask(number, color):
    """
    Função executada por cada subprocesso. Mostra início, execução e finalização.
    
    Args:
        number (int): Número base para o cálculo.
        color (str): Cor associada ao subprocesso.
    """
    try:
        # Informações do subprocesso
        pid = os.getpid();
        ppid = os.getppid();
        initTime = datetime.now().strftime("%H:%M:%S");
        
        # Início do subprocesso
        print(f"\n{color}{TermColors.BOLD}{'='*40}")
        print(f"[INÍCIO] Subprocesso {number} iniciado!")
        print(f"PID: {pid} | Processo Principal: {ppid} | Hora: {initTime}{TermColors.RESET}")
        
        # Execução do subprocesso
        print(f"{color}[EXECUÇÃO] Calculando {number}³...{TermColors.RESET}")
        time.sleep(3);  # Simulação de execução
        result = number ** 3;
        print(f"{color}[RESULTADO] {number}³ = {result}{TermColors.RESET}")
        
        # Finalização do subprocesso
        endTime = datetime.now().strftime("%H:%M:%S");
        print(f"{color}{TermColors.BOLD}[FINALIZAÇÃO] Subprocesso {number} finalizado às {endTime}{TermColors.RESET}")
        print(f"{color}{'='*40}{TermColors.RESET}")
    except Exception as e:
        print(f"{color}[ERRO] PID: {os.getpid()} | {e}{TermColors.RESET}");

def manageSubProcesses(numSubProcesses):
    """
    Cria e gerencia subprocessos com cores para maior clareza.
    
    Args:
        numSubProcesses (int): Número de subprocessos a serem criados.
    """
    print(f"\n{'#'*50}\n{TermColors.BOLD}{TermColors.BLUE}[PROCESSO PRINCIPAL] Gerenciando {numSubProcesses} subprocessos.{TermColors.RESET}\n{'#'*50}")
    processes = [];
    colors = [TermColors.RED, TermColors.GREEN, TermColors.YELLOW, TermColors.MAGENTA, TermColors.CYAN, TermColors.ORANGE];

    try:
        # Criar subprocessos
        for i in range(1, numSubProcesses + 1):
            print(f"{TermColors.BLUE}[PROCESSO PRINCIPAL] Criando subprocesso {i}...{TermColors.RESET}")
            color = colors[i-1];
            process = multiprocessing.Process(target=subProcessTask, args=(i, color));
            processes.append(process);
            process.start();
            print(f"{TermColors.BLUE}[PROCESSO PRINCIPAL] Subprocesso {i} iniciado | PID: {process.pid}{TermColors.RESET}")
        
        # Aguardar conclusão
        print(f"\n{TermColors.BLUE}[PROCESSO PRINCIPAL] Aguardando finalização dos subprocessos...\n{'-'*50}{TermColors.RESET}")
        for process in processes:
            process.join();
            print(f"{TermColors.BLUE}[PROCESSO PRINCIPAL] Subprocesso concluído | PID: {process.pid}{TermColors.RESET}")
        
    except Exception as e:
        print(f"{TermColors.BLUE}[PROCESSO PRINCIPAL] ERRO: {e}{TermColors.RESET}")
    finally:
        print(f"{'#'*50}\n{TermColors.BLUE}[PROCESSO PRINCIPAL] Todos os subprocessos foram finalizados.\n{'#'*50}{TermColors.RESET}")
