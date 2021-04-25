import ipaddress

internet_v4 = ipaddress.ip_network("192.168.2.0/24")

for x in internet_v4.hosts():
    print(x)


"""

artigo bem util com um tutorial para utilziar esse módulo
https://docs.python.org/pt-br/3/howto/ipaddress.html#ipaddress-howto

"""