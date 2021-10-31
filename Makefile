PKG=''
srv:
	docker exec -it backend_picamix_1 /bin/bash

setenv:
	cp .env-example-back backend/.env

back-install:
	python3 -m pip install $(PKG)

back-uninstall:
	python3 -m pip uninstall $(PKG)

back-upgrade:
	python3 -m pip install --upgrade $(PKG)

back-list-packages:
	python3 -m pip list

back-setup:
	yes | python3 -m pip install -r backend/requirements.txt

back-clear:
	yes | python3 -m pip uninstall -r backend/requirements.txt

back-restart:
	make back-stop back-start

back-start:
	cd backend && docker-compose up --build -d --remove-orphans

back-stop:
	cd backend && docker-compose down
