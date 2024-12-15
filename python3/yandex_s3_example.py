import boto3
from botocore.client import Config
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Параметры подключения
ACCESS_KEY = 'YCAJEBroZohgmETsUhiJ5zTFs'
SECRET_KEY = 'YCOxfenUj9v-OQRby-7cQzlR8UICOWqsa65Gl5-N'
BUCKET_NAME = 'bookss'
REGION = 'ru-central1'  # Пример региона

# Создание клиента S3 с настройками Yandex Object Storage
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    endpoint_url='https://storage.yandexcloud.net',
    region_name=REGION,
    config=Config(signature_version='s3v4'),
)

def upload_file(file_path, object_name):
    """
    Загрузка файла в Yandex Object Storage.
    :param file_path: Путь к локальному файлу
    :param object_name: Путь в бакете
    """
    try:
        s3_client.upload_file(file_path, BUCKET_NAME, object_name)
        print(f"Файл {file_path} успешно загружен как {object_name} в бакет {BUCKET_NAME}.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except NoCredentialsError:
        print("Неверные учетные данные.")
    except PartialCredentialsError:
        print("Не хватает части учетных данных.")

def download_file(object_name, file_path):
    """
    Скачивание файла из Yandex Object Storage.
    :param object_name: Путь в бакете
    :param file_path: Путь к локальному файлу
    """
    try:
        s3_client.download_file(BUCKET_NAME, object_name, file_path)
        print(f"Файл {object_name} успешно скачан как {file_path} из бакета {BUCKET_NAME}.")
    except FileNotFoundError:
        print(f"Файл {object_name} не найден в бакете.")
    except NoCredentialsError:
        print("Неверные учетные данные.")
    except PartialCredentialsError:
        print("Не хватает части учетных данных.")

def list_objects(prefix=''):
    """
    Перечисление объектов в бакете.
    :param prefix: Префикс для фильтрации объектов
    """
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)
        if 'Contents' in response:
            print(f"Объекты в бакете {BUCKET_NAME}:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"В бакете {BUCKET_NAME} нет объектов с префиксом '{prefix}'.")
    except NoCredentialsError:
        print("Неверные учетные данные.")
    except PartialCredentialsError:
        print("Не хватает части учетных данных.")

if __name__ == "__main__":
    # Загрузка файла
    upload_file('/mnt/d/обама/python3/python3/python3/filee.txt', 'folder/in/bucket/fileee.txt')

    # Скачивание файла
    download_file('folder/in/bucket/file.txt', '/mnt/d/обама/python3/python3/python3/downloaded_filee.txt')

    # Перечисление объектов
    list_objects('folder/in/bucket/')

