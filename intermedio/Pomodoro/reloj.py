import time

def tiempo(minutos : int =0):
    total_segundos = minutos * 60 
    for dif in range(total_segundos, -1, -1):
        yield dif
        if dif >0:
            time.sleep(1)