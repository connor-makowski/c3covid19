c3covid19
==========
Python wrapper for easy use of the [C3 Covid 19 Data Lake](https://c3.ai/covid-19-api-documentation/#section/Using-C3.ai-APIs).

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

### Getting Started
1) Import c3api into your project
```
from c3covid19 import c3api
```



### Output Data




### Full Example
```py
from c3covid19 import c3api

cnx=c3api()
germany_request={
  "spec": {
    "filter": 'id == "Germany"'
  }
}

germany=cnx.query(data_type='outbreaklocation', parameters=germany_request)

print(germany)
```
