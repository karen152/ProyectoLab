
###con correo mal hecho
            
import tkinter as tk
from tkinter import messagebox
from db import inicializar_db, agregar_paciente, obtener_paciente, guardar_diagnostico, obtener_historial, obtener_correo_paciente
from fuzzy_logic import SistemaDifuso
from recommendations import generar_recomendaciones
from historial_visualization import mostrar_historial

import smtplib
import ssl
from correoelect import DiagnosticoDifusoApp
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt


# Inicializa la base de datos
inicializar_db()


class SistemaDiagnosticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Diagnóstico Médico")
        self.root.geometry("500x500")

        # Pantalla de Login
        self.login_frame = tk.Frame(root)
        self.login_frame.pack(pady=50)

        self.label = tk.Label(self.login_frame, text="Sistema Difuso de Diagnóstico Médico", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.boton_iniciar_sesion = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.grid(row=1, column=0, pady=10)

        self.boton_registro = tk.Button(self.login_frame, text="Registrarse", command=self.registro)
        self.boton_registro.grid(row=1, column=1, pady=10)
        
        self.ultimo_historial = None


    def iniciar_sesion(self):
        self.login_frame.pack_forget()
        self.ventana_sesion = tk.Frame(self.root)
        self.ventana_sesion.pack(pady=50)

        self.label_cuil = tk.Label(self.ventana_sesion, text="Ingrese su CUIL", font=("Arial", 12))
        self.label_cuil.pack(pady=5)

        self.entry_cuil = tk.Entry(self.ventana_sesion)
        self.entry_cuil.pack(pady=5)

        self.boton_login = tk.Button(self.ventana_sesion, text="Iniciar Sesión", command=self.verificar_login)
        self.boton_login.pack(pady=10)

    def verificar_login(self):
        cuil = self.entry_cuil.get()
        paciente = obtener_paciente(cuil)
        if paciente:
            self.cuil = cuil
            self.abrir_perfil(cuil)
        else:
            messagebox.showerror("Error", "CUIL no registrado. Por favor, regístrese primero.")

    def abrir_perfil(self, cuil):
        self.ventana_sesion.pack_forget()
        self.perfil_frame = tk.Frame(self.root)
        self.perfil_frame.pack(pady=50)

        self.label_perfil = tk.Label(self.perfil_frame, text=f"Perfil de Paciente: CUIL {cuil}", font=("Arial", 16))
        self.label_perfil.pack(pady=10)

        self.boton_historial = tk.Button(self.perfil_frame, text="Ver Historial Gráfico",
                                         command=lambda: self.mostrar_historial(self.cuil))
        self.boton_historial.pack(pady=10)

        self.boton_datos = tk.Button(self.perfil_frame, text="Capturar Datos Nuevos",
                                     command=lambda: self.obtener_datos(self.cuil))
        self.boton_datos.pack(pady=10)
        #agregado:
    
        
        self.boton_descargar_pdf = tk.Button(self.perfil_frame, text="Descargar PDF",
                                     command=lambda: self.descargar_pdf(self.cuil))
        self.boton_descargar_pdf.pack(pady=10)
        
        ############################
        self.boton_enviar = tk.Button(self.root, text="Enviar Correo", command=self.abrienviocorreo)
        self.boton_enviar.pack(pady=10)

    # def abrienviocorreo(self):

    #  abrir = DiagnosticoDifusoApp( root)
    def abrienviocorreo(self):
    # Abrir la interfaz de correo
     correo_ventana = tk.Toplevel(self.root)
     DiagnosticoDifusoApp(correo_ventana)

        
        #########################


    def registro(self):
        self.login_frame.pack_forget()
        self.ventana_registro = tk.Frame(self.root)
        self.ventana_registro.pack(pady=50)

        self.label_nombre = tk.Label(self.ventana_registro, text="Nombre", font=("Arial", 12))
        self.label_nombre.pack(pady=5)

        self.entry_nombre = tk.Entry(self.ventana_registro)
        self.entry_nombre.pack(pady=5)

        self.label_edad = tk.Label(self.ventana_registro, text="Edad", font=("Arial", 12))
        self.label_edad.pack(pady=5)

        self.entry_edad = tk.Entry(self.ventana_registro)
        self.entry_edad.pack(pady=5)

        self.label_telefono = tk.Label(self.ventana_registro, text="Teléfono", font=("Arial", 12))
        self.label_telefono.pack(pady=5)

        self.entry_telefono = tk.Entry(self.ventana_registro)
        self.entry_telefono.pack(pady=5)

        self.label_cuil_registro = tk.Label(self.ventana_registro, text="CUIL", font=("Arial", 12))
        self.label_cuil_registro.pack(pady=5)
        ################################33
        
        self.label_correo = tk.Label(self.ventana_registro, text="Correo Electrónico", font=("Arial", 12))
        self.label_correo.pack(pady=5)

        # Campo de entrada para correo electrónico
        self.entry_correo = tk.Entry(self.ventana_registro)
        self.entry_correo.pack(pady=5)
        
        ############################################

        self.entry_cuil_registro = tk.Entry(self.ventana_registro)
        self.entry_cuil_registro.pack(pady=5)

        self.boton_registrar = tk.Button(self.ventana_registro, text="Registrar", command=self.registrar_paciente)
        self.boton_registrar.pack(pady=10)

    def registrar_paciente(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        telefono = self.entry_telefono.get()
        cuil = self.entry_cuil_registro.get()
        
        ##################################
        correo = self.entry_correo.get()

        if obtener_paciente(cuil):
            messagebox.showerror("Error", "El CUIL ya está registrado.")
        else:
            agregar_paciente(nombre, edad, telefono, cuil, correo)
            messagebox.showinfo("Éxito", "Registro exitoso. Puede iniciar sesión ahora.")
            self.ventana_registro.pack_forget()
            self.login_frame.pack(pady=50)
        
        ##########################

        # if obtener_paciente(cuil):
        #     messagebox.showerror("Error", "El CUIL ya está registrado.")
        # else:
        #     agregar_paciente(nombre, edad, telefono, cuil)
        #     messagebox.showinfo("Éxito", "Registro exitoso. Puede iniciar sesión ahora.")
        #     self.ventana_registro.pack_forget()
        #     self.login_frame.pack(pady=50)



    def mostrar_historial(self, cuil):
     datos_historial = obtener_historial(cuil)  # Obtiene el historial del paciente
     if datos_historial:  # Si hay datos disponibles
        datos = {
            "temperatura": [registro[2] for registro in datos_historial],
            "frecuencia_cardiaca": [registro[3] for registro in datos_historial],
            "presion_arterial": [registro[4] for registro in datos_historial],
            "diagnostico": [registro[5] for registro in datos_historial]
        }

        # Generar el gráfico
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        axs = axs.ravel()

        axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
        axs[0].set_title("Evolución de la Temperatura")
        axs[0].set_xlabel("Sesión")
        axs[0].set_ylabel("Temperatura (°C)")
        axs[0].legend()

        axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
        axs[1].set_title("Evolución de la Frecuencia Cardíaca")
        axs[1].set_xlabel("Sesión")
        axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
        axs[1].legend()

        axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
        axs[2].set_title("Evolución de la Presión Arterial")
        axs[2].set_xlabel("Sesión")
        axs[2].set_ylabel("Presión Arterial (mmHg)")
        axs[2].legend()

        axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
        axs[3].set_title("Evolución del Diagnóstico")
        axs[3].set_xlabel("Sesión")
        axs[3].set_ylabel("Diagnóstico")
        axs[3].legend()

        plt.tight_layout()
        plt.show()
     else:  # Si no hay datos en la base de datos
        messagebox.showinfo("Historial", "No hay datos disponibles.")

    
    def obtener_datos(self, cuil):
        self.ventana_datos = tk.Toplevel(self.root)
        self.ventana_datos.title("Captura de Datos")

        self.label_temperatura = tk.Label(self.ventana_datos, text="Temperatura (°C):", font=("Arial", 12))
        self.label_temperatura.pack(pady=5)
        self.entry_temperatura = tk.Entry(self.ventana_datos)
        self.entry_temperatura.pack(pady=5)

        self.label_presion = tk.Label(self.ventana_datos, text="Presión Arterial (mmHg):", font=("Arial", 12))
        self.label_presion.pack(pady=5)
        self.entry_presion = tk.Entry(self.ventana_datos)
        self.entry_presion.pack(pady=5)

        self.label_frecuencia = tk.Label(self.ventana_datos, text="Frecuencia Cardíaca (lpm):", font=("Arial", 12))
        self.label_frecuencia.pack(pady=5)
        self.entry_frecuencia = tk.Entry(self.ventana_datos)
        self.entry_frecuencia.pack(pady=5)

        self.label_oxigeno = tk.Label(self.ventana_datos, text="Nivel de Oxígeno (%):", font=("Arial", 12))
        self.label_oxigeno.pack(pady=5)
        self.entry_oxigeno = tk.Entry(self.ventana_datos)
        self.entry_oxigeno.pack(pady=5)

        self.boton_guardar = tk.Button(self.ventana_datos, text="Guardar Datos",
                                       command=lambda: self.realizar_diagnostico(cuil))
        self.boton_guardar.pack(pady=10)
    
    
        
    def realizar_diagnostico(self, cuil):
     try:
        # Capturar los valores ingresados por el usuario
        temperatura = float(self.entry_temperatura.get())
        presion_arterial = float(self.entry_presion.get())
        frecuencia_cardiaca = int(self.entry_frecuencia.get())
        nivel_oxigeno = float(self.entry_oxigeno.get())

        # Validar rangos
        if not (90 <= nivel_oxigeno <= 101):
            raise ValueError("El nivel de oxígeno debe estar entre 90 y 101.")

        # Preparar los datos del usuario para el diagnóstico
        datos_usuario = {
            "temperatura": temperatura,
            "presion_arterial": presion_arterial,
            "frecuencia_cardiaca": frecuencia_cardiaca,
            "nivel_oxigeno": nivel_oxigeno
        }

        # Generar el diagnóstico con el sistema difuso
        sistema_difuso = SistemaDifuso()
        resultado_numerico = sistema_difuso.diagnosticar(datos_usuario)

        # Traducir el resultado a una descripción
        if resultado_numerico <= 0.4:
            diagnostico_descriptivo = "Estable"
        elif resultado_numerico <= 0.7:
            diagnostico_descriptivo = "Observación"
        else:
            diagnostico_descriptivo = "Alta probabilidad de infección"

        # Generar recomendaciones
        recomendaciones = generar_recomendaciones(datos_usuario, resultado_numerico)

        # Mostrar al usuario
        mensaje_diagnostico = f"Diagnóstico: {diagnostico_descriptivo} ({resultado_numerico:.2f})\n\n"
        mensaje_recomendaciones = "Recomendaciones:\n" + "\n".join(recomendaciones)
        messagebox.showinfo("Diagnóstico y Recomendaciones", mensaje_diagnostico + mensaje_recomendaciones)

        # Guardar el diagnóstico y las recomendaciones en el historial
        guardar_diagnostico(cuil, datos_usuario, resultado_numerico)  # <- IMPORTANTE: GUARDA EL DIAGNÓSTICO

        if not self.ultimo_historial:
            self.ultimo_historial = {
                "temperatura": [],
                "presion_arterial": [],
                "frecuencia_cardiaca": [],
                "nivel_oxigeno": [],
                "diagnostico": [],
                "diagnostico_descriptivo": [],
                "recomendaciones": []
            }

        self.ultimo_historial["temperatura"].append(temperatura)
        self.ultimo_historial["presion_arterial"].append(presion_arterial)
        self.ultimo_historial["frecuencia_cardiaca"].append(frecuencia_cardiaca)
        self.ultimo_historial["nivel_oxigeno"].append(nivel_oxigeno)
        self.ultimo_historial["diagnostico"].append(resultado_numerico)
        self.ultimo_historial["diagnostico_descriptivo"].append(diagnostico_descriptivo)
        self.ultimo_historial["recomendaciones"].append(recomendaciones)

     except ValueError as e:
        messagebox.showerror("Entrada Inválida", str(e))
     except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {e}")

        
        
    def descargar_pdf(self, cuil):
       if not self.ultimo_historial:
        messagebox.showerror("Error", "Primero debe ingresar síntomas y ver el diagnóstico antes de descargar el PDF.")
        return

    # Crear el archivo PDF
       pdf_path = f"diagnostico_{cuil}.pdf"
       c = canvas.Canvas(pdf_path, pagesize=letter)
       c.drawString(100, 750, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")

    # Agregar los datos del historial al PDF
       datos = self.ultimo_historial
       c.drawString(100, 730, "Últimos Datos Biométricos:")
       c.drawString(120, 710, f"Temperatura: {datos['temperatura'][-1]}°C")
       c.drawString(120, 690, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
       c.drawString(120, 670, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")

    # Validar que nivel_oxigeno esté disponible
       if "nivel_oxigeno" in datos and datos["nivel_oxigeno"]:
        c.drawString(120, 650, f"Nivel de Oxígeno: {datos['nivel_oxigeno'][-1]}%")
       else:
        c.drawString(120, 650, "Nivel de Oxígeno: No disponible.")

    # Mostrar el diagnóstico descriptivo en el PDF
       if "diagnostico" in datos and datos["diagnostico"]:
        c.drawString(120, 630, f"Diagnóstico: {datos['diagnostico'][-1]}")  # Texto descriptivo
       else:
        c.drawString(120, 630, "Diagnóstico: No disponible.")

    # Agregar recomendaciones
       y_position = 610
       if "recomendaciones" in datos and datos["recomendaciones"]:
        c.drawString(100, y_position, "Recomendaciones:")
        y_position -= 20
        for recomendacion in datos["recomendaciones"][-1]:
            c.drawString(120, y_position, f"- {recomendacion}")
            y_position -= 20  # Ajusta la posición vertical para cada recomendación
       else:
        c.drawString(100, y_position, "Recomendaciones: No disponibles.")
        y_position -= 20

    # Generar el gráfico con subplots
       fig, axs = plt.subplots(2, 2, figsize=(12, 10))
       axs = axs.ravel()

       axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
       axs[0].set_title("Evolución de la Temperatura")
       axs[0].set_xlabel("Sesión")
       axs[0].set_ylabel("Temperatura (°C)")
       axs[0].legend()

       axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
       axs[1].set_title("Evolución de la Frecuencia Cardíaca")
       axs[1].set_xlabel("Sesión")
       axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
       axs[1].legend()

       axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
       axs[2].set_title("Evolución de la Presión Arterial")
       axs[2].set_xlabel("Sesión")
       axs[2].set_ylabel("Presión Arterial (mmHg)")
       axs[2].legend()

       axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
       axs[3].set_title("Evolución del Diagnóstico")
       axs[3].set_xlabel("Sesión")
       axs[3].set_ylabel("Diagnóstico")
       axs[3].legend()
 
       plt.tight_layout()

    # Guardar el gráfico como imagen temporal
       temp_image_path = "temp_historial.png"
       plt.savefig(temp_image_path)
       plt.close()

    # Insertar el gráfico en el PDF
       c.drawImage(temp_image_path, 100, 250, width=400, height=300)

    # Eliminar la imagen temporal después de usarla
       import os
       os.remove(temp_image_path)

    # Guardar el archivo PDF
       c.save()
       messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")
       
       
    
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDiagnosticoApp(root)
    root.mainloop()
   
        
