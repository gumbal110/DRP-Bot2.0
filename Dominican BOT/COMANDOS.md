"""
📚 REFERENCIA COMPLETA DE COMANDOS
Todos los comandos disponibles en el bot
"""

# ============================================================================
# 💰 COMANDOS DE ECONOMÍA
# ============================================================================

/balance
  Descripción: Ver tu saldo de dinero (mano + banco)
  Uso: /balance
  Alternativa: /balance @usuario (ver saldo de otro)
  Requiere: Nada

/work
  Descripción: Trabajar y ganar dinero aleatorio
  Uso: /work
  Recompensa: 100-500 moneda
  Cooldown: 1 hora (configurable)
  Requiere: Nada

/daily
  Descripción: Recompensa diaria
  Uso: /daily
  Recompensa: 500-1500 moneda
  Cooldown: 24 horas (configurable)
  Requiere: Nada

/payday
  Descripción: Cobrar sueldo según tu rol principal
  Uso: /payday
  Recompensa: Depende del rol
  Cooldown: 12 horas (configurable)
  Requiere: Tener al menos 1 rol con sueldo
  Nota: Cobra el sueldo más alto si tienes varios roles

/depositar <cantidad>
  Descripción: Depositar dinero en el banco
  Uso: /depositar 1000
  Requiere: Tener la cantidad en mano
  Nota: El dinero en banco es seguro

/retirar <cantidad>
  Descripción: Retirar dinero del banco
  Uso: /retirar 500
  Requiere: Tener la cantidad en banco
  Nota: Retira a dinero en mano

/transferir @usuario <cantidad>
  Descripción: Transferir dinero a otro usuario
  Uso: /transferir @Juan 1000
  Requiere: Tener la cantidad en mano
  Nota: No se puede transferir a sí mismo

/top
  Descripción: Ver ranking de usuarios más ricos
  Uso: /top
  Muestra: Top 10 usuarios
  Nota: Suma dinero en mano + banco

# ============================================================================
# 🪪 COMANDOS DE IDENTIDAD / CÉDULA
# ============================================================================

/cedula
  Descripción: Ver tu cédula de identidad
  Uso: /cedula
  Muestra:
    - Tu nombre
    - ID de Discord
    - Número único de cédula
    - Fecha de creación de cuenta
    - Fecha de ingreso al servidor
    - Tus roles
    - Tu avatar
  Nota: Se crea automáticamente si no existe

/ver_cedula @usuario
  Descripción: Ver cédula de otro usuario
  Uso: /ver_cedula @Juan
  Requiere: El usuario debe estar en el servidor

/crear_cedula @usuario
  Descripción: [ADMIN] Crear cédula para un usuario
  Uso: /crear_cedula @Juan
  Requiere: Ser administrador
  Nota: Genera automáticamente un ID único

/editar_cedula @usuario
  Descripción: [ADMIN] Actualizar cédula de usuario
  Uso: /editar_cedula @Juan
  Requiere: Ser administrador
  Nota: Regenera el ID de cédula

/eliminar_cedula @usuario
  Descripción: [ADMIN] Eliminar cédula de usuario
  Uso: /eliminar_cedula @Juan
  Requiere: Ser administrador

# ============================================================================
# ⚙️ COMANDOS DE ADMINISTRACIÓN
# ============================================================================

/set_sueldo @rol <cantidad>
  Descripción: Establecer sueldo para un rol
  Uso: /set_sueldo @VIP 2000
  Requiere: Ser administrador
  Nota: Se cobra con /payday
  Ejemplos:
    /set_sueldo @Miembro 500
    /set_sueldo @VIP 2000
    /set_sueldo @Moderador 3000
    /set_sueldo @Administrador 5000

/config <opcion> <valor>
  Descripción: [ADMIN] Configurar servidor
  Requiere: Ser administrador
  Opciones:
  
  logs #canal
    Configura canal para registrar eventos
    Ej: /config logs #📋-logs
  
  bienvenida #canal
    Configura canal para mensaje de bienvenida
    Ej: /config bienvenida #👋-bienvenida
  
  moneda <emoji/símbolo>
    Cambia el símbolo de moneda
    Ej: /config moneda RD$
    Ej: /config moneda 💰
    Ej: /config moneda 🪙
    Default: 💵
  
  payday <tiempo>
    Configura cooldown de payday
    Ej: /config payday 12h
    Ej: /config payday 1d
    Formato: 1h, 24h, 1d, 30m, etc
    Default: 12 horas
  
  work <tiempo>
    Configura cooldown de work
    Ej: /config work 1h
    Ej: /config work 30m
    Formato: 1h, 30m, etc
    Default: 1 hora
  
  daily <tiempo>
    Configura cooldown de daily
    Ej: /config daily 24h
    Ej: /config daily 1d
    Formato: 24h, 1d, etc
    Default: 24 horas

/mostrar_config
  Descripción: [ADMIN] Ver configuración actual del servidor
  Uso: /mostrar_config
  Requiere: Ser administrador
  Muestra:
    - Canal de logs
    - Canal de bienvenida
    - Moneda actual
    - Cooldowns configurados

# ============================================================================
# 📚 COMANDO DE AYUDA
# ============================================================================

/help
  Descripción: Ver lista de todos los comandos
  Uso: /help
  Muestra: Todos los comandos disponibles
  Nota: Actualiza cuando cargues nuevos comandos

# ============================================================================
# 🎯 EVENTOS AUTOMÁTICOS
# ============================================================================

BIENVENIDA POR DM
  Cuando un usuario entra al servidor:
  - Recibe un DM automático de bienvenida
  - Incluye lista de comandos principales
  - Información de soporte
  Nota: Si no se puede enviar DM, se ignora el error

ENTRADA AL SERVIDOR
  Se registra automáticamente en logs:
  - Nombre del usuario
  - ID de Discord
  - Hora de entrada
  - Información de entrada

SALIDA DEL SERVIDOR
  Se registra automáticamente en logs:
  - Nombre del usuario
  - ID de Discord
  - Hora de salida

# ============================================================================
# 📊 LOGS AUTOMÁTICOS
# ============================================================================

El bot registra automáticamente:
- Entrada de miembros
- Salida de miembros
- Comandos /work usados
- Comandos /daily usados
- Comandos /payday usados
- Transferencias de dinero
- Depósitos y retiros
- Creación/edición/eliminación de cédulas
- Cambios de configuración
- Sueldos establecidos

Ubicación: Bot base de datos SQLite (bot_database.db)
Ver: Los administradores pueden ver logs en el canal configurado

# ============================================================================
# 💡 TIPS Y TRUCOS
# ============================================================================

1. AHORRAR DINERO
   - Usa /depositar para guardar dinero en banco
   - El banco es seguro de transferencias accidentales
   - Retira con /retirar cuando lo necesites

2. MAXIMIZAR INGRESOS
   - Haz /work cada hora para ganar dinero
   - Obtén /daily para bonificación diaria
   - Logra /payday en tu rol principal
   - Combina las tres para máximo dinero

3. ROLES Y SUELDOS
   - Si tienes múltiples roles, cobras el más alto
   - Pide a admins que agreguen sueldos a tus roles
   - Sube en la jerarquía para más sueldo

4. CÉDULA PERSONAL
   - Tu cédula se crea automáticamente
   - Es un documento único de identidad
   - Contiene tu información importante
   - Muéstrala a otros con /cedula

5. TRANSFERENCIAS
   - Transfiere dinero a otros usuarios
   - Útil para prestar o compartir
   - Se registra en logs
   - No se puede revertir (¡sé cuidadoso!)

# ============================================================================
# ⌚ COOLDOWNS POR DEFECTO
# ============================================================================

/work     → 1 hora
/daily    → 24 horas
/payday   → 12 horas

(Los administradores pueden cambiar estos valores)

# ============================================================================
# 👥 PERMISOS REQUERIDOS
# ============================================================================

COMANDOS PÚBLICOS (Todos):
- /balance, /work, /daily, /payday
- /depositar, /retirar, /transferir, /top
- /cedula, /ver_cedula
- /help

COMANDOS ADMIN REQUERIDO:
- /set_sueldo (Admin)
- /config (Admin)
- /mostrar_config (Admin)
- /crear_cedula, /editar_cedula, /eliminar_cedula (Admin)

# ============================================================================
# 🔑 CARACTERES ESPECIALES PERMITIDOS
# ============================================================================

MONEDAS (en /config moneda):
💵 💴 💶 💷 💸 💰
🪙 🏦 💳 RD$ USD 
€ £ ¥ ₽ ₩

EMOJIS ÚTILES:
👑 VIP
🏆 Premium
⭐ Gold
💎 Diamond
🥇 Primera
🥈 Segunda
🥉 Tercera

# ============================================================================
# 📝 FORMATOS ACEPTADOS
# ============================================================================

CANTIDADES:
- Números enteros: 1000
- Decimales: 1000.50
- Montos grandes: 100000

TIEMPO (para cooldowns):
- Segundos: 60s
- Minutos: 30m
- Horas: 1h, 12h, 24h
- Días: 1d, 7d

CANALES (en config):
- #nombre-canal
- Solo escribe el nombre o menciona

# ============================================================================
# ✅ CHECKLIST DE CONFIGURACIÓN
# ============================================================================

□ Crear bot en Discord Developer Portal
□ Copiar token
□ Habilitar Intents (Message Content, Members, Presence)
□ Generar link de invitación
□ Agregar bot al servidor
□ Instalar dependencias: pip install -r requirements.txt
□ Configurar DISCORD_TOKEN en variables de entorno
□ Ejecutar: python main.py
□ Ejecutar como admin: /config logs #canal
□ Ejecutar como admin: /config bienvenida #canal
□ Ejecutar como admin: /config moneda 💵
□ Ejecutar como admin: /set_sueldo @rol 500
□ Probar: /balance, /work, /cedula, /help
□ ¡Listo! Tu bot está configurado

═══════════════════════════════════════════════════════════════════════════

¡Disfruta tu bot! 🤖 🇩🇴
