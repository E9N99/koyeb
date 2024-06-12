FROM python:latest
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY . /app/
WORKDIR /app/
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
CMD ["bash", "zthon.sh"]
