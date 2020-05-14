FROM gengmei-docker.pkg.coding.net/tob/image/dev

COPY . /srv/apps/unimetad
WORKDIR /srv/apps/unimetad
COPY .env /srv/apps/unimetad/app/config.py
RUN pip install -r requirements.txt
ENTRYPOINT ["scripts/deploy"]


