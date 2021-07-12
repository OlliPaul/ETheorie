from DataStructures import Entscheidungsmodell
import numpy as np


class AdditiveModel(Entscheidungsmodell):

    def __init__(self, alts, weights):
        super(AdditiveModel, self).__init__("Additive Model", alts)
        self.weights = weights

    def __call__(self, *args, **kwargs):
        best_alt_ind = 0
        best_alt_val = -9999999999

        for alt_ind, alt in enumerate(self.alts):
            cur_val = 0

            for ind, weight in enumerate(self.weights):
                cur_val += alt.get(ind) * weight

            if cur_val == best_alt_val:
                print("Maybe here´s a problem look further into it")
                print("{} and {} are equally good".format(self.alts[best_alt_ind], self.alts[alt_ind]))
            if cur_val > best_alt_val:
                best_alt_ind = alt_ind
                best_alt_val = cur_val
        return self.alts[best_alt_ind], best_alt_val


class EasyAHP(Entscheidungsmodell):

    def __init__(self, alts, weight_matrix):
        super(EasyAHP, self).__init__("Vereinfachte AHP", alts)
        weights = self.calc_weights(weight_matrix)
        self.add_model = AdditiveModel(alts, weights)

    def __call__(self, *args, **kwargs):
        return self.add_model()

    def calc_weights(self, weight_matrix):
        sum_rows = np.sum(np.asarray(weight_matrix), axis=1)
        sum_all = np.sum(sum_rows, axis=0)
        weights = np.around(sum_rows / sum_all, 2)
        return list(weights)


class Koerth(Entscheidungsmodell):

    def __init__(self, alts):
        super(Koerth, self).__init__("Körth", alts)
        alt_mat = np.asarray([alt.env_status for alt in alts])
        col_max = np.max(alt_mat, axis=0)
        self.col_max = col_max

    def __call__(self, *args, **kwargs):
        div_mat = []
        for alt in self.alts:
            alt_vals_normed = []
            for ind, val in enumerate(alt.env_status):
                alt_vals_normed.append(val / self.col_max[ind])
            div_mat.append(alt_vals_normed)
        div_mat = np.min(div_mat, axis=1)
        return self.alts[np.argmax(div_mat)], np.max(div_mat)


class MaxiMin(Entscheidungsmodell):

    def __init__(self, alts):
        super(MaxiMin, self).__init__("MaxiMin", alts)

    def __call__(self, *args, **kwargs):
        div_mat = [alt.env_status for alt in self.alts]
        div_mat = np.min(div_mat, axis=1)
        return self.alts[np.argmax(div_mat)], np.max(div_mat)


class MaxiMax(Entscheidungsmodell):

    def __init__(self, alts):
        super(MaxiMax, self).__init__("MaxiMax", alts)

    def __call__(self, *args, **kwargs):
        div_mat = [alt.env_status for alt in self.alts]
        div_mat = np.max(div_mat, axis=1)
        return self.alts[np.argmax(div_mat)], np.max(div_mat)


class Hurwicz(Entscheidungsmodell):

    def __init__(self, alts, alpha):
        super(Hurwicz, self).__init__("Hurwicz", alts)
        self.mins = np.asarray([np.min(np.asarray(alt.env_status)) for alt in alts])
        self.maxs = np.asarray([np.max(np.asarray(alt.env_status)) for alt in alts])
        self.alpha = alpha

    def __call__(self, *args, **kwargs):
        weighted_min_max = self.alpha * self.maxs + (1 - self.alpha) * self.mins
        return self.alts[np.argmax(weighted_min_max)], np.max(weighted_min_max)


class Laplace(Entscheidungsmodell):

    def __init__(self, alts):
        super(Laplace, self).__init__("Laplace", alts)
        div_mat = np.asarray([alt.env_status for alt in alts])
        self.div_mat = div_mat / alts[0].len()

    def __call__(self, *args, **kwargs):
        div_mat = np.sum(self.div_mat, axis=1)
        return self.alts[np.argmax(div_mat)], np.max(div_mat)

class NiehansSavage(Entscheidungsmodell):

    def __init__(self, alts):
        super(NiehansSavage, self).__init__("Niehans-Savage", alts)
        self.alt_mat = np.asarray([alt.env_status for alt in alts])
        self.col_max = np.max(self.alt_mat, axis=0)

    def __call__(self, *args, **kwargs):
        alt_mat = np.abs(np.subtract(self.alt_mat, self.col_max))
        alt_mat = np.max(alt_mat, axis=1)
        return self.alts[np.argmin(alt_mat)], np.min(alt_mat)


