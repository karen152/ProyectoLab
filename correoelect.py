import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class DiagnosticoDifusoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enviar correo")
        self.cuil_paciente_actual = None
        self.correo_paciente = None
        self.archivos_adjuntos = []  # Lista para almacenar los archivos seleccionados

        # Input para ingresar el CUIL
        self.cuil_label = tk.Label(root, text="Ingrese el CUIL del paciente:")
        self.cuil_label.pack()
        self.cuil_entry = tk.Entry(root, width=30)
        self.cuil_entry.pack()

        self.cargar_button = tk.Button(root, text="Cargar Paciente", command=self.seleccionar_paciente)
        self.cargar_button.pack()

        # Crear widgets para mensaje y asunto
        self.asunto_label = tk.Label(root, text="Asunto:")
        self.asunto_label.pack()
        self.asunto_entry = tk.Entry(root, width=50)
        self.asunto_entry.pack()

        self.mensaje_label = tk.Label(root, text="Mensaje:")
        self.mensaje_label.pack()
        self.mensaje_text = tk.Text(root, height=10, width=50)
        self.mensaje_text.pack()

        # Botón para adjuntar archivos
        self.adjuntar_button = tk.Button(root, text="Adjuntar Archivos", command=self.adjuntar_archivos)
        self.adjuntar_button.pack()

        # Botón para enviar el correo
        self.enviar_button = tk.Button(root, text="Enviar Correo", command=self.enviar_correo)
        self.enviar_button.pack()

    # def seleccionar_paciente(self):
    #     """Obtiene el correo del paciente según el CUIL ingresado"""
    #     cuil = self.cuil_entry.get().strip()
    #     if not cuil:
    #         messagebox.showerror("Error", "Debe ingresar un CUIL.")
    #         return

    #     paciente = self.obtener_paciente_por_id(cuil)
    #     if paciente:
    #         self.cuil_paciente_actual = cuil
    #         self.correo_paciente = paciente['correo']
    #         messagebox.showinfo("Paciente Cargado", f"Correo del paciente: {self.correo_paciente}")
    #     else:
    #         messagebox.showerror("Error", "No se encontró un paciente con el CUIL ingresado.")
    
    # def seleccionar_paciente(self):
    #     """Obtiene el correo del paciente según el CUIL ingresado"""
    #     cuil = self.cuil_entry.get().strip()
    #     if not cuil:
    #         messagebox.showerror("Error", "Debe ingresar un CUIL.")
    #         return

    #     paciente = self.obtener_paciente_por_id(cuil)
    #     if paciente:
    #         self.cuil_paciente_actual = cuil
    #         self.correo_paciente = paciente['correo']
    #         messagebox.showinfo("Paciente Cargado", f"Correo del paciente: {self.correo_paciente}")

    #         # Configurar asunto y mensaje predefinidos
    #         self.asunto_entry.delete(0, tk.END)
    #         self.asunto_entry.insert(0, "Diagnóstico Personalizado")

    #         mensaje_predefinido = (
    #             f"Hola {paciente['nombre']},\n\n"
    #             "Adjuntamos a este correo el informe detallado de su diagnóstico médico personalizado. "
    #             "Si tiene alguna consulta, no dude en contactarnos.\n\n"
    #             "Saludos cordiales, Sofia aguirre y karen barraza"
    #         )
    #         self.mensaje_text.delete("1.0", tk.END)
    #         self.mensaje_text.insert("1.0", mensaje_predefinido)
    #     else:
    #         messagebox.showerror("Error", "No se encontró un paciente con el CUIL ingresado.")
    
    # def seleccionar_paciente(self):
    #     """Obtiene el correo del paciente según el CUIL ingresado y adjunta el PDF automáticamente"""
    #     cuil = self.cuil_entry.get().strip()
    #     if not cuil:
    #         messagebox.showerror("Error", "Debe ingresar un CUIL.")
    #         return

    #     paciente = self.obtener_paciente_por_id(cuil)
    #     if paciente:
    #         self.cuil_paciente_actual = cuil
    #         self.correo_paciente = paciente['correo']
    #         messagebox.showinfo("Paciente Cargado", f"Correo del paciente: {self.correo_paciente}")

    #         # Configurar asunto y mensaje predefinidos
    #         self.asunto_entry.delete(0, tk.END)
    #         self.asunto_entry.insert(0, "Diagnóstico Personalizado")

    #         mensaje_predefinido = (
    #             f"Hola {paciente['nombre']},\n\n"
    #             "Adjuntamos a este correo el informe detallado de su diagnóstico médico personalizado. "
    #             "Si tiene alguna consulta, no dude en contactarnos.\n\n"
    #             "Saludos cordiales,\nEl equipo médico"
    #         )
    #         self.mensaje_text.delete("1.0", tk.END)
    #         self.mensaje_text.insert("1.0", mensaje_predefinido)

    #         # Generar automáticamente el PDF y adjuntarlo
    #         pdf_path = f"diagnostico_{cuil}.pdf"
    #         self.generar_pdf(cuil, pdf_path)  # Método para crear el PDF
    #         self.archivos_adjuntos.append(pdf_path)  # Agregar PDF a la lista de adjuntos
    #         messagebox.showinfo("PDF Generado", f"El PDF se ha adjuntado automáticamente: {pdf_path}")

    #     else:
    #         messagebox.showerror("Error", "No se encontró un paciente con el CUIL ingresado.")

    def seleccionar_paciente(self):
        """Obtiene el correo del paciente según el CUIL ingresado y adjunta el PDF automáticamente"""
        cuil = self.cuil_entry.get().strip()
        if not cuil:
            messagebox.showerror("Error", "Debe ingresar un CUIL.")
            return

        paciente = self.obtener_paciente_por_id(cuil)
        if paciente:
            self.cuil_paciente_actual = cuil
            self.correo_paciente = paciente['correo']
            messagebox.showinfo("Paciente Cargado", f"Correo del paciente: {self.correo_paciente}")

            # Configurar asunto y mensaje predefinidos
            self.asunto_entry.delete(0, tk.END)
            self.asunto_entry.insert(0, "Diagnóstico Personalizado")

            mensaje_predefinido = (
                f"Hola {paciente['nombre']},\n\n"
                "Adjuntamos a este correo el informe detallado de su diagnóstico médico personalizado. "
                "Si tiene alguna consulta, no dude en contactarnos.\n\n"
                "Saludos cordiales,\nEl equipo médico"
            )
            self.mensaje_text.delete("1.0", tk.END)
            self.mensaje_text.insert("1.0", mensaje_predefinido)

            # Generar automáticamente el PDF y adjuntarlo
            pdf_path = f"diagnostico_{cuil}.pdf"
            self.generar_pdf(cuil, pdf_path)  # Generar el PDF
            self.archivos_adjuntos.append(pdf_path)  # Agregar PDF a la lista de adjuntos
            messagebox.showinfo("PDF Generado", f"El PDF se ha adjuntado automáticamente: {pdf_path}")

        else:
            messagebox.showerror("Error", "No se encontró un paciente con el CUIL ingresado.")


    def obtener_paciente_por_id(self, cuil):
        """Consulta la base de datos para obtener datos del paciente"""
        conn = sqlite3.connect('pacientes.db')
        cursor = conn.cursor()
        query = "SELECT nombre, correo FROM pacientes WHERE cuil = ?"
        cursor.execute(query, (cuil,))
        paciente = cursor.fetchone()
        conn.close()

        if paciente:
            return {'nombre': paciente[0], 'correo': paciente[1]}
        return None

    def adjuntar_archivos(self):
        """Abre un cuadro de diálogo para seleccionar archivos y los almacena en una lista"""
        archivos = filedialog.askopenfilenames(title="Seleccionar Archivos",
                                               filetypes=(("Todos los archivos", "."),
                                                          ("Archivos PDF", "*.pdf"),
                                                          ("Archivos de imagen", "*.jpg *.png *.jpeg"),
                                                          ("Archivos de Word", "*.doc *.docx")))
        if archivos:
            self.archivos_adjuntos.extend(archivos)  # Añadir los archivos seleccionados
            messagebox.showinfo("Archivos Adjuntos", f"Se han adjuntado {len(archivos)} archivos.")

    def enviar_correo(self):
        """Envía un correo al paciente con los archivos adjuntos"""
        asunto = self.asunto_entry.get().strip()
        mensaje = self.mensaje_text.get("1.0", tk.END).strip()

        if not asunto or not mensaje:
            messagebox.showerror("Error", "El asunto y el mensaje no pueden estar vacíos.")
            return

        if not self.correo_paciente:
            messagebox.showerror("Error", "Debe seleccionar un paciente primero.")
            return

        # Configuración del correo
        from_email = "karenbarraza152@gmail.com"  # Reemplazar con tu correo
        to_email = self.correo_paciente
        contraseña = "szsl anno sxwp dhyq"  # Reemplazar con tu contraseña de correo

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain', 'utf-8'))

        # Adjuntar archivos
        for archivo in self.archivos_adjuntos:
            try:
                with open(archivo, 'rb') as f:
                    adjunto = MIMEBase('application', 'octet-stream')
                    adjunto.set_payload(f.read())
                    encoders.encode_base64(adjunto)
                    adjunto.add_header('Content-Disposition', f'attachment; filename="{archivo.split("/")[-1]}"')
                    msg.attach(adjunto)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo adjuntar el archivo {archivo}. Error: {e}")

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(from_email, contraseña)
                server.sendmail(from_email, to_email, msg.as_string())
            messagebox.showinfo("Éxito", "Correo enviado con éxito.")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Error de autenticación. Verifica tu correo y contraseña.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo enviar el correo. Error: {e}")


# Inicializar la app
if __name__== "__main__":
 root = tk.Tk()
 app = DiagnosticoDifusoApp(root)
 root.mainloop()

   


# szsl anno sxwp dhyq