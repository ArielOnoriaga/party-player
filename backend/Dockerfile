FROM python:3.10.0-slim-buster

WORKDIR picamix/

COPY . .

RUN /bin/bash -c "yes | python3 -m pip install -r requirements.txt"

EXPOSE 8989

CMD python3 simpleServer.py
