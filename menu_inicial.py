def menu_inicial():

    mensagem_erro = "Valor inválido!"
    valor_ok = "opção selecionada{}"

    while True:
        print("""
    1 - Crie uma conta
    2 - Selecione  uma conta
    3 - Sair do menu inicial 
        """)
        try:
            x = int(input("Selecione uma das opções abaixo:"))

            if x > 3:
                raise ValueError(mensagem_erro)
            elif x < 0:
                raise ValueError(mensagem_erro)
            else:
                print(valor_ok.format(x))
                return x

        except ValueError as v_e:
            print(v_e)


