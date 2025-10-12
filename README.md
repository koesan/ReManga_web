<div align="center">
   
# ReManga (Manga Processing Web App)

![Screenshot from 2024-12-28 05-31-22](https://github.com/user-attachments/assets/b647b75e-c3cb-480d-9837-36dd25f84e12)


## 📎 Live Demo - Canlı Demo

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Demo-yellow?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/koesan/mangaspaces)

**🇹🇷 Hugging Face üzerinde test etmek için yukarıdaki simgeye tıklayabilirsiniz.**  
**🇬🇧 You can click the icon above to test on Hugging Face.**

---

</div>

## English

### Description
This project is a web application designed for manga translation and coloring. Users can colorize manga images, translate them, or do both. The post-processing results are downloaded as a ZIP file.

### Features
- **Colorize**: Colorizes black and white manga pages.
- **Translate**: Translate manga text to another language(The project involves English-Turkish translation. Changes made in the code can also be translated into other languages.).
- **Combine**: Perform both operations simultaneously.
- User-friendly interface with clear buttons and status indicators.
- Automatic download of processed results.

### How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/koesan/ReManga_web.git
   cd ReManga_web
   ```
2. Install the necessary dependencies:
   ```bash
   pip3 install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 flask==3.1.0 
   ```
   
3. **Download Necessary Files**  
   Download [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) and place it in `networks` folder of the cloned repository.
   
4. Start the server:
   ```bash
   python app.py
   ```
5. Open your web browser and navigate to `http://127.0.0.1:5000`.


---

## Türkçe

### Açıklama
Bu proje, manga çevri ve renklendirme için tasarlanmış bir web uygulamasıdır. Kullanıcılar manga görsellerini renklendirme, çeviri veya her iki işlemi birden gerçekleştirebilir. İşlem sonrası sonuçlar bir ZIP dosyası olarak indirilir.

### Özellikler
- **Renklendirme**: Siyah-beyaz manga sayfalarını renklendirir.
- **Çeviri**: Manga metinlerini başka bir dile çevirin(Proje İngilizce-Türkçe çeviriyi içermektedir. Kodda yapılan değişiklikler diğer dillere de çevrilebilir.).
- **Birleştirme**: Her iki işlemi aynı anda gerçekleştirin.
- Kullanıcı dostu arayüz ile kolay kullanım.
- İşlem sonuçlarının otomatik indirilmesi.

### Çalıştırma Talimatları
1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/koesan/ReManga_web.git
   cd ReManga_web
   ```
2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip3 install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 flask==3.1.0 
   ```
   
3. **Gerekli Dosyaları İndir**  
   [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) dosyasını indirin ve klonlanmış deponun `networks` klasörüne yerleştirin.

4. Sunucuyu başlatın:
   ```bash
   python app.py
   ```
5. Web tarayıcınızı açın ve `http://127.0.0.1:5000` adresine gidin.
