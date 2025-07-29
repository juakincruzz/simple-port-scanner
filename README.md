# 🔍 Simple Port Scanner

Escáner de puertos TCP en Python, con soporte para:
- Escaneo multihilo (rápido)
- Detección de puertos abiertos
- Banner grabbing (identificación de servicios)
- Exportación de resultados en JSON

---

## 🚀 ¿Cómo funciona?

El script realiza un escaneo de los primeros 1024 puertos de una IP o dominio, detecta cuáles están abiertos y si es posible, identifica el servicio mediante banner grabbing.

---

## ⚙️ Requisitos

- Python 3.x
- Sistema operativo: Windows, Linux o macOS
- Acceso a terminal

---

## 🧪 Ejecución

```bash
# Clona el repositorio
git clone https://github.com/juakincruzz/simple-port-scanner.git
cd simple-port-scanner

# Crea y activa entorno virtual (opcional)
python -m venv venv
.\venv\Scripts\activate    # En Windows
source venv/bin/activate  # En Linux/macOS

# Ejecuta el escáner
python scanner.py
