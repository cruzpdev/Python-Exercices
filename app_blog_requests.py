"""
1 - definir o objetivo da API
um api de blog, onde poderemos consultar, editar, criar e excluir postagens em um blog usando a API
2 - qual será o URL base do api?
Quando você cria uma aplicação local, ela terá um url tipo http://localhost:5000, porém quando você for subir isso para a nuvem, você tera que comprar ou usar um dominio como url base, por exemplo: http://meublog.com/api
3 - quais são os endpoints?
Se seu requisito é de consultar, editar, criar e excluir postagens, então você terá 4 endpoints, um para cada ação
4 - quais recursos serão disponibilizados pelo api: 
informações sobre as postagens
5 - Quais verbos http serão utilizados?
GET - para consultar
POST - para criar
PUT - para editar
DELETE - para excluir
6 - quais são os URL completos de cada um?
GET - http://meublog.com/api/postagens
GET id HTTP://meublog.com/api/postagens/1
POST - http://meublog.com/api/postagens
PUT - http://meublog.com/api/postagens/1
DELETE - http://meublog.com/api/postagens/1


"""

from flask import Flask, jsonify, request
from estrutura_banco_de_dados_blog import Autor, Postagem, app, db


postagens = [
    {
        'título': 'minha história',
        'autor': 'João Silva'
    },
    {
        'título': 'Novo dispositivo Sony',
        'autor': 'Howard Stringer'	
    },
    {
        'título': 'lançamento do ano',
        'autor': 'Jeff Bezos'
    }
]

#ROTA PADRÃO - GET http://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

#GET COM ID - GET http://localhost:5000/postagens/2 
@app.route('/postagens/<int:id>',methods = ['GET'])
def obter_postagem_por_indice(id):
    return jsonify(postagens[id])

# POST -  criar nova postagem http://localhost:5000/postagens
@app.route('/postagens', methods = ['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem,200)

# PUT - editar postagem http://localhost:5000/postagens/0
@app.route('/postagens/<int:id>', methods=['PUT'])
def alterar_postagem(id):
    postagem_alterada = request.get_json()
    postagens[id].update(postagem_alterada)

    return jsonify(postagens[id],200)

# DELETE - excluir postagem http://localhost:5000/postagens/0
@app.route('/postagens/<int:id>', methods=['DELETE'])
def excluir_postagem(id):
    try:
        if postagens[id] is not None:
            del postagens[id]
            return jsonify({'status': 'ok'},200)
    except:
        return jsonify({'status': 'erro'},404)

@app.route('/autores')
def obter_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
    return jsonify(lista_de_autores)

@app.route('/autores/<int:id_autor>',methods=['GET'])
def obter_autor_por_id(id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor com id {id_autor} não encontrado'),404
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email

    return jsonify(f'Você buscou o autor {autor_atual}'),200

@app.route('/autores',methods=['POST'])
def novo_autor():
    novo_autor = request.get_json()
    autor = Autor(
        nome=novo_autor['nome'],
        email=novo_autor['email'],
        senha=novo_autor['senha'])

@app.route('/autores/<int:id_autor>',methods=['PUT'])
def alterar_autor(id_autor):
    usuario_a_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    try:
        if not autor:
            return jsonify(f'Autor com id {id_autor} não encontrado'),404
    except:
        pass
    try:
        autor.nome = usuario_a_alterar['nome']
    except:
        pass
    try:    
        autor.email = usuario_a_alterar['email']
    except:
        pass
    try:
        autor.senha = usuario_a_alterar['senha']
    except:
        pass

@app.route('/autores/<int:id_autor>',methods=['DELETE'])
def excluir_autor(id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify(f'Autor com id {id_autor} não encontrado'),404
    db.session.delete(autor_existente)
    db.session.commit()

    return jsonify(f'Autor com id {id_autor} excluído com sucesso'),200
app.run(port=5000, host='localhost', debug=True)
