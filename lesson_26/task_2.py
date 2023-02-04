from queue import LifoQueue, Queue, SimpleQueue, PriorityQueue

test_ok = "[test{OK} and (if I {})]"
test_bad = "[test{OK and (if I {})]"
test_case = []
test_case.append(test_ok)
test_case.append(test_bad)


def check_balance(s: str): #Главное правило, стєк в более вісоким приорритетом не может обнулиться первым
    q_list = {"[]": LifoQueue(), "()": LifoQueue(), "{}": LifoQueue()}
    pr_count = 1
    for item in s:
        match item:
            case "[":
                q_list["[]"].put_nowait(item)
            case ']':
                q_list["[]"].get_nowait()
            case '(':
                q_list["()"].put_nowait(item)
            case ')':
                q_list["()"].get_nowait()
            case '{':
                q_list["{}"].put_nowait(item)
            case '}':
                q_list["{}"].get_nowait()
    return True if (q_list["[]"].empty() and q_list["{}"].empty() and q_list["()"].empty()) else False


if __name__ == '__main__':
    for test in test_case:
        result = check_balance(test)
        print(f'For test string "{test}" have such result for cheking is brackets are balanced:\n {result}')
