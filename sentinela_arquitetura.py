import shutil
import os
import time
import pyautogui  # Biblioteca para controlar o mouse
from datetime import datetime

# --- CONFIGURAÇÕES ---
# No seu Nitro V15, ajustaremos a letra do pendrive
arquivo_projeto = "C:/Users/Documentos/Arquitetura/projeto_atual.dwg"
pasta_pendrive = "D:/Backups_Sentinela/"
intervalo_backup = 600  # Salva a cada 10 minutos
intervalo_mouse = 60    # Mexe o mouse a cada 1 minuto para não dormir

def sentinela():
    print("="*40)
    print("🛡️ MODO SENTINELA ATIVADO")
    print("Seu notebook não vai dormir e o backup está agendado.")
    print("="*40)

    contagem_tempo = 0

    try:
        while True:
            # 1. Simula movimento do mouse para manter o PC acordado
            # Move o mouse 1 pixel para a direita e 1 para a esquerda
            pyautogui.moveRel(1, 0)
            pyautogui.moveRel(-1, 0)
            
            # 2. Verifica se é hora de fazer o Backup
            if contagem_tempo >= intervalo_backup:
                if os.path.exists(pasta_pendrive):
                    data_hora = datetime.now().strftime("%H-%M-%S")
                    destino = os.path.join(pasta_pendrive, f"backup_{data_hora}.bak")
                    shutil.copy2(arquivo_projeto, destino)
                    print(f"✅ Backup de segurança feito no pendrive às {data_hora}")
                else:
                    print("⚠️ Pendrive não detectado! Conecte para salvar.")
                
                contagem_tempo = 0 # Reinicia a contagem do backup

            time.sleep(intervalo_mouse) 
            contagem_tempo += intervalo_mouse

    except KeyboardInterrupt:
        print("\n🛡️ Modo Sentinela desativado pelo usuário.")

if __name__ == "__main__":
    sentinela()
