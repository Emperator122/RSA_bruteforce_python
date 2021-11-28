from abc import ABC, abstractmethod


class PQBruteforceMethod(ABC):
    def __init__(self, n):
        self.n = n

    @abstractmethod
    def brutefroce(self) -> (int, int, int):  # p, q, iterations count
        pass
