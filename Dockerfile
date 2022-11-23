FROM python:3.11

WORKDIR /talanakombat
COPY requirementes.txt /talanakombat/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /talanakombat/requirementes.txt

COPY . /talanakombat/

CMD bash -c "while true; do sleep 1; done"