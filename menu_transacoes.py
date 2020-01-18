def menu_transacoes():

    mensagem_erro = "Valor inválido!"
    valor_ok = "Selecionada opção {}"

    while True:
        print("""
    1 - Efetuar depósito
    2 - Efetuar saque
    3 - Histórico detalhado
    4 - Sair 
        """)
        try:
            x = int(input("Selecione uma operação: "))

            if x > 4:
                raise ValueError(mensagem_erro)
            elif x < 0:
                raise ValueError(mensagem_erro)
            else:
                print(valor_ok.format(x))
                return x

        except ValueError as v_e:
            print(v_e)
