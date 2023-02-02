# Write a console application which takes as an input a city name
# and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use openweathermap.org

import requests

url = f'http://api.openweathermap.org/data/2.5/weather'
APPID = '2a4ff86f9aaa70041ec8e82db64abf56'


def get_city():
    city = input("Enter City to know the weather:\n")
    return city

def print_info(l):
    print(f'In city right now:\n{l[0]}\n{l[1]}\n{l[2]}')

if __name__ == '__main__':
    status = True
    print("So, you can find out the weather in any city or type '0' to exit")
    while status:
        try:
            city = get_city()
            if city == '0':
                status = False
                break
            params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
            resp = requests.get(url=url, params=params)
            if resp.ok:
                print(resp.json())
                print(resp.json()['weather'][0]['main'])
                data = resp.json()
                print_info([data['weather'][0]['main'],
                            data['weather'][0]['description'],
                            f"Temp: {data['main']['temp']} K"])
            else:
                print('wrong city name, try one more time')
                city = get_city()
        except Exception as e:
            print("By")
            status = False