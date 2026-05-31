import tkinter as tk

class PersonajeSimulado:
    def __init__(self, nombre, vida_maxima):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima

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

        # característica del prota
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



if __name__ == "__main__":
    ventana_madre = tk.Tk()
    ventana_madre.title("Ventana Raíz del Sistema")
    ventana_madre.geometry("200x100")
    
    tk.Label(ventana_madre, text="Ventana principal activa.\nLa interfaz de combate\nse abrió encima.", pady=20).pack()

    jugador_test = Simulado1(nombre="Rayner", vida_maxima=60)
    enemigo_test = Simulado2(nombre="Campesino", vida_maxima=40)

    callback_test = lambda resultado: print(f"Combate terminado. ¿Ganó?: {resultado}")

    app_combate = VentanaCombate(ventana_madre, jugador_test, enemigo_test, callback_test)

    ventana_madre.mainloop()