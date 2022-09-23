import sys
import math
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('N')

    return parser

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    N = int(namespace.N)
    sqrt = math.sqrt(5)
    result = (1 / sqrt) * ( pow((1 + sqrt)/ 2, N) - pow((1 - sqrt)/ 2, N) )
    print(round(result))
