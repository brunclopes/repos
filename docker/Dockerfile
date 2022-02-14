# VERSAO 2.1.0
# AUTOR: Ricardo "Openin" Gouvea
# DESCRICAO: Container com Pentaho Data Integration

FROM ubuntu:focal-20210609
LABEL maintainer="Openin"

# Nunca solicita ao usuário as opções de instalação / configuração de pacotes
ENV DEBIAN_FRONTEND noninteractive
ENV TZ America/Sao_Paulo

# PDI
ENV PDI_RELEASE=9.1 \
    PDI_VERSION=9.1.0.0-324 \
    PDI_HOME=/opt/pentaho \
    KETTLE_HOME=/opt/repository \
    PDI_REPOSITORY=/opt/repository/pentaho \
    JAVA_HOME=/opt/java/openjdk
    
RUN apt-get update && apt-get install -y \
# Latest version
        wget \
        unzip \
        python3 \
        python3-pip \
        groff \
        less \
        git \
        vim \
# Especific version
        #wget=1.20.3-1ubuntu1 \
        #unzip=6.0-25ubuntu1 \
        #python3=3.8.2-0ubuntu2 \
        #python3-pip=20.0.2-5ubuntu1.5 \
        #groff=1.22.4-4build1 \
        #less=551-1ubuntu0.1 \
        #git=1:2.25.1-1ubuntu3.1 \
        net-tools \
        tzdata \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN /usr/bin/wget --progress=dot:mega https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u292-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u292b10.tar.gz -O /tmp/openjdk.tar.gz \
    # https://github.com/AdoptOpenJDK/openjdk8-binaries/releases
    && /usr/bin/wget --progress=dot:mega https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -O /tmp/awscliv2.zip \
    && /usr/bin/unzip -q /tmp/awscliv2.zip \
    && ./aws/install

# RUN mkdir -p $PDI_REPOSITORY
# RUN mkdir -p $PDI_REPOSITORY/.meta
# RUN mkdir -p $KETTLE_HOME/.kettle
# RUN mkdir -p $KETTLE_HOME/logs
RUN mkdir -p $PDI_HOME \
    && mkdir -p $JAVA_HOME \
    && cd $JAVA_HOME \
    && tar -xf /tmp/openjdk.tar.gz --strip-components=1 \
    && rm -rf /tmp/openjdk.tar.gz

ENV PATH="$JAVA_HOME/bin:$PATH"
    
#COPY pdi-ce-${PDI_VERSION}.zip /tmp/pdi-ce-${PDI_VERSION}.zip
RUN /usr/bin/wget --progress=dot:giga https://ufpr.dl.sourceforge.net/project/pentaho/Pentaho%20${PDI_RELEASE}/client-tools/pdi-ce-${PDI_VERSION}.zip -O /tmp/pdi-ce-${PDI_VERSION}.zip \
    && /usr/bin/unzip -q /tmp/pdi-ce-${PDI_VERSION}.zip -d $PDI_HOME \
    && rm /tmp/pdi-ce-${PDI_VERSION}.zip \
    && apt-get autoremove \
    && apt-get clean

EXPOSE 8082

COPY carte-config.xml /opt/pentaho/data-integration/pwd
COPY AthenaJDBC42_2.0.27.1000.jar /opt/pentaho/data-integration/lib
COPY redshift-jdbc42-2.0.0.4.jar /opt/pentaho/data-integration/lib
COPY execute.sh /
RUN ["chmod", "+x", "/execute.sh"]
ENTRYPOINT ["/execute.sh"]

#-rwxr-xr-x 1 root root  369 Jul  9 19:54 execute.sh
#-rw-r--r-- 1 root root  369 Aug 21 15:29 execute.sh
# Commando para gerar a imagem, entrar onde esta o Dockerfile
# cd /opt/pentaho/docker
# docker build -t pentaho/dataintegration:9.1 .

# cd ~/git/carte-docker
# docker run -d -p 8082:8082 --name pentaho-dataintegration -v /opt/repository:/opt/repository -e "AWS_ACCESS_KEY=AKIA5ANTT2XIZFKSEHGK" -e "AWS_SECRET_KEY=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" -e "REGION=us-west-2" -it pentaho/dataintegration:9.1
# docker ps
# docker exec -it pentaho-dataintegration bash
# docker stop pentaho-dataintegration
# docker rmi -f image-id
# docker rm registry-name (docker rm pentaho-dataintegration)
# wget --progress=dot:giga https://ufpr.dl.sourceforge.net/project/pentaho/Pentaho%20${PDI_RELEASE}/client-tools/pdi-ce-${PDI_VERSION}.zip -O /optpentaho/pdi-ce-${PDI_VERSION}.zip

# wget --progress=dot:mega https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u292-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u292b10.tar.gz -O /opt/pentaho/openjdk.tar.gz