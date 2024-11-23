import sqlite3

DB_NAME = "pacientes.db"

def inicializar_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Tabla de pacientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            telefono TEXT NOT NULL,
            cuil TEXT UNIQUE NOT NULL
        )
    """)
    # Tabla de historial
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cuil TEXT NOT NULL,
            temperatura REAL,
            frecuencia_cardiaca INTEGER,
            presion_arterial INTEGER,
            nivel_oxigeno INTEGER,
            diagnostico TEXT,  -- Cambié de REAL a TEXT
            fecha TEXT,
            FOREIGN KEY (cuil) REFERENCES pacientes (cuil)
        )
    """)
    conn.commit()
    conn.close()

def agregar_paciente(nombre, edad, telefono, cuil):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO pacientes (nombre, edad, telefono, cuil) 
            VALUES (?, ?, ?, ?)
        """, (nombre, edad, telefono, cuil))
        conn.commit()
    except sqlite3.IntegrityError:
        print("El CUIL ya está registrado.")
    finally:
        conn.close()

def obtener_paciente(cuil):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE cuil = ?", (cuil,))
    paciente = cursor.fetchone()
    conn.close()
    return paciente

def guardar_diagnostico(cuil, datos, resultado):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO historial (cuil, temperatura, frecuencia_cardiaca, presion_arterial, nivel_oxigeno, diagnostico, fecha) 
        VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
    """, (cuil, datos["temperatura"], datos["frecuencia_cardiaca"], datos["presion_arterial"], datos["nivel_oxigeno"], resultado))
    conn.commit()
    conn.close()

def obtener_historial(cuil):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historial WHERE cuil = ?", (cuil,))
    historial = cursor.fetchall()
    conn.close()
    return historial
