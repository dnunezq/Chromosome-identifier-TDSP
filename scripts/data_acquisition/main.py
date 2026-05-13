import os
import yaml
from pathlib import Path

def load_data(data_dir: str):
    """
    Carga e inspecciona los datos de cromosomas desde la carpeta local 'data'.
    Este script asume que los datos ya están ubicados en la carpeta indicada.
    """
    print(f"Iniciando carga de datos desde: {data_dir}")
    
    data_path = Path(data_dir)
    yaml_file = data_path / "data.yaml"
    
    if not data_path.exists():
        print(f"Error: El directorio de datos no existe: {data_path}")
        return None
        
    if not yaml_file.exists():
        print(f"Error: No se encontró el archivo de configuración data.yaml en {data_path}")
        return None

    # Leer configuración YAML
    with open(yaml_file, 'r') as f:
        config = yaml.safe_load(f)
        
    print("\n--- Resumen del Dataset ---")
    print(f"Número de clases: {config.get('nc', 'Desconocido')}")
    print(f"Clases: {config.get('names', [])}")
    
    # Contar imágenes en los splits (train, val, test)
    splits = ['train', 'valid', 'test']
    for split in splits:
        split_dir = data_path / split / "images"
        if split_dir.exists():
            num_images = len(list(split_dir.glob("*.jpg")))
            print(f"Imágenes en conjunto de {split}: {num_images}")
        else:
            print(f"Conjunto de {split} no encontrado en {split_dir}")
            
    print("---------------------------\n")
    print("Datos cargados correctamente para su posterior procesamiento.")
    return config

if __name__ == '__main__':
    # Ruta a los datos asumiendo ejecución desde la raíz del proyecto
    dataset_path = os.path.join("data", "raw", "chromosoma-1")
    
    config_data = load_data(dataset_path)
