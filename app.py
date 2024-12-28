import os
import io
import zipfile
from flask import Flask, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename
from main import main
import torch
import gc

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Dosyaların kaydedileceği dizin
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

def clear_cuda_memory():
    """
    CUDA belleğini temizlemek ve GPU'yu sıfırlamak için bir yardımcı işlev.
    """
    try:
        if torch.cuda.is_available():
            # GPU üzerindeki PyTorch işlemlerini boşalt
            torch.cuda.empty_cache()
            torch.cuda.synchronize()
            print("CUDA belleği temizlendi.")

            # Garbage collector çalıştır
            gc.collect()
            print("Garbage collector çağrıldı.")
        else:
            print("CUDA kullanılabilir değil.")
    except Exception as e:
        print(f"CUDA belleği temizlenirken bir hata oluştu: {e}")

@app.route('/process', methods=['POST'])
def process():
    clear_cuda_memory()

    # Yüklenen dosyaları al
    uploaded_files = request.files.getlist('images')
    operation = request.form.get('operation')

    # Bellekte dosyaları saklayacak bir dictionary
    in_memory_files = {}

    for file in uploaded_files:
        if file.filename != '':
            filename = secure_filename(file.filename)
            in_memory_files[filename] = file.read()

    # İşlem
    results = main(in_memory_files, operation)

    # ZIP dosyasını kaydedelim
    zip_filename = os.path.join(UPLOAD_FOLDER, 'results.zip')
    with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for filename, file_data in results.items():
            zipf.writestr(filename, file_data)

    # Kullanıcıya ZIP dosyasını indirmeleri için link verelim
    download_url = url_for('download', filename='results.zip', _external=True)

    # JSON olarak indirme linkini döndürelim
    return {'status': 'ready', 'download_url': download_url}

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
