import sys
import requests
import json

headers = {
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br',
    'cookie':'mycarfax=;'
}

vehicleVin = ''
vehicleId = ''
#'https://www.mycarfax.com/Service/myxapi/vehicle/{vin}' // POST - add to pull records
#'https://www.mycarfax.com/Service/myxapi/vehicle/{id}' // GET - pull records
# https://www.mycarfax.com/Service/myxapi/states/getUsAndCanadaStates // get states/names
# https://www.mycarfax.com/Service/myxapi/lookupByVin/{vin} // pull generic vehicle info from vin
 
# lookup car by plate
plateId = input('Plate number:')
plateState = input('State:')
url = str.format('https://www.mycarfax.com/Service/myxapi/lookupByStatePlate/{0}/{1}', plateState, plateId)
r = requests.get(url, headers=headers)
print(r.text)
exit()

# add vehicle to account
url = str.format('https://www.mycarfax.com/Service/myxapi/vehicle/{0}', vehicleVin)
r = requests.post(url, headers=headers, data={'accountId': '000000000'})

# dump info
with open('carinfo_dump.json', 'w') as f:
  json.dump(r.text, f, ensure_ascii=False)

# remove from account
url = str.format('https://www.mycarfax.com/Service/myxapi/vehicle/{0}', vehicleId)
r = requests.delete(url, headers=headers)

print('done')
#print(r.text)