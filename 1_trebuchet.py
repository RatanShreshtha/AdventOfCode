total = 0
digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

with open('./data/1_calibration_document.txt', 'r') as f:
    for line in f:
        number = ''

        for left in line:
            if left in digits:
                number += left
                break
        
        for right in line[::-1]:
            if right in digits:
                number += right
                break
        
        total += int(number)

print(total)