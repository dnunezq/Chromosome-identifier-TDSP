# Diccionario de datos

## Dataset: Cromosomas en metafase

Dataset de imagenes de cromosomas en metafase con anotaciones de objetos para 24 categorias cromosomicas.

### Contexto del dataset

- Fuente: *An Open Dataset of Annotated Metaphase Cell Images for Chromosome Identification*.
- Cobertura: 1,598 fetos de mujeres embarazadas en estudios prenatales (2014-2021).
- Institucion: Cytogenetic Laboratory, Department of Women Medicine, Taichung Veterans General Hospital.
- Tamano reportado: 5.000 anotaciones para 24 categorias de cromosomas.
- Estructura local en el proyecto:
	- `data/raw/JEPG/`: imagenes `.jpg`
	- `data/raw/annotations/`: anotaciones `.xml` (formato tipo Pascal VOC)

## Clasificacion cromosomica (24 categorias)

Los cromosomas humanos se agrupan tradicionalmente en A-G segun tamano y posicion del centromero.

| Grupo | Cromosomas | Tipo morfologico | Descripcion |
| --- | --- | --- | --- |
| A | 1-3 | Metacentricos grandes | Son los cromosomas de mayor tamano, con centromero central y brazos de longitud similar. |
| B | 4-5 | Submetacentricos grandes | Ligeramente mas pequenos que los del grupo A, con un brazo largo y un brazo corto por la posicion del centromero. |
| C | 6-12, X | Submetacentricos medianos | Presentan una disminucion clara de tamano respecto a A y B, y mantienen diferencias de longitud entre brazos; incluye al cromosoma X. |
| D | 13-15 | Acrocentricos medianos | El centromero se ubica cercano a un extremo, generando un brazo p muy corto y un brazo q mas largo. |
| E | 16-18 | 16 metacentrico; 17-18 submetacentricos cortos | Cromosomas de tamano corto: el 16 es metacentrico y los 17 y 18 son submetacentricos. |
| F | 19-20 | Metacentricos cortos | Cromosomas pequenos con centromero central y brazos de longitud relativamente similar. |
| G | 21-22, Y | Acrocentricos cortos | Corresponden a los cromosomas de menor tamano; 21 y 22 son acrocentricos, y el cromosoma Y tambien se incluye en este grupo. |

## Diccionario de campos

### A. Metadatos de imagen (carpeta `JEPG`)

| Campo | Descripcion | Tipo de dato | Rango/Valores | Fuente |
| --- | --- | --- | --- | --- |
| image_file | Nombre del archivo de imagen | String | `*.jpg` (ej. `103064.jpg`) | `data/raw/JEPG/` |
| image_path | Ruta local del archivo | String | Ruta en sistema de archivos | Construido por script |
| image_width | Ancho de la imagen en pixeles | Integer | Entero positivo | `<size><width>` en XML |
| image_height | Alto de la imagen en pixeles | Integer | Entero positivo | `<size><height>` en XML |
| image_depth | Canales de color | Integer | Usualmente 3 (RGB) | `<size><depth>` en XML |

### B. Metadatos de anotacion (carpeta `annotations`)

| Campo | Descripcion | Tipo de dato | Rango/Valores | Fuente |
| --- | --- | --- | --- | --- |
| annotation_file | Nombre del archivo de anotacion | String | `*.xml` (ej. `103064.xml`) | `data/raw/annotations/` |
| folder | Carpeta de origen declarada en XML | String | Texto libre | `<folder>` |
| filename | Archivo imagen referenciado en XML | String | `*.jpg` | `<filename>` |
| original_path | Ruta original declarada por el proveedor | String | Ruta absoluta/relativa | `<path>` |
| database | Fuente declarada en XML | String | Texto libre | `<source><database>` |
| segmented | Indicador de segmentacion | Integer | 0/1 | `<segmented>` |

### C. Objetos anotados (bounding boxes)

Cada archivo XML puede contener multiples objetos `<object>`.

| Campo | Descripcion | Tipo de dato | Rango/Valores | Fuente |
| --- | --- | --- | --- | --- |
| class_name | Etiqueta del cromosoma anotado | String | 24 categorias (`A1`...`G22`, `X`, `Y`) | `<object><name>` |
| xmin | Coordenada minima en eje X | Integer | `0 <= xmin < xmax <= image_width` | `<bndbox><xmin>` |
| ymin | Coordenada minima en eje Y | Integer | `0 <= ymin < ymax <= image_height` | `<bndbox><ymin>` |
| xmax | Coordenada maxima en eje X | Integer | `0 <= xmin < xmax <= image_width` | `<bndbox><xmax>` |
| ymax | Coordenada maxima en eje Y | Integer | `0 <= ymin < ymax <= image_height` | `<bndbox><ymax>` |

## Notas de calidad y anotacion

- Las anotaciones fueron realizadas por un asistente entrenado durante 3 meses por tecnicos especialistas del laboratorio.
- Las coordenadas de caja delimitadora permiten tareas de deteccion y localizacion de cromosomas.
- Este proyecto documenta el dataset en formato XML; no utiliza el esquema YOLO normalizado (`x_center`, `y_center`, `width`, `height`) en su version actual de datos crudos.
