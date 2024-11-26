# ---------------------------------------------------------------------------------
# Arquivo principal
# Orquestra a execução do programa, exibindo a legenda e gerenciando subprocessos
# ---------------------------------------------------------------------------------

from legend import printLegend
from subprocess_manager import manageSubProcesses

def main():
    """
    Função principal do programa.
    """
    print("\n==== INÍCIO DO GERENCIAMENTO DE SUBPROCESSOS ====\n");
    
    # Exibir a legenda com as cores e subprocessos
    printLegend();
    
    # Gerenciar subprocessos (quantidade definida aqui)
    manageSubProcesses(6);
    
    print("\n==== PROGRAMA ENCERRADO ====\n");

if __name__ == "__main__":
    main();
