from ping3 import ping

def ms():
    resultado = ping('8.8.8.8')
    vlr = resultado * 1000

    return round(vlr, 2)


print("seu ping é", ms(),"ms")