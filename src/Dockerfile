FROM python:3.9-slim

WORKDIR /app

# COPY requirements.txt .
RUN pip install requests
RUN pip install flask
# --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY your_code.py .

CMD [ "python", "./your_code.py"]