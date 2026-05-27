"""
⚙️ CONFIGURACIONES GLOBALES DEL BOT
Valores por defecto y constantes
"""

# ==================== COLORES ====================

COLORES = {
    "azul": 0x3498db,
    "verde": 0x2ecc71,
    "rojo": 0xe74c3c,
    "naranja": 0xe67e22,
    "morado": 0x9b59b6,
    "rosa": 0xff1493,
}

# ==================== EMOJIS ====================

EMOJIS = {
    "dinero": "💵",
    "cedula": "🪪",
    "config": "⚙️",
    "admin": "👨‍💼",
    "ayuda": "📚",
    "exito": "✅",
    "error": "❌",
    "advertencia": "⚠️",
    "info": "ℹ️",
    "trabajo": "💼",
    "banco": "🏦",
    "superior": "🏆",
}

# ==================== COOLDOWNS (en segundos) ====================

COOLDOWNS = {
    "work": 3600,       # 1 hora
    "daily": 86400,     # 24 horas
    "payday": 43200,    # 12 horas
}

# ==================== SUELDOS ALEATORIOS ====================

SUELDO_TRABAJO = {
    "minimo": 100,
    "maximo": 500,
}

SUELDO_DAILY = {
    "minimo": 500,
    "maximo": 1500,
}

# ==================== MENSAJES ====================

MENSAJE_BIENVENIDA = """
👋 ¡Bienvenido a **{servidor}**!

Nos alegra que te hayas unido a nuestra comunidad. Aquí encontrarás:

💰 **Economía** - Gana dinero trabajando
🪪 **Cédulas** - Tu documento de identidad
⚙️ **Configuración** - Personaliza tu experiencia
📊 **Rankings** - Compite con otros usuarios

Usa `/help` para ver todos los comandos.
¡Que disfrutes! ❤️
"""

# ==================== MENSAJES DE ERROR ====================

ERRORES = {
    "sin_permisos": "❌ No tienes permisos para usar este comando",
    "sin_dinero": "❌ No tienes suficiente dinero",
    "usuario_no_existe": "❌ El usuario no existe",
    "ya_existe": "❌ Ya existe un registro con esos datos",
    "cooldown": "⏳ Debes esperar {tiempo} antes de usar este comando",
    "sin_rol": "❌ No tienes un rol con sueldo",
    "valor_invalido": "❌ El valor ingresado no es válido",
}

# ==================== MENSAJES DE ÉXITO ====================

EXITOS = {
    "dinero_recibido": "✅ Recibiste {moneda} {cantidad}",
    "dinero_transferido": "✅ Transferiste {moneda} {cantidad}",
    "cedula_creada": "✅ Cédula creada exitosamente",
    "config_actualizada": "✅ Configuración actualizada",
    "sueldo_cobrado": "✅ Payday recibido: {moneda} {cantidad}",
}

# ==================== FOOTERS ====================

FOOTER_BOT = "🇩🇴 Dominican Bot"
FOOTER_ICON = "https://cdn.discordapp.com/emojis/1081664993644347522.png"

# ==================== OTROS ====================

PREFIJO = "!"
MONEDA_DEFAULT = "💵"
COLOR_DEFAULT = 0x3498db
VERSION = "1.0.0"

# ==================== CONFIGURACIÓN DE BASE DE DATOS ====================

DATABASE_FILE = "bot_database.db"

TABLAS = [
    "usuarios",
    "economia",
    "salarios_roles",
    "cedulas",
    "config",
    "logs",
]

# ==================== VALORES POR DEFECTO ====================

CONFIG_DEFAULT = {
    "canal_logs": None,
    "canal_bienvenida": None,
    "mensaje_bienvenida": MENSAJE_BIENVENIDA,
    "color_embed": "3498db",
    "moneda": "💵",
    "cooldown_payday": 43200,
    "cooldown_work": 3600,
    "cooldown_daily": 86400,
}

# ==================== LÍMITES ====================

LIMITES = {
    "nombre_usuario_max": 32,
    "descripcion_max": 2000,
    "cantidad_max_transferencia": float('inf'),
    "cantidad_min_transferencia": 1,
}

# ==================== PERMISOS ====================

PERMISOS_REQUERIDOS = {
    "bot": [
        "send_messages",
        "embed_links",
        "manage_messages",
        "read_messages",
    ],
    "admin": [
        "administrator",
    ],
}

# ==================== EVENTOS REGISTRADOS ====================

TIPOS_LOG = [
    "miembro_entra",
    "miembro_sale",
    "work",
    "daily",
    "payday",
    "transferencia",
    "deposito",
    "retiro",
    "cedula_creada",
    "cedula_editada",
    "cedula_eliminada",
    "config_actualizada",
    "sueldo_establecido",
]
