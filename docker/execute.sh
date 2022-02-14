#!/bin/bash

#Configuracao para uso do repositorio na AWS 
aws configure set aws_access_key_id $AWS_ACCESS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set default.region $REGION

# Set permissão para executar
chmod -R 775 /opt/pentaho/data-integration/carte.sh

# Run carte
exec /opt/pentaho/data-integration/carte.sh pwd/carte-config.xml