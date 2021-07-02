listaTiempoSalida=[]
listaTiempoLlegada=[]

def registro(listaTiempoSalida,listaTiempoLlegada):
    print("registrar tiempo de salida hora:min::seg")
    horas=float(input("ingrese hora : "))
    minutos= float(input("ingrese min: "))
    segundos=float(input("ingrese seg: "))
    tuplaTiempoSalida=(horas,minutos,segundos)
    listaTiempoSalida.append(tuplaTiempoSalida)


    print("registrar tiempo de llegada hora:min::seg")
    hora2 =    float(input("ingrese la hora: "))
    minutos2 =  float(input("ingrese la minutos: "))
    segundos2 = float(input("ingrese la segundos: "))
    tuplaTiempoLlegada = (hora2, minutos2, segundos2)
    listaTiempoLlegada.append(tuplaTiempoLlegada)

def tiempoTotal(listaTiempoSalida,listaTiempoLlegada):
    minutosSalida=listaTiempoSalida[0][0]*60+listaTiempoSalida[0][1]+listaTiempoSalida[0][2]/60
    minutosLlegada=listaTiempoLlegada[0][0]*60+listaTiempoLlegada[0][1]+listaTiempoLlegada[0][2]/60

    total=round(minutosLlegada-minutosSalida,2)
    return print("tiempo total en minutos que tomo en llegar: " +str(total))

registro(listaTiempoSalida,listaTiempoLlegada)
tiempoTotal(listaTiempoSalida,listaTiempoLlegada)
print(listaTiempoSalida)

# tupla=(2,4,5)
# lista=[]
# lista.append(tupla)
# print(lista[0][0]+lista[0][1])

