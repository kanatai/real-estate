FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY ./ /app
RUN pip3 install -r /app/requirements.txt

CMD python manage.py collectstatic --no-input
