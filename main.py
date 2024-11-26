import os
import multiprocessing
import time
from datetime import datetime

def tarefa_filho(numero):
    """
    Função executada por cada processo filho.
    Realiza um cálculo simples e exibe informações organizadas.
    """
    try:
        pid = os.getpid()
        ppid = os.getppid()
        inicio = datetime.now().strftime("%H:%M:%S")
        
        print(f"\n{'='*40}\n[FILHO] Iniciando processo filho\n"
              f"PID: {pid} | Pai: {ppid} | Início: {inicio}")
        print(f"[FILHO] PID: {pid} | Tarefa: Calculando {numero}²\n{'='*40}")
        
        time.sleep(2)  # Simula execução
        resultado = numero ** 2
        
        fim = datetime.now().strftime("%H:%M:%S")
        print(f"[FILHO] PID: {pid} | Resultado: {numero}² = {resultado}")
        print(f"[FILHO] PID: {pid} | Finalizando processo | Fim: {fim}\n{'='*40}")
    except Exception as e:
        print(f"[FILHO] PID: {os.getpid()} | ERRO: {e}")

def criar_processos(num_processos):
    """
    Cria e gerencia processos filhos com execução multitarefa.
    """
    print(f"\n{'#'*50}\n[PAI] PID: {os.getpid()} | Criando {num_processos} processos filhos\n{'#'*50}")
    processos = []

    try:
        # Criação dos processos filhos
        for i in range(1, num_processos + 1):
            print(f"[PAI] Criando processo filho {i}...")
            filho = multiprocessing.Process(target=tarefa_filho, args=(i,))
            processos.append(filho)
            filho.start()
            print(f"[PAI] Processo filho {i} iniciado | PID: {filho.pid}")

        print(f"\n[PAI] Todos os processos filhos foram criados. Aguardando finalização...\n{'-'*50}")
        
        # Aguardando a finalização de todos os filhos
        for filho in processos:
            filho.join()
            print(f"[PAI] Processo filho concluído | PID: {filho.pid}")

    except Exception as e:
        print(f"[PAI] ERRO durante execução: {e}")
    finally:
        print(f"{'#'*50}\n[PAI] Todos os processos foram finalizados.\n{'#'*50}")

def main():
    """
    Função principal do programa.
    """
    print("\n==== INÍCIO DO GERENCIAMENTO DE PROCESSOS ====\n")
    try:
        num_processos = 3  # Defina o número de processos filhos
        criar_processos(num_processos)
    except KeyboardInterrupt:
        print("\n[PAI] Execução interrompida pelo usuário.")
    except Exception as e:
        print(f"[PAI] ERRO no programa principal: {e}")
    finally:
        print("\n==== PROGRAMA ENCERRADO ====\n")

if __name__ == "__main__":
    main()
