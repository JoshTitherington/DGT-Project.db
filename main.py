from flask import Flask, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    print("I'm Here", id)
    conn = sqlite3.connect("Database.db.db")
    cur = conn.cursor()
    #cur.execute("SELECT * FROM game WHERE id=?;",(id,))
    #cur.execute(" select * from game order by name;")
    cur.execute(" select game.id, game.name, imgroute.path, imgroute.alt_text from game join imgroute on game.img_id = imgroute.id")
    games = cur.fetchall()
    conn.close()
    return render_template("page1.html", games=games)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/videogame/<int:id>")
def videogame(id):
    print("I'm Here", id)
    conn = sqlite3.connect("Database.db.db")
    cur = conn.cursor()
    #cur.execute("SELECT * FROM game WHERE id=?;",(id,))
    cur.execute(" select game.id, game.name, imgroute.path, imgroute.alt_text from game join imgroute on game.img_id = imgroute.id where game.id = ?;",(id,))
    game = cur.fetchone()
    conn.close()
    return render_template("page.html", game=game)

def main():
    # Create a list of page data
    pages = [
        {'title': 'Page 1', 'image': 'images/page1.jpg', 'alt': 'Page 1 Image', 'description': 'Description for page 1'},
        {'title': 'Page 2', 'image': 'images/page2.jpg', 'alt': 'Page 2 Image', 'description': 'Description for page 2'},
        # Add more pages as needed
    ]
    return render_template('page1.html', pages=pages)

@app.route('/page/<int:page_id>')
def page(page_id):
    pages = [
        {'title': 'Page 1', 'image': 'images/page1.jpg', 'alt': 'Page 1 Image', 'description': 'Description for page 1'},
        {'title': 'Page 2', 'image': 'images/page2.jpg', 'alt': 'Page 2 Image', 'description': 'Description for page 2'},
        # Add more pages as needed
    ]
    page = pages[page_id - 1]  # Get the page data based on the ID
    return render_template('page.html', page_title=page['title'], image_path=page['image'], image_alt=page['alt'], description=page['description'])

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run()