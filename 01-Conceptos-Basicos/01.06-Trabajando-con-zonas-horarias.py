#################################################
# Trabajando con fechas - Zonas horarias        #
#################################################

# Importación de módulos
from datetime import datetime
import pytz

# Mostrar las diferentes zonas horarias
print(pytz.all_timezones)
print("")

# Mostrar información sobre la fecha actual, sin zona horaria
dt = datetime.now()
print(f"Fecha: {dt}")
print(f"Zona horaria: {dt.tzinfo}\n")

# Mostrar información sobre la fecha actual, con zona horaria
dtTokyo = datetime.now(pytz.timezone("Asia/Tokyo"))
print(f"Fecha de Tokyo: {dtTokyo}")
print(f"Zona horaria: {dtTokyo.tzinfo}\n")
