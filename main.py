import requests

API = 'http://logs.tf/api/v1/log'

def get_logs(steam_id):
    r = requests.get(API + '?player=' + steam_id)
    logs = r.json()['logs']
    final_list = []
    for x in range(0, 10):
        final_list.append(logs[x])

    return final_list

print(get_logs('76561198061182835'))
