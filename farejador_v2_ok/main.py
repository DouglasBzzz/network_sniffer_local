import subprocess
import ipaddress

def farejador():
    ativos = []

    subrede = ipaddress.ip_network("192.168.2.1/23", strict=False)
    for i in subrede.hosts():
        i = str(i)
        retval = subprocess.call(["ping", "-c1", "-n", "-i0.1", "-W1", i])
        if retval == 0:
            ativos.append(i)
        for ip in ativos:
            print(ip + " está ativo ")


if __name__ == "__main__":
    farejador()