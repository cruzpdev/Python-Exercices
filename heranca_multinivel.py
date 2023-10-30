class usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao
    
    def registrar_funcionario(self):
        print(f'Funcionário(a) {self.nome} registrado com sucesso!')

# Classe Gestor herda da classe usuario
class gestor(usuario):
    def __init__(self, nome, salario, profissao, setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel
    
    def definir_setor(self, setor):
        print(f'Definindo o setor para {setor}')

usuario1 = usuario('João', 2000, 'Analista') # Instanciando a classe usuario
usuario1.registrar_funcionario() 

gestor1 = Gestor('Maria', 5000, 'Gestora', 'TI') # Instanciando a classe Gestor
gestor1.registrar_funcionario() 


#evite usar mais de dois niveis! 