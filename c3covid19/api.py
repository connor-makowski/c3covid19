import requests
from c3covid19.formatting import out_formats

class c3api(out_formats):
    def __init__(self, api_root_url="https://api.c3.ai/covid/api", api_version=1, api_headers={'Content-type':'application/json','Accept':'application/json'}):
        """
        Initialize a c3api class object.

        Takes in the following optional kwargs:

        - api_root_url:
            - Type: String
            - What: The Root path of the URL
                - Note: The api URL up to the API Version Number
            - Default: "https://api.c3.ai/covid/api"
        - api_version:
            - Type: Int
            - What: The url path that specifies api version. Example: .../api/{api_version}/...
            - Default: 1
        - api_headers:
            - Type: Dictionary
            - What: A dictionary of headers to submit with an api post request
            - Default: {'Content-type':'application/json','Accept':'application/json'}
        """
        self.api_root_url=api_root_url
        self.api_version=api_version
        self.api_headers=api_headers

    def change_api_version(self, api_version):
        """
        Change the api_version after the class has been initialized.

        Takes in the following required kwarg:

        - api_version:
            - Type: Int
            - What: The url path that specifies api version. Example: .../api/{api_version}/...
        """
        self.api_version=api_version

    def change_api_root_url(self, api_root_url):
        """
        Change the api_root_url after the class has been initialized.

        Takes in the following required kwarg:

        - api_root_url:
            - Type: String
            - What: The Root path of the URL
                - The api URL up to the API Version Number
        """
        self.api_root_url=api_root_url

    def change_api_headers(self, api_headers):
        """
        Change the api_headers after the class has been initialized.

        Takes in the following required kwarg:

        - api_headers:
            - Type: Dictionary
            - What: A dictionary of headers to submit with an api post request
        """
        self.api_headers=api_headers

    def get_url(self, data_type, api):
        """
        A function to return the full api url for posting a request.

        Takes in the following required kwargs:

        - data_type:
            - Type: String
            - What: The data "Type" as specified by the c3.ai covid19 documentation
            - Example: "outbreaklocation"
            - Example: "linelistrecord"
        - api:
            - Type: String
            - What: The API method to post
            - Example: "fetch"
            - Example: "evalmetrics"

        Also pulls in the following class variables to build out the URL:

        - self.api_root_url
        - self.api_version
        - Note: These would be specified at the class level using   self.change_api_{variable}
        """
        ordered_list=[self.api_root_url, self.api_version, data_type, api]
        return '/'.join([str(i) for i in ordered_list])

    def request(self, data_type, parameters, api='fetch', output_type="all", outfile='./output'):
        """
        A function to make a post request to the C3.ai covid19 Data Lake
        and return the results in a python formatted dictionary

        Takes in the following required kwargs:

        - data_type:
            - Type: String
            - What: The data "Type" as specified by the c3.ai covid19 documentation
            - Example: "outbreaklocation"
            - Example: "linelistrecord"
        - parameters:
            - Type: Dictionary
            - What: A dictionary object to serialize and post as the request JSON to the api
            - Example: {"spec": {"filter": 'id == "Germany"'}}
            - More Info: https://c3.ai/covid-19-api-documentation/#section/Using-C3.ai-APIs/Using-fetch

        Takes in the following optional kwargs:

        - api:
            - Type: String
            - What: The API method to post
            - Example: "fetch"
            - Example: "evalmetrics"
            - Default: "fetch"
        - output_type:
            - Type: String
            - What: The output data or file type
            - Default: "all"
            - Choices:
                - all: A dictionary with all returned data
                - objs: Python list of the returned `objs`
                - pd: Pandas DF of the returned `objs`
                - np: Numpy Array of the returned `objs`
                - csv: Writes a csv and returns python list of the returned `objs`
                - tab: Writes a tab and returns python list of the returned `objs`
        - outfile:
            - Type: String
            - What: The file path to output to
            - Default: "./output"
            - Example: "../my_output"
            - Note: Do not include the file extension
            - Note: Is only used in `csv` and `tab` `output_type`s

        On HTTPS failure (Non 200 Response):
        
        - Raises an exception with the response number
        - Cause: May be a number of reasons
            - Most likely: Invalid api_root_url, api_version, data_type or api
        """
        data=requests.post(self.get_url(data_type=data_type, api=api), json=parameters, headers=self.api_headers)
        if str(data.status_code)=="200":
            return self.get_output(data=data.json(), output_type=output_type, outfile=outfile)
        else:
            raise Exception('HTTPS Request failed with status code: {}'.format(data.status_code))
