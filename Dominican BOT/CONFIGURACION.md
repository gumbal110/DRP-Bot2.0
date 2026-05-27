"""
📋 EJEMPLO DE CONFIGURACIÓN
Aquí se muestran todas las opciones de configuración disponibles
"""

# ==================== PASOS DE CONFIGURACIÓN ====================

# 1. CREAR EL BOT EN DISCORD
# - Ve a https://discord.com/developers/applications
# - Click en "New Application"
# - Nombre: "Dominican Bot"
# - Ve a "Bot" y click "Add Bot"
# - Copia el token bajo el nombre del bot

# 2. CONFIGURAR INTENTS
# En la sección "Bot":
# - Message Content Intent: ON (Azul)
# - Server Members Intent: ON (Azul)
# - Presence Intent: ON (Azul)

# 3. CONFIGURAR OAUTH2
# - Ve a "OAuth2" > "URL Generator"
# - Scopes: "bot"
# - Permissions:
#   ✓ Send Messages
#   ✓ Embed Links
#   ✓ Read Messages/View Channels
#   ✓ Manage Messages

# 4. AGREGAR A TU SERVIDOR
# - Copia la URL generada
# - Abre en navegador
# - Selecciona tu servidor
# - Autoriza

# 5. CONFIGURAR EN REPLIT (o localmente)
# - Crea las variables de entorno
# - DISCORD_TOKEN = tu_token_aqui

# ==================== COMANDOS DE CONFIGURACIÓN ====================

# Una vez el bot esté en el servidor, como ADMINISTRADOR ejecuta:

# Configurar canal de logs
/config logs #📋-logs

# Configurar canal de bienvenida
/config bienvenida #👋-bienvenida

# Cambiar moneda (default: 💵)
/config moneda RD$
/config moneda 💰
/config moneda 🪙

# Configurar cooldowns
/config payday 12h    # Payday cada 12 horas
/config work 1h       # Work cada 1 hora
/config daily 24h     # Daily cada 24 horas

# ==================== CONFIGURAR SUELDOS ====================

# Para cada rol, establece su sueldo:
/set_sueldo @Miembro 500
/set_sueldo @VIP 2000
/set_sueldo @Moderador 3000
/set_sueldo @Administrador 5000

# Cuando alguien use /payday, cobrará el sueldo más alto de sus roles

# ==================== CANALES RECOMENDADOS ====================

# Crea estos canales en tu servidor:

# 📋-logs
# Categoría: Administración
# Privado: Solo admins
# Aquí se registran todas las acciones

# 👋-bienvenida
# Categoría: General
# Público
# Aquí llegan mensajes de bienvenida

# 💰-economia
# Categoría: General
# Público
# Para comandos de dinero

# 🪪-identidad
# Categoría: General
# Público
# Para ver cédulas

# ==================== ROLES SUGERIDOS ====================

# Crea estos roles (en orden):

# 1. @Bots
#    - Permiso: Manage Webhooks, Embed Links
#    - Color: Gris

# 2. @Administrador
#    - Permisos: Todos
#    - Color: Rojo

# 3. @Moderador
#    - Permisos: Moderate (Kick, Ban, Timeout)
#    - Color: Naranja

# 4. @VIP
#    - Permiso: -
#    - Color: Dorado

# 5. @Miembro
#    - Permiso: -
#    - Color: Azul

# ==================== PRIMEROS COMANDOS ====================

# Para probar:

# Ver tu balance
/balance

# Ver tu cédula
/cedula

# Trabajar
/work

# Recompensa diaria
/daily

# Ver ranking
/top

# Transferir dinero (requiere otro usuario)
/transferir @usuario 100

# ==================== VARIABLES DE ENTORNO REPLIT ====================

# En Replit, ve a Secrets (🔒) y configura:

# DISCORD_TOKEN = tu_token_de_discord_aqui

# ==================== OPCIONES AVANZADAS ====================

# Mensaje personalizado de bienvenida
/config bienvenida_msg "Bienvenido a [servidor]! Lee #reglas"

# Color principal de embeds (hex)
/config color "3498db"  # Azul
/config color "2ecc71"  # Verde
/config color "e74c3c"  # Rojo

# ==================== TROUBLESHOOTING ====================

# Si el bot no responde:
# 1. Verifica el token en variables de entorno
# 2. Comprueba que el bot tenga permisos en el servidor
# 3. Revisa que los Intents estén habilitados
# 4. Reinicia el bot

# Si los comandos no funcionan:
# 1. Usa /help para listar comandos
# 2. Verifica que tengas los permisos necesarios
# 3. Algunos comandos requieren ser admin

# Si la base de datos se corrompe:
# 1. Elimina bot_database.db
# 2. Reinicia el bot (se creará automáticamente)

# ==================== SOPORTE ====================

# Para más ayuda:
# - Lee README.md
# - Revisa los comentarios en el código
# - Pregunta en tu servidor Discord
