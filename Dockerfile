FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask scikit-learn joblib

EXPOSE 5000

CMD ["python", "3app.py"]
