# Módulo de gestão de quartos

def verificar_disponibilidade(numero_quarto):
    """Verifica se um quarto está disponível"""
    print(f"Verificando quarto {numero_quarto}")

def ocupar_quarto(numero_quarto):
    """Marca um quarto como ocupado"""
    print(f"Quarto {numero_quarto} ocupado")

# Nova funcionalidade
def listar_quartos_disponiveis():
    """Mostra todos os quartos disponíveis"""
    print("Quartos disponíveis: 101, 102, 105")
def libertar_quarto(numero_quarto):
    """Liberta um quarto ocupado"""
    print(f"Quarto {numero_quarto} libertado")