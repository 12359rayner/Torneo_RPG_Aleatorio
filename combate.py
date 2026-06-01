import tkinter as tk
from tkinter import messagebox
import random


class PersonajeSimulado:
    def __init__(self, nombre, vida_maxima, ataque, defensa):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima
        self.ataque = ataque
        self.defensa = defensa

    def recibir_danio(self, cantidad):
        self.vida_actual -= cantidad
        if self.vida_actual < 0:
            self.vida_actual = 0

    def esta_vivo(self):
        return self.vida_actual > 0

class Simulado1(PersonajeSimulado):
    pass

class Simulado2(PersonajeSimulado):
    pass

class VentanaCombate:
    def __init__(self, maestro, jugador, enemigo, llamada_de_victoria):
        self.ventana = tk.Toplevel(maestro)
        self.ventana.title(f"Torneo: {jugador.nombre} vs {enemigo.nombre}")
        self.ventana.geometry("500x550")
        self.ventana.config(bg="#2c3e50")
        self.jugador = jugador
        self.enemigo = enemigo
        self.llamada_de_Victoria = llamada_de_victoria

        tk.Label(self.ventana, text="¡Empieza el combate!", fg="white", bg="#2c3e50", font=("Arial", 14, "bold")).pack(pady=10)

        # Característica del prota
        frame_j = tk.Frame(self.ventana, bg="#34495e", pady=10)
        frame_j.pack(fill="x", padx=20)
        tk.Label(frame_j, text=f"{jugador.nombre} ({jugador.__class__.__name__})", fg="#ecf0f1", bg="#34495e", font=("Arial", 12)).pack()
        self.vida_jugador = tk.Label(frame_j, text=f"Vida: {jugador.vida_actual}/{jugador.vida_maxima}", fg="#2ecc71", bg="#34495e", font=("Arial", 14, "bold"))
        self.vida_jugador.pack()

        # Característica del Enemigo
        frame_e = tk.Frame(self.ventana, bg="#34495e", pady=10)
        frame_e.pack(fill="x", padx=20, pady=10)
        tk.Label(frame_e, text=f"{enemigo.nombre}", fg="#ecf0f1", bg="#34495e", font=("Arial", 12)).pack()
        self.vida_enemigo = tk.Label(frame_e, text=f"Vida: {enemigo.vida_actual}/{enemigo.vida_maxima}", fg="#e74c3c", bg="#34495e", font=("Arial", 14, "bold"))
        self.vida_enemigo.pack()

        self.btn_atacar = tk.Button(self.ventana, text="Atacar", bg="#e67e22", fg="white", font=("Arial", 12, "bold"), width=20, command=self.accion_atacar)
        self.btn_atacar.pack(pady=5)
        
        self.btn_curar = tk.Button(self.ventana, text="Curar", bg="#27ae60", fg="white", font=("Arial", 12, "bold"), width=20, command=self.accion_curar)
        self.btn_curar.pack(pady=5)

        self.txt_log = tk.Text(self.ventana, height=10, width=55, state="disabled", font=("Consolas", 9))
        self.txt_log.pack(pady=10)

    def log(self, mensaje):
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state="disabled")

    def accion_atacar(self):
        dado = random.randint(1, 6)
        danio = max(1, (self.jugador.ataque + dado) - self.enemigo.defensa)
        self.enemigo.recibir_danio(danio)
        self.log(f"-> Atacas con un {dado}. ¡Haces {danio} de daño!")
        self.actualizar_estado()

    def accion_curar(self):
        dado = random.randint(1, 6)
        cura = self.jugador.defensa + dado
        self.jugador.vida_actual = min(self.jugador.vida_maxima, self.jugador.vida_actual + cura)
        self.log(f"-> Usas medicina (+{cura} PS).")
        self.actualizar_estado()

    def actualizar_estado(self):
        self.vida_jugador.config(text=f"Vida: {self.jugador.vida_actual}/{self.jugador.vida_maxima}")
        self.vida_enemigo.config(text=f"Vida: {self.enemigo.vida_actual}/{self.enemigo.vida_maxima}")
        if self.verificar_final(): return

        self.btn_atacar.config(state="disabled")
        self.btn_curar.config(state="disabled")
        self.ventana.after(1000, self.turno_rival)

    def turno_rival(self):
        dado_ia = random.randint(1, 6)
        if self.enemigo.vida_actual < self.enemigo.vida_maxima and random.random() < 0.3:
            cura = self.enemigo.defensa + dado_ia
            self.enemigo.vida_actual = min(self.enemigo.vida_maxima, self.enemigo.vida_actual + cura)
            self.log(f"<- El rival se defiende y cura +{cura} PS.")
        else:
            danio = max(1, (self.enemigo.ataque + dado_ia) - self.jugador.defensa)
            self.jugador.recibir_danio(danio)
            self.log(f"<- Rival saca un {dado_ia}. ¡Te quita {danio} de vida!")
        
        self.vida_jugador.config(text=f"Vida: {self.jugador.vida_actual}/{self.jugador.vida_maxima}")
        self.vida_enemigo.config(text=f"Vida: {self.enemigo.vida_actual}/{self.enemigo.vida_maxima}")
        
        if not self.verificar_final():
            
            self.btn_atacar.config(state="normal")
            self.btn_curar.config(state="normal")

    def verificar_final(self):
        if not self.enemigo.esta_vivo():
            messagebox.showinfo("Victoria", "Has ganado el combate!")
            self.ventana.destroy()
            self.llamada_de_Victoria(True)
            return True
        if not self.jugador.esta_vivo():
            messagebox.showerror("Derrota", "Has caido en combate...")
            self.ventana.destroy()
            self.llamada_de_Victoria(False)
            return True
        return False
    

if __name__ == "__main__":
    ventana_madre = tk.Tk()
    ventana_madre.title("Ventana raiz del sistema")
    ventana_madre.geometry("200x100")
    
    tk.Label(ventana_madre, text="Ventana principal activa.\nLa interfaz de combate\nse abrio encima.", pady=20).pack()


    jugador_test = Simulado1(nombre="Rayner", vida_maxima=60, ataque=12, defensa=8)
    enemigo_test = Simulado2(nombre="Campesino", vida_maxima=40, ataque=8, defensa=4)

    callback_test = lambda resultado: print(f"Combate terminado. Gano?: {resultado}")

    app_combate = VentanaCombate(ventana_madre, jugador_test, enemigo_test, callback_test)

    ventana_madre.mainloop()