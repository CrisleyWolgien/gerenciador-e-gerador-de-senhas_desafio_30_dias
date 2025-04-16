import json
import time
import random
import string
import sys


def abrirArquivo():
    try:
        with open('senhas.json', 'r', encoding="utf-8") as arquivo:
            senhas = json.load(arquivo)
            senhas_personalizadas = senhas.get("senhas_personalizadas", {})
            senhas_aleatorias = senhas.get("senhas_aleatorias", {})
    except (FileNotFoundError, json.JSONDecodeError):
        senhas_personalizadas = {}
        senhas_aleatorias = {}
    return senhas_personalizadas, senhas_aleatorias


def salvarArquivo(senhas_personalizadas, senhas_aleatorias):
    dados = {
        "senhas_personalizadas": senhas_personalizadas,
        "senhas_aleatorias": senhas_aleatorias
    }

    with open("senhas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def adicionarSenhaPersonalizada():  # adicionar senha aleatoria
    senhas_personalizada, senhas_aleatorias = abrirArquivo()

    id_nova_senha = str(
        max([int(k) for k in senhas_personalizada.keys()] + [0]) + 1)

    print("Adicionar nova senha")
    print('-----------------')
    nome = input("Digite o nome da senha: ")
    senha = input("Digite a senha: ")
    apps = input("Digite onde a senha é utilizada separado por vírgula: ")

    app = [item.strip() for item in apps.split(",")]

    senha_personalizada = {
        "name": nome,
        "password": senha,
        "appsUsed": app
    }

    senhas_personalizada[id_nova_senha] = senha_personalizada

    salvarArquivo(senhas_personalizada, senhas_aleatorias)
    print("Senha salva com sucesso")
    time.sleep(1)
    menu()


def gerarSenhaAleatoria():
    print("Adicionar nova senha")
    print('---------------------')

    qntCaractere = input("Digte a quantia de caractere: ")

    while not qntCaractere.isdigit():
        print("Digite um numero valido.")
        qntCaractere = input("Digte a quantia de caractere: ")
    qntCaractere = int(qntCaractere)

    print(f'''
        Tipo de senha:
          [1] - senha Numerica.
          [2] - Senha de letras.
          [3] - Senha de letras e numeros.
          [4] - Senha com caracteres especiais,
          [0] - voltar
          ''')

    tipoDeSenha = input('Digite o tipo de senha que deseja: ')

    while not tipoDeSenha.isdigit():
        print('Digite um resposta valida.')
        tipoDeSenha = input('Digite o tipo de senha que deseja: ')

    match tipoDeSenha:
        case "1":
            senhaNumerica(qntCaractere)
        case "2":
            senhaDeLetras(qntCaractere)
        case "3":
            senhaDeLetreENumero(qntCaractere)
        case "4":
            senhaDeLetreNumeroEEspecial(qntCaractere)
        case "0":
            menu()


def senhaNumerica(qntCaractere):

    senha_personalizada, senhas_aleatoria = abrirArquivo()
    id_nova_senha = str(
        max([int(k) for k in senhas_aleatoria.keys()] + [0]) + 1)

    listSenha = []
    for i in range(qntCaractere):
        i = + 1
        numerosRandom = random.randrange(0, 9)
        numeroDaSenha = numerosRandom
        listSenha.append(numeroDaSenha)
    senha = "".join(str(numero) for numero in listSenha)
    print("Senha criada")
    print("-------------")

    nome = input("Digite o nome da senha: ")
    apps = input("Digite onde a senha é utilizada separado por vírgula: ")

    app = [item.strip() for item in apps.split(",")]

    senha_aleatoria = {
        "name": nome,
        "password": senha,
        "appsUsed": app
    }

    senhas_aleatoria[id_nova_senha] = senha_aleatoria
    salvarArquivo(senha_personalizada, senhas_aleatoria)
    print("Senha salva com sucesso")
    print("-------------------------")
    print(f'''
                Senha
             Nome: {nome}
             Senha: {senha}
             Apps usados: {app}
              ''')
    time.sleep(1)
    menu()


def senhaDeLetras(qntCaractere):
    senha_personalizada, senhas_aleatoria = abrirArquivo()
    id_nova_senha = str(
        max([int(k) for k in senhas_aleatoria.keys()] + [0]) + 1)

    letraMinuscula = False
    letraMaiuscula = False

    while not letraMinuscula or letraMaiuscula:
        senha = ''.join(random.choices(string.ascii_letters,
                        k=(qntCaractere)))  # cria a  senha

        for char in senha:  # verifica se possui caractere maiusculo e minusculo
            if char.isupper():
                letraMaiuscula = True

            else:
                letraMinuscula = True
    print(senha)

    print("Senha criada")
    print("-------------")

    nome = input("Digite o nome da senha: ")
    apps = input("Digite onde a senha é utilizada separado por vírgula: ")

    app = [item.strip() for item in apps.split(",")]

    senha_aleatoria = {
        "name": nome,
        "password": senha,
        "appsUsed": app
    }

    senhas_aleatoria[id_nova_senha] = senha_aleatoria
    salvarArquivo(senha_personalizada, senhas_aleatoria)
    print("Senha salva com sucesso")
    print("-------------------------")
    print(f'''
                Senha
             Nome: {nome}
             Senha: {senha}
             Apps usados: {app}
              ''')
    time.sleep(1)
    menu()


def senhaDeLetreENumero(qntCaractere):
    senha_personalizada, senhas_aleatoria = abrirArquivo()
    id_nova_senha = str(
        max([int(k) for k in senhas_aleatoria.keys()] + [0]) + 1)

    letraMinuscula = False
    letraMaiuscula = False
    numero = False

    # verifica se contem letras e numeros
    while not (letraMinuscula and letraMaiuscula and numero):

        caractere = string.ascii_letters + string.digits
        senha = ''.join(random.choices(
            caractere,  k=(qntCaractere)))  # cria a  senha
        for char in senha:  # verifica se possui caractere maiusculo e minusculo
            if char.isupper():
                letraMaiuscula = True

            elif char.islower():
                letraMinuscula = True

            else:
                numero = True

    print(senha)

    print("Senha criada")
    print("-------------")

    nome = input("Digite o nome da senha: ")
    apps = input("Digite onde a senha é utilizada separado por vírgula: ")

    app = [item.strip() for item in apps.split(",")]

    senha_aleatoria = {
        "name": nome,
        "password": senha,
        "appsUsed": app
    }

    senhas_aleatoria[id_nova_senha] = senha_aleatoria
    salvarArquivo(senha_personalizada, senhas_aleatoria)
    print("Senha salva com sucesso")
    print("-------------------------")
    print(f'''
                Senha
             Nome: {nome}
             Senha: {senha}
             Apps usados: {app}
              ''')
    time.sleep(1)
    menu()


def senhaDeLetreNumeroEEspecial(qntCaractere):
    senha_personalizada, senhas_aleatoria = abrirArquivo()
    id_nova_senha = str(
        max([int(k) for k in senhas_aleatoria.keys()] + [0]) + 1)

    letraMinuscula = False
    letraMaiuscula = False
    numero = False
    caractereEspecial = False

    especiais_permitidos = "@#!?$%&*"

    # verifica se contem letras e numeros
    while not (letraMinuscula and letraMaiuscula and numero and caractereEspecial):

        caractere = string.ascii_letters + string.digits + especiais_permitidos
        senha = ''.join(random.choices(
            caractere,  k=(qntCaractere)))  # cria a  senha
        for char in senha:  # verifica se possui caractere maiusculo e minusculo
            if char.isupper():
                letraMaiuscula = True

            elif char.islower():
                letraMinuscula = True

            elif char.isdigit():
                numero = True

            elif char in especiais_permitidos:
                caractereEspecial = True
    print(senha)

    print("Senha criada")
    print("-------------")

    nome = input("Digite o nome da senha: ")
    apps = input("Digite onde a senha é utilizada separado por vírgula: ")

    app = [item.strip() for item in apps.split(",")]

    senha_aleatoria = {
        "name": nome,
        "password": senha,
        "appsUsed": app
    }

    senhas_aleatoria[id_nova_senha] = senha_aleatoria
    salvarArquivo(senha_personalizada, senhas_aleatoria)
    print("Senha salva com sucesso")
    print("-------------------------")
    print(f'''
                Senha
             Nome: {nome}
             Senha: {senha}
             Apps usados: {app}
              ''')
    time.sleep(1)
    menu()


def listarSenhas():
    senhas_personalizadas, senhas_aleatorias = abrirArquivo()

    print("listar Senhas:")
    print("---------------")
    print("Senhas Personalizadas:")

    for id, senha_personalizada in senhas_personalizadas.items():
        print(f'''
              
              Nome: {senha_personalizada["name"]}
              Senha: {senha_personalizada["password"]}
              Apps usados: {senha_personalizada["appsUsed"]}

          ------------------
               ''')

    print("Senhas Aleatorias:")

    for id, senha_aleatoria in senhas_aleatorias.items():
        print(f'''
              Nome: {senha_aleatoria["name"]}
              Senha: {senha_aleatoria["password"]}
              Apps usados: {senha_aleatoria["appsUsed"]}

          ------------------
               ''')
    time.sleep(1)
    menu()


def excluirSenha():
    print("Excluir senha")
    print("---------------")
    print("")
    print('''
           Selecione o tipo de senha:
          
          [1] - senha Personalizada.
          [2] - Senha Aleatoria.
          [0] - voltar
          ''')

    SelecaoSenha = input("Digite um numero: ")

    while not SelecaoSenha.isdigit():
        print("Digite um numero valido.")
        SelecaoSenha = input("Digite um numero: ")

    match SelecaoSenha:
        case "1":
            excluirSenhaPersonalizada()
        case "2":
            excluirSenhaAleatoria()
        case "0":
            menu()


def excluirSenhaPersonalizada():
    senhas_personalizadas, senhas_aleatorias = abrirArquivo()

    print("Selecione a senha que deseja excluir:")
    print("Senhas Personalizadas:")

    for id, senha_personalizada in senhas_personalizadas.items():
        print(f'''
              
              ID: {id}
              Nome: {senha_personalizada["name"]}
              Senha: {senha_personalizada["password"]}

          ------------------
               ''')

    senhaEscolhida = input("Digite o ID da senha escolhida: ")

    while senhaEscolhida not in senhas_personalizadas:
        print("Digite uma senha existente")
        senhaEscolhida = input("Digite o ID da senha escolhida: ")

    del senhas_personalizadas[senhaEscolhida]
    salvarArquivo(senhas_personalizadas, senhas_aleatorias)
    print("Senha Removida com sucesso")
    time.sleep(1)
    menu()


def excluirSenhaAleatoria():

    senhas_personalizadas, senhas_aleatorias = abrirArquivo()

    print("Selecione a senha que deseja excluir:")
    print("Senhas Personalizadas:")

    for id, senha_aleatoria in senhas_aleatorias.items():
        print(f'''
              
              ID: {id}
              Nome: {senha_aleatoria["name"]}
              Senha: {senha_aleatoria["password"]}

          ------------------
               ''')

    senhaEscolhida = input("Digite o ID da senha escolhida: ")

    while senhaEscolhida not in senhas_aleatorias:
        print("Digite uma senha existente")
        senhaEscolhida = input("Digite o ID da senha escolhida: ")

    del senhas_aleatorias[senhaEscolhida]
    salvarArquivo(senhas_personalizadas, senhas_aleatorias)
    print("Senha Removida com sucesso")
    time.sleep(1)
    menu()


def editarSenha():
    print("Editar Senha")
    print("----------------")
    print("")
    print('''
           Selecione o tipo de senha:
          
          [1] - senha Personalizada.
          [2] - Senha Aleatoria.
          [0] - voltar
          ''')
    SelecaoSenha = input("Digite um numero: ")

    while not SelecaoSenha.isdigit():
        print("Digite um numero valido.")
        SelecaoSenha = input("Digite um numero: ")

    match SelecaoSenha:
        case "1":
            editarSenhaPersonalizada()
        case "2":
            editarSenhaAleatoria()
        case "0": 
            menu()


def editarSenhaPersonalizada():
    senhas_personalizadas, senhas_aleatorias = abrirArquivo()

    print("Selecione a senha que deseja editar:")
    print("Senhas Personalizadas:")

    for id, senha_personalizada in senhas_personalizadas.items():
        print(f'''
              ID: {id}
              Nome: {senha_personalizada["name"]}
              Senha: {senha_personalizada["password"]}
          ------------------
        ''')

    senhaEscolhida = input("Digite o ID da senha escolhida: ")
    while senhaEscolhida not in senhas_personalizadas:
        print("Digite uma senha existente.")
        senhaEscolhida = input("Digite o ID da senha escolhida: ")

    print('''
           Selecione o que deseja editar:
          [1] - Nome
          [2] - Senha
          [3] - Apps usados 
          [0] - voltar
    ''')

    opcaoSelecionada = input("Digite o número da opção: ")
    while not opcaoSelecionada.isdigit():
        print("Digite um número válido.")
        opcaoSelecionada = input("Digite o número da opção: ")

    match opcaoSelecionada:
        case "1":
            modificaNome(senhas_personalizadas, senhas_aleatorias, senhaEscolhida, True)
        case "2":
            modifcaSenha(senhas_personalizadas, senhas_aleatorias, senhaEscolhida, True)
        case "3":
            modificaApps(senhas_personalizadas, senhas_aleatorias, senhaEscolhida, True)
        case "0": 
            editarSenha()


def editarSenhaAleatoria():
    senhas_personalizadas, senhas_aleatorias = abrirArquivo()

    print("Selecione a senha que deseja editar:")
    print("Senhas Aleatórias:")

    for id, senha_aleatoria in senhas_aleatorias.items():
        print(f'''
              ID: {id}
              Nome: {senha_aleatoria["name"]}
              Senha: {senha_aleatoria["password"]}
          ------------------
        ''')

    senhaEscolhida = input("Digite o ID da senha escolhida: ")
    while senhaEscolhida not in senhas_aleatorias:
        print("Digite uma senha existente.")
        senhaEscolhida = input("Digite o ID da senha escolhida: ")

    print('''
           Selecione o que deseja editar:
          [1] - Nome
          [2] - Senha
          [3] - Apps usados 
          [0] - voltar
    ''')

    opcaoSelecionada = input("Digite o número da opção: ")
    while not opcaoSelecionada.isdigit():
        print("Digite um número válido.")
        opcaoSelecionada = input("Digite o número da opção: ")

    match opcaoSelecionada:
        case "1":
            modificaNome(senhas_aleatorias, senhas_personalizadas, senhaEscolhida, False)
        case "2":
            modifcaSenha(senhas_aleatorias, senhas_personalizadas, senhaEscolhida, False)
        case "3":
            modificaApps(senhas_aleatorias, senhas_personalizadas, senhaEscolhida, False)
        case "0":
            editarSenha()




def modificaNome(dicionario_alvo, outro_dicionario, id, eh_personalizada):
    novo_nome = input("Digite o novo nome: ")
    dicionario_alvo[id]["name"] = novo_nome
    if eh_personalizada:
        salvarArquivo(dicionario_alvo, outro_dicionario)
    else:
        salvarArquivo(outro_dicionario, dicionario_alvo)
    print("Nome atualizado com sucesso!")
    editarNovamente = input("Deseja editar novamente? (S/N): ")

    while editarNovamente.upper() not in ["S", "N"]:
        print("Digite uma opção válida.")
        editarNovamente = input("Deseja editar novamente? (S/N): ")

    if editarNovamente.upper() == "S":
        time.sleep(1)
        editarSenha()
    else:
        time.sleep(1)
        menu()

def modifcaSenha(dicionario_alvo, outro_dicionario, id, eh_personalizada):
    nova_senha = input("Digite a nova senha: ")
    dicionario_alvo[id]["password"] = nova_senha
    if eh_personalizada:
        salvarArquivo(dicionario_alvo, outro_dicionario)
    else:
        salvarArquivo(outro_dicionario, dicionario_alvo)
    print("Senha atualizada com sucesso!")
    editarNovamente = input("Deseja editar novamente? (S/N): ")

    while editarNovamente.upper() not in ["S", "N"]:
        print("Digite uma opção válida.")
        editarNovamente = input("Deseja editar novamente? (S/N): ")

    if editarNovamente.upper() == "S":
        time.sleep(1)
        editarSenha()
    else:
        time.sleep(1)
        menu()

def modificaApps(dicionario_alvo, outro_dicionario, id, eh_personalizada):
    apps = input("Digite onde a senha é utilizada, separado por vírgula: ")
    app_list = [item.strip() for item in apps.split(",")]
    dicionario_alvo[id]["appsUsed"] = app_list
    if eh_personalizada:
        salvarArquivo(dicionario_alvo, outro_dicionario)
    else:
        salvarArquivo(outro_dicionario, dicionario_alvo)
    print("Apps usados atualizados com sucesso!")
    editarNovamente = input("Deseja editar novamente? (S/N): ")

    while editarNovamente.upper() not in ["S", "N"]:
        print("Digite uma opção válida.")
        editarNovamente = input("Deseja editar novamente? (S/N): ")

    if editarNovamente.upper() == "S":
        time.sleep(1)
        editarSenha()
    else:
        time.sleep(1)
        menu()




def menu():
    while True:
        print("Bem-vindo ao gerenciador de senhas")
        print("Selecione a opção desejada:")
        print('''
        [1] - Adicionar senha personalizada
        [2] - Listar senhas 
        [3] - Remover senha
        [4] - Gerar senha aleatória
        [5] - Editar senha 
        [0] - Sair
        ''')

        opcao = input("Digite o número da opção escolhida: ")

        if opcao not in ["0", "1", "2", "3", "4", "5"]:
            print("Opção inválida! Tente novamente.\n")
            continue

        match opcao:
            case "1":
                adicionarSenhaPersonalizada()
            case "2":
                listarSenhas()
            case "3":
                excluirSenha()
            case "4":
                gerarSenhaAleatoria()
            case "5":
                editarSenha()
            case "0":
                print("Saindo... Até logo!")
                sys.exit()



menu()
