# Definición de los datos

## Origen de los datos

Los datos provienen del artículo *"An Open Dataset of Annotated Metaphase Cell Images for Chromosome Identification"*. El conjunto de datos original fue compilado a partir de 1,598 fetos de mujeres embarazadas sometidas a estudios cromosómicos prenatales entre 2014 y 2021 en el Laboratorio de Citogenética del Hospital General de Veteranos de Taichung. Las anotaciones fueron realizadas por personal médico capacitado. Posteriormente, los datos fueron procesados mediante Roboflow, donde las imágenes se redimensionaron a 640x640 píxeles y se dividieron en conjuntos de entrenamiento, validación y prueba.

## Especificación de los scripts para la carga de datos

- Se utiliza el script `scripts/data_acquisition/main.py` para cargar e inspeccionar localmente los datos, validando la configuración en el archivo `data.yaml` y contabilizando el número de imágenes disponibles en cada subconjunto (train, valid, test). 

## Referencias a rutas o bases de datos origen y destino

El proyecto actualmente maneja los datos de forma local en el sistema de archivos, sin una base de datos relacional externa.

### Rutas de origen de datos

- **Ubicación de los archivos:** `data/raw/chromosoma-1/`
- **Estructura de los archivos:**
  - El directorio contiene un archivo `data.yaml` con la definición de las 24 clases de cromosomas.
  - Existen tres carpetas principales: `train/`, `valid/` y `test/`.
  - Dentro de cada una de estas, hay carpetas de `images/` (contienen las imágenes de células en metafase) y `labels/` (contienen archivos `.txt` con las coordenadas de las cajas delimitadoras para cada imagen).
- **Procedimientos de transformación y limpieza (origen):** Inicialmente, el dataset ya viene redimensionado (640x640) y pre-dividido por la herramienta Roboflow. El preprocesamiento adicional (como normalización de imágenes) se realizará en las fases posteriores de entrenamiento.

### Base de datos de destino

- **Especificación:** No aplica. Los datos se mantienen estructurados en carpetas dentro del repositorio local/entorno de entrenamiento.
- **Estructura:** Sistema de archivos estándar.
- **Procedimientos de carga:** Los datos son leídos directamente por los DataLoaders de la red neuronal durante el entrenamiento a partir de la ruta local `data/raw/chromosoma-1/`.
