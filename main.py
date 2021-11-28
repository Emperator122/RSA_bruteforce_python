from libs.rsa.rsa_bruteforce import RSABruteforce


# data input
n = 677589755606669856748917594751895987582327041933285274616037
e = 5
encrypted_message = [1482983448278432, 1510598768350176, 1531578985264449, 1538623954900000, 1449033801989157,
                     1524559844999168, 33554432, 1462538217461399, 1415708784197632, 1524559844999168, 1632591617145743]

# code
rsa_bruteforce = RSABruteforce(n, e)
decrypted_message = rsa_bruteforce.bruteforce(encrypted_message)
print('Decrypted message')
print(list(map(lambda ch: chr(ch), decrypted_message)))
