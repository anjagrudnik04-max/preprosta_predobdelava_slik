import uvod_opencv
import cv2 as cv
import numpy as np

slika = cv.imread("slika.jpg")

if slika is None:
    print("Slika ni najdena!")
    exit()

slika = slika.astype(np.float32) / 255

povecana = uvod_opencv.povecaj_za_faktor_2(slika)
zmanjsana = uvod_opencv.zmanjsaj_za_faktor_2(slika)
podslike = uvod_opencv.razrezi_sliko(slika, 100, 100)
stevilo = uvod_opencv.prestej_piksle_z_barvo(slika, (0,0,0), (1,1,1))
zrcaljena = uvod_opencv.zrcali_sliko_vertikalno(slika, "ZL")

print("Vse funkcije delujejo brez crasha")
