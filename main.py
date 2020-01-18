"""Importando classes e funções"""

import Conta, json
from menu_transacoes import menu_transacoes
from menu_inicial import menu_inicial


"""Criação de Variáveis"""

lista_correntistas = []
correntista_selecionado = None

"""Funções"""

def opcao_deposita():

    """Função deposita do menu de transações"""

    print("Depositando")
    valor_deposito = float(input("{}, digite o valor a ser depositado: ".format(correntista_selecionado.nome())))
    correntista_selecionado.deposita(valor_deposito)
    print("Seu saldo é: ", correntista_selecionado.saldo())


def opcao_saca():

    """Função saca do menu de transações"""

    print("Sacando")
    valor_saque = float(input("{}, digite o valor a ser sacado: ".format(correntista_selecionado.nome())))
    correntista_selecionado.saca(valor_saque)
    print("Seu saldo é: ", correntista_selecionado.saldo())


def opcao_historico():

    """Função histórico do menu de transações"""

    print("Histórico de ultimas transações:")
    for item in correntista_selecionado:
        print(item)


def cria_conta():

    """Função criação de conta"""

    nome = input("Digite o nome do titular da conta: ").upper()
    cpf = input("Digite o cpf do titular da conta: ")
    saldo = float(input("Digite o saldo inicial do titular da conta: "))
    a = Conta.Conta(nome, cpf, saldo)
    return a


def cria_menu_transacoes():

    """Função criar menu de transações"""

    while True:
        opcao_menu_transacoes = menu_transacoes()
        if opcao_menu_transacoes == 1:
            opcao_deposita()
        elif opcao_menu_transacoes == 2:
            opcao_saca()
        elif opcao_menu_transacoes == 3:
            opcao_historico()
        else:
            break


def imprime_contas():

    """Print todas as contas inseridas noa rquivo json"""

    for c in range(len(lista_correntistas)):
        print(lista_correntistas[c].nome())


def serialize():
    lista_serialize = []
    for conta in lista_correntistas:
        lista_serialize.append(conta.serialize())

    return {
        "Contas": lista_serialize
    }


def salvar():
    with open('banco.json', 'w') as arquivo:
        json.dump(serialize(), arquivo, indent=4)


def carrega_contas():
    with open('banco.json', 'r') as arquivo:
        data = json.load(arquivo)

        for c in range(len(data["Contas"])):
            c1 = Conta.Conta(data["Contas"][c]["nome"], data["Contas"][c]["cpf"], data["Contas"][c]["saldo"])
            lista_correntistas.append(c1)


"""Execução"""


carrega_contas()

while True:

    """Cria menu inicial"""

    opcao_menu_inicial = menu_inicial()

    if opcao_menu_inicial == 1:

        """Cria opção nova conta"""

        conta_nova = cria_conta()
        lista_correntistas.append(conta_nova)

    elif opcao_menu_inicial == 2:

        """Selecionar conta"""

        try:

            imprime_contas()
            conta_selecionada = str(input("Digite o nome do titular: ").upper())

            """Criar menu de transações e execução de transações"""

            for c in range(len(lista_correntistas)):

                if conta_selecionada in lista_correntistas[c].nome():
                    correntista_selecionado = lista_correntistas[c]
                    print("Nome: {}".format(lista_correntistas[c].nome()))
                    print("Saldo: R$ {}".format(lista_correntistas[c].saldo()))
                    cria_menu_transacoes()
                elif (conta_selecionada not in lista_correntistas[c].nome()) and (c == (len(lista_correntistas) -1)):
                    continue
                else:
                    continue

        except ValueError as msg:
            print(msg)

    else:
        salvar()
        break


