FROM python:3.8.10

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PATH=/home/pumuser/.local/bin:$PATH
ENV FT_APP_ENV="docker"

RUN mkdir /src/sync -p

RUN apt-get update \
  && apt-get -y install sudo libatlas3-base curl sqlite3 libhdf5-serial-dev  \
  && apt-get clean \
  && useradd -u 1000 -G sudo -U -m -s /bin/bash pumuser \
  && chown pumuser:pumuser /src \
  # Allow sudoers
  && echo "pumuser ALL=(ALL) NOPASSWD: /bin/chown" >> /etc/sudoers \
  chown pumuser:pumuser /src

COPY --chown=pumuser:pumuser . /src/sync

WORKDIR /src/sync

USER pumuser


RUN pip install -r requirements.txt

#ENTRYPOINT ["tail", "-f", "/dev/null"]
#CMD ["main.py"]
#ENTRYPOINT ["python3"]

