# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use Threads for making requests to reddit API.
import requests
import threading
import json

url = "https://api.pushshift.io/reddit/comment/search/"
params = []
params.append({"author":"gunmunz"})
params.append({"subreddit_id":"t5_2w844"})
params.append({"subreddit_id":"t5_2qh8u"})
params.append({"author":"Significant-While265"})

def func(url_, params_, result: list):
    data = requests.get(url=url_, params=params_)
    result.append(data.json())
    return result

if __name__ == '__main__':
    result = []
    threads = []
    for item in params:
        threads.append(threading.Thread(target=func, args=(url, item, result)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    with open('my_file.json', 'w') as f:
        json.dump(result, f)

