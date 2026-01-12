# ==========================================
# SISTEMA DE ESTOQUE - CONCESSIONÁRIA RP
# ==========================================

estoque = {
    "Panto": 5,
    "Sultan": 3,
    "Comet": 2,
    "Zentorno": 1
}

def consultar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for carro, quantidade in estoque.items():
        status = "✅ DISPONÍVEL" if quantidade > 0 else "❌ ESGOTADO"
        print(f"{carro}: {quantidade} unidades [{status}]")

def vender_carro(nome_carro):
    if nome_carro in estoque:
        if estoque[nome_carro] > 0:
            estoque[nome_carro] -= 1
            print(f"\n🚀 Venda realizada! Restam {estoque[nome_carro]} unidades de {nome_carro}.")
        else:
            print(f"\n⚠️ Erro: O {nome_carro} está esgotado!")
    else:
        print("\n❓ Esse carro não existe no sistema.")

# --- Testando o Sistema ---
consultar_estoque()

venda = input("\nQual carro foi vendido? ")
vender_carro(venda)

consultar_estoque()
