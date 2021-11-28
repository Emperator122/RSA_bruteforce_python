from libs.p_q_bruteforce.fermat_factorization import FermatFactorization, PQBruteforceMethod
from libs.rsa.rsa_decoder import RSADecrypter
from libs.misc.gcd import gcd_extended
from libs.misc.euler_function import simple_p_q
from libs.misc.simple_linear_debug_log import Log as Logger

DEFAULT_P_Q_BRUTEFORCE_METHOD = FermatFactorization
Log = Logger()


class RSABruteforce:
    def __init__(self, n, e, bruteforce_method: PQBruteforceMethod = None):
        self.n = n
        self.e = e
        self.bruteforce_method = bruteforce_method \
            if bruteforce_method is not None else DEFAULT_P_Q_BRUTEFORCE_METHOD(n)

    def bruteforce(self, encrypted_chunked_message: list) -> list:
        Log.track_time('Getting p and q')
        (p, q, iter_count) = self.bruteforce_method.brutefroce()
        assert p * q == self.n, 'p q bruteforce error: pq != n'
        Log.log_timed('SUCCESS: p=%s, q=%s, iteration=%s' % (p, q, iter_count))

        phi = simple_p_q(p, q)

        Log.track_time('Getting private key using gcd_extended')
        (_, d, _) = gcd_extended(self.e, phi)
        while d < 0:  # d have to be > 0
            d += phi
        Log.log_timed('SUCCESS: d=%s' % d)

        Log.track_time('Decoding')
        decrypter = RSADecrypter(d, self.n)
        decrypted_message = decrypter.decrypt(encrypted_chunked_message)
        Log.log_timed('SUCCESS: message=%s' % decrypted_message)

        return decrypted_message
