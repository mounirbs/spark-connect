FROM spark:3.5.4-java17-python3

USER root

# Install Python Dependencies
COPY ./requirements.txt /opt/   
RUN pip install -r /opt/requirements.txt

# Install required jars
RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-connect_2.12/3.5.4/spark-connect_2.12-3.5.4.jar -P /opt/spark/jars/

USER spark
