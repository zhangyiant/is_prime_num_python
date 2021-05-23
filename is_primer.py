def is_primer(num):
    result = True
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
    return result

def main():
    for i in range(2, 101):
        if is_primer(i):
            print(i)
    return


if __name__ == '__main__':
    main()
