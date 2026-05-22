
# Reporte de Datos: Detección y Clasificación de Cromosomas

Este documento contiene los resultados del análisis exploratorio de datos de nuestro dataset de imágenes y anotaciones de cariotipos humanos.

## Resumen general de los datos

El conjunto de datos se divide en dos estructuras principales interconectadas (imágenes y cromosomas):

* **Número total de observaciones:** Contamos con **5,000** registros de imágenes y **229,852** registros de cromosomas individuales detectados dentro de esas imágenes.
* **Variables:** * *Set de Imágenes (4 variables):* `id_image`, `file_name` (categóricas/texto), `width`, `height` (numéricas enteras).
* *Set de Cromosomas (10 variables):* `id_chromosome`, `id_image`, `etiqueta` (categóricas/texto), y `xmin`, `ymin`, `xmax`, `ymax`, `bbox_width`, `bbox_height`, `bbox_area` (numéricas enteras).


* **Valores faltantes:** No se detectó la presencia de valores nulos o faltantes (0%) en ninguna de las variables de ambos conjuntos.
* **Distribución general:** Las imágenes presentan una alta variabilidad en sus dimensiones (anchos entre 360 y 1360 píxeles). La distribución de cromosomas por imagen se concentra fuertemente alrededor de la media biológica esperada (46 cromosomas).

## Resumen de calidad de los datos

El dataset destaca por su excelente nivel de limpieza y organización desde la fuente:

* **Valores faltantes y duplicados:** 0 registros nulos y 0 registros duplicados (0%).
* **Valores extremos y errores:** No se encontraron coordenadas inválidas (0 bounding boxes inválidos). El conteo de cromosomas por imagen oscila entre 43 y 50, lo cual es un rango biológico y técnico aceptable (posibles cromosomas superpuestos u omitidos).
* **Acciones tomadas:** * No fue necesario realizar imputación de datos.
* Se realizó **Ingeniería de Características (Feature Engineering)** calculando variables derivadas fundamentales: `bbox_width`, `bbox_height`, `bbox_area` y el `area_ratio` (proporción que ocupa el cromosoma respecto a la imagen total).
* Se derivó el sexo biológico del paciente basándose en la presencia de cromosomas X e Y.



## Variable objetivo

Nuestra variable objetivo primaria para la tarea de clasificación es **`etiqueta`** (la clase del cromosoma).

* **Distribución:** Es una variable categórica multiclasa compuesta por **24 clases únicas** (autosomas A1 a G22, y sexuales X, Y).
* **Comportamiento:** El dataset está **perfectamente balanceado** para los cromosomas autosómicos, con cada clase agrupando aproximadamente 10,000 instancias. Las clases sexuales muestran la distribución biológica natural de la cohorte (X con 7,334 instancias y Y con 2,564 instancias), provenientes de 2,549 hombres y 2,445 mujeres.
* **Gráficos:** El histograma de "Distribución de clases de cromosomas" confirma visualmente este balance perfecto en los autosomas y la proporción escalonada de los cromosomas sexuales.

## Variables individuales

Análisis detallado de las características predictoras (Bounding Boxes y dimensiones):

* **Dimensiones de la imagen (`width`, `height`):** Tienen medias de 749 y 708 píxeles respectivamente.
* *Transformación sugerida:* Será estrictamente necesario aplicar un *resizing* (redimensionamiento) estandarizado o *padding* para alimentar estas imágenes a una red neuronal convolucional (CNN).


* **Dimensiones del cromosoma (`bbox_width`, `bbox_height`, `bbox_area`):** El área media es de ~5,237 px², con una dispersión amplia (min: 440 px², max: 43,884 px²).
* **Número de cromosomas por imagen (`chromosome_count`):** Media de 45.97 y mediana de 46.

