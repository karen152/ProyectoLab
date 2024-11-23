import tkinter as tk
# from tkinter import messagebox
# from input_data import obtener_datos_usuario
# from fuzzy_logic import SistemaDifuso
# from visualization import mostrar_graficos
# from db import inicializar_db, agregar_paciente, obtener_paciente, guardar_diagnostico, obtener_historial
# from historial_visualization import mostrar_historial
# from recommendations import generar_recomendaciones


# class SistemaDiagnosticoApp:
#     # Llama a inicializar_db para crear las tablas si no existen    
#     inicializar_db()

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sistema de Diagnóstico Médico")
#         self.root.geometry("500x400")

#         # Pantalla de Login
#         self.login_frame = tk.Frame(root)
#         self.login_frame.pack(pady=50)

#         self.label = tk.Label(self.login_frame, text="Sistema Difuso de Diagnóstico Médico", font=("Arial", 16))
#         self.label.grid(row=0, column=0, columnspan=2, pady=10)

#         self.boton_iniciar_sesion = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.iniciar_sesion)
#         self.boton_iniciar_sesion.grid(row=1, column=0, pady=10)

#         self.boton_registro = tk.Button(self.login_frame, text="Registrarse", command=self.registro)
#         self.boton_registro.grid(row=1, column=1, pady=10)

#     def iniciar_sesion(self):
#         # Mostrar ventana de inicio de sesión
#         self.login_frame.pack_forget()  # Oculta la pantalla de login
#         self.ventana_sesion = tk.Frame(self.root)
#         self.ventana_sesion.pack(pady=50)

#         self.label_cuil = tk.Label(self.ventana_sesion, text="Ingrese su CUIL", font=("Arial", 12))
#         self.label_cuil.pack(pady=5)

#         self.entry_cuil = tk.Entry(self.ventana_sesion)
#         self.entry_cuil.pack(pady=5)

#         self.boton_login = tk.Button(self.ventana_sesion, text="Iniciar Sesión", command=self.verificar_login)
#         self.boton_login.pack(pady=10)

#     def verificar_login(self):
#         cuil = self.entry_cuil.get()
#         paciente = obtener_paciente(cuil)  # Verifica si el CUIL existe en la base de datos
#         if paciente:
#             self.cuil = cuil  # Guardamos el CUIL en el objeto
#             self.abrir_perfil(cuil)
#         else:
#             messagebox.showerror("Error", "CUIL no registrado. Por favor, regístrese primero.")

#     def abrir_perfil(self, cuil):
#         # Una vez que el usuario inicia sesión, mostramos su perfil
#         self.ventana_sesion.pack_forget()  # Oculta la pantalla de sesión
#         self.perfil_frame = tk.Frame(self.root)
#         self.perfil_frame.pack(pady=50)

#         self.label_perfil = tk.Label(self.perfil_frame, text=f"Perfil de Paciente: CUIL {cuil}", font=("Arial", 16))
#         self.label_perfil.pack(pady=10)

#         # Botones para ver historial y capturar nuevos datos
#         self.boton_historial = tk.Button(self.perfil_frame, text="Ver Historial Gráfico", command=lambda: self.mostrar_historial(self.cuil))
#         self.boton_historial.pack(pady=10)

#         self.boton_datos = tk.Button(self.perfil_frame, text="Capturar Datos Nuevos", command=lambda: self.obtener_datos(self.cuil))
#         self.boton_datos.pack(pady=10)

#     def registro(self):
#         # Mostrar ventana de registro
#         self.login_frame.pack_forget()  # Oculta la pantalla de login
#         self.ventana_registro = tk.Frame(self.root)
#         self.ventana_registro.pack(pady=50)

#         self.label_nombre = tk.Label(self.ventana_registro, text="Nombre", font=("Arial", 12))
#         self.label_nombre.pack(pady=5)

#         self.entry_nombre = tk.Entry(self.ventana_registro)
#         self.entry_nombre.pack(pady=5)

#         self.label_edad = tk.Label(self.ventana_registro, text="Edad", font=("Arial", 12))
#         self.label_edad.pack(pady=5)

#         self.entry_edad = tk.Entry(self.ventana_registro)
#         self.entry_edad.pack(pady=5)

#         self.label_telefono = tk.Label(self.ventana_registro, text="Teléfono", font=("Arial", 12))
#         self.label_telefono.pack(pady=5)

#         self.entry_telefono = tk.Entry(self.ventana_registro)
#         self.entry_telefono.pack(pady=5)

#         self.label_cuil_registro = tk.Label(self.ventana_registro, text="CUIL", font=("Arial", 12))
#         self.label_cuil_registro.pack(pady=5)

#         self.entry_cuil_registro = tk.Entry(self.ventana_registro)
#         self.entry_cuil_registro.pack(pady=5)

#         self.boton_registrar = tk.Button(self.ventana_registro, text="Registrar", command=self.registrar_paciente)
#         self.boton_registrar.pack(pady=10)

#     def registrar_paciente(self):
#         nombre = self.entry_nombre.get()
#         edad = self.entry_edad.get()
#         telefono = self.entry_telefono.get()
#         cuil = self.entry_cuil_registro.get()

#         # Verificar que el CUIL no esté registrado ya
#         if obtener_paciente(cuil):
#             messagebox.showerror("Error", "El CUIL ya está registrado.")
#         else:
#             # Registrar el nuevo paciente
#             agregar_paciente(nombre, edad, telefono, cuil)
#             messagebox.showinfo("Éxito", "Registro exitoso. Puede iniciar sesión ahora.")
#             self.ventana_registro.pack_forget()
#             self.login_frame.pack(pady=50)

#     def mostrar_historial(self, cuil):
#         # Lógica para mostrar el historial (gráfico)
#         datos_historial = obtener_historial(cuil)  # Cargar datos desde la base de datos
#         if datos_historial:
#             mostrar_historial(datos_historial)  # Mostrar gráficos
#         else:
#             messagebox.showinfo("Historial", "No hay datos disponibles.")

#     def obtener_datos(self, cuil):
#         # Crear ventana para ingresar los datos biométricos
#         self.ventana_datos = tk.Toplevel(self.root)
#         self.ventana_datos.title("Captura de Datos")

#         # Labels y campos de entrada
#         self.label_temperatura = tk.Label(self.ventana_datos, text="Temperatura (°C):", font=("Arial", 12))
#         self.label_temperatura.pack(pady=5)
#         self.entry_temperatura = tk.Entry(self.ventana_datos)
#         self.entry_temperatura.pack(pady=5)

#         self.label_presion = tk.Label(self.ventana_datos, text="Presión Arterial (mmHg):", font=("Arial", 12))
#         self.label_presion.pack(pady=5)
#         self.entry_presion = tk.Entry(self.ventana_datos)
#         self.entry_presion.pack(pady=5)

#         self.label_frecuencia = tk.Label(self.ventana_datos, text="Frecuencia Cardíaca (lpm):", font=("Arial", 12))
#         self.label_frecuencia.pack(pady=5)
#         self.entry_frecuencia = tk.Entry(self.ventana_datos)
#         self.entry_frecuencia.pack(pady=5)

#         self.label_oxigeno = tk.Label(self.ventana_datos, text="Nivel de Oxígeno (%):", font=("Arial", 12))

#     def realizar_diagnostico(self, cuil):
#      try:
#         # Obtener los datos ingresados
#         temperatura = float(self.entry_temperatura.get())
#         presion_arterial = float(self.entry_presion.get())
#         frecuencia_cardiaca = int(self.entry_frecuencia.get())
#         nivel_oxigeno = float(self.entry_oxigeno.get())

#         # Validar los datos dentro de los rangos permitidos
#         if not (34 <= temperatura <= 42):
#             raise ValueError("La temperatura debe estar entre 34°C y 42°C.")
#         if not (80 <= presion_arterial <= 180):
#             raise ValueError("La presión arterial debe estar entre 80 mmHg y 180 mmHg.")
#         if not (50 <= frecuencia_cardiaca <= 130):
#             raise ValueError("La frecuencia cardíaca debe estar entre 50 bpm y 130 bpm.")
#         if not (90 <= nivel_oxigeno <= 100):
#             raise ValueError("El nivel de oxígeno debe estar entre 90% y 100%.")

#         # Crear un diccionario con los datos ingresados
#         datos_usuario = {
#             "temperatura": temperatura,
#             "presion_arterial": presion_arterial,
#             "frecuencia_cardiaca": frecuencia_cardiaca,
#             "nivel_oxigeno": nivel_oxigeno
#         }

#         # Realizar diagnóstico con el sistema difuso
#         sistema_difuso = SistemaDifuso()
#         resultado = sistema_difuso.diagnosticar(datos_usuario)

#         if resultado is not None:
#             messagebox.showinfo("Diagnóstico", f"Diagnóstico final: {resultado:.2f}")
#             # Guardar diagnóstico en la base de datos
#             guardar_diagnostico(cuil, datos_usuario, resultado)
#             # Mostrar gráficos personalizados
#             mostrar_graficos(datos_usuario)
#         else:
#             messagebox.showerror("Error", "No se pudo generar el diagnóstico. Verifica los datos ingresados.")
#      except ValueError as ve:
#         # Manejar errores de validación de datos
#         messagebox.showerror("Error", f"Datos inválidos: {ve}")
#      except Exception as e:
#         # Manejar errores generales
#         messagebox.showerror("Error", f"Se produjo un error inesperado: {e}")
        
#         if __name__ == "__main__":
#            root = tk.Tk()
#            app = SistemaDiagnosticoApp(root)
#            root.mainloop()



   