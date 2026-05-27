"""
✅ FUNCIONES DE VALIDACIÓN Y UTILIDADES
"""

import discord
from discord.ext import commands
from datetime import datetime, timedelta
from utils.database import obtener_cooldown
import random
import string

def generar_cedula_id():
    """Generar un ID único para cédula"""
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=12))

def format_fecha(timestamp):
    """Formatear timestamp a fecha legible"""
    if timestamp is None:
        return "N/A"
    
    fecha = datetime.fromtimestamp(timestamp)
    return fecha.strftime("%d/%m/%Y - %H:%M")

def verificar_cooldown(tiempo_anterior, cooldown_segundos):
    """Verificar si un cooldown ha terminado"""
    tiempo_actual = int(datetime.now().timestamp())
    tiempo_restante = (tiempo_anterior + cooldown_segundos) - tiempo_actual
    
    if tiempo_restante > 0:
        return False, tiempo_restante
    return True, 0

def formato_tiempo(segundos):
    """Convertir segundos a formato legible"""
    if segundos < 60:
        return f"{segundos}s"
    elif segundos < 3600:
        return f"{segundos // 60}m {segundos % 60}s"
    elif segundos < 86400:
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        return f"{horas}h {minutos}m"
    else:
        dias = segundos // 86400
        horas = (segundos % 86400) // 3600
        return f"{dias}d {horas}h"

def es_administrador(ctx):
    """Verificar si el usuario es administrador"""
    return ctx.author.guild_permissions.administrator

def requerido_admin():
    """Decorador para comandos que requieren admin"""
    async def predicate(ctx):
        if not ctx.author.guild_permissions.administrator:
            return False
        return True
    return commands.check(predicate)

def generar_sueldo_trabajo():
    """Generar cantidad aleatoria para work"""
    return random.randint(100, 500)

def generar_sueldo_daily():
    """Generar cantidad aleatoria para daily"""
    return random.randint(500, 1500)

def obtener_roles_principales(member):
    """Obtener roles principales de un usuario"""
    roles = [role.mention for role in member.roles[1:]]  # Excluir @everyone
    return roles[:5] if roles else ["Sin roles"]  # Máximo 5 roles

def convertir_a_segundos(tiempo_str):
    """Convertir strings como '12h', '24h', '1d' a segundos"""
    tiempo_str = tiempo_str.lower().strip()
    
    if tiempo_str.endswith('s'):
        return int(tiempo_str[:-1])
    elif tiempo_str.endswith('m'):
        return int(tiempo_str[:-1]) * 60
    elif tiempo_str.endswith('h'):
        return int(tiempo_str[:-1]) * 3600
    elif tiempo_str.endswith('d'):
        return int(tiempo_str[:-1]) * 86400
    
    return None

# Configuración global
MONEDA_DEFAULT = "💵"
COLOR_DEFAULT = "3498db"
COOLDOWN_DEFAULT = {
    "payday": 43200,    # 12 horas
    "work": 3600,       # 1 hora
    "daily": 86400      # 24 horas
}
