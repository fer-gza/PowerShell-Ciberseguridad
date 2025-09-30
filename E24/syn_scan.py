from scapy.all import IP, TCP, sr
import csv

# 1) Leer hosts descubiertos
with open("arp_hosts.txt") as f:
    hosts = [line.split(",")[0] for line in f]

puertos = [22, 80, 443]
resultados = []

# 2) Para cada host, enviar SYN y ver respuesta
for ip in hosts:
    abiertos = []
    for p in puertos:
        pkt = IP(dst=ip) / TCP(dport=p, flags="S")
        resp, _ = sr(pkt, timeout=1, verbose=0)
        if resp:
            abiertos.append(p)
    print(f"{ip} → puertos abiertos: {abiertos}")
    resultados.append((ip, abiertos))

# 3) Guardar matrix en CSV
with open("syn_scan.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP"] + [str(p) for p in puertos])
    for ip, abiertos in resultados:
        row = [ip] + [("Yes" if p in abiertos else "No") for p in puertos]
        writer.writerow(row)
print("→ Guardado en syn_scan.csv")
