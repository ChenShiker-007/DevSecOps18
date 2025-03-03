import requests

url = 'https://steelseries.com/blue/'

response = requests.get(url)    

print(f'The status code for this url {url} -> {response.status_code}')

if response.status_code == 200:
    print(f'The page was successfully loaded -> {response.status_code}')
else:
    print(f'The page could not be loaded -> {response.status_code}')



# requests.