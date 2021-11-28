from libs.misc.module_fast_pow import sqr_power_mod


class RSADecrypter:
    d = None
    n = None

    def __init__(self, d, n):
        self.d = d
        self.n = n

    def decrypt(self, encrypted_chunked_message: list) -> list:
        return list(map(lambda el: sqr_power_mod(el, self.d, self.n), encrypted_chunked_message))
