def mostFrequent(path):
    file = open(path, 'r')
    text = file.readlines()
    file.close()

    text_string = ""
    for line in text:
        text_string += " " + line
    text_string = text_string.split()

    frequency = {}
    num_words = 0

    for word in text_string:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
        num_words += 1

    words = frequency.keys()

    top_five = []

    for n in range(5):
        maximum_frequency = ("", 0)
        for word in words:
            if frequency[word] > maximum_frequency[1]:
                maximum_frequency = (word, frequency[word])
        top_five.append(maximum_frequency)
        frequency[maximum_frequency[0]] = -1

    n = len(top_five)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if top_five[j][1] == top_five[j + 1][1] and top_five[j][0] > top_five[j + 1][0]:
                temp = top_five[j]
                top_five[j] = top_five[j + 1]
                top_five[j + 1] = temp
            j += 1
        i += 1

    print()
    for line in top_five:
        print(f"{line[0]}: {line[1]}")
