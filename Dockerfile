
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /carrinho_de_compra
WORKDIR /carrinho_de_compra
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements.txt /carrinho_de_compra/
#COPY requirements-opt.txt /webapps/
RUN pip install -r /carrinho_de_compra/requirements.txt
#RUN pip install -r /webapps/requirements-opt.txt
ADD . /carrinho_de_compra/
# Django service
EXPOSE 8000
#CMD python /carrinho_de_compra/manage.py migrate 

