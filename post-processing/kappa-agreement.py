#!/usr/bin/env python3

from sklearn.metrics import cohen_kappa_score

# '1' means that the fuzzer was the (equal) best, '0' otherwise

cov = [
    0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, # bloaty
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, # curl
    0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, # freetype2
    1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, # harfbuzz
    1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, # jsoncpp
    0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, # lcms
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # libjpeg-turbo
    1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, # libpng
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, # mbedtls
    0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, # openssl
    0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, # openthread
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, # php
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, # proj4
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # re2
    0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, # sqlite3
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, # systemd
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # vorbis
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # woff2
    0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, # zlib
]

auc = [
    1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, # bloaty
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, # curl
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, # freetype2
    1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, # harfbuzz
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, # jsoncpp
    0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, # lcms
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # libjpeg-turbo
    1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, # libpng
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, # mbedtls
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, # openssl
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, # openthread
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, # php
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # proj4
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, # re2
    0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, # sqlite3
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, # systemd
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, # vorbis
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, # woff2
    1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, # zlib
]

kappa = cohen_kappa_score(cov, auc)
print(f'kappa = {kappa:.2f}')