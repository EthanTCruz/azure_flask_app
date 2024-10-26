FROM python:3.11.0
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "/app/app.py"]