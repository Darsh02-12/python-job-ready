import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
# print(response.status_code)   # 200 means success; 404 = not found; 500 = server error
data = response.json()        # converts the JSON response into a Python dict
if response.status_code ==200:
    print(f'Setup: {data["setup"]} \nPunchline: {data["punchline"]}')
else:
    print("Something went wrong")