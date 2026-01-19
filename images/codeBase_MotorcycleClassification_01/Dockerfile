FROM python:3.13.9

# Requirements-Datei kopieren
COPY requirements.txt /tmp/requirements.txt

# Dependencies aus requirements.txt installieren
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Alle drei Apps kopieren
COPY code/App01.py /codeBase/App01.py
COPY code/App02.py /codeBase/App02.py
COPY code/App03.py /codeBase/App03.py