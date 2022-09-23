import sys

if __name__ == "__main__":

    numberslist = sys.argv[1:]

    def even_numbers(numberslist):
        i = 0
        for number in numberslist:
            if ( (int(number) % 2) == 0):
                i += 1
        return i

#    print(even_numbers(numberslist))

    def decorator(even_numbers):
        evens = even_numbers(numberslist)
        if   evens == 0:
            print("Нету(")
            sys.exit(1)
        elif evens >= 10:
            print("Многа!")
            sys.exit(1)

        return evens

    print(decorator(even_numbers))
