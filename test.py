from uvod_opencv import *
import cv2 as cv
import numpy as np

# naloži sliko
slika = cv.imread("slika.jpg")

# normalizacija kot v navodilih
slika = slika.astype(np.float32) / 255


print("Original dimenzije:", slika.shape)

# test povečave
povecana = povecaj_za_faktor_2(slika)
print("Povecana:", povecana.shape)

# test zmanjšanja
zmanjsana = zmanjsaj_za_faktor_2(slika)
print("Zmanjsana:", zmanjsana.shape)

# test razreza
podslike = razrezi_sliko(slika, 100, 100)
print("Stevilo podslik:", len(podslike))

# test barvnega filtra
stevilo = prestej_piksle_z_barvo(slika, (0,0,0), (1,1,1))
print("Piksli v območju:", stevilo)

# test zrcaljenja
zrcaljena = zrcali_sliko_vertikalno(slika, "ZL")
print("Zrcaljenje uspešno:", zrcaljena.shape)

print("Vse funkcije delujejo brez crasha")
