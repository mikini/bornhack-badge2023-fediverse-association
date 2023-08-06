#! /usr/bin/python
import serial
import requests

def main():
    print("Present an NFC tag to query for fediverse association")
    try:
        ser = serial.Serial("/dev/ttyACM0")
        ser.write(4) # send EOT to make sure card application is running, doesn't work find out why
        line = ser.readline()
        while line:
            id = line.partition(":")[2].strip().replace(":", "")
            if id:
                print(id)
                accts = getAccount(id)
                if len(accts):
                    for account in accts:
                        print("Found account: {} identifying itself on the fediverse as BornHack badge 2023 id {}".format(account, id))
                    getLastPost(accts[0])
                else:
                    print("No accounts identifies as BornHack badge 2023 id: {} on the fediverse".format(id))
            line = ser.readline()
    except IOError:
        print("serial error")

def getAccount(id):
    servers = ["mastodon.social", "fosstodon.org"]
    accounts = []
    for server in servers:
        search_res = requests.get("https://{}/api/v2/search?q={}".format(server, id)).json()
        for account in search_res["accounts"]:
            accounts.append("@{}@{}".format(account["acct"], server))
    return accounts

def getLastPost(account):
    pass

if __name__ == "__main__":
    main()
