import requests
import json

#метод POST
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
headers = {'accept': 'application/json',
            'Content-Type': 'application/json'}

data = json.dumps(data)

res1 = requests.post(f"https://petstore.swagger.io/v2/pet", headers=headers, data=data)

print(res1.status_code)
print(res1.json())

dict = res1.json()


#метод PUT

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
headers = {'accept': 'application/json',
            'Content-Type': 'application/json'}

data = json.dumps(data)

res2 = requests.post(f"https://petstore.swagger.io/v2/pet", headers=headers, data=data)

print(res2.status_code)
print(res2.json())

# метод GEt

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.json())


#метод DELETE
petId = dict['id']
headers = {'accept': 'application/json'}
res3 = requests.post(f"https://petstore.swagger.io/v2/pet/{petId}", headers=headers)

print(res3.status_code)
print(res3.json())
