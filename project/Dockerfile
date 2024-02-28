FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /project

RUN pip install pipenv
COPY Pipfile* /project/
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . /backend/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000