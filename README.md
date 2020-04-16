c3covid19
==========
Python wrapper for easy use of the [C3 Covid 19 Data Lake](https://c3.ai/covid-19-api-documentation/#section/Using-C3.ai-APIs).


Full API Documentation
--------
https://connor-makowski.github.io/c3covid19/

Features
--------

- Simplified python access to the c3 data lake.

Setup
----------

Make sure you have Python 3.6.x (or higher) installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation

```
pip install c3covid19
```

### Quick Start
1) Import c3api into your project
```py
from c3covid19 import c3api
```

2) Initialize a `c3api` connection object
```py
cnx=c3api()
```

3) Specify your JSON request as a python dictionary:
```py
germany_request={
  "spec": {
    "filter": 'id == "Germany"'
  }
}
```

4) request from the connection object:
```py
germany=cnx.request(data_type='outbreaklocation', parameters=germany_request, api='fetch')
```
  - Notes:
    - `data_type` is the data "Type" as specified by the c3.ai covid19 documentation [here](https://c3.ai/covid-19-api-documentation/#section/C3.ai-APIs-for-COVID-19-Unified-Data)
    - `parameters` is the JSON Request you will be posting to the api
    - `api` is the specific API to hit and defaults to `fetch` if not specified.

5) Print the results:
```py
print(germany)
```


### Output Data
Output data will be in the format set by the C3 Covid19 Data Lake team. See their documentation [here](https://c3.ai/covid-19-api-documentation/#section/Using-C3.ai-APIs).


### Full Example
```py
from c3covid19 import c3api

cnx=c3api()
germany_request={
  "spec": {
    "filter": 'id == "Germany"'
  }
}

germany=cnx.request(data_type='outbreaklocation', parameters=germany_request)

print(germany)
```
