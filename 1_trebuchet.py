total = 0
digits_in_words = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("./data/1_calibration_document.txt", "r") as f:
    for line in f:
        n = len(line)
        number = ""

        stop = False

        for i in range(n):
            if stop:
                break

            for j in range(i, n):
                if line[i:j] in digits_in_words:
                    digit = digits_in_words[line[i:j]]
                    number += str(digit)
                    stop = True
                    break

        stop = False
        for i in range(n, -1, -1):
            if stop:
                break

            for j in range(n, -1, -1):
                if line[j:i] in digits_in_words:
                    digit = digits_in_words[line[j:i]]
                    number += str(digit)
                    stop = True
                    break

        total += int(number)

print(total)
