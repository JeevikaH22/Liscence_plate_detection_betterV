FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user requirements.txt $HOME/app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user app.py $HOME/app/app.py
COPY --chown=user templates/ $HOME/app/templates/
COPY --chown=user static/ $HOME/app/static/

RUN mkdir -p $HOME/app/static/uploads

RUN mkdir -p $HOME/app/runs/detect/train/weights/
COPY --chown=user lisence_plate_detection.pt $HOME/app/runs/detect/train/weights/best.pt

EXPOSE 7860

CMD ["python", "app.py"]