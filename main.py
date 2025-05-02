import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client["BD_MATEUS"]
colecao_tarefas = db["tarefas"]


def obter_proximo_id():
    ultima_tarefa = colecao_tarefas.find_one(sort=[("_id", pymongo.DESCENDING)])
    if ultima_tarefa:
        return ultima_tarefa["_id"] + 1
    else:
        return 1

def adicionar_tarefa(descricao):
    id_tarefa = obter_proximo_id()
    tarefa = {"_id": id_tarefa, "descricao": descricao}
    resultado = colecao_tarefas.insert_one(tarefa)
    print(f"Tarefa adicionada com ID: {id_tarefa}")


def listar_tarefas():
    tarefas = colecao_tarefas.find()
    for tarefa in tarefas:
        print(f"ID: {tarefa['_id']}, Descrição: {tarefa['descricao']}")


def remover_tarefa(id_tarefa):
    id_tarefa = int(id_tarefa)  
    resultado = colecao_tarefas.delete_one({"_id": id_tarefa})
    if resultado.deleted_count == 1:
        print(f"Tarefa com ID {id_tarefa} removida com sucesso.")
    else:
        print(f"Tarefa com ID {id_tarefa} não encontrada.")

while True:
    print("\nOpções:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        descricao = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(descricao)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        id_tarefa = input("Digite o ID da tarefa a ser removida: ")
        remover_tarefa(id_tarefa)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
