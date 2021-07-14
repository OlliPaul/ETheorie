from DataStructures.DataStructures import *


def main():
    u_func = lambda x: x ** 0.5 + 8

    wahrscheinlichkeitsverteilung = Wahrscheinlichkeitsverteilung([64, 25], [0.4, 0.6])
    print(wahrscheinlichkeitsverteilung.erwartungswert())
    print(wahrscheinlichkeitsverteilung.nutzenerwartungswert(u_func))
    print(wahrscheinlichkeitsverteilung.sicherheitsäquvivalent(u_func))
    print(wahrscheinlichkeitsverteilung.risikoprämie(u_func))
    wahrscheinlichkeitsverteilung.plot_erwartungswert_nutzenfunktion(u_func, 0, 50)
    wahrscheinlichkeitsverteilung.plot_erwartungswert_nutzenfunktion(u_func, 30, 45)

    print(korrelationskoeffizient([2, 4, 6, 3, 0, -3, -6, 0, 20, 40],
                                  [30, 60, 90, 45, 0, -45, -90, 0, 300, 600]))

    aktien = [Aktie(0.06, 0.1),
              Aktie(0.12, 0.15)]
    portfolio = Portfolio(aktien, [0.3, 0.7], 0.2)

    print(portfolio.portfolio_rendite())
    print(portfolio.portfolio_volatilitaet())
    print(portfolio.mvp())
    print(portfolio.erwartungswert_mvp())
    print(portfolio.volatilität_mvp())

    u_func = "x**0.5+8"
    other_func = "x**0.1+4"
    print(ara(u_func))
    plot_ara(u_func, other_func, 0, 100)
    print(rra(u_func))


if __name__ == "__main__":
    main()
