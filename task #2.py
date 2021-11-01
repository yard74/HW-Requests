# from pprint import pprint
import requests
import re


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        file_name_on_disk = re.split('\\\\|/', file_path)[-1]
        headers = self.get_headers()
        params = {"path": file_name_on_disk, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, file_path):
        response_dict = self._get_upload_link(file_path=file_path)
        href = response_dict.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл успешно загружен.")


if __name__ == '__main__':
    token = str(input('Введите ваш OAuth токен: '))
    path_to_file = str(input('Введите путь до файла: '))
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
