FROM python:3.10.0-slim-buster

WORKDIR picamix/

COPY . .

RUN /bin/bash -c "yes | python3 -m pip install -r requirements.txt"

EXPOSE 5000

# CMD python3 python_rest/server.py
CMD flask run
