import tkinter as tk
from personajes import Guerrero, Asesino, Paladin, Salvaje
from torneo import iniciar_torneo

def iniciar_juego(clase_elegida, entrada_nombre, ventana_principal):
    
    nombre = entrada_nombre.get().strip()
    
    if nombre == "":
        nombre = "Heroe Anonimo"
        
    if clase_elegida == "Guerrero": 
        jugador = Guerrero(nombre)
    elif clase_elegida == "Asesino": 
        jugador = Asesino(nombre)
    elif clase_elegida == "Paladin": 
        jugador = Paladin(nombre)
    elif clase_elegida == "Salvaje": 
        jugador = Salvaje(nombre)
    
    ventana_principal.withdraw()
    
    iniciar_torneo(ventana_principal, jugador)
    
    ventana_principal.deiconify() 

def main():
    ventana = tk.Tk()
    ventana.title("Torneo Aleatorio RPG")
    ventana.geometry("400x500")
    ventana.config(bg="#2c3e50")

    tk.Label(ventana, text="Torneo Aleatorio RPG", font=("Arial", 18, "bold"), bg="#2c3e50", fg="#f1c40f").pack(pady=20)
    
    tk.Label(ventana, text="Nombre de tu personaje:", bg="#2c3e50", fg="white", font=("Arial", 12)).pack()
    entrada_nombre = tk.Entry(ventana, font=("Arial", 14), justify="center")
    entrada_nombre.pack(pady=5)
    
    tk.Label(ventana, text="\nElige tu Arquetipo:", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=10)
    

    btn_guerrero = tk.Button(ventana, text="Guerrero (Equilibrado)", bg="#3498db", fg="white", font=("Arial", 12, "bold"),
                            command=lambda: iniciar_juego("Guerrero", entrada_nombre, ventana))
    btn_guerrero.pack(fill="x", padx=40, pady=5)
    
    btn_asesino = tk.Button(ventana, text="Asesino (Puro Dano)", bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                            command=lambda: iniciar_juego("Asesino", entrada_nombre, ventana))
    btn_asesino.pack(fill="x", padx=40, pady=5)
    
    btn_paladin = tk.Button(ventana, text="Paladin (Pura Defensa)", bg="#9b59b6", fg="white", font=("Arial", 12, "bold"),
                            command=lambda: iniciar_juego("Paladin", entrada_nombre, ventana))
    btn_paladin.pack(fill="x", padx=40, pady=5)
    
    btn_salvaje = tk.Button(ventana, text="Salvaje (Mucha Vida)", bg="#e67e22", fg="white", font=("Arial", 12, "bold"),
                            command=lambda: iniciar_juego("Salvaje", entrada_nombre, ventana))
    btn_salvaje.pack(fill="x", padx=40, pady=5)

    
    ventana.mainloop()

if __name__ == "__main__":
    main()