import requests
import json

API_URL = "https://crudcrud.com/api/01d5dec1bb2142ccbd7d45537694d97c"

Employees_JSON = {
    "employees":[
        {"id":"1","first_name":"Nichola","last_name":"Davies","age":"34", "gender":"Male","salary":"1230"},
        {"id":"2","first_name":"Deirdre","last_name":"Paterson","age":"41", "gender":"Female","salary":"1000"},
        {"id":"3","first_name":"Sonia","last_name":"Butler","age":"28", "gender":"Female","salary":"1500"},
        {"id":"4","first_name":"Jacob","last_name":"Metcalfe","age":"42", "gender":"Male","salary":"2000"},
        {"id":"5","first_name":"Fiona","last_name":"Clarkson","age":"39", "gender":"Female","salary":"1850"}
    ]
}

Employees_JSON_UPDATED = {
    "employees":[
        {"id":"1","first_name":"Nicholas","last_name":"Davies","age":"34", "gender":"Male","salary":"1230"},
        {"id":"2","first_name":"Deirdre","last_name":"Paterson","age":"41", "gender":"Female","salary":"1000"},
        {"id":"3","first_name":"Sonia","last_name":"Butler","age":"28", "gender":"Female","salary":"1700"},
        {"id":"5","first_name":"Fiona","last_name":"Clarkson","age":"40", "gender":"Female","salary":"1850"}
    ]
}
Employee_ID = "609d16f513120c03e81ca5c6"

#post_request = requests.post(f"{API_URL}/employees", json=Employees_JSON)
id_changer = requests.put(f"{API_URL}/employees/{Employee_ID}", json=Employees_JSON_UPDATED)
print(id_changer.status_code)

#ეს უკვე დაწერილი კოდია, შესაბამისად post მოდული 'გაკომენტარებულია'

