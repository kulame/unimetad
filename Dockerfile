FROM gengmei-docker.pkg.coding.net/tob/image/dev

COPY . /srv/apps/unimetad
WORKDIR /srv/apps/unimetad
RUN pip install -r requirements.txt
COPY env /srv/apps/unimetad/local.conf
ENTRYPOINT ["scripts/deploy"]


