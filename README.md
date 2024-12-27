# ReManga (Manga Processing Web App)

## English

### Description
This project is a web application designed for manga processing. Users can upload manga images and perform operations like colorization, translation, or both. The processed results can then be downloaded in a ZIP file.

### Features
- **Colorize**: Add color to black-and-white manga pages.
- **Translate**: Translate manga text to another language.
- **Combine**: Perform both operations simultaneously.
- User-friendly interface with clear buttons and status indicators.
- Automatic download of processed results.

### How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/manga-processing-webapp.git
   cd manga-processing-webapp
   ```
2. Install the necessary dependencies:
   ```bash
   pip3 install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 flask==3.1.0 
   ```
3. Start the server:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000`.

### Directory Structure
```
manga-processing-webapp/
├── static/
│   ├── wallpaper.jpg
├── templates/
│   ├── index.html
├── app.py
├── requirements.txt
└── README.md
```

---

## Türkçe

### Açıklama
Bu proje, manga işlemleri için tasarlanmış bir web uygulamasıdır. Kullanıcılar manga görsellerini yükleyebilir ve renklendirme, çeviri veya her iki işlemi birden gerçekleştirebilir. İşlem sonrası sonuçlar bir ZIP dosyası olarak indirilebilir.

### Özellikler
- **Renklendirme**: Siyah-beyaz manga sayfalarına renk ekleyin.
- **Çeviri**: Manga metinlerini başka bir dile çevirin.
- **Birleştirme**: Her iki işlemi aynı anda gerçekleştirin.
- Kullanıcı dostu arayüz ile kolay kullanım.
- İşlem sonuçlarının otomatik indirilmesi.

### Çalıştırma Talimatları
1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/yourusername/manga-processing-webapp.git
   cd manga-processing-webapp
   ```
2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip3 install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 flask==3.1.0 
   ```
3. Sunucuyu başlatın:
   ```bash
   python app.py
   ```
4. Web tarayıcınızı açın ve `http://127.0.0.1:5000` adresine gidin.

### Dizin Yapısı
```
manga-processing-webapp/
├── static/
│   ├── wallpaper.jpg
├── templates/
│   ├── index.html
├── app.py
├── requirements.txt
└── README.md
```
