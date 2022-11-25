FROM ubuntu
FROM python:3.9
# update
RUN apt update

# Setup Server Environment
RUN apt install -y \
    socat

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyyaml

# add new user if it is needed
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
RUN pip3 install pyyaml
# Change user and work directory
WORKDIR /home/ctf
COPY ./Classer.py .
USER ctf

# Entry point
EXPOSE 80
ENTRYPOINT socat tcp-l:80,fork,reuseaddr exec:'python3 Classer.py' && /bin/bash