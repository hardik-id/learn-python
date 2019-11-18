import requests
import sys

if(len(sys.argv)<2):    
    sys.exit("One argument is expected.")

response = requests.get("http://www.mocky.io/v2/5dadc1602d00008040e4bcb3")
print("Plain Text: ", response.text)

jsonResponse = response.json()

print("Type of jsonResponse: ", type(jsonResponse))
print(jsonResponse[sys.argv[1]])


def something():
    print("something")


if __name__ == "__main__":
    something()
