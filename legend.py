# ---------------------------------------------------------------------------------
# Módulo legend
# Exibe a legenda que explica as cores e subprocessos
# ---------------------------------------------------------------------------------

from term_colors import TermColors

def printLegend():
    """
    Função para exibir a legenda com as cores e suas funções correspondentes.
    """
    print(f"{TermColors.BLUE}Processo Principal:{TermColors.RESET} Gerencia os subprocessos.")
    print(f"{TermColors.RED}Subprocesso 1:{TermColors.RESET} Calcula o cubo de 1 (Vermelho).")
    print(f"{TermColors.GREEN}Subprocesso 2:{TermColors.RESET} Calcula o cubo de 2 (Verde).")
    print(f"{TermColors.YELLOW}Subprocesso 3:{TermColors.RESET} Calcula o cubo de 3 (Amarelo).")
    print(f"{TermColors.MAGENTA}Subprocesso 4:{TermColors.RESET} Calcula o cubo de 4 (Magenta).")
    print(f"{TermColors.CYAN}Subprocesso 5:{TermColors.RESET} Calcula o cubo de 5 (Ciano).")
    print(f"{TermColors.ORANGE}Subprocesso 6:{TermColors.RESET} Calcula o cubo de 6 (Laranja).")
    print(f"\n{'-'*50}\n")
