import io

import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd

def download_from_s3(bucket_name, key):
    """
    Скачивание файла из S3-бакета

    :param bucket_name: Название S3-бакета
    :param object_name: Имя объекта в S3 (ключ)
    :param file_name: Имя файла для сохранения на локальном диске
    :return: True если файл успешно скачан, иначе False
    """
    s3_client = boto3.client('s3')

    try:
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
        csv_content = s3_object['Body'].read().decode('utf-8')


        print(csv_content)
        return csv_content
    except NoCredentialsError:
        print("Ошибка авторизации")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

bucket_name = 'morixjobucket'
key = 'example.csv'

download_successful = download_from_s3(bucket_name, key)
if download_successful:
    print(f"Файл '{key}' успешно скачан.")
else:
    print("Ошибка скачивания файла.")
