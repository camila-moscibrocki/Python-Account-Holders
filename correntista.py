class Correntista:
    def __str__(self):
        return "..."

c = Correntista("Leo", 500.00)

print(c)
print(c.nome())
print(c.saldo())
c.deposita(25.50)
c.saque(50.0)

for hist in c:
    print(hist)
