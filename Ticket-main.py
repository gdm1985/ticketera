from bdacceso import *
from metodos import *

#ver posibilidad de armar clase con los datos, para enviar a la BD

#Establezco conexion con BD
conexion, cursor = conexionBD()

while True:
    menu()

    opcion = str.upper(input("Ingresa la opción que deseas: "))
    if opcion == 'Q':
        break

    elif opcion == '1':
        # Lista de datos que deseas insertar en la base de datos
        #como medida de seguridad puedo tomar los datos antes y verificar que en telefono sea numero, luego los envio
        datos_a_insertar = [input("nombre: "), input("apellido: "), (input("telefono: ")), input("edificio: "),
                            input("observaciones: "), "Abierto"]

        # Sentencia SQL para insertar datos en la tabla
        sql_insertar = "INSERT INTO usuarios (nombre, apellido, telefono, edificio, observaciones,estado) VALUES (%s, %s, %s, %s, %s, %s)"
        # Impacto de la query en la BD
        cursor.execute(sql_insertar, datos_a_insertar)
        # Confirmar los cambios en la base de datos
        conexion.commit()
        clear_console()

    elif opcion == '2':
        #Consultar reclamos abiertos existentes

        sql_consulta = "SELECT * FROM usuarios WHERE estado = 'abierto';"

        cursor.execute(sql_consulta)
        datos_a_leer = cursor.fetchall()
        for fila in datos_a_leer:
            fecha=fila[1].strftime("%d-%m-%Y %H:%M:%S")
            print("_"*100)
            print(f"ID: {fila[0]}\t{fecha}\t{fila[2]} {fila[3]}\t\tTeñ: {fila[4]}\tEdificio: {fila[5]}\n\n\t\tComentarios:{fila[6]}\n\n\t\tEstado:{fila[7]}")
            print(""*100)
        input("presione enter para continuar")
        clear_console()

    elif opcion == '3':
        #Consultar reclamos cerrados existentes

        sql_consulta = "SELECT * FROM usuarios WHERE estado = 'cerrado';"

        cursor.execute(sql_consulta)
        datos_a_leer = cursor.fetchall()
        for fila in datos_a_leer:
            fecha=fila[1].strftime("%d-%m-%Y %H:%M:%S")
            print("_"*100)
            print(f"ID: {fila[0]}\t{fecha}\t{fila[2]} {fila[3]}\t\tTeñ: {fila[4]}\tEdificio: {fila[5]}\n\n\t\tComentarios:{fila[6]}\n\n\t\tEstado:{fila[7]}")
            print(""*100)
        input("presione enter para continuar")
        clear_console()

    elif opcion == '4':
        id=[int(input("ingrese id a cerrar"))]
        sql_modif="UPDATE usuarios SET estado = 'Cerrado' WHERE id = %s; "
        cursor.execute(sql_modif,id)
        conexion.commit()
        clear_console()

# Cerrar el cursor y la conexión
cerrarBD(cursor,conexion)
