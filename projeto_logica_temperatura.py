
# Lista com nomes dos meses
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Lista para armazenar as temperaturas maximas
temperaturas = []

# Entrada de dados com validação
for i in range(12):
    while True:
        try:
            entrada = input(f"Digite a temperatura maxima para o mes {meses[i].capitalize()} (em °C): ")
            temp = float(entrada.replace(',', '.'))
            if -60 <= temp <= 50:
                temperaturas.append(temp)
                break
            else:
                print("Temperatura fora do intervalo permitido (-60°C a +50°C). Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Calculos
media = sum(temperaturas) / 12
meses_escaldantes = sum(1 for t in temperaturas if t >= 33)
indice_max = temperaturas.index(max(temperaturas))
indice_min = temperaturas.index(min(temperaturas))

# Resultados
print("\n Resultados:")
print(f"Temperatura média máxima anual: {media:.2f}°C")
print(f"Quantidade de meses escaldantes (>33°C): {meses_escaldantes}")
print(f"Mês mais escaldante do ano: {meses[indice_max].capitalize()}")
print(f"Mês menos quente do ano: {meses[indice_min].capitalize()}")
input("\nPressione enter para sair...")
