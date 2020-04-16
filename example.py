from c3covid19 import c3api

cnx=c3api()
germany_request={
  "spec": {
    "filter": 'id == "Germany"'
  }
}

germany=cnx.query(data_type='outbreaklocation', parameters=germany_request)

print(germany)
