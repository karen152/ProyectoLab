
###con correo mal hecho
            
import tkinter as tk
from tkinter import messagebox
from db import inicializar_db, agregar_paciente, obtener_paciente, guardar_diagnostico, obtener_historial, obtener_correo_paciente
from fuzzy_logic import SistemaDifuso
from recommendations import generar_recomendaciones
from historial_visualization import mostrar_historial
from PIL import Image, ImageTk  # Librería para imágenes

import os
import smtplib
import ssl
from correoelect import DiagnosticoDifusoApp
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

import ttkbootstrap as ttk
#from tkinter import messagebox
from styles import StyledContainer, custom_styles
# Inicializa la base de datos
inicializar_db()


class SistemaDiagnosticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Diagnóstico Médico")
        self.root.geometry("500x500")
        
        # Cargar estilos personalizados
        custom_styles()

        # Crear pantalla principal con diseño estilizado
        # self.crear_pantalla_principal()
        # self.container = StyledContainer(self.root)
        
        self.container = StyledContainer(self.root)
        self.crear_pantalla_principal()
         
        # Conectar botones a sus comandos
    #     self.container.login_button.config(command=self.iniciar_sesion)
    #    # self.container.register_button.config(command=self.registro)
    #     self.container.register_button.config(command=self.registro)


        # Pantalla de Login
        # self.login_frame = tk.Frame(root)
        # self.login_frame.pack(pady=50)

        # self.label = tk.Label(self.login_frame, text="Sistema Difuso de Diagnóstico Médico", font=("Arial", 16))
        # self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # self.boton_iniciar_sesion = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        # self.boton_iniciar_sesion.grid(row=1, column=0, pady=10)

        # self.boton_registro = tk.Button(self.login_frame, text="Registrarse", command=self.registro)
        # self.boton_registro.grid(row=1, column=1, pady=10)
        
        self.ultimo_historial = None

  
    def crear_pantalla_principal(self):
        # Eliminar cualquier pantalla previa
        for widget in self.root.winfo_children():
            widget.destroy()

        # Contenedor principal estilizado
        self.container = StyledContainer(self.root)

        # Conectar botones a sus comandos
        # self.container.login_button.config(command=self.mostrar_pantalla_login)
        # #self.container.register_button.config(command=self.mostrar_pantalla_registro)
        # self.container.register_button.config(command=self.registro)
        #self.container.login_button.config(command=self.iniciar_sesion_desde_principal)
        # self.container.login_button.config(command=self.iniciar_sesion_desde_principal)

        # self.container.register_button.config(command=self.registro)
        
        self.container.login_button.config(command=self.iniciar_sesion_desde_principal)

    # Conectar el botón de "Registrarse" al método registro
        self.container.register_button.config(command=self.registro)
    
  

         
         
    def iniciar_sesion_desde_principal(self):
        # cuil = self.entry_cuil_principal.get().strip()
        #cuil = self.container.cuil_input.get().strip()
        cuil = self.container.cuil_input.get().strip()
        if not cuil:
             messagebox.showerror("Error", "Debe ingresar un CUIL para iniciar sesión.")
             return

        paciente = obtener_paciente(cuil)
        if paciente:
            self.cuil = cuil
            self.abrir_perfil(cuil)
        else:
              messagebox.showerror("Error", "CUIL no registrado. Por favor, regístrese primero.")
        
  
   


        
    # def iniciar_sesion(self):
    #     self.login_frame.pack_forget()
    #     self.ventana_sesion = tk.Frame(self.root)
    #     self.ventana_sesion.pack(pady=50)

    #     self.label_cuil = tk.Label(self.ventana_sesion, text="Ingrese su CUIL", font=("Arial", 12))
    #     self.label_cuil.pack(pady=5)

    #     self.entry_cuil = tk.Entry(self.ventana_sesion)
    #     self.entry_cuil.pack(pady=5)

    #     self.boton_login = tk.Button(self.ventana_sesion, text="Iniciar Sesión", command=self.verificar_login)
    #     self.boton_login.pack(pady=10)
    def mostrar_pantalla_login(self):
        # Eliminar pantalla actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear nueva pantalla para iniciar sesión
        self.login_frame = ttk.Frame(self.root, padding=20)
        self.login_frame.pack(fill="both", expand=True)

        label = ttk.Label(self.login_frame, text="Iniciar Sesión", font=("Arial", 16, "bold"))
        label.pack(pady=10)

        self.cuil_entry = ttk.Entry(self.login_frame, font=("Arial", 12), bootstyle="default")
        self.cuil_entry.pack(fill="x", pady=10)

        login_button = ttk.Button(
            self.login_frame, 
            text="Ingresar", 
            bootstyle="success", 
            command=self.verificar_login
        )
        login_button.pack(fill="x", pady=10)

        back_button = ttk.Button(
            self.login_frame,
            text="Volver",
            bootstyle="secondary",
            command=self.crear_pantalla_principal
        )
        back_button.pack(fill="x", pady=10)

  
     #####
     
       

    #####
    # def abrir_perfil(self, cuil):
    #     # Limpiar la ventana actual
    #     for widget in self.root.winfo_children():
    #         widget.destroy()

    #     # Crear el frame para el perfil del paciente
    #     self.perfil_frame = ttk.Frame(self.root, padding=20)
    #     self.perfil_frame.pack(fill="both", expand=True)

    #     label_perfil = ttk.Label(
    #         self.perfil_frame, 
    #         text=f"Perfil de Paciente: CUIL {cuil}", 
    #         font=("Arial", 16, "bold")
    #     )
    #     label_perfil.pack(pady=10)

    #     boton_historial = ttk.Button(
    #         self.perfil_frame, 
    #         text="Ver Historial Gráfico", 
    #         bootstyle="info", 
    #         command=lambda: self.mostrar_historial(cuil)
    #     )
    #     boton_historial.pack(fill="x", pady=10)

    #     boton_datos = ttk.Button(
    #         self.perfil_frame, 
    #         text="Capturar Datos Nuevos", 
    #         bootstyle="primary", 
    #         command=lambda: self.obtener_datos(cuil)
    #     )
    #     boton_datos.pack(fill="x", pady=10)

    #     boton_descargar_pdf = ttk.Button(
    #         self.perfil_frame, 
    #         text="Descargar PDF", 
    #         bootstyle="success", 
    #         command=lambda: self.descargar_pdf(cuil)
    #     )
    #     boton_descargar_pdf.pack(fill="x", pady=10)

    #     boton_enviar = ttk.Button(
    #         self.perfil_frame, 
    #         text="Enviar Correo", 
    #         bootstyle="secondary", 
    #         command=self.abrienviocorreo
    #     )
    #     boton_enviar.pack(fill="x", pady=10)

    #     boton_volver = ttk.Button(
    #         self.perfil_frame,
    #         text="Volver",
    #         bootstyle="danger",
    #         command=self.crear_pantalla_principal
    #     )
    #     boton_volver.pack(fill="x", pady=10)
    
    # def abrir_perfil(self, cuil):
    #     # Limpiar la ventana actual
    #     for widget in self.root.winfo_children():
    #         widget.destroy()

    #     # Crear el frame para el perfil del paciente
    #     self.perfil_frame = ttk.Frame(self.root, padding=20)
    #     self.perfil_frame.pack(fill="both", expand=True)

    #     label_perfil = ttk.Label(
    #         self.perfil_frame, 
    #         text=f"Perfil de Paciente: CUIL {cuil}", 
    #         font=("Arial", 16, "bold")
    #     )
    #     label_perfil.pack(pady=10)

    #     boton_historial = ttk.Button(
    #         self.perfil_frame, 
    #         text="Ver Historial Gráfico", 
    #         bootstyle="info", 
    #         command=lambda: self.mostrar_historial(cuil)
    #     )
    #     boton_historial.pack(fill="x", pady=10)

    #     boton_datos = ttk.Button(
    #         self.perfil_frame, 
    #         text="Capturar Datos Nuevos", 
    #         bootstyle="primary", 
    #         command=lambda: self.obtener_datos(cuil)
    #     )
    #     boton_datos.pack(fill="x", pady=10)

    #     boton_descargar_pdf = ttk.Button(
    #         self.perfil_frame, 
    #         text="Descargar PDF", 
    #         bootstyle="success", 
    #         command=lambda: self.descargar_pdf(cuil)
    #     )
    #     boton_descargar_pdf.pack(fill="x", pady=10)

    #     boton_enviar = ttk.Button(
    #         self.perfil_frame, 
    #         text="Enviar Correo", 
    #         bootstyle="secondary", 
    #         command=self.abrienviocorreo
    #     )
    #     boton_enviar.pack(fill="x", pady=10)

    #     boton_volver = ttk.Button(
    #         self.perfil_frame,
    #         text="Volver",
    #         bootstyle="danger",
    #         command=self.crear_pantalla_principal
    #     )
    #     boton_volver.pack(fill="x", pady=10)
    
    
    def abrir_perfil(self, cuil):
        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear el contenedor principal para el perfil
        self.perfil_frame = ttk.Frame(self.root, padding=20)
        self.perfil_frame.pack(fill="both", expand=True)

        # Título del perfil
        label_perfil = ttk.Label(
            self.perfil_frame,
            text=f"Perfil de Paciente: CUIL {cuil}",
            font=("Arial", 16, "bold")
        )
        label_perfil.pack(pady=10)

        # Botón para ver historial gráfico
        boton_historial = ttk.Button(
            self.perfil_frame,
            text="Ver Historial Gráfico",
            bootstyle="info",
            command=lambda: self.mostrar_historial(cuil)
        )
        boton_historial.pack(fill="x", pady=10)

        # Botón para capturar nuevos datos
        boton_datos = ttk.Button(
            self.perfil_frame,
            text="Capturar Datos Nuevos",
            bootstyle="primary",
            command=lambda: self.obtener_datos(cuil)
        )
        boton_datos.pack(fill="x", pady=10)

        img_descargar = Image.open("iconos/descargar.jpg")  # Ruta de tu ícono
        img_descargar = img_descargar.resize((30, 30))  # Redimensionar ícono
        self.icono_descargar = ImageTk.PhotoImage(img_descargar)  # Guardar referencia
        # Botón para descargar PDF
        boton_descargar_pdf = ttk.Button(
            self.perfil_frame,
            text="Descargar PDF",
            image=self.icono_descargar,  # Agregar ícono
            compound="right", 
            # bootstyle="success",
            bootstyle="secondary",    
            command=lambda: self.descargar_pdf(cuil)
        )
        boton_descargar_pdf.pack(fill="x", pady=10)
        
    #      img_correo = Image.open("iconos/gmail.png")  # Ruta de tu ícono
    # img_correo = img_correo.resize((20, 20))
    # self.icono_correo = ImageTk.PhotoImage(img_correo)

        
        # Botón para enviar correo
        boton_enviar = ttk.Button(
            self.perfil_frame,
            text="Enviar Correo",
            bootstyle="secondary",
            command=self.abrienviocorreo
        )
        boton_enviar.pack(fill="x", pady=10)

        # Botón para volver a la pantalla principal
        boton_volver = ttk.Button(
            self.perfil_frame,
            text="Volver",
            bootstyle="danger",
            command=self.crear_pantalla_principal
        )
        boton_volver.pack(fill="x", pady=10)
        
        # boton_datos = ttk.Button(
        # self.perfil_frame,
        # text="Capturar Datos Nuevos",
        # bootstyle="primary",
        # command=lambda: self.obtener_datos(cuil)  # Llama al método obtener_datos
        # )
        # boton_datos.pack(fill="x", pady=10)


        # Aquí puedes agregar más widgets o funcionalidades que estaban en tu proyecto original.




    def registro(self):
        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear nueva pantalla para registrarse
        self.register_frame = ttk.Frame(self.root, padding=20)
        self.register_frame.pack(fill="both", expand=True)

        label = ttk.Label(
            self.register_frame, 
            text="Registro de Usuario", 
            font=("Arial", 16, "bold")
        )
        label.pack(pady=10)

        # Campos de entrada para registro
        self.nombre_entry = ttk.Entry(self.register_frame, font=("Arial", 12), bootstyle="default")
        self.nombre_entry.pack(fill="x", pady=10)
        self.nombre_entry.insert(0, "Nombre Completo")

        self.edad_entry = ttk.Entry(self.register_frame, font=("Arial", 12), bootstyle="default")
        self.edad_entry.pack(fill="x", pady=10)
        self.edad_entry.insert(0, "Edad")

        self.telefono_entry = ttk.Entry(self.register_frame, font=("Arial", 12), bootstyle="default")
        self.telefono_entry.pack(fill="x", pady=10)
        self.telefono_entry.insert(0, "Teléfono")

        self.cuil_entry = ttk.Entry(self.register_frame, font=("Arial", 12), bootstyle="default")
        self.cuil_entry.pack(fill="x", pady=10)
        self.cuil_entry.insert(0, "CUIL")

        self.correo_entry = ttk.Entry(self.register_frame, font=("Arial", 12), bootstyle="default")
        self.correo_entry.pack(fill="x", pady=10)
        self.correo_entry.insert(0, "Correo Electrónico")

        register_button = ttk.Button(
            self.register_frame, 
            text="Registrar", 
            bootstyle="primary", 
            command=self.registrar_paciente
        )
        register_button.pack(fill="x", pady=10)

        back_button = ttk.Button(
            self.register_frame,
            text="Volver",
            bootstyle="secondary",
            command=self.crear_pantalla_principal
        )
        back_button.pack(fill="x", pady=10)


    def registrar_paciente(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        telefono = self.telefono_entry.get()
        cuil = self.cuil_entry.get()
        correo = self.correo_entry.get()

        if obtener_paciente(cuil):
            messagebox.showerror("Error", "El CUIL ya está registrado.")
        else:
            agregar_paciente(nombre, edad, telefono, cuil, correo)
            messagebox.showinfo("Éxito", "Registro exitoso. Puede iniciar sesión ahora.")
            # self.crear_pantalla_principal()
            self.cuil = cuil  # Guardar el CUIL registrado
            self.abrir_perfil(cuil)  # Redirigir automáticamente al perfil
            






    def iniciar_sesion(self):
        cuil = self.container.cuil_input.get()
        paciente = obtener_paciente(cuil)
        if paciente:
           self.cuil = cuil
           self.abrir_perfil(cuil)
        else:
             messagebox.showerror("Error", "CUIL no registrado. Por favor, regístrese primero.")
             
   

    # def verificar_login(self):
    #     cuil = self.entry_cuil.get()
    #     paciente = obtener_paciente(cuil)
    #     if paciente:
    #         self.cuil = cuil
    #         self.abrir_perfil(cuil)
    #     else:
    #         messagebox.showerror("Error", "CUIL no registrado. Por favor, regístrese primero.")
    
    def verificar_login(self):
        cuil = self.cuil_entry.get()
        paciente = obtener_paciente(cuil)
        if paciente:
            messagebox.showinfo("Éxito", f"Bienvenido, paciente con CUIL {cuil}")
            #self.crear_pantalla_principal()
            self.abrir_perfil(cuil)
        else:
            messagebox.showerror("Error", "CUIL no registrado. Por favor, regístrese primero.")


    # def abrir_perfil(self, cuil):
    #     self.ventana_sesion.pack_forget()
    #     self.perfil_frame = tk.Frame(self.root)
    #     self.perfil_frame.pack(pady=50)

    #     self.label_perfil = tk.Label(self.perfil_frame, text=f"Perfil de Paciente: CUIL {cuil}", font=("Arial", 16))
    #     self.label_perfil.pack(pady=10)

    #     self.boton_historial = tk.Button(self.perfil_frame, text="Ver Historial Gráfico",
    #                                      command=lambda: self.mostrar_historial(self.cuil))
    #     self.boton_historial.pack(pady=10)

    #     self.boton_datos = tk.Button(self.perfil_frame, text="Capturar Datos Nuevos",
    #                                  command=lambda: self.obtener_datos(self.cuil))
    #     self.boton_datos.pack(pady=10)
    #     #agregado:
    
        
    #     self.boton_descargar_pdf = tk.Button(self.perfil_frame, text="Descargar PDF",
    #                                  command=lambda: self.descargar_pdf(self.cuil))
    #     self.boton_descargar_pdf.pack(pady=10)
        
    #     ############################
    #     self.boton_enviar = tk.Button(self.root, text="Enviar Correo", command=self.abrienviocorreo)
    #     self.boton_enviar.pack(pady=10)
    
   
     

    # def abrienviocorreo(self):

    #  abrir = DiagnosticoDifusoApp( root)
    def abrienviocorreo(self):
    # Abrir la interfaz de correo
     correo_ventana = tk.Toplevel(self.root)
     DiagnosticoDifusoApp(correo_ventana)

        
        #########################


    # def registro(self):
    #     self.login_frame.pack_forget()
    #     self.ventana_registro = tk.Frame(self.root)
    #     self.ventana_registro.pack(pady=50)

    #     self.label_nombre = tk.Label(self.ventana_registro, text="Nombre", font=("Arial", 12))
    #     self.label_nombre.pack(pady=5)

    #     self.entry_nombre = tk.Entry(self.ventana_registro)
    #     self.entry_nombre.pack(pady=5)

    #     self.label_edad = tk.Label(self.ventana_registro, text="Edad", font=("Arial", 12))
    #     self.label_edad.pack(pady=5)

    #     self.entry_edad = tk.Entry(self.ventana_registro)
    #     self.entry_edad.pack(pady=5)

    #     self.label_telefono = tk.Label(self.ventana_registro, text="Teléfono", font=("Arial", 12))
    #     self.label_telefono.pack(pady=5)

    #     self.entry_telefono = tk.Entry(self.ventana_registro)
    #     self.entry_telefono.pack(pady=5)

    #     self.label_cuil_registro = tk.Label(self.ventana_registro, text="CUIL", font=("Arial", 12))
    #     self.label_cuil_registro.pack(pady=5)
    #     ################################33
        
    #     self.label_correo = tk.Label(self.ventana_registro, text="Correo Electrónico", font=("Arial", 12))
    #     self.label_correo.pack(pady=5)

    #     # Campo de entrada para correo electrónico
    #     self.entry_correo = tk.Entry(self.ventana_registro)
    #     self.entry_correo.pack(pady=5)
        
    #     ############################################

    #     self.entry_cuil_registro = tk.Entry(self.ventana_registro)
    #     self.entry_cuil_registro.pack(pady=5)

    #     self.boton_registrar = tk.Button(self.ventana_registro, text="Registrar", command=self.registrar_paciente)
    #     self.boton_registrar.pack(pady=10)

    # def registrar_paciente(self):
    #     nombre = self.entry_nombre.get()
    #     edad = self.entry_edad.get()
    #     telefono = self.entry_telefono.get()
    #     cuil = self.entry_cuil_registro.get()
        
    #     ##################################
    #     correo = self.entry_correo.get()

    #     if obtener_paciente(cuil):
    #         messagebox.showerror("Error", "El CUIL ya está registrado.")
    #     else:
    #         agregar_paciente(nombre, edad, telefono, cuil, correo)
    #         messagebox.showinfo("Éxito", "Registro exitoso. Puede iniciar sesión ahora.")
    #         self.ventana_registro.pack_forget()
    #         self.login_frame.pack(pady=50)
    
   

        
        ##########################

        # if obtener_paciente(cuil):
        #     messagebox.showerror("Error", "El CUIL ya está registrado.")
        # else:
        #     agregar_paciente(nombre, edad, telefono, cuil)
        #     messagebox.showinfo("Éxito", "Registro exitoso. Puede iniciar sesión ahora.")
        #     self.ventana_registro.pack_forget()
        #     self.login_frame.pack(pady=50)



    # def mostrar_historial(self, cuil):
    #  datos_historial = obtener_historial(cuil)  # Obtiene el historial del paciente
    #  if datos_historial:  # Si hay datos disponibles
    #     datos = {
    #         "temperatura": [registro[2] for registro in datos_historial],
    #         "frecuencia_cardiaca": [registro[3] for registro in datos_historial],
    #         "presion_arterial": [registro[4] for registro in datos_historial],
    #         "diagnostico": [registro[5] for registro in datos_historial]
    #     }

    #     # Generar el gráfico
    #     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #     axs = axs.ravel()

    #     axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #     axs[0].set_title("Evolución de la Temperatura")
    #     axs[0].set_xlabel("Sesión")
    #     axs[0].set_ylabel("Temperatura (°C)")
    #     axs[0].legend()

    #     axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #     axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #     axs[1].set_xlabel("Sesión")
    #     axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #     axs[1].legend()

    #     axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #     axs[2].set_title("Evolución de la Presión Arterial")
    #     axs[2].set_xlabel("Sesión")
    #     axs[2].set_ylabel("Presión Arterial (mmHg)")
    #     axs[2].legend()

    #     axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #     axs[3].set_title("Evolución del Diagnóstico")
    #     axs[3].set_xlabel("Sesión")
    #     axs[3].set_ylabel("Diagnóstico")
    #     axs[3].legend()

    #     plt.tight_layout()
    #     plt.show()
    #  else:  # Si no hay datos en la base de datos
    #     messagebox.showinfo("Historial", "No hay datos disponibles.")
    
    
    # def mostrar_historial(self, cuil):
    #  datos_historial = obtener_historial(cuil)  # Obtiene el historial del paciente
    #  if datos_historial:  # Verifica que haya datos disponibles
    #     datos = {
    #         "temperatura": [registro[2] for registro in datos_historial],
    #         "frecuencia_cardiaca": [registro[3] for registro in datos_historial],
    #         "presion_arterial": [registro[4] for registro in datos_historial],
    #         "nivel_oxigeno": [registro[5] for registro in datos_historial]
    #     }

    #     # Generar el gráfico actual (subplots separados)
    #     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #     axs = axs.ravel()

    #     axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #     axs[0].set_title("Evolución de la Temperatura")
    #     axs[0].set_xlabel("Sesión")
    #     axs[0].set_ylabel("Temperatura (°C)")
    #     axs[0].legend()

    #     axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #     axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #     axs[1].set_xlabel("Sesión")
    #     axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #     axs[1].legend()

    #     axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #     axs[2].set_title("Evolución de la Presión Arterial")
    #     axs[2].set_xlabel("Sesión")
    #     axs[2].set_ylabel("Presión Arterial (mmHg)")
    #     axs[2].legend()

    #     axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #     axs[3].set_title("Evolución del Diagnóstico")
    #     axs[3].set_xlabel("Sesión")
    #     axs[3].set_ylabel("Diagnóstico")
    #     axs[3].legend()

    #     plt.tight_layout()
    #     plt.show()

    #     # Generar el gráfico de barras (nuevo gráfico)
    #     import numpy as np

    #     sesiones = np.arange(1, len(datos["temperatura"]) + 1)  # Sesiones (1, 2, 3, ...)
    #     bar_width = 0.2  # Ancho de las barras
    #     plt.figure(figsize=(12, 6))

    #     # Barras
    #     plt.bar(sesiones - bar_width * 1.5, datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #     plt.bar(sesiones - bar_width * 0.5, datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #     plt.bar(sesiones + bar_width * 0.5, datos["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
    #     plt.bar(sesiones + bar_width * 1.5, datos["nivel_oxigeno"], bar_width, label='Nivel de Oxígeno (%)', color='purple')

    #     # Etiquetas y título
    #     plt.xlabel("Sesión")
    #     plt.ylabel("Valores")
    #     plt.title("Resumen de Valores Biométricos por Sesión")
    #     plt.xticks(sesiones)  # Etiquetas en el eje X
    #     plt.legend()
    #     plt.tight_layout()

    #     # Mostrar el gráfico de barras
    #     plt.show()
    #  else:
    #     messagebox.showinfo("Historial", "No hay datos disponibles.")

    # def mostrar_historial(self, cuil):
    # # Obtener el historial del paciente desde la base de datos
    #  datos_historial = obtener_historial(cuil)
    #  if datos_historial:  # Verifica si hay datos disponibles
    #     # Procesar los datos en un diccionario
    #     try:
    #         datos = {
    #             "temperatura": [registro[2] for registro in datos_historial],
    #             "frecuencia_cardiaca": [registro[3] for registro in datos_historial],
    #             "presion_arterial": [registro[4] for registro in datos_historial],
    #             "diagnostico": [registro[5] for registro in datos_historial],
    #         }
    #     except IndexError:
    #         messagebox.showerror("Error", "Los datos no están completos en la base de datos.")
    #         return

    #     # Generar gráficos individuales (ya existente)
    #     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #     axs = axs.ravel()

    #     axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #     axs[0].set_title("Evolución de la Temperatura")
    #     axs[0].set_xlabel("Sesión")
    #     axs[0].set_ylabel("Temperatura (°C)")
    #     axs[0].legend()

    #     axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #     axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #     axs[1].set_xlabel("Sesión")
    #     axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #     axs[1].legend()

    #     axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #     axs[2].set_title("Evolución de la Presión Arterial")
    #     axs[2].set_xlabel("Sesión")
    #     axs[2].set_ylabel("Presión Arterial (mmHg)")
    #     axs[2].legend()

    #     axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #     axs[3].set_title("Evolución del Diagnóstico")
    #     axs[3].set_xlabel("Sesión")
    #     axs[3].set_ylabel("Diagnóstico")
    #     axs[3].legend()

    #     plt.tight_layout()
    #     plt.show()

    #     # Generar gráfico de barras (nuevo gráfico)
    #     import numpy as np

    #     sesiones = np.arange(1, len(datos["temperatura"]) + 1)
    #     bar_width = 0.2

    #     plt.figure(figsize=(12, 6))
    #     plt.bar(sesiones - bar_width * 1.5, datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #     plt.bar(sesiones - bar_width * 0.5, datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #     plt.bar(sesiones + bar_width * 0.5, datos["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
    #     plt.bar(sesiones + bar_width * 1.5, datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

    #     plt.xlabel("Sesión")
    #     plt.ylabel("Valores")
    #     plt.title("Resumen de Valores Biométricos por Sesión")
    #     plt.legend()
    #     plt.tight_layout()
    #     plt.show()

    #  else:
    #     messagebox.showinfo("Historial", "No hay datos disponibles.")

    
    # def obtener_datos(self, cuil):
    #     self.ventana_datos = tk.Toplevel(self.root)
    #     self.ventana_datos.title("Captura de Datos")

    #     self.label_temperatura = tk.Label(self.ventana_datos, text="Temperatura (°C):", font=("Arial", 12))
    #     self.label_temperatura.pack(pady=5)
    #     self.entry_temperatura = tk.Entry(self.ventana_datos)
    #     self.entry_temperatura.pack(pady=5)

    #     self.label_presion = tk.Label(self.ventana_datos, text="Presión Arterial (mmHg):", font=("Arial", 12))
    #     self.label_presion.pack(pady=5)
    #     self.entry_presion = tk.Entry(self.ventana_datos)
    #     self.entry_presion.pack(pady=5)

    #     self.label_frecuencia = tk.Label(self.ventana_datos, text="Frecuencia Cardíaca (lpm):", font=("Arial", 12))
    #     self.label_frecuencia.pack(pady=5)
    #     self.entry_frecuencia = tk.Entry(self.ventana_datos)
    #     self.entry_frecuencia.pack(pady=5)

    #     self.label_oxigeno = tk.Label(self.ventana_datos, text="Nivel de Oxígeno (%):", font=("Arial", 12))
    #     self.label_oxigeno.pack(pady=5)
    #     self.entry_oxigeno = tk.Entry(self.ventana_datos)
    #     self.entry_oxigeno.pack(pady=5)

    #     self.boton_guardar = tk.Button(self.ventana_datos, text="Guardar Datos",
    #                                    command=lambda: self.realizar_diagnostico(cuil))
    #     self.boton_guardar.pack(pady=10)
    
    
    def obtener_datos(self, cuil):
    # Crear una ventana para capturar nuevos datos
      self.ventana_datos = tk.Toplevel(self.root)
      self.ventana_datos.title("Captura de Datos")

    # Campo: Temperatura
      label_temperatura = tk.Label(self.ventana_datos, text="Temperatura (°C):", font=("Arial", 12))
      label_temperatura.pack(pady=5)
      self.entry_temperatura = tk.Entry(self.ventana_datos)
      self.entry_temperatura.pack(pady=5)

    # Campo: Presión Arterial
      label_presion = tk.Label(self.ventana_datos, text="Presión Arterial (mmHg):", font=("Arial", 12))
      label_presion.pack(pady=5)
      self.entry_presion = tk.Entry(self.ventana_datos)
      self.entry_presion.pack(pady=5)

    # Campo: Frecuencia Cardíaca
      label_frecuencia = tk.Label(self.ventana_datos, text="Frecuencia Cardíaca (lpm):", font=("Arial", 12))
      label_frecuencia.pack(pady=5)
      self.entry_frecuencia = tk.Entry(self.ventana_datos)
      self.entry_frecuencia.pack(pady=5)

    # Campo: Nivel de Oxígeno
      label_oxigeno = tk.Label(self.ventana_datos, text="Nivel de Oxígeno (%):", font=("Arial", 12))
      label_oxigeno.pack(pady=5)
      self.entry_oxigeno = tk.Entry(self.ventana_datos)
      self.entry_oxigeno.pack(pady=5)

    #Botón para guardar los datos y realizar el diagnóstico
      boton_guardar = tk.Button(self.ventana_datos, text="Guardar Datos",
                               command=lambda: self.realizar_diagnostico(cuil))
      boton_guardar.pack(pady=10)
      
       
        # boton_datos = ttk.Button(
        # self.perfil_frame,
        # text="Capturar Datos Nuevos",
        # bootstyle="primary",
        # command=lambda: self.obtener_datos(cuil)  # Llama al método obtener_datos
        # )
        # boton_datos.pack(fill="x", pady=10)

    
    
    def mostrar_historial(self, cuil):
     datos_historial = obtener_historial(cuil)  # Obtiene el historial del paciente
     if datos_historial:  # Verifica si hay datos disponibles
        try:
            # Procesar los datos en un diccionario
            datos = {
                "temperatura": [registro[2] for registro in datos_historial if registro[2] is not None],
                "frecuencia_cardiaca": [registro[3] for registro in datos_historial if registro[3] is not None],
                "presion_arterial": [registro[4] for registro in datos_historial if registro[4] is not None],
                "diagnostico": [registro[5] for registro in datos_historial if registro[5] is not None],
            }

            # Validar que haya datos en todas las listas
            for key, values in datos.items():
                if not values:  # Si alguna lista está vacía
                    raise ValueError(f"No hay datos válidos para {key}. Los gráficos no se pueden generar correctamente.")

            # Generar gráficos individuales (subplots)
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

            # Generar el gráfico de barras (nuevo gráfico)
            import numpy as np
            sesiones = np.arange(1, len(datos["temperatura"]) + 1)
            bar_width = 0.2

            plt.figure(figsize=(12, 6))
            plt.bar(sesiones - bar_width * 1.5, datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
            plt.bar(sesiones - bar_width * 0.5, datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
            plt.bar(sesiones + bar_width * 0.5, datos["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
            plt.bar(sesiones + bar_width * 1.5, datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

            plt.xlabel("Sesión")
            plt.ylabel("Valores")
            plt.title("Resumen de Valores Biométricos por Sesión")
            plt.legend()
            plt.tight_layout()
            plt.show()

        except ValueError as e:
            messagebox.showinfo("Datos insuficientes", str(e))

     else:
        messagebox.showinfo("Historial", "No hay datos disponibles.")

        
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
        
    # def descargar_pdf(self, cuil):
    #     # Obtener historial directamente de la base de datos
    #     datos_historial = obtener_historial(cuil)
    #     if not datos_historial:
    #         messagebox.showerror("Error", "No hay historial disponible para descargar el PDF.")
    #         return

    #     # Procesar los datos del historial
    #     datos = {
    #         "temperatura": [registro[2] for registro in datos_historial if registro[2] is not None],
    #         "frecuencia_cardiaca": [registro[3] for registro in datos_historial if registro[3] is not None],
    #         "presion_arterial": [registro[4] for registro in datos_historial if registro[4] is not None],
    #         "diagnostico": [registro[5] for registro in datos_historial if registro[5] is not None],
    #         "recomendaciones": [registro[5] for registro in datos_historial if registro[5] is not None]  # Ajusta según el índice correcto
    #     }

    #     # Validar que haya datos suficientes para los gráficos
    #     if not all(len(values) > 0 for values in datos.values()):
    #         messagebox.showerror("Error", "No hay suficientes datos para generar los gráficos en el PDF.")
    #         return

    #     # Crear el archivo PDF
    #     pdf_path = f"diagnostico_{cuil}.pdf"
    #     c = canvas.Canvas(pdf_path, pagesize=letter)
    #     y_position = 750  # Posición inicial del contenido en el eje Y

    #     # Título principal
    #     c.drawString(100, y_position, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")
    #     y_position -= 20

    #     # Agregar datos biométricos al PDF
    #     c.drawString(100, y_position, "Últimos Datos Biométricos:")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Temperatura: {datos['temperatura'][-1]}°C")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Diagnóstico: {datos['diagnostico'][-1]}")
    #     y_position -= 40

    #     # Agregar recomendaciones
    #     c.drawString(100, y_position, "Recomendaciones:")
    #     y_position -= 20
    #     for recomendacion in datos["recomendaciones"]:
    #         c.drawString(120, y_position, f"- {recomendacion}")
    #         y_position -= 20

    #     try:
    #         # Generar el gráfico original (4 subplots)
    #         fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #         axs = axs.ravel()

    #         axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #         axs[0].set_title("Evolución de la Temperatura")
    #         axs[0].set_xlabel("Sesión")
    #         axs[0].set_ylabel("Temperatura (°C)")
    #         axs[0].legend()

    #         axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #         axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #         axs[1].set_xlabel("Sesión")
    #         axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #         axs[1].legend()

    #         axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #         axs[2].set_title("Evolución de la Presión Arterial")
    #         axs[2].set_xlabel("Sesión")
    #         axs[2].set_ylabel("Presión Arterial (mmHg)")
    #         axs[2].legend()

    #         axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #         axs[3].set_title("Evolución del Diagnóstico")
    #         axs[3].set_xlabel("Sesión")
    #         axs[3].set_ylabel("Diagnóstico")
    #         axs[3].legend()

    #         plt.tight_layout()
    #         original_graph_path = "original_historial.png"
    #         plt.savefig(original_graph_path)
    #         plt.close()

    #         c.drawImage(original_graph_path, 100, y_position - 300, width=400, height=300)
    #         os.remove(original_graph_path)

    #         # Generar gráfico de barras
    #         sesiones = range(1, len(datos["temperatura"]) + 1)
    #         bar_width = 0.2

    #         plt.figure(figsize=(12, 6))
    #         plt.bar([s - bar_width * 1.5 for s in sesiones], datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #         plt.bar([s - bar_width * 0.5 for s in sesiones], datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #         plt.bar([s + bar_width * 0.5 for s in sesiones], datos["presion_arterial"], bar_width, label='Presión Arterial', color='red')
    #         plt.bar([s + bar_width * 1.5 for s in sesiones], datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

    #         plt.xlabel("Sesión")
    #         plt.ylabel("Valores")
    #         plt.title("Resumen de Valores Biométricos por Sesión")
    #         plt.legend()
    #         plt.tight_layout()

    #         barras_path = "barras_historial.png"
    #         plt.savefig(barras_path)
    #         plt.close()

    #         c.drawImage(barras_path, 100, y_position - 600, width=400, height=300)
    #         os.remove(barras_path)

    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error al generar los gráficos: {e}")
    #         return

    #     # Guardar el PDF
    #     c.save()
    #     messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")
        
    ####porfa san expedito te lo pido porfa
    
    def descargar_pdf(self, cuil):
        # Obtener historial directamente de la base de datos
        datos_historial = obtener_historial(cuil)
        if not datos_historial:
            messagebox.showerror("Error", "No hay historial disponible para descargar el PDF.")
            return

        # Procesar los datos del historial
        datos = {
            "temperatura": [registro[2] for registro in datos_historial if registro[2] is not None],
            "frecuencia_cardiaca": [registro[3] for registro in datos_historial if registro[3] is not None],
            "presion_arterial": [registro[4] for registro in datos_historial if registro[4] is not None],
            "diagnostico": [registro[5] for registro in datos_historial if registro[5] is not None],
        }

        # Validar que haya datos suficientes para los gráficos
        if not all(len(values) > 0 for values in datos.values()):
            messagebox.showerror("Error", "No hay suficientes datos para generar los gráficos en el PDF.")
            return

        # Crear el archivo PDF
        pdf_path = f"diagnostico_{cuil}.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        y_position = 750  # Posición inicial del contenido en el eje Y

        # Título principal
        c.drawString(100, y_position, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")
        y_position -= 20

        # Agregar datos biométricos al PDF
        c.drawString(100, y_position, "Últimos Datos Biométricos:")
        y_position -= 20
        c.drawString(120, y_position, f"Temperatura: {datos['temperatura'][-1]}°C")
        y_position -= 20
        c.drawString(120, y_position, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
        y_position -= 20
        c.drawString(120, y_position, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")
        y_position -= 20
        c.drawString(120, y_position, f"Diagnóstico: {datos['diagnostico'][-1]}")
        y_position -= 40

        # Incluir recomendaciones (de último diagnóstico)
        recomendaciones = generar_recomendaciones(
            {
                "temperatura": datos["temperatura"][-1],
                "presion_arterial": datos["presion_arterial"][-1],
                "frecuencia_cardiaca": datos["frecuencia_cardiaca"][-1],
                "nivel_oxigeno": 95  # Valor por defecto si no está en la base de datos
            },
            datos["diagnostico"][-1]
        )

        c.drawString(100, y_position, "Recomendaciones:")
        y_position -= 20
        for recomendacion in recomendaciones:
            c.drawString(120, y_position, f"- {recomendacion}")
            y_position -= 20

        try:
            # Generar el gráfico original (4 subplots)
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
            original_graph_path = "original_historial.png"
            plt.savefig(original_graph_path)
            plt.close()

            c.drawImage(original_graph_path, 100, y_position - 300, width=400, height=300)
            os.remove(original_graph_path)

            # Generar gráfico de barras
            sesiones = range(1, len(datos["temperatura"]) + 1)
            bar_width = 0.2

            plt.figure(figsize=(12, 6))
            plt.bar([s - bar_width * 1.5 for s in sesiones], datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
            plt.bar([s - bar_width * 0.5 for s in sesiones], datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
            plt.bar([s + bar_width * 0.5 for s in sesiones], datos["presion_arterial"], bar_width, label='Presión Arterial', color='red')
            plt.bar([s + bar_width * 1.5 for s in sesiones], datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

            plt.xlabel("Sesión")
            plt.ylabel("Valores")
            plt.title("Resumen de Valores Biométricos por Sesión")
            plt.legend()
            plt.tight_layout()

            barras_path = "barras_historial.png"
            plt.savefig(barras_path)
            plt.close()

            c.drawImage(barras_path, 100, y_position - 600, width=400, height=300)
            os.remove(barras_path)

        except Exception as e:
            messagebox.showerror("Error", f"Error al generar los gráficos: {e}")
            return

        # Guardar el PDF
        c.save()
        messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")

           
    # def descargar_pdf(self, cuil):
    #     # Obtener historial directamente de la base de datos
    #     datos_historial = obtener_historial(cuil)
    #     if not datos_historial:
    #         messagebox.showerror("Error", "No hay historial disponible para descargar el PDF.")
    #         return

    #     # Procesar los datos del historial
    #     datos = {
    #         "temperatura": [registro[2] for registro in datos_historial if registro[2] is not None],
    #         "frecuencia_cardiaca": [registro[3] for registro in datos_historial if registro[3] is not None],
    #         "presion_arterial": [registro[4] for registro in datos_historial if registro[4] is not None],
    #         "diagnostico": [registro[5] for registro in datos_historial if registro[5] is not None],
    #     }

    #     # Validar que haya datos suficientes para los gráficos
    #     if not all(len(values) > 0 for values in datos.values()):
    #         messagebox.showerror("Error", "No hay suficientes datos para generar los gráficos en el PDF.")
    #         return

    #     # Crear el archivo PDF
    #     pdf_path = f"diagnostico_{cuil}.pdf"
    #     c = canvas.Canvas(pdf_path, pagesize=letter)
    #     y_position = 750  # Posición inicial del contenido en el eje Y

    #     # Título principal
    #     c.drawString(100, y_position, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")
    #     y_position -= 20

    #     # Agregar datos biométricos al PDF
    #     c.drawString(100, y_position, "Últimos Datos Biométricos:")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Temperatura: {datos['temperatura'][-1]}°C")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")
    #     y_position -= 20
    #     c.drawString(120, y_position, f"Diagnóstico: {datos['diagnostico'][-1]}")
    #     y_position -= 40

    #     try:
    #         # Generar el gráfico original (4 subplots)
    #         fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #         axs = axs.ravel()

    #         axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #         axs[0].set_title("Evolución de la Temperatura")
    #         axs[0].set_xlabel("Sesión")
    #         axs[0].set_ylabel("Temperatura (°C)")
    #         axs[0].legend()

    #         axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #         axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #         axs[1].set_xlabel("Sesión")
    #         axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #         axs[1].legend()

    #         axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #         axs[2].set_title("Evolución de la Presión Arterial")
    #         axs[2].set_xlabel("Sesión")
    #         axs[2].set_ylabel("Presión Arterial (mmHg)")
    #         axs[2].legend()

    #         axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #         axs[3].set_title("Evolución del Diagnóstico")
    #         axs[3].set_xlabel("Sesión")
    #         axs[3].set_ylabel("Diagnóstico")
    #         axs[3].legend()

    #         plt.tight_layout()
    #         original_graph_path = "original_historial.png"
    #         plt.savefig(original_graph_path)
    #         plt.close()

    #         c.drawImage(original_graph_path, 100, y_position - 300, width=400, height=300)
    #         os.remove(original_graph_path)

    #         # Generar gráfico de barras
    #         sesiones = range(1, len(datos["temperatura"]) + 1)
    #         bar_width = 0.2

    #         plt.figure(figsize=(12, 6))
    #         plt.bar([s - bar_width * 1.5 for s in sesiones], datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #         plt.bar([s - bar_width * 0.5 for s in sesiones], datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #         plt.bar([s + bar_width * 0.5 for s in sesiones], datos["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
    #         plt.bar([s + bar_width * 1.5 for s in sesiones], datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

    #         plt.xlabel("Sesión")
    #         plt.ylabel("Valores")
    #         plt.title("Resumen de Valores Biométricos por Sesión")
    #         plt.legend()
    #         plt.tight_layout()

    #         barras_path = "barras_historial.png"
    #         plt.savefig(barras_path)
    #         plt.close()

    #         c.drawImage(barras_path, 100, y_position - 600, width=400, height=300)
    #         os.remove(barras_path)

    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error al generar los gráficos: {e}")
    #         return

    #     # Guardar el PDF
    #     c.save()
    #     messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")

 

           

     
                           
        
    

    # def descargar_pdf(self, cuil):
    #  if not self.ultimo_historial:
    #   messagebox.showerror("Error", "Primero debe ingresar síntomas y ver el diagnóstico antes de descargar el PDF.")
    #   return

    # # Crear el archivo PDF
    #  pdf_path = f"diagnostico_{cuil}.pdf"
    #  c = canvas.Canvas(pdf_path, pagesize=letter)
    #  c.drawString(100, 750, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")

    #  datos = self.ultimo_historial

    # # Guardar el gráfico de barras como imagen
    #  import numpy as np
    #  import matplotlib.pyplot as plt

    #  sesiones = np.arange(1, len(datos["temperatura"]) + 1)
    #  bar_width = 0.2

    #  plt.figure(figsize=(12, 6))
    #  plt.bar(sesiones - bar_width * 1.5, datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #  plt.bar(sesiones - bar_width * 0.5, datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #  plt.bar(sesiones + bar_width * 0.5, datos["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
    #  plt.bar(sesiones + bar_width * 1.5, datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

    #  plt.xlabel("Sesión")
    #  plt.ylabel("Valores")
    #  plt.title("Resumen de Valores Biométricos por Sesión")
    #  plt.legend()
    #  plt.tight_layout()

    #  barras_path = "barras_historial.png"
    #  plt.savefig(barras_path)
    #  plt.close()

    # # Insertar el gráfico en el PDF
    #  c.drawImage(barras_path, 100, 250, width=400, height=300)

    # # Eliminar la imagen temporal después de usarla
    #  import os
    #  os.remove(barras_path)

    # # Guardar el PDF
    #  c.save()
    #  messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")
    
    #este de abajo es jeje

    # def descargar_pdf(self, cuil):
    #   if not self.ultimo_historial:
    #     messagebox.showerror("Error", "Primero debe ingresar síntomas y ver el diagnóstico antes de descargar el PDF.")
    #     return

    # # Crear el archivo PDF
    #   pdf_path = f"diagnostico_{cuil}.pdf"
    #   c = canvas.Canvas(pdf_path, pagesize=letter)
    #   y_position = 750  # Posición inicial del contenido en el eje Y

    # # Título principal
    #   c.drawString(100, y_position, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")
    #   y_position -= 20

    # # Datos biométricos
    #   datos = self.ultimo_historial
    #   c.drawString(100, y_position, "Últimos Datos Biométricos:")
    #   y_position -= 20
    #   c.drawString(120, y_position, f"Temperatura: {datos['temperatura'][-1]}°C")
    #   y_position -= 20
    #   c.drawString(120, y_position, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
    #   y_position -= 20
    #   c.drawString(120, y_position, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")
    #   y_position -= 20
    #   c.drawString(120, y_position, f"Nivel de Oxígeno: {datos['nivel_oxigeno'][-1]}%")
    #   y_position -= 40

    # # Diagnóstico descriptivo
    #   c.drawString(100, y_position, f"Diagnóstico: {datos['diagnostico_descriptivo'][-1]}")
    #   y_position -= 20

    # # Recomendaciones
    #   c.drawString(100, y_position, "Recomendaciones:")
    #   y_position -= 20
    #   for recomendacion in datos["recomendaciones"][-1]:
    #     c.drawString(120, y_position, f"- {recomendacion}")
    #     y_position -= 20

    # # Generar y agregar el gráfico original (subplots)
    #     import matplotlib.pyplot as plt
    #     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #     axs = axs.ravel()

    #     axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #     axs[0].set_title("Evolución de la Temperatura")
    #     axs[0].set_xlabel("Sesión")
    #     axs[0].set_ylabel("Temperatura (°C)")
    #     axs[0].legend()

    #     axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #     axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #     axs[1].set_xlabel("Sesión")
    #     axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #     axs[1].legend()

    #     axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #     axs[2].set_title("Evolución de la Presión Arterial")
    #     axs[2].set_xlabel("Sesión")
    #     axs[2].set_ylabel("Presión Arterial (mmHg)")
    #     axs[2].legend()

    #     axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #     axs[3].set_title("Evolución del Diagnóstico")
    #     axs[3].set_xlabel("Sesión")
    #     axs[3].set_ylabel("Diagnóstico")
    #     axs[3].legend()

    #     plt.tight_layout()
    #     original_graph_path = "original_historial.png"
    #     plt.savefig(original_graph_path)
    #     plt.close()

    # # Insertar el gráfico original en el PDF
    #     c.drawImage(original_graph_path, 100, y_position - 300, width=400, height=300)
    #     y_position -= 320  # Ajustar espacio después del gráfico original

    # # Eliminar el gráfico original temporal
    #     import os
    #     os.remove(original_graph_path)

    # # Generar y agregar el nuevo gráfico de barras
    #     import numpy as np
    #     sesiones = np.arange(1, len(datos["temperatura"]) + 1)
    #     bar_width = 0.2

    #     plt.figure(figsize=(12, 6))
    #     plt.bar(sesiones - bar_width * 1.5, datos["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #     plt.bar(sesiones - bar_width * 0.5, datos["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #     plt.bar(sesiones + bar_width * 0.5, datos["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
    #     plt.bar(sesiones + bar_width * 1.5, datos["diagnostico"], bar_width, label='Diagnóstico', color='purple')

    #     plt.xlabel("Sesión")
    #     plt.ylabel("Valores")
    #     plt.title("Resumen de Valores Biométricos por Sesión")
    #     plt.legend()
    #     plt.tight_layout()

    #     barras_path = "barras_historial.png"
    #     plt.savefig(barras_path)
    #     plt.close()

    # # Insertar el gráfico de barras en el PDF
    #     c.drawImage(barras_path, 100, y_position - 300, width=400, height=300)

    # # Eliminar el gráfico de barras temporal
    #     os.remove(barras_path)

    # # Guardar el archivo PDF
    #     c.save()
    #     messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")
    
    
    # def descargar_pdf(self, cuil):
    #   if not self.ultimo_historial:
    #     messagebox.showerror("Error", "Primero debe ingresar síntomas y ver el diagnóstico antes de descargar el PDF.")
    #     return

    # # Crear el archivo PDF
    #    pdf_path = f"diagnostico_{cuil}.pdf"
    #    c = canvas.Canvas(pdf_path, pagesize=letter)
    #    y_position = 750  # Posición inicial del contenido en el eje Y

    # # Título principal
    #    c.drawString(100, y_position, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")
    #    y_position -= 20

    # # Datos biométricos
    #    datos = self.ultimo_historial
    #    c.drawString(100, y_position, "Últimos Datos Biométricos:")
    #    y_position -= 20
    #    c.drawString(120, y_position, f"Temperatura: {datos['temperatura'][-1]}°C")
    #    y_position -= 20
    #    c.drawString(120, y_position, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
    #    y_position -= 20
    #   c.drawString(120, y_position, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")
    #   y_position -= 20
    #   c.drawString(120, y_position, f"Nivel de Oxígeno: {datos['nivel_oxigeno'][-1]}%")
    #   y_position -= 40

    # # Diagnóstico descriptivo
    #   c.drawString(100, y_position, f"Diagnóstico: {datos['diagnostico_descriptivo'][-1]}")
    #   y_position -= 20

    # # Recomendaciones
    #   c.drawString(100, y_position, "Recomendaciones:")
    #   y_position -= 20
    #   for recomendacion in datos["recomendaciones"][-1]:
    #     c.drawString(120, y_position, f"- {recomendacion}")
    #     y_position -= 20

    # # Validar y procesar los datos para los gráficos
    # try:
    #     datos_validados = {
    #         "temperatura": [val for val in datos["temperatura"] if val is not None],
    #         "frecuencia_cardiaca": [val for val in datos["frecuencia_cardiaca"] if val is not None],
    #         "presion_arterial": [val for val in datos["presion_arterial"] if val is not None],
    #         "diagnostico": [val for val in datos["diagnostico"] if val is not None],
    #     }

    #     for key, values in datos_validados.items():
    #         if not values:  # Si alguna lista está vacía
    #             raise ValueError(f"No hay datos válidos para {key}. Los gráficos no se pueden generar correctamente.")

    #     # Generar gráfico original (subplots)
    #     import matplotlib.pyplot as plt
    #     fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #     axs = axs.ravel()

    #     axs[0].plot(datos_validados["temperatura"], marker='o', label="Temperatura")
    #     axs[0].set_title("Evolución de la Temperatura")
    #     axs[0].set_xlabel("Sesión")
    #     axs[0].set_ylabel("Temperatura (°C)")
    #     axs[0].legend()

    #     axs[1].plot(datos_validados["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #     axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #     axs[1].set_xlabel("Sesión")
    #     axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #     axs[1].legend()

    #     axs[2].plot(datos_validados["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #     axs[2].set_title("Evolución de la Presión Arterial")
    #     axs[2].set_xlabel("Sesión")
    #     axs[2].set_ylabel("Presión Arterial (mmHg)")
    #     axs[2].legend()

    #     axs[3].plot(range(len(datos_validados["diagnostico"])), datos_validados["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #     axs[3].set_title("Evolución del Diagnóstico")
    #     axs[3].set_xlabel("Sesión")
    #     axs[3].set_ylabel("Diagnóstico")
    #     axs[3].legend()

    #       plt.tight_layout()
    #       original_graph_path = "original_historial.png"
    #       plt.savefig(original_graph_path)
    #       plt.close()
    #       c.drawImage(original_graph_path, 100, y_position - 300, width=400, height=300)
    #       os.remove(original_graph_path)

    #     # Generar y agregar gráfico de barras
    #     sesiones = range(1, len(datos_validados["temperatura"]) + 1)
    #     bar_width = 0.2

    #     plt.figure(figsize=(12, 6))
    #     plt.bar([s - bar_width * 1.5 for s in sesiones], datos_validados["temperatura"], bar_width, label='Temperatura (°C)', color='blue')
    #     plt.bar([s - bar_width * 0.5 for s in sesiones], datos_validados["frecuencia_cardiaca"], bar_width, label='Frecuencia Cardíaca (bpm)', color='green')
    #     plt.bar([s + bar_width * 0.5 for s in sesiones], datos_validados["presion_arterial"], bar_width, label='Presión Arterial (mmHg)', color='red')
    #     plt.bar([s + bar_width * 1.5 for s in sesiones], datos_validados["diagnostico"], bar_width, label='Diagnóstico', color='purple')

    #     plt.xlabel("Sesión")
    #     plt.ylabel("Valores")
    #     plt.title("Resumen de Valores Biométricos por Sesión")
    #     plt.legend()
    #     plt.tight_layout()

    #     barras_path = "barras_historial.png"
    #     plt.savefig(barras_path)
    #     plt.close()
    #     c.drawImage(barras_path, 100, y_position - 600, width=400, height=300)
    #     os.remove(barras_path)

    # except ValueError as e:
    #     messagebox.showinfo("Datos insuficientes", str(e))

    # # Guardar el PDF
    # c.save()
    # messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")



        

   
      
          



    #     #este de abajo es el si
    # def descargar_pdf(self, cuil):
    #    if not self.ultimo_historial:
    #     messagebox.showerror("Error", "Primero debe ingresar síntomas y ver el diagnóstico antes de descargar el PDF.")
    #     return

    # # Crear el archivo PDF
    #    pdf_path = f"diagnostico_{cuil}.pdf"
    #    c = canvas.Canvas(pdf_path, pagesize=letter)
    #    c.drawString(100, 750, f"Diagnóstico y Recomendaciones para CUIL: {cuil}")

    # # Agregar los datos del historial al PDF
    #    datos = self.ultimo_historial
    #    c.drawString(100, 730, "Últimos Datos Biométricos:")
    #    c.drawString(120, 710, f"Temperatura: {datos['temperatura'][-1]}°C")
    #    c.drawString(120, 690, f"Frecuencia Cardíaca: {datos['frecuencia_cardiaca'][-1]} bpm")
    #    c.drawString(120, 670, f"Presión Arterial: {datos['presion_arterial'][-1]} mmHg")

    # # Validar que nivel_oxigeno esté disponible
    #    if "nivel_oxigeno" in datos and datos["nivel_oxigeno"]:
    #     c.drawString(120, 650, f"Nivel de Oxígeno: {datos['nivel_oxigeno'][-1]}%")
    #    else:
    #     c.drawString(120, 650, "Nivel de Oxígeno: No disponible.")

    # # Mostrar el diagnóstico descriptivo en el PDF
    #    if "diagnostico" in datos and datos["diagnostico"]:
    #     c.drawString(120, 630, f"Diagnóstico: {datos['diagnostico'][-1]}")  # Texto descriptivo
    #    else:
    #     c.drawString(120, 630, "Diagnóstico: No disponible.")

    # # Agregar recomendaciones
    #    y_position = 610
    #    if "recomendaciones" in datos and datos["recomendaciones"]:
    #     c.drawString(100, y_position, "Recomendaciones:")
    #     y_position -= 20
    #     for recomendacion in datos["recomendaciones"][-1]:
    #         c.drawString(120, y_position, f"- {recomendacion}")
    #         y_position -= 20  # Ajusta la posición vertical para cada recomendación
    #    else:
    #     c.drawString(100, y_position, "Recomendaciones: No disponibles.")
    #     y_position -= 20

    # # Generar el gráfico con subplots
    #    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    #    axs = axs.ravel()

    #    axs[0].plot(datos["temperatura"], marker='o', label="Temperatura")
    #    axs[0].set_title("Evolución de la Temperatura")
    #    axs[0].set_xlabel("Sesión")
    #    axs[0].set_ylabel("Temperatura (°C)")
    #    axs[0].legend()

    #    axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca")
    #    axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    #    axs[1].set_xlabel("Sesión")
    #    axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    #    axs[1].legend()

    #    axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial")
    #    axs[2].set_title("Evolución de la Presión Arterial")
    #    axs[2].set_xlabel("Sesión")
    #    axs[2].set_ylabel("Presión Arterial (mmHg)")
    #    axs[2].legend()

    #    axs[3].plot(range(len(datos["diagnostico"])), datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    #    axs[3].set_title("Evolución del Diagnóstico")
    #    axs[3].set_xlabel("Sesión")
    #    axs[3].set_ylabel("Diagnóstico")
    #    axs[3].legend()
 
    #    plt.tight_layout()

    # # Guardar el gráfico como imagen temporal
    #    temp_image_path = "temp_historial.png"
    #    plt.savefig(temp_image_path)
    #    plt.close()

    # # Insertar el gráfico en el PDF
    #    c.drawImage(temp_image_path, 100, 250, width=400, height=300)

    # # Eliminar la imagen temporal después de usarla
    #    import os
    #    os.remove(temp_image_path)

    # # Guardar el archivo PDF
    #    c.save()
    #    messagebox.showinfo("PDF Generado", f"El PDF se ha guardado como {pdf_path}")
       
       
    
if __name__ == "__main__":
    #root = tk.Tk()
    root = ttk.Window(themename="flatly")  # Moderniza la ventana     
    app = SistemaDiagnosticoApp(root)
    root.mainloop()
   
# #    if __name__ == "__main__":
# #     root = ttk.Window(themename="flatly")  # Moderniza la ventana
# #     app = SistemaDiagnosticoApp(root)
# #     root.mainloop() 
        
