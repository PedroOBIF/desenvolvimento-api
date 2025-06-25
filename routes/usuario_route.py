from flask import Blueprint, request, jsonify
from services.usuario_service import criar_usuario, listar_usuarios, listar_um_usuario, atualizar_usuario, deletar_usuario
from utils.error_messages import ERROR as ERRO

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["POST"])
def criar():
    dados_body = request.json
    novo_usuario, erro = criar_usuario(dados_body)

    if erro:
        error_info = ERRO.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": error_info["mensagem"]}), error_info["status"]
    return jsonify(novo_usuario.to_dict()), 201

@usuarios_bp.route("/usuarios", methods=["GET"])
def lista_usuarios():
    return jsonify(listar_usuarios()), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    usuario_encontrado, erro = listar_um_usuario(id)

    if erro:
        error_info = ERRO[erro]
        return jsonify({"mensagem": error_info["mensagem"]}), error_info["status"]
    return jsonify(usuario_encontrado.to_dict()), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def atualizar(id):
    usuario, erro = atualizar_usuario(id, request.json)

    if erro:
        error_info = ERRO[erro]
        return jsonify({"mensagem": error_info["mensagem"]}), error_info["status"]
    return jsonify(usuario.to_dict()), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar(id):
    sucesso, erro = deletar_usuario(id)

    if erro:
        error_info = ERRO[erro]
        return jsonify({"mensagem": error_info["mensagem"]}), error_info["status"]
    return "", 204    