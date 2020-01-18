class Conta:
    """Classe"""

    def __init__(self, nome, cpf, saldo):
        """Construtor"""

        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__historico = []
        self.__index = -1

    def __str__(self):
        """String"""

        return "Correntista: {}; Saldo: {}".format(self.__nome, self.__saldo)

    def deposita(self, valor):
        """Depósito"""

        self.__saldo += valor
        self.__historico.append("DEPOSITO: {}".format(valor))

    def saca(self, valor):
        """Saque"""

        if valor <= 0:
            raise ValueError("Valor inválido!")
        else:
            if self.__saldo >= valor:
                self.__saldo -= valor
                self.__historico.append("SAQUE: {}".format(valor))
            else:
                raise ValueError("Saldo insuficiente!")

    def imprime_historico(self):
        """imprimir histórico"""

        print(self.__historico)

    def nome(self):
        """Get nome"""

        return self.__nome

    def saldo(self):
        """Get saldo"""

        return self.__saldo

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        """Iter"""

        self.__index += 1
        if self.__index == len(self.__historico):
            raise StopIteration

        return self.__historico[self.__index]

    def serialize(self):
        return {
            "nome": self.__nome,
            "cpf": self.__cpf,
            "saldo": self.__saldo
        }