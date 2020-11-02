import csv

def CargarDatosModificar(archivo):
    try:
        with open (archivo, "a") as f:
            escritor = csv.writer(f)
            flag = "si"
            campos = ["Legajo", "Apellido", "Nombre", "Total Vacaiones"]
            while flag == "si":
                lista_empleado = []
                for x in range (4):
                    dato = input(f"Ingrese el {campos[x]} del empleado")
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
                    dato = input(f"Ingrese el {campos[x]} del empleado")
                    lista_empleado.append(dato)
                escritor.writerow(lista_empleado)
                flag = input("Desea ingresar otro empleado? si/no\n")
    except IOError:
        print("Hubo un error al intentar abrir el archivo")



def ConsultarDias():
    print("Hola")

print("Bienvenido al gestor de vacaciones de empleados")
lista_archivos = []
flag = "0"
while flag != "3":
    flag = input("Ingrese el número de opción que desea realizar.\n1- Cargar Datos de Legajo de los empleados\n2- Consultar los días restantes de vacaciones de un empleado\n3- Salir\n")
    if flag == "1":
        nombre_archivo = input("Ingrese el nombre del archivo csv donde desea cargar los datos\n")
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
        ConsultarDias()
    if flag == "3":
        print("Gracias por utilizar el sistema")
    if flag != "1" and flag != "2" and flag != "3":
        print("Ingresó un caracter no válido")
