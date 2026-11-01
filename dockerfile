FROM python:3.11-slim
WORKDIR /app
COPY *.py .
CMD ["python", "Inventory_Manager.py"]
