#! /usr/bin/env python3

import serial
import requests

def main():
    print("Present an NFC tag to query for fediverse association")
    try:
        ser = serial.Serial("/dev/ttyACM0")
        ser.write(4) # send EOT to make sure card application is running, doesn't work find out why
        while True:
            line = ser.readline().decode()
            print(line)
            id = line.partition(":")[2].strip().replace(":","")
            if id:
                print(id)
                accts = getAccount(id)
                print(accts)
                if len(accts):
                    for account in accts:
                        print("Found account: {} identifying itself on the fediverse as BornHack badge 2023 id {}".format(account, id))
                    getLastPost(accts[0])
                else:
                    print("No accounts identifies as BornHack badge 2023 id: {} on the fediverse".format(id))
    except IOError:
        print("serial error")

def getAccount(id):
    servers = [
               "fosstodon.org"
               , "mastodon.social"
              ]
    accounts = []
    for server in servers:
        # https://docs.joinmastodon.org/methods/search/
        search_res = requests.get("https://{}/api/v2/search?q={}&type=accounts".format(server, id)).json()
        #print(search_res)
        for account in search_res["accounts"]:
            accounts.append("@{} ({})".format(account["acct"], account["display_name"]))
    return accounts

def getLastPost(account):
    pass

if __name__ == "__main__":
    main()
