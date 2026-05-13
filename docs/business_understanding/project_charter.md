# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Chromosome Identifier

## Objetivo del Proyecto

La identificación de cromosomas es un pilar fundamental de la investigación genética y el diagnóstico clínico. La detección y clasificación precisa de los cromosomas es esencial para diagnosticar trastornos genéticos, guiar el cuidado prenatal y otros campos. Los métodos manuales tradicionales para el análisis cromosómico, aunque confiables, son muy laboriosos y consumen mucho tiempo, lo que los hace menos prácticos en entornos médicos de alta demanda.

El desarrollo de una red neuronal para la identificación de cromosomas ofrece una solución prometedora a estos desafíos. Al automatizar el proceso de detección y clasificación, las redes neuronales pueden mejorar significativamente la eficiencia del análisis cromosómico. Este avance tecnológico es particularmente importante en varias áreas clave:

1. **Diagnóstico de trastornos genéticos:** La identificación temprana y precisa de anomalías cromosómicas puede llevar a intervenciones oportunas para afecciones como el síndrome de Down, el síndrome de Edwards y el síndrome de Patau. Los sistemas automatizados pueden proporcionar diagnósticos rápidos y precisos, lo cual es esencial para mejorar los resultados en los pacientes.

2. **Cuidado y tamizaje prenatal:** En el cuidado prenatal, un análisis cromosómico eficiente es crucial para evaluar la salud fetal. Automatizar este proceso con redes neuronales puede reducir la carga de trabajo del personal médico y garantizar resultados más rápidos y precisos, los cuales son vitales para tomar decisiones médicas informadas durante el embarazo.

![Ejemplo Cromosomas](https://github.com/dnunezq/Chromosome-identifier/blob/main/NotebookImages/example_chromosoma.jpg?raw=true)


## Alcance del Proyecto

### Incluye:

- **Datos:** Conjunto de imágenes de células en metafase anotadas para la identificación de cromosomas, agrupadas en 24 categorías (Grupos A-G, más X e Y). Este conjunto de datos se basa en el artículo *"An Open Dataset of Annotated Metaphase Cell Images for Chromosome Identification"* y fue recopilado a partir de estudios cromosómicos prenatales realizados en el Laboratorio de Citogenética del Hospital General de Veteranos de Taichung (2014-2021).
- **Resultados:** Un modelo de red neuronal entrenado capaz de detectar y clasificar cromosomas con alta precisión en nuevas imágenes.
- **Criterios de éxito:** Precisión y recall (como mAP) consistentes con los estándares para automatizar la detección manual, idealmente acercándose a las métricas documentadas en la literatura de referencia (e.g. mAP cercano a 98% en clasificación).

### Excluye:

- Diagnóstico automatizado de enfermedades o condiciones genéticas específicas (el proyecto se limita únicamente a la identificación y clasificación de los cromosomas).
- Otros tipos de análisis de imágenes médicas fuera de células en metafase.

## Metodología

Team Data Science Process (TDSP) adaptada para un problema de Visión Computacional y Detección de Objetos.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y adquisición de datos | 1 semana | - |
| Preprocesamiento y análisis exploratorio | 1 semana | - |
| Modelamiento y entrenamiento de la red neuronal | 1 semana | - |
| Evaluación | 1 semana | - |
| Despliegue / Entrega | 1 semana | - |

## Equipo del Proyecto

- **Líder del Proyecto y Científico de Datos:** David Alexander Núñez Quintero

## Presupuesto

Infraestructura de cómputo y recursos locales para entrenamiento de modelos de Deep Learning.

## Stakeholders

- Investigadores genéticos y especialistas clínicos.
- **Expectativas:** Reducir la carga de trabajo del personal médico, obtener diagnósticos más rápidos y precisos, y mejorar la toma de decisiones clínicas.

## Aprobaciones

- N/A
