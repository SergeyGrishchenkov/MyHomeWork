# Try to write data to JSON file, handle exceptions. If it’s not possible to write data print “Bad JSON file format”.
# Create two functions: write_json() and read_json(), try to operate with then in main() function.
# Create JSON string. Use the separators parameter.
# Try to append to JSON file.
# Find an open API, write a simple get request, get jSON and write it to text file and JSON file
# You have two JSON strings, try to merge then to one valid JSON string.
import json
our_dic = {1: 'dsfhgrt'}

with open('our_json.json', 'w') as f:
    try:
        if not isinstance(our_dic, dict):
            raise()
        json.dump(our_dic, f)
    except:
        print('Bad JSON file format')

# def write_json(our_dic, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(our_dic, f)
#
# def read_json(file_name):
#     with open(file_name, 'r') as f:
#         return json.load(f)
#
# def main():
#     our_dic = {1: 'dsfhgrt'}
#     file_name = 'json2.json'
#     write_json(our_dic, file_name)
#     result = read_json(file_name)
#     print(result)
#
# if __name__ == '__main__':
#     main()

# our_dic = {1: 'dsfhgrt', 2: ['11', '22']}
# a = json.dumps(our_dic, indent=4, separators=(',', ':'))
# print(a)

# our_dic = {3: '333'}
# with open('our_json.json', 'w+') as f:
#     data = json.load(f)
#     #d.update(our_dic)
#     print(data)
#     #json.dump(d, f)

# our_dic1 = {1: '111'}
# our_dic2 = {3: '333', 2: ['11', '22']}
# a1 = json.dumps(our_dic1, indent=4, separators=(',', ':'))
# a2 = json.dumps(our_dic2, indent=4, separators=(',', ':'))
# print(a1)
# print(a2)
# a3 = a1 + a2
# # print(a3)
# dic1 = json.loads(a1)
# dic2 = json.loads(a2)
# dic1.update(dic2)
# print(dic1)
# a3 = json.dumps(dic1, indent=4, separators=(',', ':'))
# print(a3)
