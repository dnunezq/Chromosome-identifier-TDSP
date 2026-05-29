# Reporte del Modelo Final

## Resumen Ejecutivo

En este documento se presentan los resultados definitivos tras el entrenamiento y evaluación del modelo de detección de objetos final. Se seleccionó la arquitectura **YOLOv26 Medium (`yolo26m`)**, la cual alcanzó unas métricas sobresalientes en el conjunto de prueba (Test Set). Destaca su métrica principal **mAP50-95 con un valor de 85.98% (~86%)**, superando ampliamente las expectativas de línea base sin mostrar indicios de sobreajuste (overfitting). Los resultados confirman la capacidad del modelo para realizar detecciones precisas y confiables en entornos de producción.

## Descripción del Problema

El proyecto aborda la tarea compleja de **Detección de Objetos**, donde el objetivo no es solo clasificar la presencia de un elemento, sino localizarlo espacialmente dentro de la imagen. 
*   **Contexto:** Se cuenta con imágenes en diversas condiciones y se requiere aislar e identificar correctamente instancias de 24 clases diferentes.
*   **Objetivos:** Construir un modelo automatizado que maximice tanto la correcta identificación (clase) como la precisión espacial de la caja (bounding box).
*   **Justificación:** Automatizar esta labor con altos estándares geométricos y semánticos (mAP50-95) permite acelerar el procesamiento de imágenes a escala, reduciendo el error humano, particularmente frente a los falsos negativos que se presentaban con arquitecturas más livianas.

## Descripción del Modelo

Para resolver el problema se optó por la arquitectura **YOLOv26 Medium (`yolo26m`)**. 
*   **Metodología:** Se utilizó aprendizaje por transferencia (Transfer Learning) partiendo de pesos preentrenados, entrenando la red profunda con las imágenes redimensionadas a 640x640 píxeles y sus respectivas anotaciones.
*   **Justificación de elección:** Anteriormente se experimentó con un modelo Baseline *Nano* (`yolo26n`), el cual arrojó un mAP50-95 de ~80.4% pero presentaba dificultades con los falsos negativos y texturas complejas (confusión con el *Background*). Posteriormente, se evaluó un entrenamiento adicional con la arquitectura *Small* (`yolo26s`) variando la resolución de las imágenes de entrada; si bien sus resultados mejoraron significativamente y fueron muy similares a los de arquitecturas más grandes, se determinó mantener la variante *Medium* (`yolo26m`) como el modelo definitivo para producción. La arquitectura *Medium* proporciona de forma inherente una mayor profundidad de red y capacidad paramétrica (sin depender de alteraciones extremas en la resolución de entrada), permitiendo extraer características robustas que corrigen sólidamente las debilidades del baseline a cambio de un aumento aceptable en el tiempo de inferencia.

## Evaluación del Modelo

Durante la fase documentada en `evaluation.ipynb`, el modelo final fue sometido tanto a validación mediante la API nativa de Ultralytics (`model.val()`) como a comparación visual contra los Ground Truths reales extraídos manualmente para asegurar máxima transparencia.

**Resultados en el Test Set Independent:**
*   **mAP50-95:** **85.98% (0.8598)**
*   **Comportamiento de Overfitting:** No ser percibe. Las métricas de prueba empataron sólidamente con las de validación durante el entrenamiento, confirmando la generalización robusta del modelo.
*   **Evaluación Visual:** Se creó una visualización paramétrica mapeando píxel a píxel las anotaciones reales `.txt` en rojo enfrentadas a la predicción del modelo. El alto porcentaje del mAP50-95 quedó confirmado al notar un solapamiento casi perfecto entre las predicciones algorítmicas y la realidad etiquetada.

## Conclusiones y Recomendaciones

**Conclusiones:**
*   **Puntos Fuertes:** El modelo `yolo26m` ofrece un excelente balance entre Precision y Recall total. Superar el 85% en la métrica más restrictiva de COCO (mAP50-95) para 24 clases verifica el éxito analítico del proyecto.
*   **Puntos Débiles / Limitaciones:** Como modelo *Medium*, el costo computacional de inferencia es ligeramente mayor al modelo inicial, requiriendo un mejor equipo si se pretende usar en entornos de muy altos frames por segundo (FPS) continuos con video en vivo.


## Referencias

*   Cuadernos de experimentación propios: `scripts/training/training_yolov2.ipynb` y `scripts/evaluation/evaluation.ipynb`.
*   Directorio de datos preprocesados definidos globalmente en `data/processed/data.yml`.
*   [Ultralytics YOLO Documentation](https://docs.ultralytics.com/)
