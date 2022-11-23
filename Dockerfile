FROM python:3.11

WORKDIR /talanakombat
COPY requirements.txt /talanakombat/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /talanakombat/requirements.txt

COPY . /talanakombat/

CMD bash -c "while true; do sleep 1; done"