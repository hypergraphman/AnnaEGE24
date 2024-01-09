from ipaddress import ip_network

net = ip_network('10.7.46.6/255.255.240.0', False)
k = 0
for ad in net:
    x = f'{int(ad):0>32b}'[16:]
    if sum(map(int, x)) > 4:
        k += 1
print(k)