import socket
from datetime import datetime
import threading
import json

print_lock = threading.Lock()
results = []

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode(errors='ignore').strip()
            except:
                banner = "No banner recibido"
            with print_lock:
                print(f"[+] Puerto {port} abierto - Banner: {banner}")
                results.append({
                    "puerto": port,
                    "banner": banner
                })
        sock.close()
    except:
        pass

def main():
    target = input("Introduce IP o dominio: ")
    start_time = datetime.now()

    threads = []

    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = datetime.now()
    print(f"Escaneo completado en: {end_time - start_time}")

    # Guardar resultados
    nombre_archivo = f"resultados_{target.replace('.', '_')}.json"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"\nResultados guardados en {nombre_archivo}")

if __name__ == "__main__":
    main()
