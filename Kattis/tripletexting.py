# https://open.kattis.com/problems/tripletexting
# accepted answer, CPU time: 0.05s


"""
Sample input:
hellohrllohello

Sample output:
hello

"""

if __name__ == '__main__':
    from sys import stdin

    text = stdin.readline().strip()

    word_length = len(text) // 3

    words = [text[:word_length], text[word_length: 2 * word_length], text[2 * word_length:]]

    for word in words:
        if words.count(word) >= 2:
            print(word)
            exit()
