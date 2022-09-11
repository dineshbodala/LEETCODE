numEnglish  = { 0:'zero ', 1:'one ', 2:'two ', 3:'three ', 4:'four ',
                5:'five ', 6:'six', 7:'seven ', 8:'eight ', 9:'nine ' }

def displayEnglishDigits(number):
    if number == 0:
        return ""
    digit = numEnglish[number % 10]
    return displayEnglishDigits(number // 10) + digit

print(displayEnglishDigits(412))