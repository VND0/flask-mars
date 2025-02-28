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
    <h1>Жди нас, Марс!</h1>
    <img src={url_for("static", filename="img/Mars.png")} alt="Нужен static/Mars.webp">
    <p>Вот она какая, красная планета.</p>
    """
    return template


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
