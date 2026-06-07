import json

while True:
    print("---Menu---")
    print("1. Enter URL \n2. See URLs\n3. EXIT")
    print("----------")
    ch = int(input("\n\nWhat do you Choose - "))

    def enter_url():
        url = input("Paste the URL - ")
        with open("download.json", "w") as file:
            json.dump(url, file, indent=4)
        print("URL Downloaded")

    def see_url():
        with open("download.json", "r") as file:
            down = file.read()

        print(down)

    if ch == 1:
        enter_url()
    elif ch == 2:
        see_url()
    elif ch == 3:
        break
    else:
        print("Invalid Option")
