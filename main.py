import requests
import json



def obtenertoken(user,password):

    url_controller = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

    # obtener ticket
    userData = {
        "aaaUser": {
            "attributes": {
                "name": user,
                "pwd": password
            }
        }
    }
    ticketHeader = {"content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url_controller, data=json.dumps(userData), headers=ticketHeader, verify=False)
    token = (response.json()['imdata'][0]['aaaLogin']['attributes']['token'])
    return token


token = obtenertoken("admin", "!v3G@!4@Y")



def obtenertenants():
    url_Tenants = "https://sandboxapicdc.cisco.com/api/class/fvTenant.json"
    requests.packages.urllib3.disable_warnings()
    tenantsHeader = {"content-type": "application/json", "Cookie" : f"APIC-Cookie={token}"}
    responseTenants = requests.get(url_Tenants, headers=tenantsHeader, verify=False)
    return responseTenants


response = obtenertenants().json()
tenants = response['imdata']

for tenant in tenants:
    print(f"Tenant name: {tenant['fvTenant']['attributes']['name']}")

