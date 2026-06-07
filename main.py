import json

import requests

while True:
    print("---Menu---")
    print("1. Enter URL \n2. See URLs\n3. EXIT")
    print("----------")
    ch = int(input("\n\nWhat do you Choose - "))

    def enter_url():
        url = input("Paste the URL - ")
        response = requests.get(url)

        data = {"url": url, "status": response.status_code}

        with open("download.json", "w") as file:
            json.dump(data, file, indent=4)

        print(response.status_code)
        print(response.text[:100])
        print("URL Downloaded")

    def see_url():
        with open("download.json", "r") as file:
            down = json.load(file)

        print(down)

    if ch == 1:
        enter_url()
    elif ch == 2:
        see_url()
    elif ch == 3:
        break
    else:
        print("Invalid Option")
