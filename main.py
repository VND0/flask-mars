from flask import Flask, url_for

app = Flask(__name__)

PROMO = """<p>
Человечество вырастает из детства.
<br>
Человечеству мала одна планета.
<br>
Мы сделаем обитаемыми безжизненные пока планеты.
<br>
И начнем с Марса!
<br>
Присоединяйся!
</p>
"""


@app.get("/")
def name():
    return "<p>Миссия Колонизация Марса</p>"


@app.get("/index")
def index():
    return "<p>И на Марсе будут яблони цвести!</p>"


@app.get("/promotion")
def promotion():
    return PROMO


@app.get("/image_mars")
def mars_image():
    template = f"""
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content=" width=device-width, initial-scale=1.0">
        
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for("static", filename="css/styles.css")}">
        
        <title>Mars</title>
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src={url_for("static", filename="img/Mars.png")} alt="Нужен static/Mars.webp">
    <div class="alert alert-primary" role="alert">
        Человечество вырастает из детства.
    </div>
    <div class="alert alert-secondary" role="alert">
        Человечеству мала одна планета.
    </div>
    <div class="alert alert-success" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-danger" role="alert">
        И начнем с Марса!
    </div>
    <div class="alert alert-warning" role="alert">
        Присоединяйся!
    </div>
    </body>
    </html>
    """
    return template


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
