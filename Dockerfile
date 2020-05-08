FROM gengmei-docker.pkg.coding.net/tob/image/base

COPY . /srv/apps/unimetad
WORKDIR /srv/apps/unimetad
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]


