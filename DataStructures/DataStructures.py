import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from sympy import *
from sympy.utilities.lambdify import lambdify


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


class Wahrscheinlichkeitsverteilung:

    def __init__(self, vals, weights):
        self.vals = np.asarray(vals)
        self.weights = np.asarray(weights)

    def erwartungswert(self, vals=None):
        if vals is None:
            return self.vals @ np.transpose(self.weights)
        return vals @ np.transpose(self.weights)

    def nutzenerwartungswert(self, func):
        u_vals = np.asarray([func(val) for val in self.vals])
        return self.erwartungswert(u_vals)

    def sicherheitsäquvivalent(self, func):
        u_mean = self.nutzenerwartungswert(func)
        root_func = lambda x: func(x) - u_mean
        sae = fsolve(root_func, 0)
        return sae[0]

    def risikoprämie(self, func):
        return self.erwartungswert() - self.sicherheitsäquvivalent(func)

    def plot_erwartungswert_nutzenfunktion(self, func, min, max, steps=11):
        f, ax = plt.subplots(1)

        # plot u(x)
        xs = np.linspace(min, max, 101)
        ys = [func(x) for x in xs]
        ax.plot(xs, ys)

        # plot mean
        mean_ys = np.linspace(0, func(self.erwartungswert()), 101)
        ax.plot([self.erwartungswert() for _ in range(101)], mean_ys, label='E(x)')

        # plot sicherheitsäquvivalent
        mean_ys = np.linspace(0, func(self.sicherheitsäquvivalent(func)), 101)
        ax.plot([self.sicherheitsäquvivalent(func) for _ in range(101)], mean_ys, label='SÄ')

        # plot E(u(x))
        mean_xs = np.linspace(0, self.sicherheitsäquvivalent(func), 101)
        ax.plot(mean_xs, [func(self.sicherheitsäquvivalent(func)) for _ in range(101)], label='E(u(x))')

        plt.xticks(np.linspace(min, max, steps))
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=min)
        plt.grid()
        plt.legend()
        plt.show()


class Aktie:
    def __init__(self, rendite, volatilitaet):
        self.mean = rendite
        self.std = volatilitaet


class Portfolio:

    def __init__(self, aktien, anteile, korrelation):
        self.aktien = aktien
        self.weights = anteile
        self.korrelation = korrelation

    def portfolio_rendite(self):
        renditen = np.asarray([akt.mean for akt in self.aktien])
        return renditen @ np.transpose(np.asarray(self.weights))

    def portfolio_volatilitaet(self):
        if len(self.aktien) > 2:
            raise NotImplementedError("Sorry das musst du selber machen")
        return math.sqrt((self.weights[0] ** 2) * (self.aktien[0].std ** 2)
                         + (self.weights[1] ** 2) * (self.aktien[1].std ** 2)
                         + 2 * self.weights[0] * self.weights[1] * self.aktien[0].std * self.aktien[
                             1].std * self.korrelation)

    def mvp(self):
        if len(self.aktien) > 2:
            raise NotImplementedError("Sorry deine Aufgabe jetzt")
        mvp = ((self.aktien[1].std ** 2) - self.aktien[0].std * self.aktien[1].std * self.korrelation) / (
                (self.aktien[0].std ** 2) + (self.aktien[1].std ** 2) - 2 * self.aktien[0].std * self.aktien[
            1].std * self.korrelation)
        return mvp

    def erwartungswert_mvp(self):
        if len(self.aktien) > 2:
            raise NotImplementedError("Sorry deine Aufgabe jetzt")
        xa = self.mvp()
        return xa * self.aktien[0].mean + (1. - xa) * self.aktien[1].mean

    def volatilität_mvp(self):
        if len(self.aktien) > 2:
            raise NotImplementedError("Sorry das musst du selber machen")
        xa = self.mvp()
        return math.sqrt((xa ** 2) * (self.aktien[0].std ** 2)
                         + ((1. - xa) ** 2) * (self.aktien[1].std ** 2)
                         + 2 * xa * (1. - xa) * self.aktien[0].std * self.aktien[
                             1].std * self.korrelation)


def korrelationskoeffizient(z1, z2):
    return np.corrcoef(z1, z2)[0, 1]


def ara(func, symbol='x'):
    x = Symbol(symbol)
    func_prime = diff(func, x)
    func_prime_prime = diff(func_prime, x)
    return -func_prime_prime / func_prime


def rra(func, symbol='x'):
    ara_ = ara(func, symbol)
    rra = lambda x: lambdify(Symbol(symbol), ara_)(x) * x
    return rra


def plot_ara(func1, func2, min, max, symbol1='x', symbol2='x', steps=11):
    ara1 = ara(func1)
    ara1 = lambdify(Symbol(symbol1), ara1)
    ara2 = ara(func2)
    ara2 = lambdify(Symbol(symbol2), ara2)

    f, ax = plt.subplots(1)

    # plot ara1(x)
    xs = np.linspace(min, max, 101)
    ys = [ara1(x) for x in xs]
    ax.plot(xs, ys, label='ara1')

    # plot ara2(x)
    xs = np.linspace(min, max, 101)
    ys = [ara2(x) for x in xs]
    ax.plot(xs, ys, label='ara2')

    plt.xticks(np.linspace(min, max, steps))
    ax.set_ylim(ymin=0, ymax=1)
    ax.set_xlim(xmin=min)
    plt.grid()
    plt.legend()
    plt.show()


def plot_fsd(func1, func2, min, max, symbol1='x', symbol2='x'):
    start = Float('-inf')
    start = -1
    x1 = Symbol(symbol1)
    x2 = Symbol(symbol2)
    xs = np.linspace(min, max, 51)

    f, ax = plt.subplots(1)

    print(integrate(func1, x1))
    func1 = lambdify(x1, integrate(func1, x1))
    func2 = lambdify(x2, integrate(func2, x2))
    y_func1 = [func1(x) for x in xs]
    y_func2 = [func2(x) for x in xs]

    ax.plot(xs, y_func1, label='func1')
    ax.plot(xs, y_func2, label='func2')

    ax.set_ylim(ymin=0, ymax=1)
    ax.set_xlim(xmin=min)
    plt.grid()
    plt.legend()
    plt.show()


def normal_dist_func(mean, var):
    return '(1/sqrt(2*3.14159265359*{}))*e**(-((x-{})**2)/(2{}))'.format(var, mean, var)

class Produkt:

    def __init__(self, name, kosten, max_absatz=0, ):
        pass

