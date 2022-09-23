import sys
import math

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].isnumeric():
            N = int(sys.argv[1])
            sqrt = math.sqrt(5)
            result = (1 / sqrt) * ( pow((1 + sqrt)/ 2, N) - pow((1 - sqrt)/ 2, N) )
            print(round(result))
        else:
            print("Error: the argument should be integer!")
            sys.exit(1)
    else:
        if len(sys.argv) > 2:
            print("Error: You need to put only one numeral argument (int)!");
            sys.exit(1)
        if len(sys.argv) < 2:
            print("Error: numeral argument (int) is needed!")
            sys.exit(1)
