# Módulo de gestão de reservas

def criar_reserva(cliente, quarto, data):
    """Cria uma nova reserva"""
    print(f"Reserva criada para {cliente} no quarto {quarto}")

def cancelar_reserva(numero_reserva):
    """Cancela uma reserva"""
    print(f"Reserva {numero_reserva} cancelada")

def listar_reservas():
    """Mostra todas as reservas ativas"""
    print("Reservas ativas:")