from DataStructures import *
from Entscheidungsmodelle import *


def main():
    alts = [Alternative("a1", [2000, 2500, 5000, 500]),
            Alternative("a2", [1500, 3000, -250, 8000]),
            Alternative("a3", [1400, 2500, 300, 600])]
    lambda_ = 0.7

    maximin = MaxiMin(alts)
    print(maximin())

    maximax = MaxiMax(alts)
    print(maximax())

    hurwicz = Hurwicz(alts, lambda_)
    print(hurwicz())

    laplace = Laplace(alts)
    print(laplace())

    niesav = NiehansSavage(alts)
    print(niesav())


if __name__ == "__main__":
    main()
