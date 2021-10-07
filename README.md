# Engenharia de Dados Cloud

Arquivos criados para os desafios e atividades do Bootcamp de Engenharia de Dados Cloud do IGTI

## Primeira atividade
A primeira atividade consiste em analisar dados do resultado do último Enem. Os dados estão disponíveis ao público no site do [Inep](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados).

###   🛶  **Criação do Data Lake usando S3**
Para isso os dados são colocados em um Data Lake usando o serviço S3 do Amazon Web Services (AWS). Para fazer o upload, usei o Boto3, uma biblioteca da própria amazon que ajuda a gerenciar alguns serviços via código. O código usado está no arquivo [boto_uploader.py](boto_uploader.py)

### ⚙️ **Transformação do arquivo CSV usando PySpark no Amazon EMR**
Em seguida, o arquivo, que tem cerca de 3Gb de tamanha, com mais de 5M de registros, pode ser transformado em Parquet para um armazenamento e processamento com maior desempenho.

Para isso, criei um ambiente de Cluster usando AWS RMR, que é o serviço da Amazon para processamento MapReduce e usei o PySpark rodando em um JupyterNotebook criado para o cluster. O script para processamento do arquivo está em [job_spark_enem_csv_to_pq.py](job_spark_enem_csv_to_pq.py)

Alternativamente é possível usar o AWS Glue para o processamento de Big Data de forma serverless. Vide glue_job_enem.py

###  🔬 **Analisando os dados com AWS Athena**

Para analisar os dados do Datalake, é possível usar o Athenas, que é uma engine de Data Lake que possibilita consultas aos seus dados por meio de Queries SQL mesmo que eles estejam armazenados de forma desestruturada, neste caso, em Parquet. Para isso, é necessário informar os Eschema dos dados usando o Crawler do AWS Glue.

