FROM spark:3.5.4-python3
USER root
RUN apt-get update && apt-get install -y curl

# Install Python Dependencies
COPY ./requirements.txt /opt/   
RUN pip install -r /opt/requirements.txt

# Using Java 17
# https://jdk.java.net/archive/
WORKDIR /opt/java/
RUN curl "https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_linux-x64_bin.tar.gz" -o openjdk-update.tar.gz \
    && tar -xzf "openjdk-update.tar.gz" \
    && rm -rf openjdk openjdk-update.tar.gz \
    && mv jdk-* openjdk

USER spark
