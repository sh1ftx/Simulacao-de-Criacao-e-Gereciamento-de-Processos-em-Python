# ---------------------------------------------------------------------------------
# Módulo legend
# Exibe uma legenda que explica os subprocessos e as cores associadas
# ---------------------------------------------------------------------------------
from term_colors import TermColors

def printLegend():
    """
    Exibe a legenda com as cores e subprocessos associados.
    """
    print(f"{TermColors.BOLD}{TermColors.BLUE}Processo Principal:{TermColors.RESET} Gerencia todos os subprocessos.\n")
    print(f"{TermColors.RED}Subprocesso 1:{TermColors.RESET} Calcula o cubo de 1 (Vermelho).")
    print(f"{TermColors.GREEN}Subprocesso 2:{TermColors.RESET} Calcula o cubo de 2 (Verde).")
    print(f"{TermColors.YELLOW}Subprocesso 3:{TermColors.RESET} Calcula o cubo de 3 (Amarelo).")
    print(f"{TermColors.MAGENTA}Subprocesso 4:{TermColors.RESET} Calcula o cubo de 4 (Magenta).")
    print(f"{TermColors.CYAN}Subprocesso 5:{TermColors.RESET} Calcula o cubo de 5 (Ciano).")
    print(f"{TermColors.ORANGE}Subprocesso 6:{TermColors.RESET} Calcula o cubo de 6 (Laranja).")
    print(f"\n{'-'*50}\n")
