FROM spark:4.0.0-preview2-java21-python3

USER root
# Install Python Dependencies
COPY ./requirements.txt /opt/   
RUN pip install -r /opt/requirements.txt

USER spark
