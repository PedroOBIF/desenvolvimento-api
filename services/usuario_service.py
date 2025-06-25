from models.usuario import Usuario

usuarios = []
id_usuario = 0

def gerar_id():
    global id_usuario
    id_usuario += 1
    return id_usuario

def criar_usuario(dados):
    global usuarios
    for u in usuarios:
        if u.email == dados["email"]:
            return None, "user_exists"
    novo_usuario = Usuario(gerar_id(), dados["nome"], dados["email"], dados["senha"])
    usuarios.append(novo_usuario)
    return novo_usuario, None

def listar_usuarios():
    # lista = []
    # for u in usuarios:
    #     lista.append(u.to_dict())
    # return lista
    lista = [u.to_dict() for u in usuarios]
    return lista

def listar_um_usuario(id):
    for u in usuarios:
        if u.id == id:
            return u, None
    return None, "user_not_found"

def atualizar_usuario(id, novos_dados):
    usuario_encontrado, erro = listar_um_usuario(id)

    if erro:
        return None, erro
    
    novo_email = novos_dados.get("email")
    if (novo_email):
        for u in usuarios:
            if u.email == novos_dados["email"]:
                return None, "user_exists"

            
    usuario_encontrado.nome = novos_dados.get("nome", usuario_encontrado.nome)
    usuario_encontrado.email = novos_dados.get("email", usuario_encontrado.email)
    usuario_encontrado.senha = novos_dados.get("senha", usuario_encontrado.senha)
    return usuario_encontrado, None

def deletar_usuario(id):
    global usuarios
    usuario_encontrado, erro = listar_um_usuario(id)

    if erro:
        return False, erro
    
    usuarios.remove(usuario_encontrado)
    return True, None