import os
import uuid
from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
from inference import predict_image, get_class_names

app = Flask(__name__)
# The uploaded files will live here dynamically while the app is running
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # max 16MB file

# Ensure directory exists relative to app.py
os.makedirs(os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER']), exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Avoid caching/overwriting using uuid
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        
        filepath = os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        try:
            predictions = predict_image(filepath)
            image_url = url_for('static', filename=f'uploads/{unique_filename}')
            return jsonify({
                "success": True, 
                "image_url": image_url,
                "predictions": predictions
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    return jsonify({"error": "Invalid file type"}), 400

@app.route('/parse_annotation', methods=['POST'])
def parse_annotation():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    
    width = float(request.form.get('width', 0))
    height = float(request.form.get('height', 0))
    
    if file and file.filename.endswith('.txt'):
        class_names = get_class_names()
        ground_truth = []
        
        try:
            content = file.read().decode('utf-8')
            for line in content.splitlines():
                parts = line.strip().split()
                if len(parts) >= 5:
                    cls_id = int(parts[0])
                    cx = float(parts[1])
                    cy = float(parts[2])
                    w = float(parts[3])
                    h = float(parts[4])
                    
                    # Transform YOLO normalized format to absolute coords
                    abs_cx = cx * width
                    abs_cy = cy * height
                    abs_w = w * width
                    abs_h = h * height
                    
                    xmin = abs_cx - (abs_w / 2)
                    ymin = abs_cy - (abs_h / 2)
                    xmax = abs_cx + (abs_w / 2)
                    ymax = abs_cy + (abs_h / 2)
                    
                    name = class_names.get(cls_id, f"Class {cls_id}")
                    
                    ground_truth.append({
                        "class_name": name,
                        "bbox": [xmin, ymin, xmax, ymax]
                    })
            return jsonify({"success": True, "ground_truth": ground_truth})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    return jsonify({"error": "Invalid file type. Must be .txt"}), 400

if __name__ == '__main__':
    # Start the server on host 0.0.0.0 for Docker compatibility
    app.run(host='0.0.0.0', port=5000, debug=True)
