# 🚗 License Plate Detection App

An AI-powered web application that automatically detects vehicle license plates from uploaded images using computer vision.

## 🚀 Live Demo
You can try out the live interactive application directly on Hugging Face Spaces!
👉 **[Click here to view the live app](https://huggingface.co/spaces/jeevikahunnurkar/license_detection)**

---
## 🛠️ Tech Stack
* **Model:** YOLOv8 (Object Detection)
* **Backend:** Flask (Python)
* **Environment:** * 💻 **Local Development:** Python 3.13
  * 🚀 **Production (Hugging Face):** Python 3.10.11 (via Docker)

---

## 💻 How to Run Locally

### Option 1: Using Docker (Recommended)
This runs the project in the exact same Python 3.10 environment used on Hugging Face:
```bash
docker build -t license-detection .
docker run -p 7860:7860 license-detection