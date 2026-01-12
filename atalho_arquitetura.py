import webbrowser
import os

# --- FUNÇÃO DA CALCULADORA ---
def calculadora_obra():
    print("\n--- 🏗️ CALCULADORA DE OBRA INTEGRADA ---")
    largura = float(input("Digite a largura (metros): "))
    comprimento = float(input("Digite o comprimento/altura (metros): "))
    area = largura * comprimento
    print(f"✅ Área Total: {area:.2f} m²")
    
    tinta = input("Deseja calcular a tinta para essa área? (s/n): ")
    if tinta.lower() == 's':
        demãos = int(input("Quantas demãos? "))
        total_litros = (area * demãos) / 10
        print(f"✅ Você precisará de {total_litros:.2f} litros de tinta.")

# --- CONFIGURAÇÃO DO WORKSPACE ---
opcoes = {
    "1": ("ArchDaily (Inspiração)", "https://www.archdaily.com.br"),
    "2": ("Pinterest (Plantas e Cortes)", "https://www.pinterest.com"),
    "3": ("BIMobject (Objetos 3D)", "https://www.bimobject.com"),
    "4": ("AutoCAD / Revit", "C:/Caminho/Para/Seu/Programa.exe"), 
    "5": ("Pasta de Projetos (Local)", "C:/Users/Documentos/Arquitetura"),
    "6": ("YouTube (Tutoriais de Render)", "https://www.youtube.com"),
    "7": ("Calculadora de Obra (Ferramenta)", "INTERNO") # Nova opção!
}

def exibir_menu():
    print("\n" + "="*30)
    print("📐 CENTRAL DE ARQUITETURA 📐")
    print("="*30)
    for tecla, (nome, _) in opcoes.items():
        print(f"[{tecla}] - {nome}")
    print("[0] - Sair")
    print("="*30)

def iniciar():
    while True:
        exibir_menu()
        escolhas = input("\nEscolha as opções (ex: 1 7): ").split()
        
        if '0' in escolhas:
            break
            
        for num in escolhas:
            if num in opcoes:
                nome, destino = opcoes[num]
                
                if destino == "INTERNO":
                    calculadora_obra()
                elif destino.startswith("http"):
                    webbrowser.open(destino)
                else:
                    if os.path.exists(destino):
                        os.startfile(destino)
                    else:
                        print(f"⚠️ Configure o caminho de {nome} no Nitro V15!")
        
        input("\nTarefa concluída! Pressione Enter para voltar...")

if __name__ == "__main__":
    iniciar()
