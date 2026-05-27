"""
🗄️ SISTEMA DE BASE DE DATOS SQLITE3
Maneja todas las tablas y operaciones de BD
"""

import sqlite3
import os
from datetime import datetime

DATABASE = "bot_database.db"

def conectar():
    """Conectar a la base de datos"""
    return sqlite3.connect(DATABASE)

def crear_base_datos():
    """Crear todas las tablas necesarias"""
    conn = conectar()
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            user_id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            fecha_creacion INTEGER,
            fecha_ingreso INTEGER,
            cedula_id TEXT UNIQUE,
            foto_url TEXT
        )
    """)
    
    # Tabla de economía
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS economia (
            user_id INTEGER PRIMARY KEY,
            saldo REAL DEFAULT 0,
            banco REAL DEFAULT 0,
            ultima_work INTEGER,
            ultima_daily INTEGER,
            ultima_payday INTEGER,
            trabajos_hechos INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES usuarios(user_id)
        )
    """)
    
    # Tabla de salarios por rol
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS salarios_roles (
            guild_id INTEGER,
            role_id INTEGER,
            cantidad REAL,
            PRIMARY KEY(guild_id, role_id)
        )
    """)
    
    # Tabla de cédulas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cedulas (
            cedula_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            guild_id INTEGER NOT NULL,
            nombre TEXT,
            fecha_creacion TEXT,
            roles TEXT,
            FOREIGN KEY(user_id) REFERENCES usuarios(user_id)
        )
    """)
    
    # Tabla de configuración
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            guild_id INTEGER PRIMARY KEY,
            canal_logs INTEGER,
            canal_bienvenida INTEGER,
            mensaje_bienvenida TEXT,
            color_embed TEXT,
            moneda TEXT DEFAULT '💵',
            cooldown_payday INTEGER DEFAULT 43200,
            cooldown_work INTEGER DEFAULT 3600,
            cooldown_daily INTEGER DEFAULT 86400
        )
    """)
    
    # Tabla de logs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guild_id INTEGER,
            tipo TEXT,
            user_id INTEGER,
            descripcion TEXT,
            fecha TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def configurar_servidor(guild_id):
    """Crear configuración por defecto para un servidor"""
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT guild_id FROM config WHERE guild_id = ?", (guild_id,))
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO config (guild_id, moneda, color_embed)
            VALUES (?, '💵', '3498db')
        """, (guild_id,))
        conn.commit()
    
    conn.close()

# ==================== USUARIOS ====================

def crear_usuario(user_id, nombre, fecha_ingreso):
    """Crear un nuevo usuario"""
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO usuarios (user_id, nombre, fecha_creacion, fecha_ingreso)
            VALUES (?, ?, ?, ?)
        """, (user_id, nombre, int(datetime.now().timestamp()), fecha_ingreso))
        
        # Crear registro de economía
        cursor.execute("""
            INSERT INTO economia (user_id, saldo) VALUES (?, 0)
        """, (user_id,))
        
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def obtener_usuario(user_id):
    """Obtener datos de usuario"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE user_id = ?", (user_id,))
    datos = cursor.fetchone()
    conn.close()
    return datos

# ==================== ECONOMÍA ====================

def obtener_saldo(user_id):
    """Obtener saldo de usuario"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo, banco FROM economia WHERE user_id = ?", (user_id,))
    datos = cursor.fetchone()
    conn.close()
    return datos if datos else (0, 0)

def agregar_dinero(user_id, cantidad):
    """Agregar dinero al saldo"""
    conn = conectar()
    cursor = conn.cursor()
    saldo, banco = obtener_saldo(user_id)
    cursor.execute(
        "UPDATE economia SET saldo = ? WHERE user_id = ?",
        (saldo + cantidad, user_id)
    )
    conn.commit()
    conn.close()

def restar_dinero(user_id, cantidad):
    """Restar dinero del saldo"""
    conn = conectar()
    cursor = conn.cursor()
    saldo, banco = obtener_saldo(user_id)
    if saldo >= cantidad:
        cursor.execute(
            "UPDATE economia SET saldo = ? WHERE user_id = ?",
            (saldo - cantidad, user_id)
        )
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

def depositar(user_id, cantidad):
    """Depositar dinero al banco"""
    conn = conectar()
    cursor = conn.cursor()
    saldo, banco = obtener_saldo(user_id)
    if saldo >= cantidad:
        cursor.execute(
            "UPDATE economia SET saldo = ?, banco = ? WHERE user_id = ?",
            (saldo - cantidad, banco + cantidad, user_id)
        )
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

def retirar(user_id, cantidad):
    """Retirar dinero del banco"""
    conn = conectar()
    cursor = conn.cursor()
    saldo, banco = obtener_saldo(user_id)
    if banco >= cantidad:
        cursor.execute(
            "UPDATE economia SET saldo = ?, banco = ? WHERE user_id = ?",
            (saldo + cantidad, banco - cantidad, user_id)
        )
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

def transferir(user_id_desde, user_id_hacia, cantidad):
    """Transferir dinero entre usuarios"""
    if restar_dinero(user_id_desde, cantidad):
        agregar_dinero(user_id_hacia, cantidad)
        return True
    return False

def actualizar_cooldown(user_id, tipo):
    """Actualizar cooldown (work, daily, payday)"""
    conn = conectar()
    cursor = conn.cursor()
    tiempo_actual = int(datetime.now().timestamp())
    
    if tipo == "work":
        cursor.execute("UPDATE economia SET ultima_work = ? WHERE user_id = ?", (tiempo_actual, user_id))
    elif tipo == "daily":
        cursor.execute("UPDATE economia SET ultima_daily = ? WHERE user_id = ?", (tiempo_actual, user_id))
    elif tipo == "payday":
        cursor.execute("UPDATE economia SET ultima_payday = ? WHERE user_id = ?", (tiempo_actual, user_id))
    
    conn.commit()
    conn.close()

def obtener_cooldown(user_id, tipo):
    """Obtener último cooldown"""
    conn = conectar()
    cursor = conn.cursor()
    
    if tipo == "work":
        cursor.execute("SELECT ultima_work FROM economia WHERE user_id = ?", (user_id,))
    elif tipo == "daily":
        cursor.execute("SELECT ultima_daily FROM economia WHERE user_id = ?", (user_id,))
    elif tipo == "payday":
        cursor.execute("SELECT ultima_payday FROM economia WHERE user_id = ?", (user_id,))
    
    datos = cursor.fetchone()
    conn.close()
    return datos[0] if datos and datos[0] else 0

def obtener_top(guild_id, limite=10):
    """Obtener top de usuarios por saldo"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.user_id, (e.saldo + e.banco) as total
        FROM economia e
        ORDER BY total DESC
        LIMIT ?
    """, (limite,))
    datos = cursor.fetchall()
    conn.close()
    return datos

# ==================== SALARIOS ====================

def establecer_sueldo(guild_id, role_id, cantidad):
    """Establecer sueldo para un rol"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO salarios_roles (guild_id, role_id, cantidad)
        VALUES (?, ?, ?)
    """, (guild_id, role_id, cantidad))
    conn.commit()
    conn.close()

def obtener_sueldo_rol(guild_id, role_id):
    """Obtener sueldo de un rol"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cantidad FROM salarios_roles WHERE guild_id = ? AND role_id = ?
    """, (guild_id, role_id))
    datos = cursor.fetchone()
    conn.close()
    return datos[0] if datos else 0

def obtener_sueldo_mas_alto(guild_id, role_ids):
    """Obtener el sueldo más alto de los roles del usuario"""
    sueldo_maximo = 0
    for role_id in role_ids:
        sueldo = obtener_sueldo_rol(guild_id, role_id)
        if sueldo > sueldo_maximo:
            sueldo_maximo = sueldo
    return sueldo_maximo

# ==================== CÉDULAS ====================

def crear_cedula(user_id, guild_id, nombre, cedula_id, roles):
    """Crear una cédula de usuario"""
    conn = conectar()
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    roles_str = ",".join(str(r) for r in roles)
    
    cursor.execute("""
        INSERT OR REPLACE INTO cedulas (cedula_id, user_id, guild_id, nombre, fecha_creacion, roles)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (cedula_id, user_id, guild_id, nombre, fecha, roles_str))
    
    cursor.execute("UPDATE usuarios SET cedula_id = ? WHERE user_id = ?", (cedula_id, user_id))
    conn.commit()
    conn.close()

def obtener_cedula(user_id):
    """Obtener cédula de un usuario"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cedulas WHERE user_id = ?", (user_id,))
    datos = cursor.fetchone()
    conn.close()
    return datos

def eliminar_cedula(user_id):
    """Eliminar cédula de un usuario"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cedulas WHERE user_id = ?", (user_id,))
    cursor.execute("UPDATE usuarios SET cedula_id = NULL WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

# ==================== CONFIGURACIÓN ====================

def obtener_config(guild_id):
    """Obtener configuración del servidor"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM config WHERE guild_id = ?", (guild_id,))
    datos = cursor.fetchone()
    conn.close()
    return datos

def actualizar_config(guild_id, **kwargs):
    """Actualizar configuración del servidor"""
    conn = conectar()
    cursor = conn.cursor()
    
    campos = ", ".join([f"{k} = ?" for k in kwargs.keys()])
    valores = list(kwargs.values()) + [guild_id]
    
    cursor.execute(f"UPDATE config SET {campos} WHERE guild_id = ?", valores)
    conn.commit()
    conn.close()

# ==================== LOGS ====================

def registrar_log(guild_id, tipo, user_id, descripcion):
    """Registrar un evento en los logs"""
    conn = conectar()
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    cursor.execute("""
        INSERT INTO logs (guild_id, tipo, user_id, descripcion, fecha)
        VALUES (?, ?, ?, ?, ?)
    """, (guild_id, tipo, user_id, descripcion, fecha))
    
    conn.commit()
    conn.close()

def obtener_logs(guild_id, limite=10):
    """Obtener logs de un servidor"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM logs WHERE guild_id = ?
        ORDER BY id DESC
        LIMIT ?
    """, (guild_id, limite))
    datos = cursor.fetchall()
    conn.close()
    return datos
