from DataStructures.Entscheidungsmodelle import *
from DataStructures.DataStructures import *

def main():
    alts = [Alternative("Wohnung 1", [4, 6, 8, 5]),
            Alternative("Wohnung 2", [9, 3, 6, 4]),
            Alternative("Wohnung 3", [2, 9, 6, 7])]



    additive_model = AdditivesModel(alts, [0.1, 0.2, 0.3, 0.4])
    ahp = EinfacheAHP(alts, np.asarray([[1, 4, 2, 6],
                                        [0.25, 1, 0.5, 2],
                                        [0.5, 2, 1, 4],
                                        [1 / 6, 0.5, 0.25, 1]]))
    koerth = Koerth(alts)

    print(ahp())
    print(additive_model())
    print(koerth())

if __name__ == "__main__":
    main()