FROM spark:3.5.4-java17-python3

USER root
# Install Python Dependencies
COPY ./requirements.txt /opt/   
RUN pip install -r /opt/requirements.txt

USER spark
