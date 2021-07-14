import numpy as np

from DataStructures import *
from Entscheidungsmodelle import *

alts = [Alternative("Wohnung 1", [4, 6, 8, 5]),
        Alternative("Wohnung 2", [9, 3, 6, 4]),
        Alternative("Wohnung 3", [2, 9, 6, 7])]
additive_model = AdditivesModel(alts, [0.1, 0.2, 0.3, 0.4])
# print(additive_model())

ahp = EinfacheAHP(alts, np.asarray([[1, 4, 2, 6],
                                    [0.25, 1, 0.5, 2],
                                    [0.5, 2, 1, 4],
                                    [1/6, 0.5, 0.25, 1]]))
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

# prob_dist = ProbabilityDistribution([64, 25], [0.4, 0.6])
# print(prob_dist.mean())
# print(prob_dist.mean_u_func(lambda x: x ** 0.5 + 8))
# print(prob_dist.security_equvivalent(lambda x: x ** 0.5 + 8))
# print(prob_dist.risk_bonus(lambda x: x ** 0.5 + 8))
# prob_dist.plot_mean_u_func(lambda x: x ** 0.5 + 8, 0, 50)
# prob_dist.plot_mean_u_func(lambda x: x ** 0.5 + 8, 30, 45)

# print(correlation_coefficient([2, 4, 6, 3, 0, -3, -6, 0, 20, 40], [30, 60, 90, 45, 0, -45, -90, 0, 300, 600]))

#aktien = [Aktie(0.06, 0.1), Aktie(0.12, 0.15)]
#port = Portfolio(aktien, [0.3, 0.7], 0.2)
#print(port.portfolio_rendite())
#print(port.portfolio_volatilitaet())
#print(port.mvp())
#print(port.mean_mvp())
#print(port.std_mvp())

#print(ara('x**0.5+8'))
#plot_ara('x**0.5+8', 'x**0.1+4', 0, 100)
#print(rra('x**0.5+8'))

#plot_fsd(normal_dist_func(0.16, 0.2**2), normal_dist_func(0.04, 0.2**2), -0.8, 1)

print(foobar("-e**(-2.5*w)", 'w', [normal_dist_func(0.1, 0.2**2)], "0.02", "x"))