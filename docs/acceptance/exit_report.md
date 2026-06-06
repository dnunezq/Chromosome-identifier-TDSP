# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados definitivos del proyecto de machine learning para la identificación de cromosomas. Se implementó exitosamente un modelo de detección de objetos basado en la arquitectura YOLOv26. Aunque el modelo alcanzó métricas muy favorables (mAP50-95 del ~86%), durante la experimentación en producción se evidenció que en ciertos casos tiende a confundir algunos cromosomas con el fondo (background). No obstante, la aplicación web desarrollada puede ser una herramienta que puede dar soporte al proceso manual.

## Resultados del proyecto

- **Entregables:** Se entregó un modelo entrenado (`yolo26m`), cuadernos de experimentación documentados, una API para inferencia y una aplicación web funcional con interfaz gráfica.
- **Evaluación del modelo:** El modelo final (YOLOv26 Medium) superó ampliamente al modelo base en las métricas de prueba, alcanzando un mAP50-95 de 85.98%.
- **Comportamiento en Producción:** A pesar de los buenos resultados globales, se detectó una limitación importante: el modelo tiende a no detectar ciertos cromosomas por imagen, clasificándolos como *background* (lo cual fue previamente anticipado en la matriz de confusión). 

## Lecciones aprendidas

- **Manejo de Datos y Modelamiento:** La calidad de las anotaciones y el tamaño de las imágenes (redimensionadas a 640x640) fueron clave para el rendimiento. Las arquitecturas más complejas (*Medium*) mostraron mejor robustez frente al ruido comparado con versiones *Nano*.
- **Desafíos:** La principal dificultad ha sido la separación entre cromosomas con texturas complejas y el fondo, lo cual sigue siendo el mayor generador de falsos negativos.
- **Recomendaciones:** Para futuras iteraciones, se recomienda aplicar técnicas de aumento de datos más agresivas o métodos específicos para objetos pequeños/densos, así como refinar los umbrales de confianza (*confidence thresholds*) dinámicamente.

## Impacto del proyecto

- **Impacto en el Negocio:** La herramienta automatiza en gran medida la labor de identificación. Aunque no reemplaza por completo el análisis experto debido a los falsos negativos observados, su uso reduce significativamente el tiempo operativo al funcionar como una excelente herramienta de **apoyo e insumo**.
- **Aplicación Pública:** La solución ya se encuentra desplegada y disponible para su uso público en el siguiente enlace: [Chromosome Identifier TDSP](https://chromosome-identifier-tdsp-production.up.railway.app/).
- **Oportunidades de mejora:** Investigar en ensambles de modelos o arquitecturas específicas para segmentación de instancias que reduzcan la confusión con el fondo.

## Conclusiones

- El proyecto concluyó exitosamente su ciclo de vida, desde el procesamiento de datos hasta el despliegue en producción.
- A pesar de las limitaciones de detección descritas, la herramienta web demuestra un funcionamiento robusto y aporta un gran valor como soporte analítico para los especialistas.

## Agradecimientos

- Agradecimientos al equipo de trabajo, expertos en el dominio y a los colaboradores que aportaron los datos y el feedback esencial para afinar el modelo.
