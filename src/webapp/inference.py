import os
from ultralytics import YOLO

# Resolve paths safely
_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_MODEL_PATH = os.path.join(_BASE_DIR, 'scripts', 'training', 'runs', 'train', '26m', 'yolo_vertex_exp-7', 'weights', 'best.pt')

MODEL_PATH = os.environ.get('MODEL_PATH', DEFAULT_MODEL_PATH)

try:
    if os.path.exists(MODEL_PATH):
        model = YOLO(MODEL_PATH)
    else:
        print(f"Warning: Model file not found at {MODEL_PATH}.")
        model = None
except Exception as e:
    print(f"Warning: Could not load model at {MODEL_PATH}. Error: {e}")
    model = None

def get_class_names():
    if model is not None and hasattr(model, 'names'):
        return model.names
    return {}

def predict_image(image_path):
    if model is None:
        raise ValueError("Model is not loaded.")
        
    # Agregamos parámetros:
    # conf: confianza mínima.
    # iou: solapamiento máximo permitido.
    # agnostic_nms=True: elimina duplicados sobre el mismo objeto incluso si el modelo cree que son de clases diferentes.
    results = model(image_path, conf=0.50, iou=0.45, agnostic_nms=True)
    
    predictions = []
    # Using the first result (since only one image is processed at a time)
    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                xyxy = box.xyxy[0].tolist() # [x1, y1, x2, y2]
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                name = model.names[cls] if hasattr(model, 'names') else str(cls)
                
                predictions.append({
                    "bbox": xyxy,
                    "confidence": conf,
                    "class_id": cls,
                    "class_name": name
                })
                
    return predictions
