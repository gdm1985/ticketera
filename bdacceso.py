#Importar para poder manejar BD
import mysql.connector

#conexion a BD utilizando manejo de errores
def conexionBD():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="$oldier82",
            database="projectx"
        )
        print("Conectado a la base de datos projectx")
        # Crear un objeto cursor para ejecutar consultas SQL
        cursor = conexion.cursor()
        return conexion, cursor
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None


# Cerrar el cursor y la conexión
def cerrarBD(cursor,conexion):
    cursor.close()
    conexion.close()

#asi llamo a la BD para conectarme
#conexion,cursor = conexionBD()