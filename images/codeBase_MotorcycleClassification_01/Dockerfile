FROM python:3.13.9

# Requirements-Datei kopieren
COPY requirements.txt /tmp/requirements.txt

# Dependencies aus requirements.txt installieren
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Python-Script kopieren
COPY code/App02.py /codeBase/App01.py

# Script ausführen
CMD ["python3", "/codeBase/App01.py"]