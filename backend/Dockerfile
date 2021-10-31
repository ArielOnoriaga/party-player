FROM python:3.10.0-slim-buster

WORKDIR src/

ADD requirements.txt src/requirements.txt
ADD simpleServer.py src/simpleServer.py
COPY . .

RUN /bin/bash -c "yes | python3 -m pip install -r src/requirements.txt"

EXPOSE 8989

CMD python3 src/simpleServer.py
