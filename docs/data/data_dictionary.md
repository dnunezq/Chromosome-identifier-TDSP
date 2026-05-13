# Diccionario de datos

## Dataset: Chromosoma-1

Dataset de imágenes de cromosomas en metafase con anotaciones para detección y clasificación de objetos. Contiene imágenes y etiquetas de coordenadas para 24 categorías de cromosomas.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Imagen | Fotografía o escaneo de células en metafase | Imagen (JPG/PNG) | Diversas resoluciones | Dataset original / Roboflow |
| Label_class | Categoría del cromosoma | Entero (Categoría) | 0 a 23 (24 clases en total correspondientes a los grupos A-G, X, Y) | Archivos de anotación (.txt) |
| x_center | Coordenada X del centro del cuadro delimitador | Flotante | 0.0 a 1.0 (normalizado) | Archivos de anotación (.txt) |
| y_center | Coordenada Y del centro del cuadro delimitador | Flotante | 0.0 a 1.0 (normalizado) | Archivos de anotación (.txt) |
| width | Ancho del cuadro delimitador | Flotante | 0.0 a 1.0 (normalizado) | Archivos de anotación (.txt) |
| height | Alto del cuadro delimitador | Flotante | 0.0 a 1.0 (normalizado) | Archivos de anotación (.txt) |

- **Imagen**: Archivos de imagen que contienen los cromosomas esparcidos.
- **Label_class**: Índice de la clase correspondiente al cromosoma: `0: A1` a `21: G22`, `22: X`, `23: Y`.
- **x_center, y_center, width, height**: Coordenadas del cuadro delimitador (bounding box) que marcan la ubicación exacta del cromosoma dentro de la imagen. Los valores están normalizados con respecto a las dimensiones de la imagen.
