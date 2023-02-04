from queue import LifoQueue

test_ok = "[test{OK} and (if I {})]"
test_bad = "[test{OK and (if I {})]"

def check_balance(s):
    q = LifoQueue()
    # for item in s:

