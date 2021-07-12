import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

class Alternative:

    def __init__(self, name, env_status):
        self.name = name
        self.env_status = env_status

    def len(self):
        return len(self.env_status)

    def get(self, i):
        return self.env_status[i]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{} {}".format(self.name, self.env_status)


class Entscheidungsmodell:

    def __init__(self, name, alternatives):
        self.name = name
        self.alts = alternatives

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Implementier es doch selber")


class ProbabilityDistribution:

    def __init__(self, vals, weights):
        self.vals = np.asarray(vals)
        self.weights = np.asarray(weights)

    def mean(self, vals=None):
        if vals is None:
            return self.vals @ np.transpose(self.weights)
        return vals @ np.transpose(self.weights)

    def mean_u_func(self, func):
        u_vals = np.asarray([func(val) for val in self.vals])
        return self.mean(u_vals)

    def security_equvivalent(self, func):
        u_mean = self.mean_u_func(func)
        root_func = lambda x: func(x) - u_mean
        sae = fsolve(root_func, 0)
        return sae[0]

    def risk_bonus(self, func):
        return self.mean() - self.security_equvivalent(func)

    def plot_mean_u_func(self, func, min, max, steps=11):
        f, ax = plt.subplots(1)

        # plot u(x)
        xs = np.linspace(min, max, 101)
        ys = [func(x) for x in xs]
        ax.plot(xs, ys)

        # plot mean
        mean_ys = np.linspace(0,func(self.mean()), 101)
        ax.plot([self.mean() for _ in range(101)], mean_ys, label='E(x)')

        # plot sicherheitsäquvivalent
        mean_ys = np.linspace(0, func(self.security_equvivalent(func)), 101)
        ax.plot([self.security_equvivalent(func) for _ in range(101)], mean_ys, label='SÄ')

        # plot E(u(x))
        mean_xs = np.linspace(0, self.security_equvivalent(func), 101)
        ax.plot(mean_xs, [func(self.security_equvivalent(func)) for _ in range(101)], label='E(u(x))')

        plt.xticks(np.linspace(min, max, steps))
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=min)
        plt.grid()
        plt.legend()
        plt.show()
