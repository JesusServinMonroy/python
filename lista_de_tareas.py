import time
tareas = []

def agregar_tarea():
    tarea = input("Ingresa una tarea nueva: ")
    tareas.append(tarea)
    print("Tarea Agregada con exito")
    print("\n")
    time.sleep(5)

def eliminar_tarea():
    tarea = int(input("Ingresa la tarea que deseas eliminar"))-1
    if tarea < len(tareas):
        tareas.pop(tarea)
        print("Tarea elimincada con exito")
    else:
        print("La tarea no existe en la lista")
        print("\n")
        time.sleep(5)

def mostrar_tareas():
    if tareas:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas,1):
            print(f"{i}.- {tarea} ")
        time.sleep(5)
    else :
        print("No hay tareas en la lista")
        print("\n")
        time.sleep(5)

def main():
    opcion = 0
    while opcion != 4 :
        print("\033c", end="")
        print("\n ---Lista de Tareas---")
        print("1 Agregar tarea")
        print("2 Eliminar tarea")
        print("3 Mostrar tareas")
        print("4 Salir")
        
        opcion = int(input("Selecciona una opcion: "))
        print("\n")
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            eliminar_tarea()
        elif opcion == 3:
            mostrar_tareas()
        elif opcion == 4:
            print("Hasta luego!")
        else:
            print("opcion no valida")

if __name__ == "__main__":
    main()