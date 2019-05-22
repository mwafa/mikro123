# Mikro123

Sebuah sistem untuk menterjemahkan suara menjadi bahasa isyarat.
Aplikasi ini membantu orang-orang untuk bisa menggunakan bahasa isyarat,
sehingga bisa berkomunikasi dengan tuna rungu.

## Pre-Install

Pertama install `SpeechRecognition`, `openCV` dan `PyAudio`.

```bash
pip install SpeechRecognition
pip install opencv-python
pip install PyAudio
```

## Clone Repository

```bash
git clone https://github.com/mwafa/mikro123.git
cd mikro123
```

## Running

Menjalankan program dengan:

```bash
python start.py
```

Lalu katakan sesuatu

## Menambah Database Kata

Lektakkan video baru dengan format `.mp4` kedalam folder `video`.
Daftarkan video kedalam file `data.py`

```python
data["videoname"] = ["kata", "padanan kata"]
```