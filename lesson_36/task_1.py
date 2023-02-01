import requests
from urllib import request

wiki_test_file1 = "wiki_robot_way1.txt"
wiki_test_file2 = "wiki_robot_way2.txt"
face_test_file1 = "face_robot_way1.txt"
face_test_file2 = "face_robot_way2.txt"

urls = []
url_wiki = "https://en.wikipedia.org/wiki/robot.txt"
url_face = "https://www.facebook.com/robot.txt"
urls.append((url_wiki, wiki_test_file1, wiki_test_file2))
urls.append((url_face, face_test_file1, face_test_file2))


def main():

    for item in urls:
        # classic way, using requests library
        data1 = requests.get(item[0])
        with open(item[1], "bw") as f1:
            f1.write(data1.content)
        # second way, using request from urllib library
        request.urlretrieve(item[0], item[2])

if __name__ == '__main__':
    main()