import random

import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, key=None):
    """
    Загрузка файла в S3-бакет

    :param file_name: Файл для загрузки
    :param bucket: Название S3-бакета
    :param key: Название объекта в S3. Если не указано, будет использоваться file_name
    :return: True если файл загружен, иначе False
    """
    if key is None:
        key = file_name

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, str(random.randint(1, 100)) + key)
    except FileNotFoundError:
        print("Файл не найден")
        return False
    except NoCredentialsError:
        print("Ошибка авторизации")
        return False
    return True

file_name = 'example.csv'
bucket_name = 'morixjobucket'

upload_successful = upload_to_s3(file_name, bucket_name)
if upload_successful:
    print("Файл успешно загружен в S3")
else:
    print("Ошибка загрузки файла в S3")
