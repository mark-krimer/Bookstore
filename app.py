from flask import Flask, render_template
from books import Book

app = Flask(__name__, template_folder="temp")

all_books = [
    Book('Poems', 'Есенин С.А.', 14.99, 'poems', 'From the first collections of poetry ("Radunitsa", 1916; "Rural Book of Hours", 1918) he appeared as a subtle lyricist, a master of a deeply psychologized landscape, a singer of peasant Rus, an expert in the folk language and folk soul.'),
    Book('Master and Margarita', 'Булгаков М.А.', 17.49, 'master_and_margarita', 'The Master and Margarita is a novel by Mikhail Afanasyevich Bulgakov, work on which began in the late 1920s and continued until the writers death. The novel refers to unfinished works; After the death of her husband, the writers widow, Elena Sergeevna, carried out editing and bringing together the draft notes.'),
    Book('Idiot', 'Достоевский Ф.М.', 13.49, 'idiot', 'The Idiot is a novel by Fyodor Mikhailovich Dostoevsky, first published in the Russkiy Vestnik magazine in 1868. It was one of the most beloved works of the writer, most fully expressing both the moral and philosophical position of Dostoevsky and his artistic principles in the 1860s.'),
]

@app.route("/")
@app.route("/main")
@app.route("/home")
def home():
    return render_template("index.html", title="Bookstore")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/books")
@app.route("/catalog")
@app.route("/books/index")
def books():
    return render_template("books/index.html", books=all_books, title="Books")

@app.route('/books/book<int:id>')
def book(id):
    b = all_books[id]
    return render_template(f'books/books.html', book=b, title=f'{b.name} - {b.author}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)