# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores. Para este proyecto de detección de objetos, se seleccionó **YOLOv26 Nano (aquí referenciado como `yolo26n`)**, dado que su arquitectura ligera permite iteraciones rápidas, proporcionando al mismo tiempo una precisión competitiva para establecer nuestro umbral mínimo aceptable de detección.

## Variables de entrada

*   Imágenes redimensionadas a 640x640 píxeles.
*   Archivos de anotaciones (archivos `.txt` en formato YOLO) conteniendo las coordenadas (x_center, y_center, width, height) de las cajas delimitadoras.

## Variable objetivo

Las variables objetivo (Target) a predecir son:
1.  **Clase del objeto:** Identificación a la que pertenece cada detección dentro de las 24 clases existentes en nuestro dataset (como A1, A2, A3, etc.).
2.  **Caja delimitadora (Bounding Box):** Precisión espacial de la ubicación de los objetos detectados calculada mediante la pérdida (Box Loss y DFL Loss).

## Evaluación del modelo

### Métricas de evaluación

Para evaluar el rendimiento en detección de objetos se utilizan las siguientes métricas:
*   **Precision (P):** Porcentaje de acierto de las detecciones positivas.
*   **Recall (R):** Capacidad del modelo de encontrar todos los objetos reales en la imagen.
*   **mAP50 (Mean Average Precision al 50% de IoU):** Promedio de precisión considerando correctas las detecciones que se superponen al menos en un 50% con el ground truth.
*   **mAP50-95:** La métrica más estricta (y prioritaria para este proyecto), que evalúa de forma promediada el desempeño en umbrales altos (de 50% a 95% de superposición).

### Resultados de evaluación

A continuación se muestran los resultados generados por el modelo Baseline (`yolo26n.pt`) tras un entrenamiento de 70 épocas utilizando validación cruzada sobre nuestro subset de validación:

| Métrica | Valor Obtenido (Validación) |
| :--- | :--- |
| **Precision (P)** | 92.2% |
| **Recall (R)** | 87.2% |
| **mAP50** | 95.5% |
| **mAP50-95** | 80.4% |

## Análisis de los resultados

**Fortalezas:**
El modelo baseline ha logrado un rendimiento destacable y sumamente competitivo considerando lo rápido y ligero que resulta al entrenar. Un **mAP50-95 superior al 80%** indica una excelente predicción espacial inicial de los objetos, comprobando que los datos de entrada (Data procesada) están limpios y funcionales.

**Debilidades:**
De acuerdo al análisis de las métricas y la matriz de confusión analizada en experimentación, un `Recall` del 87.2% si bien es alto, resalta una propensión relativamente mayor a los Falsos Negativos. Al ser una red neuronal *nano*, a la arquitectura le cuesta extraer las texturas y contornos de ciertas clases o fondos muy complejos, terminando en la clasificación de objetos a la clase de fondo (Background) generada por la falta de profundidad técnica del modelo.

## Conclusiones

*   **Línea Base Exitosa:** Se establece una línea base sólida y exitosa sobre el conjunto de datos de detección.
*   **Viabilidad Confirmada:** El problema está bien formulado, las etiquetas (coordenadas de Bounding Boxes) se empalman perfectamente con los inputs, y el aprendizaje ocurre de forma estable.
*   **Estrategia de Mejora (Next Steps):** Como la métrica insignia de nuestro problema es empujar al máximo el *mAP50-95*, es justificable escalar y evaluar una arquitectura de rango superior (como `yolo26m` - medium) tratando de corregir los falsos negativos o la confusión con el fondo (Background) producida por la sencillez de los filtros del actual modelo *nano*.

## Referencias

*   Ultralytics YOLO Documentation: [https://docs.ultralytics.com/](https://docs.ultralytics.com/) 
*   Scripts de entrenamiento locales: Entrenamientos logueados en `scripts/training/runs/train/26n/`
