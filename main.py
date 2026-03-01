from ping3 import ping


def get_ping_ms():
    result = ping("8.8.8.8")
    latency_ms = result * 1000
    return round(latency_ms, 2)


print("Your ping is", get_ping_ms(), "ms")
