# Módulo de gestão de clientes

def registar_cliente(nome, email):
    """Regista um novo cliente"""
    print(f"Cliente {nome} registado com email {email}")

def listar_clientes():
    """Lista todos os clientes"""
    print("Lista de clientes:")
# Nova funcionalidade adicionada
def editar_cliente(id_cliente, novo_email):
    """Edita o email de um cliente existente"""
    print(f"Email do cliente {id_cliente} atualizado")