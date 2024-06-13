FROM ubuntu:latest

RUN apt update
RUN apt install python3 python3-pip -y

RUN pip3 install --break-system-packages torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install --break-system-packages ai2-olmo

WORKDIR /app

COPY download_pretrained_model.py /app
RUN ["/usr/bin/python3", "/app/download_pretrained_model.py"]
CMD ["sleep", "infinity"]
