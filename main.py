from simple_lama_inpainting import SimpleLama
import deepl
from tqdm import tqdm
import numpy as np
import textwrap3
from paddleocr import PaddleOCR
import cv2
from colorizator import MangaColorizator
import os
from PIL import ImageFont, ImageDraw, Image
 
def yakın_kelimeleri_bul(kordinatlar):

    sonuclar = []
    a = []
    thres = 65
    while len(kordinatlar) >= 1:
        a.append(kordinatlar[0])
        for i in kordinatlar[1:]:
            if (a[-1][0] - thres <= i[0] and a[-1][0] + thres >= i[0]) and a[-1][1] + thres > i[1]:
                a.append(i)
                kordinatlar.remove(i)
        sonuclar.append(a)
        kordinatlar.pop(0)
        a = []

    return sonuclar

def orta_nokta_bul(koordinatlar):

    x_toplam = sum(x for x, y in koordinatlar)
    y_toplam = sum(y for x, y in koordinatlar)
    ortalama_x = x_toplam / len(koordinatlar)
    ortalama_y = y_toplam / len(koordinatlar)

    return (ortalama_x, ortalama_y)

def indexleri_bul(dizi1, dizi2):

    indeksler = []
    for elemanlar in dizi2:
        eleman_indeksleri = []
        for eleman in elemanlar:
            if eleman in dizi1:
                eleman_indeksleri.append(dizi1.index(eleman))
        indeksler.append(eleman_indeksleri)

    return indeksler

def verileri_düzelt(dizi):
    duzeltilmis_elemanlar = []
    i = 0
    while i < len(dizi):

        eleman = dizi[i]
        if '-' in eleman:
            parcalar = eleman.split('-')

            if i + 1 < len(dizi):
                duzeltilmis_eleman = (parcalar[0] + dizi[i+1]).strip()
                i += 1  
            else:
                duzeltilmis_eleman = parcalar[0].strip()
        else:
            duzeltilmis_eleman = eleman

        duzeltilmis_elemanlar.append(duzeltilmis_eleman)
        i += 1 
    birlesik_string = ' '.join([eleman.lower() for eleman in duzeltilmis_elemanlar])

    return birlesik_string

def translators(text, translator):
 
    output = str(translator.translate_text(text, target_lang="TR"))
    return output

def img_mask(dizi, dizi2, resim_verisi):
    
    file_bytes = np.frombuffer(resim_verisi, np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    height, width, _ = img.shape
    img = np.zeros((height, width, 1), dtype=np.uint8)

    for eleman in dizi:

        all_x = [point[0] for sublist in eleman for point in sublist]
        all_y = [point[1] for sublist in eleman for point in sublist]
        x1, y1 = max(all_x), max(all_y)
        x2, y2 = min(all_x), min(all_y)

        img = cv2.rectangle(img, (int(x1+7), int(y1+7)), (int(x2-7), int(y2-7)), (255, 255, 255), thickness=cv2.FILLED)

    return img
    
def beyaz_kare_olustur(dizi, dizi2, resim_verisi, simple_lama):
    
    file_bytes = np.frombuffer(resim_verisi, np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    mask = img_mask(dizi, dizi2, resim_verisi)
    
    img = simple_lama(img, mask)
    değişken = 0
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Arial.ttf", 16)
    for eleman in dizi:

        all_x = [point[0] for sublist in eleman for point in sublist]
        all_y = [point[1] for sublist in eleman for point in sublist]
        x1, y1 = max(all_x), max(all_y)
        x2, y2 = min(all_x), min(all_y)

        wrapped_text = textwrap3.wrap(dizi2[değişken], width=20)
        for i, line in enumerate(wrapped_text):
            y = int((y1 + y2) / 2) + i * 20
            x = int((x1 + x2 - int(draw.textlength(line, font=font))) / 2)
            draw.text((x,y-20), line, fill=(0,0,0), font=font)
        değişken += 1

    img = np.array(img)
    return img

def unicod_textwrap(metin):
    satirlar = []
    satir = ""
    genislik = 15
    kelime_listesi = metin.split()
    
    for kelime in kelime_listesi:
        if len(satir) + len(kelime) <= genislik:
            satir += kelime + " "
        else:
            satirlar.append(satir.strip())
            satir = kelime + " "
    
    if satir:
        satirlar.append(satir.strip())
    
    return satirlar

def main(in_memory_files, operation):
    results = {}
    api = "da952e5e-99f3-49be-b09f-a4c897d561b7:fx" 

    for resim_adı, resim_verisi in tqdm(in_memory_files.items(), desc="İşleniyor", unit="resim"):
        # Resmi bellekte işle
        file_bytes = np.frombuffer(resim_verisi, np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

        # Orijinal dosya uzantısını belirle
        file_extension = resim_adı.split('.')[-1].lower()

        if operation == "translate":
            simple_lama = SimpleLama()
            translator = deepl.Translator(api)
            reader = PaddleOCR(lang='en')

            img[img >= 150] = 255

            dizi = reader.ocr(img)
            dizi = [item for sublist in dizi if sublist is not None for item in sublist]

            if len(dizi) > 1:
                kordinatlar = [orta_nokta_bul(i[0]) for i in dizi]
                kordinatlar_ = kordinatlar.copy()

                sonuclar = yakın_kelimeleri_bul(kordinatlar)
                indexler = indexleri_bul(kordinatlar_, sonuclar)

                kordinatlar = []
                konuşma_dizisi = []

                for i in indexler:
                    kordinatlar_ = []
                    string = []

                    for a in i:
                        kordinatlar_.append(dizi[a][0])
                        string.append(str(dizi[a][1][0]))

                    kordinatlar.append(kordinatlar_)
                    konuşma_dizisi.append(translators(verileri_düzelt(string), translator))

                resim = beyaz_kare_olustur(kordinatlar, konuşma_dizisi, resim_verisi, simple_lama)

                _, encoded_img = cv2.imencode(f'.{file_extension}', resim)
                results[resim_adı] = encoded_img.tobytes()

        elif operation == "colorize":
            colorizator = MangaColorizator("cpu", 'networks/generator.zip', 'networks/extractor.pth')

            if img.shape[1] % 32 != 0:
                width = 32 * (img.shape[1] // 32)
            else:
                width = img.shape[1]
            colorizator.set_image(img, width, True, 25)
            img = colorizator.colorize()
            img *= 255
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            _, encoded_img = cv2.imencode(f'.{file_extension}', img)
            results[resim_adı] = encoded_img.tobytes()

        elif operation == "both":
            simple_lama = SimpleLama()
            translator = deepl.Translator(api)
            colorizator = MangaColorizator("cpu", 'networks/generator.zip', 'networks/extractor.pth')
            reader = PaddleOCR(lang='en')

            img[img >= 150] = 255

            dizi = reader.ocr(img)
            dizi = [item for sublist in dizi if sublist is not None for item in sublist]

            if len(dizi) > 1:
                kordinatlar = [orta_nokta_bul(i[0]) for i in dizi]
                kordinatlar_ = kordinatlar.copy()

                sonuclar = yakın_kelimeleri_bul(kordinatlar)
                indexler = indexleri_bul(kordinatlar_, sonuclar)

                kordinatlar = []
                konuşma_dizisi = []

                for i in indexler:
                    kordinatlar_ = []
                    string = []

                    for a in i:
                        kordinatlar_.append(dizi[a][0])
                        string.append(str(dizi[a][1][0]))

                    kordinatlar.append(kordinatlar_)
                    konuşma_dizisi.append(translators(verileri_düzelt(string), translator))

                resim = beyaz_kare_olustur(kordinatlar, konuşma_dizisi, resim_verisi, simple_lama)

                if resim.shape[1] % 32 != 0:
                    width = 32 * (resim.shape[1] // 32)
                else:
                    width = resim.shape[1]

                colorizator.set_image(resim, width, True, 25)
                resim = colorizator.colorize()
                resim *= 255
                resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

                _, encoded_img = cv2.imencode(f'.{file_extension}', resim)
                results[resim_adı] = encoded_img.tobytes()

    return results

