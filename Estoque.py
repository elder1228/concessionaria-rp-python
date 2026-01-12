estoque = {"Panto": 5, "Sultan": 3, "Comet": 2, "Zentorno": 1}

def consultar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for carro, qtd in estoque.items():
        print(f"{carro}: {qtd} unidades")

def vender_carro(nome):
    if nome in estoque and estoque[nome] > 0:
        estoque[nome] -= 1
        print(f"\n🚀 Venda! Restam {estoque[nome]} de {nome}.")
    else:
        print("\n⚠️ Carro esgotado ou não existe.")

consultar_estoque()
venda = input("\nQual carro foi vendido? ")
vender_carro(venda)
