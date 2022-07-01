distancia = int(input("Digite a distância percorrida em m: "))
tempo = float(input("Digite o tempo em s: "))

vm = distancia / tempo

print("O tempo em m/s foi: ", vm)

distanciaKm = distancia /1000
tempoKm = tempo /3600

vm = distanciaKm / tempoKm

print("O tempo em Km/h foi: ", vm)