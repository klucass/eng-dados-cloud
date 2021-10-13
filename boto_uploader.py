import boto3
import os

# arquivo aws credentials  ignorado pelo git por motivos obvios
os.environ["AWS_SHARED_CREDENTIALS_FILE"] = ".aws/credentials"

# Usando Amazon S3
s3 = boto3.resource('s3')

# Upload do arquivo
data = open("teste.txt", "rb")
s3.Bucket("datalake-kennedylucas-igti").put_object(Key="teste.txt", Body=data)