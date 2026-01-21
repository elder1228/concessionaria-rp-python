import os
import time
import threading
import subprocess
import pyautogui
import cv2
import numpy as np
import customtkinter as ctk
from datetime import datetime
from twilio.rest import Client # Notificação WhatsApp

# ==========================================
# CONFIGURAÇÕES TÉCNICAS (MODO FANTASMA)
# ==========================================

class SentinelaMestre:
    def __init__(self):
        self.diretorio_pendrive = "E:/" # Letra do USB
        self.whatsapp_to = "whatsapp:+55XXXXXXXXXXX" # Seu número
        self.ativo = True

    def log(self, mensagem):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Sentinela]: {mensagem}")

    def motor_ia_gerador(self, prompt, software):
        """Simula a integração com API para gerar o código específico"""
        self.log(f"Gerando lógica para {software} baseada em: {prompt}")
        # Aqui o Sentinela cria o script que vai rodar no programa escolhido
        return "print('Executando automação inteligente...')"

    def gravar_janela_especifica(self, nome_projeto, stop_event):
        """Grava apenas a tela de execução do projeto"""
        screen_size = tuple(pyautogui.size())
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        video_path = f"temp_{nome_projeto}.avi"
        out = cv2.VideoWriter(video_path, fourcc, 20.0, screen_size)
        
        while not stop_event.is_set():
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        
        out.release()
        return video_path

    def self_healing_executor(self, codigo, software):
        """Tenta rodar, se der erro, ele mesmo corrige antes de finalizar"""
        tentativas = 0
        while tentativas < 3:
            # Simulação de teste de execução
            sucesso = True # Simula que o código passou no teste
            if sucesso:
                return True
            tentativas += 1
        return False

    def enviar_whatsapp(self, projeto):
        """Notifica o chefe que o lucro está garantido"""
        # Lógica Twilio aqui
        self.log(f"WhatsApp enviado: Projeto {projeto} Concluído!")

    def processar_trabalho(self, nome, software, prompt):
        """Fluxo completo de uma única tarefa (Multi-instância)"""
        stop_gravacao = threading.Event()
        
        # 1. Preparação e Gravação
        thread_video = threading.Thread(target=self.gravar_janela_especifica, args=(nome, stop_gravacao))
        thread_video.start()

        # 2. Execução e Self-Healing
        codigo = self.motor_ia_gerador(prompt, software)
        if self.self_healing_executor(codigo, software):
            self.log(f"Trabalho '{nome}' executado com sucesso.")
        
        # 3. Finalização
        time.sleep(5) # Simula o tempo de construção/codagem
        stop_gravacao.set()
        thread_video.join()

        # 4. Backup USB
        pasta_final = os.path.join(self.diretorio_pendrive, nome)
        os.makedirs(pasta_final, exist_ok=True)
        self.log(f"Arquivos de '{nome}' movidos para o Pendrive.")
        
        # 5. Notificação
        self.enviar_whatsapp(nome)

# ==========================================
# INTERFACE DE COMANDO (VISIONARISMO 2.0)
# ==========================================

class AppSentinela(ctk.CTk):
    def __init__(self, core):
        super().__init__()
        self.core = core
        self.title("SENTINELA MASTER - Multi-Work Station")
        self.geometry("700x600")
        ctk.set_appearance_mode("dark")

        # Cabeçalho
        self.label = ctk.CTkLabel(self, text="SENTINELA VISIONARY 2.0", font=("Orbitron", 26, "bold"), text_color="cyan")
        self.label.pack(pady=20)

        # Container de Tarefas
        self.scroll_tarefas = ctk.CTkScrollableFrame(self, width=600, height=300, label_text="Fila de Trabalhos Paralelos")
        self.scroll_tarefas.pack(pady=10)
        self.lista_tarefas = []

        # Inputs
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do Trabalho (Ex: Empresa A)")
        self.entry_nome.pack(pady=5, fill="x", padx=100)
        
        self.combo_soft = ctk.CTkComboBox(self, values=["AutoCAD (Casa 3D)", "Python (Segurança)", "C# (Sistemas)", "Blender"])
        self.combo_soft.pack(pady=5)

        self.text_cmd = ctk.CTkTextbox(self, height=70, width=500)
        self.text_cmd.insert("0.0", "Descreva os detalhes do projeto aqui...")
        self.text_cmd.pack(pady=10)

        # Botões
        self.btn_add = ctk.CTkButton(self, text="ADICIONAR TAREFA À FILA", command=self.add_tarefa)
        self.btn_add.pack(pady=5)

        self.btn_run = ctk.CTkButton(self, text="INICIAR TUDO (MODO FANTASMA)", fg_color="green", command=self.iniciar_tudo)
        self.btn_run.pack(pady=20)

    def add_tarefa(self):
        nome = self.entry_nome.get()
        soft = self.combo_soft.get()
        cmd = self.text_cmd.get("1.0", "end-1c")
        self.lista_tarefas.append({"nome": nome, "soft": soft, "cmd": cmd})
        
        label_t = ctk.CTkLabel(self.scroll_tarefas, text=f"📌 {nome} | {soft} | Aguardando...")
        label_t.pack(anchor="w")

    def iniciar_tudo(self):
        for tarefa in self.lista_tarefas:
            t = threading.Thread(target=self.core.processar_trabalho, args=(tarefa['nome'], tarefa['soft'], tarefa['cmd']))
            t.start()
        self.btn_run.configure(state="disabled", text="SENTINELA EM OPERAÇÃO 🤑")

if __name__ == "__main__":
    core = SentinelaMestre()
    app = AppSentinela(core)
    app.mainloop()
