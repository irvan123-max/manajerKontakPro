# Mulai dari image Python 
FROM python:3.12-slim
# Tentukan direktori kerja 
WORKDIR /app
# Kita perlu menginstal library 'redis' untuk Python 
# Pertama, kita salin HANYA file kebutihan (yang akan kita buat)
COPY requirements.txt .
RUN pip install -r requirements.txt
# Sekarang salin semua kode ptoyek kita
COPY . .
# Perintah untuk menjalankan file main.py
CMD ["python", "main.py"]