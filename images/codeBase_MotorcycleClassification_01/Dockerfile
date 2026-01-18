FROM tensorflow/tensorflow:2.15.0

# Zusätzliche Dependencies installieren
RUN pip3 install --no-cache-dir \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
    statsmodels

COPY code/App02.py /codeBase/App01.py

# Script ausführen
CMD ["python3", "/codeBase/App01.py"]