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

app = Flask(__name__)
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
    pass

@app.route('/autores/<int:id_autor>',methods=['GET'])
def obter_autor_por_id(id_autor):
    pass

@app.route('/autores',methods=['POST'])
def novo_autor():
    pass

@app.route('/autores/<int:id_autor>',methods=['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>',methods=['DELETE'])
def excluir_autor(id_autor):
    pass

app.run(port=5000, host='localhost', debug=True)
