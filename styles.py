# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *

# class StyledContainer:
#     def __init__(self, root):
#         self.frame = ttk.Frame(
#             root, 
#             bootstyle="secondary",  # Fondo personalizado
#             padding=(25, 35),
#         )
#         self.frame.pack(fill="both", expand=True, pady=20, padx=10)
        
#         # Configuración del fondo y borde
#         self.frame.configure(
#             style="CustomContainer.TFrame",
#         )
        
#         # Encabezado
#         self.heading = ttk.Label(
#             self.frame, 
#             text="Sistema Difuso de Diagnóstico Médico", 
#             font=("Arial", 16, "bold"),
#             foreground="#1089D3", 
#             anchor="center",
#         )
#         self.heading.pack(pady=10)
        
#         # Campo CUIL
#         self.cuil_input = ttk.Entry(
#             self.frame,
#             bootstyle="default",
#             font=("Arial", 12),
#             placeholder="Ingrese su CUIL",  # Agregar placeholder
#         )
#         self.cuil_input.pack(fill="x", pady=10)
        
#         # Botón de inicio de sesión
#         self.login_button = ttk.Button(
#             self.frame, 
#             text="Iniciar Sesión", 
#             bootstyle="success",
#             command=self.handle_login,
#         )
#         self.login_button.pack(fill="x", pady=(20, 10))
        
#         # Botón de registro
#         self.register_button = ttk.Button(
#             self.frame,
#             text="Registrarse",
#             bootstyle="primary",
#             command=self.handle_register,
#         )
#         self.register_button.pack(fill="x", pady=(0, 20))
    
#     def handle_login(self):
#         print("Lógica para iniciar sesión")

#     def handle_register(self):
#         print("Lógica para registrarse")
#     def custom_styles():
#      style = ttk.Style()
#     # Fondo principal
#      style.configure(
#         "CustomContainer.TFrame",
#         background="#F8F9FD",
#         borderwidth=5,
#         relief="solid",
#         bordercolor="#FFFFFF",
#     )
#     # Botón de inicio de sesión
#      style.configure(
#         "TButton",
#         font=("Arial", 12, "bold"),
#     )
#      return style


import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StyledContainer:
    def __init__(self, root):
        self.frame = ttk.Frame(
            root, 
            bootstyle="secondary",  # Fondo personalizado
            padding=(25, 35),
        )
        self.frame.pack(fill="both", expand=True, pady=20, padx=10)
        
        # Configuración del fondo y borde
        self.frame.configure(
            style="CustomContainer.TFrame",
        )
        
        # Encabezado
        self.heading = ttk.Label(
            self.frame, 
            text="Sistema Difuso de Diagnóstico Médico", 
            font=("Arial", 16, "bold"),
            foreground="#1089D3", 
            anchor="center",
        )
        self.heading.pack(pady=10)
        
        # Campo CUIL
        self.cuil_input = ttk.Entry(
            self.frame,
            bootstyle="default",
            font=("Arial", 12),
        )
        self.cuil_input.pack(fill="x", pady=10)
        
        # Botón de inicio de sesión
        self.login_button = ttk.Button(
            self.frame, 
            text="Iniciar Sesión", 
            bootstyle="success",
        )
        self.login_button.pack(fill="x", pady=(20, 10))
        
        # Botón de registro
        self.register_button = ttk.Button(
            self.frame,
            text="Registrarse",
            bootstyle="primary",
        )
        self.register_button.pack(fill="x", pady=(0, 20))

def custom_styles():
    style = ttk.Style()
    # Fondo principal
    style.configure(
        "CustomContainer.TFrame",
        background="#F8F9FD",
        borderwidth=5,
        relief="solid",
        bordercolor="#FFFFFF",
    )
    # Botón de inicio de sesión
    style.configure(
        "TButton",
        font=("Arial", 12, "bold"),
    )
    return style
