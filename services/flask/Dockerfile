FROM python:3.9

WORKDIR /file

COPY . /file

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "index.py"]    

EXPOSE 80