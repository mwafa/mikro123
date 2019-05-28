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

Menjalankan program __sekali__ dengan:

```bash
python start.py # kemudian katakan sesuatu
```

Menjalankan progam __berulang__ dengan:

```bash
python start.py loop
```

untuk mengakhiri katakan "_Tutup aplikasi_" atau tekan `ctrl + c` 

### Running tanpa suara

Kamu bisa langsung memasukkan kalimat tanpa menggunakan suara dari mic.

```bash
python start.py -m "dimana rumah pacar kamu ?"
```

### Test Spech to Text

```bash
python totext.py # kemudian katakan sesuatu
```

### Test Video Player

```bash
python play.py
```

untuk menampilkan video lebih spesifik

```bash
python play.py "videoname1" "videoname2" # dan seterusnya...
```


## Menambah Database Kata

Lektakkan video baru dengan format `.mp4` kedalam folder `video`.
Daftarkan video kedalam file `data.py`

```python
data["videoname"] = ["kata", "padanan kata"]
```