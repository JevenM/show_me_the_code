import random, string


forSelect = string.ascii_letters + string.digits
def generate(count, length):
    for i in range(count):
        str = [random.choice(forSelect) for i in range(length)]
        print("".join(str))
        with open('generateCode.txt', 'a') as f:
            f.write("".join(str) + '\n')
            f.close()


if __name__ == "__main__":
    generate(200, 8)

