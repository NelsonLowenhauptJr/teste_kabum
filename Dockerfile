FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
