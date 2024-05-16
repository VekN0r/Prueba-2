#Importo el sys para cerrar por completo el programa
import sys
#Este while es para que el usuario vea si quiere más liquidaciones
while True:    
    try:
        usuario = str(input("Ingrese el nombre del trabajador: "))
        usuarioCanNum = len(usuario)
        if usuarioCanNum > 0 and usuarioCanNum <= 30:
            pass
        else:
            print("Cantidad de caracteres fuera de rango")
    except ValueError:
        print("Error al ingresar el nombre")
    #Me avanza con mi codigo si el try esta correcto    
    else:
        while True:
            try:
                sueldoB = int(input("Ingrese sueldo base"))
            except ValueError:
                print("Ingrese dato númerico")
            else:    
                if sueldoB > 0:
                    break
                else:
                    print("Ingrese valor número positivo")
        #Hago un ciclo hasta que el usuario ingrese bien las horas trabajas            
        while True:        
            try: 
                horasTrabajadas = float(input("Ingrese horas trabajadas"))
            except ValueError:  
                print("Error al ingresar hora")  
            else:
                if horasTrabajadas <= 180:
                    print(horasTrabajadas)
                    break
                elif horasTrabajadas > 180:
                    sueldoBasTra = (sueldoB / 180) * 1.5
                    horasExtraRe = (horasTrabajadas - 180) * sueldoBasTra
                    horasExtraRedon = int(round(horasExtraRe,0))
                    break
        #Calculo todos los valores de las variables        
        ingresoT = sueldoB + horasExtraRedon
        fonasaD = ingresoT * 0.07
        fonasaDr = round(fonasaD,0)
        afpD =  ingresoT * 0.10
        afpDr = round(afpD,0)
        deSeguSo = fonasaD + afpD
        seguroSo = int(round(deSeguSo,0))
        valorConDes = ingresoT - fonasaD - afpD
        valorConDesR = round(valorConDes,0)
        def desgloce():
            print("\t\t-----Liquidación total-----")
            print(f"Nombre:\t\t\t {usuario}\t\t\tHoras Extras a pagar: {horasExtraRedon}")
            print(f"Total ingresos bruto:   {ingresoT}\t\t  Descuento Seguridad Social: {seguroSo}")
            print(f"Sueldo a pagar:\t\t{valorConDesR}")
        desgloce()
        #Creo los textos
        with open(f"Liquidacion_{usuario}.txt", "w", encoding="utf-8") as archivo:
            archivo.write("\t\t-----Liquidación total-----\n")
            archivo.write(f"Nombre:               {usuario}\n")
            archivo.write(f"Sueldo base:          {sueldoB}\n")              
            archivo.write(f"Horas extras:         {horasExtraRedon}\n") 
            archivo.write(f"Total ingresos bruto: {ingresoT}\n")
            archivo.write(f"Descuento fonasa:     {fonasaDr}\n")             
            archivo.write(f"Descuento afp:        {afpDr}\n")
            archivo.write(f"Sueldo a pagar:       {valorConDesR}\n")
    
    #Creo una funcion para ver si el usuario desea otra liquidación
    def preguntar_repetir():
        while True:
            try:
                reiLi = str(input("Desea hacer otra liquidación S/N: "))
                reiLi = reiLi.upper()
                if reiLi == "S" or reiLi == "N":
                    return reiLi
                else:
                    print("Error al ingresar respuesta")
            except ValueError:
                print("Ingrese respuesta válida")

    while True:
        reiLi = preguntar_repetir()
        if reiLi == "N":
            print("Nos vemos.")
            sys.exit()
        elif reiLi == "S":
            break
        else:
            print("Ingrese respuesta correcta")


   