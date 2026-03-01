from ping3 import ping

def ms():
    result = ping('8.8.8.8')
    vlr = result * 1000

    return round(vlr, 2)


print("your ping is", ms(),"ms")
