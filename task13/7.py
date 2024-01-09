from ipaddress import ip_network

net = ip_network('131.25.181.85/255.255.248.0', False)
k = 0
for ad in net:
    x = f'{int(ad):x}'
    # x = hex(int(ad))[2:]
    if '5' in x:
        k += 1
print(k)