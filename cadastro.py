funcionarios = {}
prox_id = 1

while True:
    nome = input("Nome (ou digite 'exit' para sair):\n")
    if nome.lower() == 'exit':
        break

    if nome.isdigit():
        print("Erro: O nome não pode ser um número.")
        continue
    
    if not nome.strip():
        print("Erro: Por favor, insira um nome válido.")
        continue
    
    idade = None
    salario = None

    try:
        idade = int(input("Idade:\n"))
        salario = float(input("Salário:\n"))
        if salario < 0:
            raise ValueError("Salário não pode ser negativo.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
            
    funcionario = {"nome": nome, "idade": idade, "salário": salario}
    funcionarios[prox_id] = funcionario
    prox_id += 1
    
for id, funcionario in funcionarios.items():
    if funcionario ["idade"] is not None and funcionario["salário"] is not None:
        print (f"ID: {id}, Nome: {funcionario['nome']}, Idade: {funcionario['idade']}, Salário: {funcionario['salário']:.2f}")