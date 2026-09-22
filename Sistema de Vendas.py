maior_igual100 = 0
maior = 0
total = 0

n = int(input("Informe a quantidade de vendas realizadas no dia: "))
if n == 8:
    for i in range(n):
        valor = int(input("Informe o valor da venda: "))
        if valor >= 100:
            maior_igual100 += 1
        total += valor
        media = total/n
        
        if valor > maior:
            maior = valor

print(f"Valor total da venda: {total:.2f}")
print(f"Vendas que foram maiores ou iguais a R$100: {maior_igual100}")
print(f"Média da venda: {media}")
print(f"Maior venda: {maior}")