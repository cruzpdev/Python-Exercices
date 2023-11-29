from flask import Flask, jsonify, request
app = Flask(__name__)
musicas = [
    {
        'título': 'saga de um vaqueiro',
        'banda': 'Catuaba com amendoin'
    },
    {
        'título': 'Territory',
        'banda': 'Sepultura'	
    },
    {
        'título': 'Hey Bulldog',
        'banda': 'Beatles'
    }
]

#ROTA PADRÃO - GET http://localhost:5000
@app.route('/musicas')
def consultar_musica():
    return jsonify(musicas)

#GET COM ID - GET http://localhost:5000/musicas/2
@app.route('/musicas/<int:id>',methods = ['GET'])
def consultar_musica_id(id):
    return jsonify(musicas[id])

# POST -  http://localhost:5000/musicas
@app.route('/musicas', methods = ['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(f'A música {musica} foi adicionada com sucesso',200)

# PUT -  http://localhost:5000/musicas/0
@app.route('/musicas/<int:id>', methods=['PUT'])
def alterar_musica(id):
    musica_alterada = request.get_json()
    musicas[id].update(musica_alterada)
    return jsonify(musicas[id],200)

# DELETE -  http://localhost:5000/musicas/0
@app.route('/musicas/<int:id>', methods=['DELETE'])
def excluir_musica(id):
    try:
        if musicas[id] is not None:
            del musicas[id]
            return jsonify({"mensagem":"musica deletada"})
    except:
        return jsonify("musica não encontrada",404)

if __name__ == '__main__':
    app.run (port = 5000, host = 'localhost', debug = True)