import math

BASE = int(input("Enter base you want to convert to: "))

def to_normal(number):
    if (number):
        output = 0
        for i in range(len(number) - 1, -1, -1):
            output += BASE ** (len(number) - i - 1) * int(str(number[i]))
        print("Base 10:", output)

def to_base(number_str, base=BASE):
    number = int(number_str)
    if number == 0:
        return [0]
    thedigits = []
    while number:
          thedigits.append(int(number % base))
          number = math.floor(number/base)
    return thedigits[::-1]

def main():
    print(f"\033[1;31;40mBase {BASE} Convertor\033[0m")
    while True:
        number = input("Input the number: ")
        print(to_base(number))
        # to_normal(number)
        print("\033[92m--------\033[0m")

main()
