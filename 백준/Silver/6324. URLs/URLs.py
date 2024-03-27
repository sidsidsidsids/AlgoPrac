N = int(input())
for n in range(N):
    addr = input()
    for i in range(2, len(addr)):
        if addr[i-2:i+1] == "://":
            protocol = addr[:i-2]
            url = addr[i+1:]
            break
    port = "<default>"
    path = "<default>"
    host = "<default>"
    flag = False
    for i in range(len(url)):
        if url[i] == ":":
            k = 1
            while i + k < len(url) and url[i+k] != "/":
                k += 1
            port = url[i+1:i+k]
            host = url[:i]
        elif url[i] == "/":
            path = url[i+1:]
            if host == "<default>":
                host = url[:i]
            break
    if host == "<default>":
        host = url

    print(f"URL #{n+1}")
    print("Protocol =",protocol)
    print("Host     =",host)
    print("Port     =",port)
    print("Path     =",path)
    print()