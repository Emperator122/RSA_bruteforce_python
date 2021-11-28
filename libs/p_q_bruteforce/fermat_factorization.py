from libs.p_q_bruteforce.p_q_brutefroce_method import PQBruteforceMethod
import math


class FermatFactorization(PQBruteforceMethod):
    def __init__(self, n):
        super().__init__(n)

    def brutefroce(self) -> (int, int, int):
        n = self.n
        n_sqrt = math.isqrt(n)
        y = n_sqrt * n_sqrt - n
        if y < 0:
            n_sqrt += 1
            y = n_sqrt * n_sqrt - n
        s = n_sqrt
        k = 0
        while True:
            y_sqrt = math.isqrt(y)
            if y_sqrt * y_sqrt == y:
                return int(n_sqrt + k + y_sqrt), int(n_sqrt + k - y_sqrt), k
            y += 2 * s + 1
            s += 1
            k += 1
