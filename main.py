# ---------------------------------------------------------------------------------
# Arquivo principal
# Controla a execução do programa e exibe informações ao usuário
# ---------------------------------------------------------------------------------

from legend import printLegend
from subprocess_manager import manageSubProcesses

def main():
    """
    Função principal do programa.
    """
    print("\n==== GERENCIADOR DE SUBPROCESSOS ====\n");
    
    # Exibir a legenda
    printLegend();
    
    # Gerenciar subprocessos
    manageSubProcesses(6);
    
    print("\n==== PROGRAMA ENCERRADO ====\n");

if __name__ == "__main__":
    main();
