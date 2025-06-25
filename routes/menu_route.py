from flask import Blueprint, jsonify
from services.menu_service import listar_menu

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/menu', methods=['GET'])
def get_menu():
    response, status_code = listar_menu()
    return jsonify(response), status_code