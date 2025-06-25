from models.menu import itens_menu

def listar_menu():
    return itens_menu if itens_menu else ({"error": "Menu não encontrado"}, 404)