def informacion(archivo):
    with open(archivo, 'r') as file:
        next(file)

        for linea in file:
            datos = linea.strip().split(';')
            nombre = datos[0]
            apellidos = datos[1]
            direccion = datos[2]
            correo = datos[3]
            print(f"Nombre: {nombre}")
            print(f"Apellidos: {apellidos}")
            print(f"Dirección: {direccion}")
            print(f"Correo: {correo}")
            print()
            
nombreArchivo = 'C:/Users/andre/Desktop/DeberesUTPL/Maestría/ejercicio-001-andresGPY22/informacion.txt'
informacion(nombreArchivo)

