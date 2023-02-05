# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use Threads for making requests to reddit API.
import requests
import threading

url = "https://api.pushshift.io/reddit/comment/search/"