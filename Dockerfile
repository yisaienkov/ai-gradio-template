FROM pytorch/pytorch:1.12.0-cuda11.3-cudnn8-runtime

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 -y && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt

RUN python -m pip install -U pip && \
    python -m pip install -r requirements.txt && \
    python -m pip cache purge

COPY ./ /app/

WORKDIR /app/

CMD python src/main.py
