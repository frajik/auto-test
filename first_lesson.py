import requests
import pprint


url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(result.text)
print("status code: " + str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print("Successfully")
else:
    print("Error")
result.encoding = "utf-8"
print()
pprint.pprint(result.text)
