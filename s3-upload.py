import boto3
from os import environ

environ["AWS_CONFIG_FILE"] = "./aws/config"
environ["AWS_SHARED_CREDENTIALS_FILE"] = "./aws/credentials"

s3 = boto3.resource('s3')
data = open('./jpeg/2021-04-24_e8910e6410c29c520b8c97bfd0d6cb3c_Marzo_2021/part-1.jpg', 'rb')
s3.Bucket('jpeg-container').put_object(Key='part-1.jpg', Body=data)