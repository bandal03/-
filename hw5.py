def read_single_digit(digit):
    hangul_digits = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return hangul_digits[int(digit)]

def read_number(number):
    result = ""
    for digit in number:
        result += read_single_digit(digit) + " "
    return result.strip()

number = input("세 자리 정수 입력: ")
print(read_number(number))
