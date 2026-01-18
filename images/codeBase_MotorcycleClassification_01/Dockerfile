FROM python:3.13.9

# TensorFlow und zusätzliche Dependencies installieren
RUN pip3 install --no-cache-dir \
    tensorflow \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
    statsmodels \
    numpy

COPY code/App02.py /codeBase/App01.py

# Script ausführen
CMD ["python3", "/codeBase/App01.py"]