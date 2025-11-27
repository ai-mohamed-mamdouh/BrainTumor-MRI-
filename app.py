import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from keras.layers import TFSMLayer
from keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


model = TFSMLayer("model_Ai_dir", call_endpoint="serving_default")

class_dict = {
    0: 'Glioma',
    1: 'Meningioma',
    2: 'No Tumor',
    3: 'Pituitary'
}

def predict_to_deploy(image_path):

    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)


    pred = model(img_array)


    if isinstance(pred, dict):
        pred = next(iter(pred.values()))

    pred = pred.numpy()  # (1, num_classes)


    class_index = int(np.argmax(pred, axis=-1)[0])
    confidence = float(pred[0][class_index])  

    label = class_dict.get(class_index, "unknown")
    return label, confidence

@app.route('/')
def index () :
    return render_template("home.html")

@app.route("/model")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_api():
    if "image" not in request.files:
        return jsonify({"error": "no image uploaded"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "empty filename"}), 400

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    temp_path = os.path.join(app.config["UPLOAD_FOLDER"], "upload.png")
    file.save(temp_path)

    label, confidence = predict_to_deploy(temp_path)

    return jsonify({
        "label": label,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)
