import random
from tkinter import messagebox
from personajes import Campesino, Guerrero, Asesino, Paladin, Salvaje
from combate import VentanaCombate

def obtener_enemigo_aleatorio(ronda_nombre):
    nombres = {
        "Semifinal": ["Ragnar", "Ezlio", "Arthur", "Brock"],
        "Final": ["Grom", "Akali", "Uther", "Rack"]
    }
    clase = random.choice([Guerrero, Asesino, Paladin, Salvaje])
    nombre = random.choice(nombres[ronda_nombre])
    return clase(nombre=f"{nombre} ({clase.__name__})")

def iniciar_torneo(root, jugador):
    messagebox.showinfo("Torneo", "El Torneo aleatorio ha Comenzado!")
    
    rondas = [
        ("Cuartos de Final", Campesino("Campesino")),
        ("Semifinal", obtener_enemigo_aleatorio("Semifinal")),
        ("Gran Final", obtener_enemigo_aleatorio("Final"))
    ]
    
    for nombre_ronda, enemigo in rondas:
        messagebox.showinfo(nombre_ronda, f"Tu oponente en {nombre_ronda} es:\n{enemigo.nombre}")
        
        resultado = {"victoria": False}
        def al_terminar(victoria):
            resultado["victoria"] = victoria
        
        ventana = VentanaCombate(root, jugador, enemigo, al_terminar)
        root.wait_window(ventana.ventana) 
        
        if not resultado["victoria"]:
            messagebox.showerror("Eliminado", f"Has caido en {nombre_ronda}. mejor suerte la proxima!")
            return
            
        if nombre_ronda != "Gran Final":
            messagebox.showinfo("¡Victoria!", "Avanzas de ronda! Descansas y tu vida se restaura hasta estar nitido.")
            jugador.reiniciar_vida()
            
    messagebox.showinfo("¡Campeon!", "¡Eres el Campeon! \nTu nombre será recordado en la historia.")

if __name__ == "__main__":
    import tkinter as tk

    test = tk.Tk()

    jugador_prueba = Guerrero("Rayner (Tester)")

    iniciar_torneo(test, jugador_prueba)

    test.destroy()
    test.mainloop()