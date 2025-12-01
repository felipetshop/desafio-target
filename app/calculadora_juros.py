import datetime

valor_produto = float(input("Digite o valor do produto: R$ "))
print("=" * 40)

data_vencimento = input("Digite a data de vencimento (DD/MM/AAAA): ")
print("=" * 40)
dia, mes, ano = map(int, data_vencimento.split('/'))

dias_vencidos = 0
dia_atual = datetime.date.today().day
if mes < datetime.date.today().month or ano < datetime.date.today().year:
    dias_vencidos = (datetime.date.today() - datetime.date(ano, mes, dia)).days

if dias_vencidos > 0:
    juros_mora = valor_produto * 0.025 * dias_vencidos
    valor_total = valor_produto + juros_mora
    print(f"Juros por mora de {dias_vencidos} dias: R$ {juros_mora:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")