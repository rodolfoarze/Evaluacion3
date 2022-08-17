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

print (token)

# consultar inventario
#getDevicesHeader = {"content-type": "application/json", "X-Auth-Token": serviceTicket}
#getDevices = requests.get(url_controller+"/api/v1/network-device", headers=getDevicesHeader)

#print(getDevices.json())


# consultar hosts
#getHostsHeader = {"content-type": "application/json", "X-Auth-Token": serviceTicket}
#getHosts = requests.get(url_controller+"/api/v1/host?limit=&offset=&sortBy=&order=&hostName=&hostMac="
                                       #"&hostType=&connectedInterfaceName=&hostIp="
                                       #"&connectedNetworkDeviceIpAddress=&subType=&filterOperation=", headers=getHostsHeader)

#print(getHosts.json())


# Consultar estado de la red

#getNetworkHealthHeader = {"content-type": "application/json", "X-Auth-Token": serviceTicket}
#getNetworkHealth = requests.get(url_controller+"/api/v1/assurance/health", headers=getNetworkHealthHeader)

#print(getNetworkHealth.json())