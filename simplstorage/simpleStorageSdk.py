from dataclasses import dataclass
import requests


@dataclass
class Store4ME():

    username: str
    access_key: str

    resquest = requests.Session()


    def set_auth_headers(self):
        headers = {'Authorization': 'token {}'.format(self.access_key)}
        return self.resquest.headers.update(headers)


    def open_file_image_path(self, path:str):
        try:
            file = open(path, 'rb')
            return file
        except Exception as err:
            raise err


    def post_image(self, image_path:str, image_name:str) -> dict:
        post_url = 'http://localhost:8000/api/upload_image'

        self.set_auth_headers()
        try:
            resp = self.resquest.post(post_url, files={'img': self.open_file_image_path(image_path)}, 
            data={'name': image_name})
            return {'status_code': resp.status_code, 'value': resp.text}
        except Exception as err:
            return err


    def get_images(self) -> dict:
        images_url = 'http://localhost:8000/api/images'
        self.set_auth_headers()
        try:
            resp = self.resquest.get(images_url)
            return {'status_code': resp.status_code, 'value': resp.text}
        except Exception as err:
            return err


    def get_image(self, id) -> dict:
        image_url = f"http://localhost:8000/api/image/{id}"
        self.set_auth_headers()
        try:
            resp = self.resquest.get(image_url)
            return {'status_code': resp.status_code, 'value': resp.text}
        except Exception as err:
            return err        


    def post_file(self, file_path:str, file_name:str) -> dict:
        post_url = 'http://localhost:8000/api/upload_file'
        self.set_auth_headers()
        file = open(file_path, 'rb')
        try:
            resp = self.resquest.post(post_url, files={'file': self.open_file_image_path(file_path)}, 
            data={'name': file_name})
            return {'status_code': resp.status_code, 'value': resp.text}
        except Exception as err:
            return err


    def get_files(self) -> dict:
        files_url = 'http://localhost:8000/api/files'
        self.set_auth_headers()
        try:
            resp = self.resquest.get(files_url)
            return {'status_code': resp.status_code, 'value': resp.text}
        except Exception as err:
            return err
    

    def get_file(self, id) -> dict:
        file_url = f"http://localhost:8000/api/file/{id}"
        self.set_auth_headers()
        try:
            resp = self.resquest.get(file_url)
            return {'status_code': resp.status_code, 'value': resp.text}
        except Exception as err:
            return err   

