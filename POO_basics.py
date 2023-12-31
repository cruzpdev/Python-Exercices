# TUTORIAL DE PROGRAMAÇÃO ORIENTADA A OBJETOS COM PYTHON

# CRIANDO E USANDO CLASSES/COMO ORIENTAÇÃO A OBJETOS É APLICADA.

# 1. classes e instâncias.
"""
CLASSES são usadas na maioria das linguagens de programação orientadas a objetos para criar objetos. Elas nos permitem agrupar logicamente dados e funções de uma forma fácil de reutilizar e também modificar, se necessário. IMPORTANTE:quando falamos de CLASSES, Os dados são representados por "atributos" e as funções que operam sobre esses dados são chamadas de "métodos".
DATA = ATTRIBUTES
FUNCTIONS = METHODS

exemplo: uma aplicação para gerenciar funcionários de uma empresa. Podemos criar uma classe chamada Employee que pode conter os atributos e métodos que definem um funcionário. Isso significa que dentro da classe Employee, podemos especificar os atributos e métodos que todos os funcionários devem ter. Depois de criar essa classe, podemos criar instâncias individuais de cada funcionário com seus atributos e métodos específicos. As instâncias são objetos criados a partir de uma classe específica.
"""

"""
class Employee: #criando uma classe
    pass
# funcionario1 e 2 são instâncias da classe Employee
funcionario1 = Employee()
funcionario2 = Employee()

# printar instâncias de uma classe retorna o endereço de memória onde elas estão armazenadas.
print(funcionario1) #<__main__.Employee object at 0x00000228FC051820>
print(funcionario2) #<__main__.Employee object at 0x00000228FC051790>

# As variáveis de instancia (instance variables) contêm ATRIBUTOS(data) únicos para cada instância.
funcionario1.nome = "Paulo"
funcionario1.sobrenome = "Cruz"
funcionario1.email = "Paulo.Cruz@company.com"
funcionario1.salario = 10000

funcionario2.nome = "Test"
funcionario2.sobrenome = "User"
funcionario2.email = "Test.User@company.com"
funcionario2.salario = 6000

print(funcionario1.email) # Paulo.Cruz@company.com
print(funcionario2.email) # Test.User@company.com

#Você não está tirando vantagem das classes dessa forma.

#Vamos setar todas essas informações de uma vez só, usando um método especial chamado __init__ (construtor). Agora, ao criar métodos dentro de uma classe, eles receberão a instância(self) como primeiro argumento

class Employee:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome}.{sobrenome}@company.com"
        self.salario = salario

funcionario1 = Employee("Paulo", "Cruz", 10000)
funcionario2 = Employee("Test", "User", 6000)
print(funcionario1.email) # Paulo.Cruz@company.com
print(funcionario2.email) # Test.User@company.com

#Vamos dizer que você queira um método que retorne o nome completo do funcionário. Você pode criar um método dentro da classe Employee que faça isso para você.

class Employee:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome}.{sobrenome}.company.com"
        self.salario = salario
    
    def fullname(self):
        return f"{self.nome} {self.sobrenome}"

funcionario1 = Employee("Paulo", "Cruz", 10000)
funcionario2 = Employee("Test", "User", 6000)

#duas formas de observar o nome completo do funcionário.

# 1. usando o método fullname() dentro da classe Employee. Classe > método > instância. Esse é o jeito mais seguro. 
print(Employee.fullname(funcionario1)) # Paulo Cruz

# 2. usando o método fullname() fora da classe Employee. Aqui o método é chamado pela instância. Instância > método. note que como fullname é um método, ele precisa de parênteses.
print (funcionario2.fullname()) # Test User
"""
# 2. Variáveis de classe.
"""class variables serão variaveis compartilhadas por todas as instâncias. vamos criar uma variável de classe que aumenta o salário de todos os funcionários em 10%.
class Employee:
    aumento = 1.1 # variável de classe
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario
    def fullname(self):
        return f"{self.nome} {self.sobrenome}"
    def dar_aumento(self): # método que aumenta o salário do funcionário
        self.salario = int(self.salario * self.aumento)

funcionario1 = Employee("Paulo", "Cruz", 10000)
funcionario2 = Employee("Test", "User", 6000)

print (funcionario1.salario) # 10000
funcionario1.dar_aumento()
print (funcionario1.salario) # 11000

# Outro exemplo. agora, vamos criar uma variável de classe que conta o número de funcionários na empresa. Para isso, vamos colocar uma incrementação dessa variável no construtor toda vez que uma nova instância for criada.

class Employee:
    qtd_funcionarios = 0 # variável de classe
    aumento = 1.1 # variável de classe
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario

        Employee.qtd_funcionarios += 1 # incrementação da variável de classe
    
    def fullname(self):
        return f"{self.nome} {self.sobrenome}"
    
    def dar_aumento(self):
        self.salario = int(self.salario * self.aumento)

print(Employee.qtd_funcionarios) # 0        
funcionario1 = Employee("Paulo", "Cruz", 10000)
funcionario2 = Employee("Test", "User", 6000)
print(Employee.qtd_funcionarios) # 2
"""
# 3. Métodos de classe e métodos estáticos (classmethods/staticmethods).
"""
um método regular automaticamente recebe a instância(self) como primeiro argumento. Métodos de classe recebem a classe(cls) como primeiro argumento. Métodos estáticos não recebem nada automaticamente. Eles se comportam como funções normais, mas estão dentro da classe porque têm alguma relação com a classe.
#Vamos criar um método de classe para setar o aumento de salário de todos os funcionários, ao invés de mudar a variavel de classe. Para isso, vamos usar o decorator @classmethod.

class Employee:
    qtd_funcionarios = 0
    aumento = 1.1
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario

        Employee.qtd_funcionarios += 1
    
    def fullname (self):
        return f"{self.nome} {self.sobrenome}"
    
    def dar_aumento(self):
        self.salario = int(self.salario * self.aumento)

    @classmethod # decorator
    def set_aumento(cls, aumento): # cls = classe
        cls.aumento = aumento

funcionario1 = Employee("Paulo", "Cruz", 10000)
funcionario2 = Employee("Test", "User", 6000)

print (Employee.aumento) # 1.1
print (funcionario1.aumento) # 1.1
print (funcionario2.aumento) # 1.1

Employee.set_aumento(100) #setando a variavel aumento via método de classe

print (Employee.aumento) # 100
print (funcionario1.aumento) # 100
print (funcionario2.aumento) # 100

# vamos dizer que outro dev está usando uma lista de funcionarios de strings strings separadas por hífen. Vamos utilizar um classmethod como construtor para receber uma string e retornar o objeto funcionario da mesma forma que a nossa classe Employee.
class Employee:
    qtd_funcionarios = 0
    aumento = 1.1
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario

        Employee.qtd_funcionarios += 1
    
    def fullname (self):
        return f"{self.nome} {self.sobrenome}"
    
    def dar_aumento(self):
        self.salario = int(self.salario * self.aumento)
    
    @classmethod
    def set_aumento(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def from_string(cls, funcionario_string): # use como argumentos a classe employee e funcionários que sejam uma string separada por hífen
        nome, sobrenome, salario = funcionario_string.split("-") # separa a string nos hifens em uma lista de strings
        return cls(nome, sobrenome, salario) # retorna um objeto funcionario com os atributos da string

funcionariostr1 = "Paulo-Cruz-10000"
funcionariostr2 = "Test-User-6000"
funcionariostr3 = "John-Doe-8000"

funcionario1 = Employee.from_string(funcionariostr1) # criando um objeto funcionario a partir de uma string

# métodos estáticos: não recebem nada automaticamente. Eles se comportam como funções normais, mas estão dentro da classe porque têm alguma relação com a classe. Vamos criar um método estático que recebe uma data e retorna se é dia útil(trabalho) ou não.

class Employee:
    qtd_funcionarios = 0
    aumento = 1.1
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario

        Employee.qtd_funcionarios += 1
            
    def fullname (self):
        return f"{self.nome} {self.sobrenome}"
    
    def dar_aumento(self):
        self.salario = int(self.salario * self.aumento)

    @classmethod
    def set_aumento(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def from_string (cls, funcionario_string):
        nome, sobrenome, salario = funcionario_string.split("-")
        return cls(nome, sobrenome, salario)
    
    @staticmethod # decorator
    def dia_util(dia): # Metodo estático. não recebe nada automaticamente
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

#descobrindo se uma data é dia util ou não
import datetime
data = datetime.date(2023, 11, 2) 
print (Employee.dia_util(data)) #True - quinta feira

""" 
# 4. Herança - criando subclasses
"""
heranças são usadas para criar subclasses que herdam todos os atributos e métodos da classe pai. Isso permite que você crie subclasses com comportamentos específicos sem afetar a classe pai. Vamos criar as subclasses Developer e Manager que herdam todos os atributos e métodos da classe Employee.

class Employee:
    
    aumento = 1.04
    
    def __init__ (self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario

    def fullname (self):
        return f"{self.nome} {self.sobrenome}"
    
    def dar_aumento(self):
        self.salario = int(self.salario * self.aumento)

class Developer(Employee):
    
    aumento = 1.10 #aumento específico da classe Developer
    
    def __init__(self, nome, sobrenome, salario, linguagem):
        super().__init__(nome, sobrenome, salario)
        self.linguagem = linguagem #adicionei um atributo específico da classe Developer

class Manager(Employee):
    
    aumento = 1.20 #aumento específico da classe Manager
    
    def __init__(self, nome, sobrenome, salario, subordinados=None): #adicionei um atributo específico da classe Manager
        super().__init__(nome, sobrenome, salario)
        if subordinados is None:
            self.subordinados = []
        else:
            self.subordinados = subordinados
    
    def add_subordinado(self, subordinado): #método para adicionar subordinados
        if subordinado not in self.subordinados:
            self.subordinados.append(subordinado)
    
    def remove_subordinado(self, subordinado): #método para remover subordinados
        if subordinado in self.subordinados:
            self.subordinados.remove(subordinado)

    def print_subordinados(self): #método para printar subordinados
        for subordinado in self.subordinados:
            print("-->", subordinado.fullname())

dev_1 = Developer('Paulo', 'Cruz', 10000, 'python')
dev_2 = Employee('Test','User', 6000)
mgr_1 = Manager('Sue', 'Smith', 9000)

"""
# 5. Métodos especiais (magic methods ou dunder methods)
"""
Métodos especiais são métodos que permitem que você crie funcionalidades específicas para suas classes que não são facilmente representadas como métodos regulares. Eles são sempre escritos com __ antes e depois do nome do método. Vamos criar um método especial que retorna a representação de repr (representação exata da construção do objeto) do objeto. um segundo método para retornar uma string er outro método especial que retorna a soma dos salários de dois objetos Employee. por ultimo, um método len que retorna o número de caracteres do nome completo do funcionário.
class Employee:

    def __init__ (self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"
        self.salario = salario
    
    def fullname (self):
        return f"{self.nome} {self.sobrenome}"

    def __repr__ (self): # método especial para retornar a representação de repr do objeto
        return f"Employee('{self.nome}', '{self.sobrenome}', '{self.salario}')"
    
    def __str__(self): # método especial para retornar uma string
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other): # método especial para retornar a soma dos salários de dois objetos Employee
        return self.salario + other.salario
    
    def __len__(self): # método especial para retornar o número de caracteres do nome completo do funcionário
        return len(self.fullname())

dev_1 = Employee('Paulo', 'Cruz', 10000)
dev_2 = Employee('Test','User', 6000)

print (dev_1 + dev_2) # 16000
print (len(dev_1)) # 10
"""
# 6  Decoradores de propriedade - getters, setters e deleters
"""
# Decoradores de propriedade são uma maneira de definir métodos getter, setter e deleters sem usar a sintaxe de métodos. Eles permitem que você defina um método, mas acesse-o como um atributo. 

class Employee:
    def __init__ (self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{nome.lower()}.{sobrenome.lower()}@company.com"

    def fullname (self):
        return f"{self.nome} {self.sobrenome}"
    
funcionario1 = Employee("Paulo", "Cruz")

print (funcionario1.nome) # Paulo
print (funcionario1.email) # paulo.cruz@company.com
print (funcionario1.fullname()) # Paulo Cruz
# vamos dizer que o funcionário mudou de nome. 
funcionario1.nome = "Test"
# apesar do atributo nome ter mudado na instancia funcionario1, o email não mudou, porque ele foi criado pelo construtor __init__. Vamos criar um decorador de propriedade para o email do funcionário e usar o metodo getter.  
O método getter é usado para retornar o valor de um atributo privado. Para isso, vamos usar o decorator @property.
class Employee:
    def __init__ (self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    @property # decorator, método getter
    def email(self): 
        return f"{self.nome.lower()}.{self.sobrenome.lower()}@company.com"
    
#agora, o email é um atributo e não um método. 

#imagine que você queira mudar o fullname do funcionário. Você não pode fazer isso porque o email é um atributo e não um método. Para isso, vamos usar o método setter.
    @property
    def fullname (self):
        return f"{self.nome} {self.sobrenome}"
    
    @fullname.setter # método setter
    def fullname(self, nome): 
        nome, sobrenome = nome.split(" ")
        self.nome = nome
        self.sobrenome = sobrenome 
    
    @fullname.deleter # método deleter
    def fullname(self):
        print("Deletando nome completo!")
        self.nome = None
        self.sobrenome = None

# agora, podemos mudar o fullname do funcionário e as informações vão mudar junto.
funcionario1 = Employee("Paulo", "Cruz")
funcionario1.fullname = "Test User"
print (funcionario1.nome) # Test
print (funcionario1.email) # test.user@company
print (funcionario1.fullname) # Test User

# deletando o funcionario:
del funcionario1.fullname # Deletando nome completo!
"""
# 7 classes e métodos abstratos
"""
from abc import ABC, abstractmethod

CLASSES ABSTRATAS: São modelos para outras classes que poderão ser criadas, não podendo ser instanciadas.

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade (self, num):
        pass
    
    @abstractmethod
    def reduzir_claridade (self, num):
       pass

class MonitorFullHD (Monitor):
    def aumentar_claridade (self, num):
        print(f"Aumentando a claridade em {num}%")
    def reduzir_claridade (self, num):
        print(f"Reduzindo a claridade em {num}%")

monitor = MonitorFullHD()
monitor.aumentar_claridade(10)
"""
# 8 polimorfismo
"""
 POLIMORFISMO: É o principio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes.

class Carro:
    def ligar(self):
        print("Ligando o carro...")
class Moto:
    def ligar(self):
        print("Ligando a moto...")

def iniciar (veiculo): #método polimórfico
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar (carro) # Ligando o carro...
iniciar (moto) # Ligando a moto..."""