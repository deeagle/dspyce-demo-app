FROM python:3-alpine3.20

LABEL org.opencontainers.image.authors="Martin Kock <code@deeagle.de>" \
      org.opencontainers.image.url="https://github.com/deeagle/dspyce-demo-app" \
      org.opencontainers.image.licenses="GPL3" \
      org.opencontainers.image.title="dspyce-demo-app" \
      org.opencontainers.image.description="Container which includes a DSpyce-demo to talk to DSpace-Demo." \
      org.opencontainers.image.vendor="deeagle.de"

WORKDIR /app

COPY ["requirements.txt", "requirements.txt"]
COPY ["main.py", "main.py"]

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
