def longest_words(file_name):
    with open(file_name, encoding='utf-8') as text:
        words = text.read().split()
        print(words)
        max_length = len(max(words, key=len))
        print(max_length)
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('article.txt'))