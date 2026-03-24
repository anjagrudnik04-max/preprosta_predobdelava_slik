from uvod_opencv import *
import cv2 as cv
import numpy as np

slika = cv.imread("slika.jpg")
slika = slika.astype(np.float32) / 255

print("Original dimenzije:", slika.shape)

povecana = povecaj_za_faktor_2(slika)
print("Povecana:", povecana.shape)

zmanjsana = zmanjsaj_za_faktor_2(slika)
print("Zmanjsana:", zmanjsana.shape)

podslike = razrezi_sliko(slika, 100, 100)
print("Stevilo podslik:", len(podslike))

stevilo = prestej_piksle_z_barvo(slika, (0,0,0), (1,1,1))
print("Piksli v območju:", stevilo)

zrcaljena = zrcali_sliko_vertikalno(slika, "ZL")
print("Zrcaljenje uspešno:", zrcaljena.shape)

print("Vse funkcije delujejo brez crasha")
