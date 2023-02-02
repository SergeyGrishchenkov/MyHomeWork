# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
import requests, json

url = "https://api.pushshift.io/reddit/comment/search/"
params = {"archived": "false"}

def func(url_, params_):
    data = requests.get(url=url_, params=params_)
    return data.json()

if __name__ == '__main__':
    result = func(url, params)
    with open('my.json', 'w') as f:
        json.dump(result, f)
        