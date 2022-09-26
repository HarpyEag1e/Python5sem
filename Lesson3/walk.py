import os
import sys

def walk(top: str) -> list[tuple]:

    # Проверка на то, что top - действительный путь к директории:
    if os.path.isdir(top) == False:
        print("Error: the argument is not a valid path to a directory!")
        sys.exit(1)

    # Костыль(простите): Без этих 2 строчек, если подавать на вход путь, оканчивающийся на '/',
    # то на выходе будут встречаться пути со сдвоенными '//' слэшами
    if (top[-1] == '/') and (len(top) != 1):
        top = top[:-1]

    # Будущий выход, return result
    result         = []
    # Пути до директорий той глубины, которую мы рассматриваем в данной итерации 'while ...'
    actPathsToDirs = [top]
    # Пути до директорий той глубины, которую мы будем рассматривать в следующей итерации
    nxtPathsToDirs = []

    # В них будут названия директорий и файлов, загоняемых в выводимые кортежи
    newDirs        = []
    newFiles       = []

    # Данный цикл за одну итерацию просматривает все директории, находящиеся на одной глубине
    # После самых глубоких директорий, actPathsToDirs будет равен 0
    while len(actPathsToDirs) != 0:

        for pathToDir in actPathsToDirs:
            for obj in os.listdir(pathToDir):

                pathToObj = pathToDir + '/' + obj

                if os.path.isdir (pathToObj) == True:
                     nxtPathsToDirs.append(pathToObj)
                     newDirs.append(obj)
                if os.path.isfile(pathToObj) == True:
                    newFiles.append(obj)

            # У нас всё есть для вывода информации о данной директории pathToDir
            result.append((pathToDir, newDirs, newFiles))
            # Они должны быть подготовлены до следующей итерации
            newDirs  = []
            newFiles = []

        # Следующий уровень директорий записывается в actPathsToDirs
        actPathsToDirs = nxtPathsToDirs
        nxtPathsToDirs = []

    #endwhile len(actPathsToDirs) != 0

    return result


if __name__ == "__main__":

    if len(sys.argv) == 2:
        if isinstance(sys.argv[1], str):
            for i in walk(sys.argv[1]):
                print(i)
        else:
            print("Error: the argument should be string!")
            sys.exit(1)
    else:
        if len(sys.argv) > 2:
            print("Error: you need to put only 1 argument!")
            sys.exit(1)
        if len(sys.argv) < 2:
            print("Error: path argument (str) is needed!")
            sys.exit(1)

