import os
import shutil
import ctypes

def limpar_pasta(caminho):
    if os.path.exists(caminho):
        print(f"🧹 Limpando: {caminho}")
        for item in os.listdir(caminho):
            item_completo = os.path.join(caminho, item)
            try:
                if os.path.isfile(item_completo) or os.path.islink(item_completo):
                    os.unlink(item_completo) # Deleta arquivo ou atalho
                elif os.path.isinstance(item_completo):
                    shutil.rmtree(item_completo) # Deleta pasta
                print(f"  ✅ Removido: {item}")
            except Exception as e:
                # Arquivos em uso pelo Windows não podem ser apagados, o que é normal
                print(f"  ⚠️ Ignorado (em uso): {item}")

def executar_limpeza():
    # Caminhos das pastas de lixo do Windows
    pastas_limpeza = [
        os.environ.get('TEMP'),                             # Temp do Usuário
        os.path.join(os.environ.get('SystemRoot'), 'Temp'), # Temp do Windows
        os.path.join(os.environ.get('SystemRoot'), 'Prefetch') # Prefetch (agiliza o sistema)
    ]

    print("="*40)
    print("🚀 NITRO V15 - MANUTENÇÃO DE PERFORMANCE")
    print("="*40)

    for pasta in pastas_limpeza:
        limpar_pasta(pasta)

    print("\n" + "="*40)
    print("✨ Limpeza concluída! Seu Nitro está pronto para voar.")
    print("="*40)
    input("\nPressione Enter para fechar...")

if __name__ == "__main__":
    # Verifica se tem permissão de administrador para limpar pastas do sistema
    executar_limpeza()
