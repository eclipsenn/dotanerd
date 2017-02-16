FROM python:3.5-slim
LABEL "author"="Dmitry Mishin"
RUN groupadd dotanerd_group && useradd --create-home --home-dir /home/dotanerd_user -g dotanerd_group dotanerd_user

# Pillow and postgres deps, nginx
RUN apt-get update && \
    apt-get install -y libpq-dev zlib1g-dev nginx && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /opt/dotanerd/
RUN apt-get update && \
    apt-get install -y gcc && \
    pip install -r /opt/dotanerd/requirements.txt && \
    apt-get purge --auto-remove -y gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/dotanerd

RUN ln -s /opt/dotanerd/dota_nerd/dn_nginx.conf /etc/nginx/sites-enabled/

COPY . /opt/dotanerd
USER dotanerd_user