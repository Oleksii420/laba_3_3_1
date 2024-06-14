from FigureReader import FigureReader

def is_not_complex(a):
    if isinstance(a, complex):
        return False
    else:
        return True

def finalResult(a_file):
    reader = FigureReader(a_file)
    figures = reader.read()
    maxVolume = 0
    maxFigure = figures[0]
    for figure in figures:
        try:
            if is_not_complex(figure.volume()) and figure.volume() > maxVolume:
                maxVolume = figure.volume()
                maxFigure = figure
        except (AttributeError, TypeError):
            continue

    print("Фігура", maxFigure, "найбільша міра =", maxVolume)







if __name__ == "__main__":
    for file in ["input01.txt", "input02.txt", "input03.txt"]:
        finalResult(file)

