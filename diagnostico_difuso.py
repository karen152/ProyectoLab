import tkinter as tk
from tkinter import messagebox
from input_data import obtener_datos_usuario
from fuzzy_logic import SistemaDifuso
from visualization import mostrar_graficos
from data_store import guardar_diagnostico, cargar_historial, cargar_datos_para_graficos, cargar_datos_historial
from recommendations import generar_recomendaciones
from historial_visualization import mostrar_historial

class SistemaDiagnosticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Diagnóstico Médico")
        self.root.geometry("500x400")

        # Etiquetas e instrucciones
        self.label = tk.Label(root, text="Sistema Difuso de Diagnóstico Médico", font=("Arial", 16))
        self.label.pack(pady=10)

        # Botón para mostrar historial gráfico
        self.boton_historial = tk.Button(root, text="Ver Historial Gráfico", command=self.mostrar_historial)
        self.boton_historial.pack(pady=10)

        # Botón para obtener datos del usuario
        self.boton_datos = tk.Button(root, text="Capturar Datos", command=self.obtener_datos)
        self.boton_datos.pack(pady=10)

    def mostrar_historial(self):
    # Cargar datos desde el historial
     try:
        datos_historial = cargar_datos_historial()  # Función que carga los datos desde JSON u otra fuente
        if datos_historial:
            print("Datos cargados para gráficos:", datos_historial)  # Depuración
            mostrar_historial(datos_historial)  # Llama a la función global con los datos
        else:
            messagebox.showinfo("Historial", "No hay datos de historial disponibles.")
     except Exception as e:
        print(f"Error al intentar mostrar el historial: {e}")
        messagebox.showerror("Error", "No se pudo cargar el historial.")


    def obtener_datos(self):
        # Capturar datos del usuario con validación
        while True:
            datos_usuario = obtener_datos_usuario()
            if datos_usuario:
                self.realizar_diagnostico(datos_usuario)
                break
            else:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos dentro de los rangos especificados.")

    def realizar_diagnostico(self, datos_usuario):
        # Instanciar el sistema difuso
        sistema_difuso = SistemaDifuso()

        # Realizar diagnóstico
        resultado = sistema_difuso.diagnosticar(datos_usuario)
        
        if resultado is not None:
            # Mostrar diagnóstico
            if resultado < 0.4:
                mensaje = "Diagnóstico: Estable"
            elif resultado < 0.7:
                mensaje = "Diagnóstico: Observación necesaria"
            else:
                mensaje = "Diagnóstico: Alta probabilidad de infección"
            
            messagebox.showinfo("Diagnóstico", f"Diagnóstico final: {resultado:.2f}\n{mensaje}")

            # Guardar diagnóstico en el historial
            guardar_diagnostico(datos_usuario, resultado)

            # Mostrar recomendaciones
            recomendaciones = generar_recomendaciones(datos_usuario, resultado)
            recomendaciones_str = "\n".join(recomendaciones)
            messagebox.showinfo("Recomendaciones", recomendaciones_str)

            # Mostrar gráficos
            mostrar_graficos(datos_usuario)
        else:
            messagebox.showerror("Error", "No se pudo generar un diagnóstico válido. Por favor, revise los datos ingresados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDiagnosticoApp(root)
    root.mainloop()