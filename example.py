from c3covid19 import c3data

cnx=c3data()
germany_request={
  "spec": {
    "filter": 'id == "Germany"'
  }
}

germany=cnx.query(data_type='outbreaklocation', parameters=germany_request)

print(germany)
