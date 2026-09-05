import os
import cv2
import time
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from ultralytics import YOLO

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")
upload_dir = os.path.join(static_dir, "uploads")

os.makedirs(upload_dir, exist_ok=True)

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir
)

model_path = os.path.join(base_dir, "runs", "detect", "train", "weights", "best.pt")
model = YOLO(model_path)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if "file" not in request.files:
            return jsonify({
                "error": "No file uploaded"
            })

        file = request.files["file"]

        if file.filename == "":
            return jsonify({
                "error": "No selected file"
            })
        
        filename = secure_filename(file.filename)
        original_path = os.path.join(upload_dir, filename)
        file.save(original_path)

        results = model.predict(
            source=original_path,
            conf=0.25,
            save=False
        )

        annotated_frame = results[0].plot()

        output_filename = f"detected_{filename}"
        output_path = os.path.join(
            upload_dir,
            output_filename
        )

        cv2.imwrite(output_path, annotated_frame)

        time.sleep(0.2)

        return render_template(
            "result.html",
            img_name=output_filename,
            moment=time.time()
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
