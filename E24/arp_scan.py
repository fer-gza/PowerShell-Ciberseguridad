from scapy.all import (Ether, ARP, srp)

# 1) Definir rango de red
network = "192.168.100.70/24"
pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)

# 2) Enviar y recibir ARP
print(f"Escaneando ARP en {network}…")
respuestas, _ = srp(pkt, timeout=3, verbose=0)

# 3) Mostrar y guardar resultados
hosts = []
for _, r in respuestas:
    hosts.append((r.psrc, r.hwsrc))
    print("Host:", r.psrc, "MAC:", r.hwsrc)

with open("arp_hosts.txt", "w") as f:
    for ip, mac in hosts:
        f.write(f"{ip},{mac}\n")
print("→ Guardado en arp_hosts.txt")
