FROM python:3.12-slim
WORKDIR /app
COPY sample-data/requirements.txt .
RUN pip install -r requirements.txt
COPY sample-data/send_sample_events.py .
CMD ["python", "send_sample_events.py"]
