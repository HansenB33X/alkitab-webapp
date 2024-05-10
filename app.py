from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Fungsi untuk mendapatkan daftar pasal
def get_passage_list():
    url = 'https://beeble.vercel.app/api/v1/passage/list'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print('Gagal mengambil daftar pasal:', response.status_code)
        return None

# Fungsi untuk mendapatkan konten pasal
def get_passage_content(book_abbr, chapter_number):
    url = f'https://beeble.vercel.app/api/v1/passage/{book_abbr}/{chapter_number}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['verses']
    else:
        print('Gagal mengambil konten pasal:', response.status_code)
        return None

# Halaman beranda
@app.route('/')
def index():
    passage_list = get_passage_list()
    return render_template('index.html', passage_list=passage_list)

# Halaman konten pasal
@app.route('/passage', methods=['POST'])
def passage():
    book_abbr = request.form['book_abbr']
    chapter_number = request.form['chapter_number']
    passage_content = get_passage_content(book_abbr, chapter_number)
    return render_template('passage.html', passage_content=passage_content)

if __name__ == '__main__':
    app.run(debug=True)

