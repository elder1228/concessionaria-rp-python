import os
import time
import threading
import keyboard  # Biblioteca para detectar M+V no PC

class FortalezaMaster:
    def __init__(self):
        self.saude = 100
        self.gerador = 100
        self.vitima_no_porta_malas = False
        self.caixa = 0
        self.atalho_ativo = True

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def cabecalho(self):
        self.limpar_tela()
        print(f"==================================================")
        print(f"       FORTALEZA OS v2.0 - SANDY SHORES")
        print(f"==================================================")
        print(f" [❤️ {self.saude}%] | [⚡ {self.gerador}%] | [💰 R$ {self.caixa}]")
        print(f"==================================================")
        print(" [!] ATALHO M+V DISPONÍVEL PARA GARAGEM")

    def abrir_garagem(self):
        """Função disparada pelo atalho M+V"""
        self.limpar_tela()
        print("\n" + "="*20)
        print(" [ 𝐆𝐀𝐑𝐀𝐆𝐄𝐌 𝐌𝐎𝐃 𝐕 ]")
        print("="*20)
        print("1. [FROTA] Civic / Lancer / S1000RR / MT-09")
        print("2. [LIMPEZA] Destruir veículo de NPC")
        print("3. [TUNING] Reparar e Trocar Placas")
        print("4. Fechar Menu")
        
        escolha = input("\nComando Garagem > ")
        if escolha == "2":
            print("\n[🔥] Veículo destruído na marina. Evidências apagadas.")
            time.sleep(2)
        elif escolha == "3":
            print("\n[🔧] Veículo novo! Placas trocadas.")
            time.sleep(2)
        self.cabecalho()

    def monitorar_teclado(self):
        """Thread que fica vigiando o atalho M+V"""
        while self.atalho_ativo:
            # Detecta se M e V estão pressionados simultaneamente
            if keyboard.is_pressed('m') and keyboard.is_pressed('v'):
                self.abrir_garagem()
                time.sleep(0.5) # Evita abrir múltiplas vezes
            time.sleep(0.1)

    def menu_principal(self):
        # Inicia a vigília do atalho M+V em background
        threading.Thread(target=self.monitorar_teclado, daemon=True).start()

        while True:
            self.cabecalho()
            print("1. Iniciar Contrato (Abordagem)")
            print("2. Ir para Galpão de Tortura (Setor C)")
            print("3. Central de Câmeras (3 Telas)")
            print("4. Sair")
            
            op = input("\nComando Principal > ")
            
            if op == "1":
                print("\n[!] Alvo rendido e no porta-malas!"); self.vitima_no_porta_malas = True
                time.sleep(2)
            elif op == "2":
                if self.vitima_no_porta_malas:
                    print("\n[💰] Dinheiro extraído! 30% enviado para Agência."); self.caixa += 1500
                    self.vitima_no_porta_malas = False
                else: print("\n[!] Porta-malas vazio.")
                time.sleep(2)
            elif op == "3":
                print("\n[TELA 1] CAM 01/02 | [TELA 2] CAM 03/04 | [TELA 3] CAM 05/06")
                input("\nPresione ENTER para voltar...")
            elif op == "4":
                self.atalho_ativo = False
                break
            self.gerador -= 1

if __name__ == "__main__":
    # Quando o notebook chegar, você precisará instalar: pip install keyboard
    app = FortalezaMaster()
    app.menu_principal()
