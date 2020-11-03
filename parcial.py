import csv
import sys

def CargarDatosModificar(archivo):
    try:
        with open (archivo, "a") as f:
            escritor = csv.writer(f)
            flag = "si"
            campos = ["Legajo", "Apellido", "Nombre", "Total Vacaiones"]
            while flag == "si":
                lista_empleado = []
                for x in range (4):
                    if x == 0 or x == 3:
                        try:
                            dato = int(input(f"Ingrese el {campos[x]} del empleado\n"))
                            lista_empleado.append(dato)
                        except ValueError:
                            print(f"Se debe ingresar un número entero para el campo {campos[x]}")
                    else:
                        dato = input(f"Ingrese el {campos[x]} del empleado\n")
                        lista_empleado.append(dato)
                escritor.writerow(lista_empleado)
                flag = input("Desea ingresar otro empleado? si/no\n")
    except IOError:
        print("Hubo un error al intentar abrir el archivo")

def CargarDatosNuevo(archivo):
    try:
        with open (archivo, "w") as f:
            escritor = csv.writer(f)
            flag = "si"
            campos = ["Legajo", "Apellido", "Nombre", "Total Vacaiones"]
            while flag == "si":
                lista_empleado = []
                for x in range (4):
                    if x == 0 or x == 3:
                        try:
                            dato = int(input(f"Ingrese el {campos[x]} del empleado\n"))
                            lista_empleado.append(dato)
                        except ValueError:
                            print(f"Se debe ingresar un número entero para el campo {campos[x]}")
                    else:
                        dato = input(f"Ingrese el {campos[x]} del empleado\n")
                        lista_empleado.append(dato)
                escritor.writerow(lista_empleado)
                flag = input("Desea ingresar otro empleado? si/no\n")
    except IOError:
        print("Hubo un error al intentar abrir el archivo")



def ConsultarDias(archivo, buscador):
    try:
        with open (archivo) as f_empleados, open("dias.csv") as f_dias:
            empleados_csv = csv.reader(f_empleados)
            dias_csv = csv.reader(f_dias)
            next(dias_csv, None)

            empleado = next(empleados_csv, None)
            dias = next(dias_csv, None)

            while empleado:
                legajo, apellido, nombre, vacaciones = empleado
                vacaciones = int(vacaciones)
                tomados = 0
                while dias and dias[0] == legajo:
                    tomados += 1
                    dias = next(dias_csv, None)
                print(f"{legajo} : {buscador}")
                if legajo == buscador:
                    restante = vacaciones - tomados
                    print(f"Legajo {legajo}: {nombre} {apellido}, le restan {restante} de vacaciones")
                    break
                empleado = next(empleados_csv, None)
    except IOError:
        print("Hubo un problema al intentar abrir el archivo")

print("Bienvenido al gestor de vacaciones de empleados")
lista_archivos = ["empleados.csv"] #lista donde se van a guardar los nombres de archivos.csv

#se crea el menú con los controles de que no se ingresen caracteres erroneos.
flag = "0"
while flag != "3":
    flag = input("Ingrese el número de opción que desea realizar.\n1- Cargar Datos de Legajo de los empleados\n2- Consultar los días restantes de vacaciones de un empleado\n3- Salir\n")
    if flag == "1":
        nombre_archivo = input("Ingrese el nombre del archivo csv donde desea cargar los datos\n")
        #se fija en en lista_archivos si ya existe ese archivo; si es así se pregunta si se lo quiere modificar o sobreescribir. Si no existe se usa la misma función que sobreescribir.
        if nombre_archivo in lista_archivos:
            opcion = "0"
            while opcion != "1" and opcion != "2":
                opcion = input("El archivo ya existe. Si desea modificarlo ingrese 1. Si desea sobreescribirlo ingrese 2.\n")
                if opcion == "1":
                    CargarDatosModificar(nombre_archivo)
                elif opcion == "2":
                    CargarDatosNuevo(nombre_archivo)
                else:
                    print("Opción incorrecta. Intente nuevamente")

        else:
            lista_archivos.append(nombre_archivo)
            CargarDatosNuevo(nombre_archivo)

    if flag == "2":
        legajo_buscado = input("Ingrese el número de legajo a buscar\n")
        id_archivo = input("Ingrese el nombre del archivo de empleados que desea utilizar\n")
        if id_archivo in lista_archivos:
            ConsultarDias(id_archivo, legajo_buscado)
        else:
            print("No existe un archivo con ese nombre")
    if flag == "3":
        print("Gracias por utilizar el sistema")
    if flag != "1" and flag != "2" and flag != "3":
        print("Ingresó un caracter no válido")
