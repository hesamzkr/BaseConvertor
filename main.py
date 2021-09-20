BASE = 7


def to_normal(number):
    if (number):
        output = 0
        for i in range(len(number) - 1, -1, -1):
            output += BASE ** (len(number) - i - 1) * int(str(number[i]))
        print("Base10:", output)


def to_base(number_str):
    if (number_str):
        output = []
        number = int(number_str)
        n = number / BASE
        while n >= 1:
            x = n % 1
            output.append(x * BASE)
            n = int(n) / BASE
        
        x = n % 1
        output.append(x * BASE)

        print(f"\033[92m--------\033[0m\n{' '.join(str(round(e)) for e in output)[::-1]}")


def main():
    print(f"\033[96mBase {BASE} Convertor\033[0m")
    while True:
        number = input("Number: ")
        to_base(number)
        # to_normal(number)
        print("\033[92m--------\033[0m")

main()