# ==============================================================
# PROJETO: Controle de Níveis de Água
# CURSO: Técnico em Desenvolvimento de Sistemas
# ALUNO: Bianca Weiss
# DESCRIÇÃO: Simula o monitoramento de um reservatório de água
#            exibindo alertas coloridos conforme o nível.
# ==============================================================

# Importa a biblioteca colorama (cores no terminal)
from colorama import Fore, Style, init

# Inicializa o colorama (necessário para funcionar no Windows)
init(autoreset=True)

# Lista com os 5 níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    """
    Recebe o número do nível (1 a 5) e retorna
    a cor correspondente usando a biblioteca colorama.
    """
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Exibe o título do programa
print("----------------------------------------")
print("  CONTROLE DE NÍVEIS DE ÁGUA")
print("----------------------------------------")
print("")

# Percorre a lista de níveis (1 a 5) e exibe cada um com sua cor
for i in range(len(niveis)):

    # O nível começa em 1 (por isso i + 1)
    nivel = i + 1

    # Obtém a cor correspondente ao nível
    cor = definir_cor(nivel)

    # Exibe a mensagem do nível com a cor escolhida
    print(cor + niveis[i])

# Restaura o estilo padrão do terminal ao final
print("")
print(Style.RESET_ALL + "----------------------------------------")
print("Monitoramento encerrado.")
print("----------------------------------------")