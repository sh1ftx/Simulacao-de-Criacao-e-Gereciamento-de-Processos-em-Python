# ---------------------------------------------------------------------------------
# Módulo term_colors
# Define as cores usadas no terminal para saída estilizada
# ---------------------------------------------------------------------------------
class TermColors:
    """
    Classe para armazenar as cores ANSI usadas no terminal.
    """
    BLUE = "\033[94m"      # Azul para o processo principal
    RED = "\033[91m"       # Vermelho para subprocesso 1
    GREEN = "\033[92m"     # Verde para subprocesso 2
    YELLOW = "\033[93m"    # Amarelo para subprocesso 3
    MAGENTA = "\033[95m"   # Magenta para subprocesso 4
    CYAN = "\033[96m"      # Ciano para subprocesso 5
    ORANGE = "\033[38;5;214m"  # Laranja para subprocesso 6
    RESET = "\033[0m"      # Reset para cor padrão do terminal
