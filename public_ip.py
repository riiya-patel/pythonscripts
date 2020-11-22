import requests
public_ip=requests.get('https://api.ipify.org').text

print(public_ip)