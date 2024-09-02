# Generador de Reportes Financieros

Este proyecto genera reportes financieros automatizados a partir de archivos Excel.

## Instalación

- Clona el repositorio.
- Navega al directorio del proyecto y activa el entorno virtual

```bash
venv\Scripts\activate #Windows
source venv/bin/activate # macOS/Linux
```

- Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

- Coloca los archivos Excel en el directorio `data/`.
- Ejecuta el script principal:

```bash
python src/main.py
```

Los reportes se generarán en el directorio `report/`.
