import csv

def CargarDatos():
    print("Hola")

def ConsultarDias():
    print("Hola")

print("Bienvenido al gestor de vacaciones de empleados")
flag = "0"
while flag != "3":
    flag = input("Ingrese el número de opción que desea realizar.\n1- Cargar Datos de Legajo de los empleados\n2- Consultar los días restantes de vacaciones de un empleado\n3- Salir\n")
    if flag == "1":
        CargarDatos()
    if flag == "2":
        ConsultarDias()
    if flag == "3":
        print("Gracias por utilizar el sistema")
    if flag != "1" and flag != "2" and flag != "3":
        print("Ingresó un caracter no válido")
