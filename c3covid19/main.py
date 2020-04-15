import requests

class c3data:
    def __init__(self, api_root_url="https://api.c3.ai/covid/api", api_version=1, api_headers={'Content-type':'application/json','Accept':'application/json'}):
        self.api_root_url=api_root_url
        self.api_version=api_version
        self.api_headers=api_headers

    def change_api_version(self, api_version):
        self.api_version=api_version

    def change_api_root_url(self, api_root_url):
        self.api_root_url=api_root_url

    def change_api_headers(self, api_headers):
        self.api_headers=api_headers

    def get_url(self, data_type, api):
        ordered_list=[self.api_root_url, self.api_version, data_type, api]
        return '/'.join([str(i) for i in ordered_list])

    def query(self, data_type, parameters, api='fetch'):
        data=requests.post(self.get_url(data_type, api), json=parameters, headers=self.api_headers)
        if str(data.status_code)=="200":
            return data.json()
        else:
            return 'Status Code of {}'.format(data.status_code)
