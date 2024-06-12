'''
Cree un menu para una empresa que permita guardar autos
un auto tiene una patente, un modelo y una marca
El menu debe tener las siguientes opciones :
1.- agregar auto
2.- imprimir todos los autos
3.- buscar auto por patente
4.- eliminar auto
5.- Modificar modelo por patente
6.- Guardar lista
7.- Cargar los datos desde un archivo
0.- salir
'''
import csv
lista=[]
while True:
    
    print ("        menu")
    print ("")
    print ("1-. Agregar auto")
    print ("2-. Imrimir todos los autos")
    print ("3-. Buscar auto por patente")
    print ("4-. Eliminar auto")
    print ("5-. Modificar auto")
    print ("6-. Generar Archivo Csv")
    print ("7-. Cargar datos desde csv")
    print ("0-. Salir")

    op=int(input("ingrese una opcion : "))

    if op==1:
        print("")
        print(".-.- A G R E G A N D O   V E H Í C U L O .-.-.-")
        print("")
        patente = input("Ingerse patente : ")
        modelo=input("ingrese modelo : ")
        marca=input("ingrese marca : ")
        #diccionario={"patente":patente,"modelo":modelo,"marca":marca}
        nueva_lista=[patente,marca,modelo]
        #lista.append(diccionario)
        lista.append(nueva_lista)
        print("")
        print("Vehículo agregado correctamente...")
        print("")

    elif op==2:
        print("")
        print(".-.- V E H Í C U L O S .-.-.-")
        print("")
        for autitos in lista:
            print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 
            print("-----")
    elif op==3:
        encontrado = False
        print("")
        patente=input("Ingrese patente a buscar: ")
        for autitos in lista:
            if patente==autitos[0]:
                print("DATOS VEHÍCULO BUSCADO : \n")
                print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 
                print("-----")
                encontrado = True
                break
            
        if encontrado==False:
            print("El vehículo no existe...")
        
    elif op==4:
        encontrado = False
        print("")
        patente=input("Ingrese patente a eliminar: ")
        for autitos in lista:
            if patente==autitos[0]:
                print("DATOS VEHÍCULO BUSCADO : \n")
                print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 
                lista.remove(autitos)
                print("Auto eliminado")
                print("-----")
                encontrado = True
                break
            
        if encontrado==False:
            print("El vehículo no existe...")
        

    elif op==5:
        encontrado = False
        print("")
        patente=input("Ingrese patente a actualizar: ")
        for autitos in lista:
            if patente==autitos["patente"]:
                print("DATOS VEHÍCULO BUSCADO : \n")
                print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 
                nuevo_modelo=input("Ingrese el nuevo modelo : ")
                autitos[2]=nuevo_modelo
                print("Auto ACTUALIZADO")
                print("-----")
                encontrado = True
                break
            
        if encontrado==False:
            print("El vehículo no existe...")
    elif op==6: 
        print('')
        print('.-.-.-.-G E N E R A N D O  A R C H I V O S  D E  D A T O S.-.-.-.-')
        print ('')
        #with open ('nombre','tipo (w/r)', newline='')
        with open ('bbdd_autos.csv','w',newline='') as bbdd_autos:
            escribir_csv= csv.writer(bbdd_autos)
            escribir_csv.writerow(['patente','marca','modelo'])
            escribir_csv.writerows(lista)
            print('Archivo generado correctamente')

    elif op==7:
        with open ('bbdd_autos.csv','r',newline='') as datos_autos:
            leer_csv=csv.reader(datos_autos)
            for fila in leer_csv:
                print (fila)
    elif op==0:
        print("")

    else:
        print("")

        

            

        

            
           
