import cv2 as cv
from pathlib import Path
BASE = Path(__file__).parent
UTILS = BASE / ".utils"
import numpy as np

def razrezi_sliko(slika: np.ndarray, sirina_ps: int, visina_ps: int):
    
    podSlike = []
    visina = slika.shape[0]
    sirina = slika.shape[1]

    for y in range (0, visina, visina_ps):
        for x in range (0, sirina, sirina_ps):
            podslika = slika[y:y+visina_ps, x:x+sirina_ps]
            podSlike.append(podslika)
    return podSlike  
# manjši popravek za revizijo 

def povecaj_za_faktor_2(slika: np.ndarray) -> np.ndarray:
    visina, sirina = slika.shape[:2]

    if len(slika.shape) == 3:
        nova_slika = np.zeros((visina*2, sirina*2, slika.shape[2]), dtype=slika.dtype)
    else:
        nova_slika = np.zeros((visina*2, sirina*2), dtype=slika.dtype)

    for i in range(visina):
        for j in range(sirina):

            nova_slika[2*i, 2*j] = slika[i, j]
            nova_slika[2*i+1, 2*j] = slika[i, j]
            nova_slika[2*i, 2*j+1] = slika[i, j]
            nova_slika[2*i+1, 2*j+1] = slika[i, j]

    return nova_slika    

def zmanjsaj_za_faktor_2(slika: np.ndarray) -> np.ndarray:
    visina, sirina = slika.shape[:2]

    if visina % 2 != 0:
        slika = slika[1:, :]
        visina -= 1

    if sirina % 2 != 0:
        slika = slika[:, 1:]
        sirina -= 1

    nova_visina = visina // 2
    nova_sirina = sirina // 2

    if len(slika.shape) == 3:
        nova = np.zeros((nova_visina, nova_sirina, slika.shape[2]), dtype=slika.dtype)
    else:
        nova = np.zeros((nova_visina, nova_sirina), dtype=slika.dtype)

    for i in range(nova_visina):
        for j in range(nova_sirina):

            blok = slika[2*i:2*i+2, 2*j:2*j+2]

            nova[i, j] = blok.mean(axis=(0,1))

    return nova

def prestej_piksle_z_barvo(slika: np.ndarray,
                           spodnja_meja: tuple[int,int,int],
                           zgornje_meja: tuple[int,int,int]) -> int:

    visina, sirina = slika.shape[:2]
    stevec = 0

    for i in range(visina):
        for j in range(sirina):

            piksel = slika[i, j]

            if (spodnja_meja[0] <= piksel[0] <= zgornje_meja[0] and
                spodnja_meja[1] <= piksel[1] <= zgornje_meja[1] and
                spodnja_meja[2] <= piksel[2] <= zgornje_meja[2]):

                stevec += 1

    return stevec

def zrcali_sliko_vertikalno(slika: np.ndarray, ROI: str) -> np.ndarray:

    visina, sirina = slika.shape[:2]
    pol_visine = visina // 2
    pol_sirine = sirina // 2

    nova = slika.copy()

    if ROI == "ZL":
        for i in range(pol_visine):
            for j in range(pol_sirine):
                nova[i, j] = slika[i, pol_sirine - j - 1]

    elif ROI == "ZD":
        for i in range(pol_visine):
            for j in range(pol_sirine, sirina):
                nova[i, j] = slika[i, sirina - (j - pol_sirine) - 1]

    elif ROI == "SL":
        for i in range(pol_visine, visina):
            for j in range(pol_sirine):
                nova[i, j] = slika[i, pol_sirine - j - 1]

    elif ROI == "SD":
        for i in range(pol_visine, visina):
            for j in range(pol_sirine, sirina):
                nova[i, j] = slika[i, sirina - (j - pol_sirine) - 1]

    return nova
