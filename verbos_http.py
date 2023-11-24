#como usar 4 principais comandos (verbos) de uma API (GET, POST, PUT, DELETE)
import requests
from pprint import pprint

# GET
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#get com id, para pegar um item especifico (id 2)
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_com_id.json())

# POST - criar um novo recurso
nova_tarefa = {'completed': False,
               'title': 'Lavar o carro',
               'userId': 1}
resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)
#pprint(resultado_post.json())

# PUT - atualizar um recurso
tarefa_alterada = {'completed': False,
               'title': 'Lavar a moto',
               'userId': 1}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)

#pprint(resultado_put.json())
#DELETE - deletar um recurso
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())