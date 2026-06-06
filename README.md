# Chromosome Identifier - TDSP

## Contexto del Proyecto

Este proyecto implementa un modelo de red neuronal para identificar y clasificar cromosomas en imágenes de células en metafase. La identificación de cromosomas es fundamental en la investigación genética y el diagnóstico clínico para la detección de trastornos genéticos y el cuidado prenatal. Los métodos manuales tradicionales son confiables pero laboriosos y consumen mucho tiempo.

Automatizar este proceso de detección y clasificación mediante redes neuronales busca mejorar significativamente la eficiencia del análisis cromosómico en entornos médicos, permitiendo diagnósticos más rápidos y precisos.

## Estructura del Proyecto (TDSP)

Esta estructura es una implementación de la metodología Team Data Science Process (TDSP) que proporciona las siguientes carpetas y archivos:

* `src`: Acá debe ir el código o implementación del proyecto en Python.
* `docs`: En esta carpeta se encuentran las plantillas de los documentos definidos en la metodología, adaptados para este proyecto.
* `scripts`: Esta carpeta debe contener los scripts/notebooks que se ejecutarán (ej. adquisición de datos, procesamiento).
* `pyproject.toml`: Archivo de definición del paquete/proyecto en Python.

## 🚀 Cómo Probar la Aplicación

La aplicación se encuentra desplegada y accesible públicamente. Puedes interactuar con el modelo directamente desde tu navegador:

🔗 **Enlace a la Web App:** [https://chromosome-identifier-tdsp-production.up.railway.app/](https://chromosome-identifier-tdsp-production.up.railway.app/)

### Datos de Prueba (Imágenes y Ground Truth)

Si deseas probar la aplicación y comparar las predicciones del modelo con las anotaciones reales (*Ground Truth*), puedes utilizar las imágenes del conjunto de pruebas que se encuentran en el repositorio.

1. **Selecciona una imagen de prueba** desde la carpeta de datos procesados, por ejemplo:
   - `data/processed/test/images/103094.jpg`
   - `data/processed/test/images/103112.jpg`
   - `data/processed/test/images/103121.jpg`

2. **Sube la imagen a la aplicación web**. El modelo procesará la imagen y te devolverá los cromosomas detectados con sus respectivas cajas limitadoras (bounding boxes).

3. **Compara con el Ground Truth**. Si deseas validar qué tan exacto fue el modelo, puedes revisar las anotaciones originales (cajas marcadas manualmente) ubicadas en la carpeta de etiquetas, las cuales tienen exactamente el mismo nombre:
   - `data/processed/test/labels/103094.txt`
   - `data/processed/test/labels/103112.txt`
   - `data/processed/test/labels/103121.txt`

> **Nota de uso:** Como se reporta en la documentación del modelo, es posible que la red tienda a confundir algunos cromosomas muy complejos con el fondo (*background*), por lo que podrías evidenciar algunos falsos negativos en ciertas imágenes. Esta aplicación está concebida como una herramienta de apoyo e insumo al proceso de identificación visual.
