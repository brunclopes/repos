## Repositório do Bootcamp Data Engineering for Analytics com AWS & Cia

Repositório do Bootcamp Realizado de Pentaho + Airflow. No bootcamp foi abordado a integração do Pentaho com o Apache Airflow. 
Foi trabalhado com o ambiente AWS, criando duas máquinas virtuais no EC2, sendo uma máquina Linux Ubuntu, e uma máquina Windows para utilização do Putty, responsável por acessar a máquina Linux. Foi instalado o Pentaho nas duas máquinas, e o desenvolvimento foi feito na máquina Windows. 
A fonte de dados foi o Amazon RDS, utilizando o banco de dados PostgreSQL, carregando os dados para um bucket S3. 
Dentro do Data Lake existiam as camadas raw, trusted e analytic. A camada raw suporta o dado cru, vindo do RDS, e a camada trusted suporta o dado já tratado. Por fim, a camada analytic suporta o dado tratado e agrupado, pronto para consumo. Nas camadas raw e trusted foi trabalhado com os arquivos csv, e na camada analytic foi trabalhado arquivos parquet. Por fim, também foi apresentado o Amazon Redshift, onde foi realizado a carga de dados vindos do S3. 
No ambiente Linux, foi instalad o Pentaho em um container Docker, com o Apache Airflow realizando a orquestração.
O repositório remoto utilizado para sincronizar os arquivos entre as máquinas foi o Github. Toda a integração de dados foi realizada com a ferramenta Pentaho Data Integration, e a orquestração foi realizada com o Carte e Apache Airflow.
Também foi possível conhecer alguns outros serviços da AWS, como o IAM, gerenciando políticas de acesso e grupos de usuários, realizando consultas no Data Lake com o Athena, e também o Glue. 
