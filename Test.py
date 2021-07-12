import numpy as np

from DataStructures import Alternative, ProbabilityDistribution
from Entscheidungsmodelle import AdditiveModel, EasyAHP, Koerth, MaxiMin, MaxiMax, Hurwicz, Laplace, NiehansSavage

alts = [Alternative("Wohnung 1", [4, 6, 8, 5]),
        Alternative("Wohnung 2", [9, 3, 6, 4]),
        Alternative("Wohnung 3", [2, 9, 6, 7])]
additive_model = AdditiveModel(alts, [0.1, 0.2, 0.3, 0.4])
# print(additive_model())

ahp = EasyAHP(alts, np.asarray([[1, 2, 3, 4],
                                [0.5, 1, 2, 3],
                                [0.33, 0.5, 1, 2],
                                [0.25, 0.33, 0.5, 1]]))
# print(ahp())

koerth = Koerth(alts)
# print(koerth())

alts = [Alternative("a1", [2000, 2500, 5000, 500]),
        Alternative("a2", [1500, 3000, -250, 8000]),
        Alternative("a3", [1400, 2500, 300, 600])]

# maximin = MaxiMin(alts)
# print(maximin())

# maximax = MaxiMax(alts)
# print(maximax())

# hurwicz = Hurwicz(alts, 0.7)
# print(hurwicz())

# laplace = Laplace(alts)
# print(laplace())

# niesav = NiehansSavage(alts)
# print(niesav())

prob_dist = ProbabilityDistribution([64, 25], [0.4, 0.6])
print(prob_dist.mean())
print(prob_dist.mean_u_func(lambda x: x ** 0.5 + 8))
print(prob_dist.security_equvivalent(lambda x: x ** 0.5 + 8))
print(prob_dist.risk_bonus(lambda x: x ** 0.5 + 8))
prob_dist.plot_mean_u_func(lambda x: x ** 0.5 + 8, 0, 50)
prob_dist.plot_mean_u_func(lambda x: x ** 0.5 + 8, 30, 45)
