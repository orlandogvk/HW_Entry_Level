import requests
import json


def print_title(name):
    print(f'Get {name}')


def get_players(value):
    data = []
    count = 0
    total_inch = 0
    sw = False
    res = requests.get('https://mach-eight.uc.r.appspot.com/')
    response = json.loads(res.text)
    data = response['values']
    print('PLAYERS')
    for x in range(0, (len(data) - 1)):
        for y in range(x + 1, len(data)):
            total_inch = int(data[x]['h_in']) + int(data[y]['h_in'])
            if total_inch == value:
                print('- ' + data[x]['first_name'] + ' ' + data[x]['last_name'] + ' & ' + data[y]['first_name']
                      + ' ' + data[y]['last_name'])
                count += 1
                sw = True
    if not sw:
        print("No matches found")
    else:
        print(f'--{count} matches found--')


if __name__ == '__main__':
    print_title('NBA players')
    value = int(input('Enter an int value: '))
    get_players(value)
