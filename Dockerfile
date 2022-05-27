FROM datajoint/djlab:latest

RUN \
  echo git >> /tmp/apt_requirements.txt && \
  /entrypoint.sh echo complete && \
  rm /tmp/apt_requirements.txt

COPY --chown=anaconda:anaconda ./start.py ./test.py ./.anaconda/

RUN pip install datajoint
