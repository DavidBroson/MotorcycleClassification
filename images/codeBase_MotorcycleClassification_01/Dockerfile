FROM tensorflow/tensorflow:latest

# Zusätzliche Dependencies installieren
RUN pip3 install --no-cache-dir \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
    statsmodels

COPY code/App01.py /codeBase/App01.py

# Script ausführen
CMD ["python3", "/codeBase/App01.py"]