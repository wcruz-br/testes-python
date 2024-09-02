import time

print("Hora atual:", time.strftime("%H:%M:%S"))

dias_desde_epoca = int(time.time() / (60 * 60 * 24))
print("Dias desde a época:", dias_desde_epoca)

print("Época:", time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(0)))
