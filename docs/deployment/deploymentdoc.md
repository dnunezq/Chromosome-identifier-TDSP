# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** YOLOv8 (Ultralytics) para identificación de cromosomas (`best.pt` de `yolo_vertex_exp-7`).
- **Plataforma de despliegue:** Contenedor Docker (Aplicación web con Flask).
- **Requisitos técnicos:** 
  - Python 3.10-slim-bullseye.
  - Librerías del sistema: `libgl1`, `libglib2.0-0` (necesarias para OpenCV).
  - Bibliotecas de Python (requirements.txt): `flask`, `werkzeug`, `Pillow`, `ultralytics`, `torch`, `pandas`.
  - Puerto de red: 5000.
- **Requisitos de seguridad:** 
  - No hay autenticación implementada por el momento en la app Flask.
  - Se utiliza `secure_filename` y UUIDs únicos en los nombres de archivo para evitar inyecciones de rutas y sobreescrituras en las cargas de imágenes.
  - Filtro de extensiones permitidas para los archivos subidos (`.png`, `.jpg`, `.jpeg`, `.txt`).
- **Diagrama de arquitectura:** Arquitectura Cliente-Servidor donde el usuario envía imágenes vía interfaz web (HTTP POST) y la aplicación Flask en el contenedor Docker ejecuta la inferencia localmente con Ultralytics YOLOv8, devolviendo las coordenadas (bounding boxes) y visualizándolas en el navegador.

## Código de despliegue

- **Archivo principal:** `src/webapp/app.py`
- **Rutas de acceso a los archivos:**
  - Código fuente: `/app/src/webapp` (en el contenedor).
  - Directorio de carga de imágenes temporales: `static/uploads/` (relativo a `app.py`).
  - Ruta de origen del modelo para Docker: `scripts/training/runs/train/26m/yolo_vertex_exp-7/weights/best.pt`.
- **Variables de entorno:**
  - `MODEL_PATH`: Define dónde se encuentra el modelo entrenado (`/app/model/best.pt` en Docker).
  - `PYTHONPATH`: Incluye el directorio `/app/src`.

## Documentación del despliegue

- **Instrucciones de instalación:**
  1. Clonar el repositorio con la rama `feature/deploy`.
  2. Asegurar que el archivo de pesos del modelo `best.pt` esté presente en la ruta requerida de la carpeta `scripts/`.
  3. Teniendo Docker instalado, construir la imagen desde la raíz del proyecto:
     `docker build -t tdsp-chromosome-deploy .`
- **Instrucciones de configuración:**
  - El Dockerfile ya contiene las instrucciones para copiar los archivos y definir las variables de entorno `MODEL_PATH` y `PYTHONPATH`. 
  - El puerto por defecto a exponer es el 5000.
- **Instrucciones de uso:**
  1. Iniciar el contenedor exponiendo el puerto:
     `docker run -p 5000:5000 tdsp-chromosome-deploy`
  2. Acceder a la interfaz web navegando a `http://localhost:5000/`.
  3. Cargar la imagen desde la interfaz para obtener las predicciones de los cromosomas (o hacer POST al endpoint `/predict` y `/parse_annotation`).
- **Instrucciones de mantenimiento:**
  - **Actualización del modelo:** Reemplazar el archivo `best.pt` por la nueva versión entrenada y reconstruir la imagen Docker.
  - **Limpieza:** Como los archivos se guardan en `static/uploads/` internamente en el contenedor, se borrarán cada vez que se destruya el contenedor. Para persistirlos a futuro, se recomendaría montar un volumen externo.
