from math import ceil
def main():
    year = input("Введіть рік: ")
    year = int(year)

    result = ceil(year/100)

    print("Століття:",result)

if __name__ == "__main__":
    main()