import sys
import argparse

def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--petal-numbers', nargs = '+', dest = "petal")
    parser.add_argument('-s', '--divination-start', choices = ['любит', 'не любит'], default = ['любит'], dest = "start")

    return parser


if __name__ == '__main__':
    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:])

    sum_of_petals = 0
    for petal in namespace.petal:
        sum_of_petals += int(petal)

    if (sum_of_petals % 2) == 0:
        if namespace.start == "любит":
            print("не любит")
        else:
            print("любит")
    else:
        if namespace.start == "любит":
            print("любит")
        else:
            print("не любит")






