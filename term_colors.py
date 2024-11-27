# ---------------------------------------------------------------------------------
# Módulo term_colors
# Define as cores e estilos usados para formatar saídas no terminal
# ---------------------------------------------------------------------------------
class TermColors:
    """
    Classe para armazenar cores ANSI usadas no terminal.
    """
    BLUE = "\033[94m"       # Azul: Processo principal
    RED = "\033[91m"        # Vermelho: Subprocesso 1
    GREEN = "\033[92m"      # Verde: Subprocesso 2
    YELLOW = "\033[93m"     # Amarelo: Subprocesso 3
    MAGENTA = "\033[95m"    # Magenta: Subprocesso 4
    CYAN = "\033[96m"       # Ciano: Subprocesso 5
    ORANGE = "\033[38;5;214m"  # Laranja: Subprocesso 6
    RESET = "\033[0m"       # Reseta a cor
    BOLD = "\033[1m"        # Negrito
    UNDERLINE = "\033[4m"   # Sublinhado
