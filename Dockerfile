# syntax = docker/dockerfile:1.2

FROM python:3.12-slim-bookworm

LABEL version="0.0.1"

# Set env vars
ENV FLASK_ENV "${FLASK_ENV}"
ENV FLASK_APP "${FLASK_APP}"
ENV FLASK_DEBUG "${FLASK_DEBUG}"

# Disable auto-cleanup after install:
RUN rm /etc/apt/apt.conf.d/docker-clean

# Install updates and cache across builds
ENV DEBIAN_FRONTEND=noninteractive
RUN --mount=type=cache,target=/var/cache/apt,id=apt apt-get update && apt-get -y upgrade

# Create user and work dir
RUN useradd --create-home app

USER app
WORKDIR /home/app/prototype
RUN mkdir --parents /home/app/prototype

# Set PATH
ENV PATH "/home/app/.local/bin/:${PATH}"
ENV PROJECT_ROOT '/home/app/time-tracker'

# Install python deps
COPY --chown=app:app ./requirements.txt ./
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/home/app/.cache/pip,id=pip pip install -r requirements.txt

# Copy the source code
COPY --chown=app . ./

# Run
EXPOSE 9000

# Blank entrypoint allows passing custom commands via `docker run`
ENTRYPOINT [ ]

CMD [ "./entrypoint.sh" ]
