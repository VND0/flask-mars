import pprint

from flask import Flask, url_for, request

app = Flask(__name__)
OCCUPATIONS = ["researcher", "builder", "pilot", "weatherman", "life_assurance",
               "radiation_engineer", "doctor", "biologist"]
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
REGISTRATION_FORM = """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content=" width=device-width, initial-scale=1.0">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <title>Mars</title>
</head>
<body class="d-flex justify-content-center">
<div>
    <h1 class="text-center">Анкета претендента</h1>
    <h2 class="text-center">На участие в миссии</h2>
    <form action="/handle-form" method="post" enctype="multipart/form-data" class="mt-4 p-3 rounded bg-warning-subtle">
        <div class="mb-3 d-flex flex-column gap-2">
            <input type="text" name="surname" placeholder="Введите фамилию" class="w-100">
            <input type="text" name="name" placeholder="Введите имя" class="w-100">
        </div>
        <input type="email" name="email" placeholder="Введите адрес почты" class="w-100 d-block mb-4">
        <div class="mb-3">
            <label for="edu-select" class="d-block mb-1">Какое у вас образование?</label>
            <select id="edu-select" class="form-select" name="education">
                <option selected value="Начальное">Начальное</option>
                <option value="Основное общее">Основное общее</option>
                <option value="Среднее профессиональное">Среднее профессиональное</option>
                <option value="Высшее">Высшее</option>
            </select>
        </div>
        <div class="mb-3">
            <label class="d-block mb-1">Какие у вас есть профессии</label>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="researcher">
                <label>Инженер-исследователь</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="builder">
                <label>Инженер-строитель</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="pilot">
                <label>Пилот</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="weatherman">
                <label>Метеоролог</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="life_assurance">
                <label>Инженер по жизнеобеспечению</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="radiation_engineer">
                <label>Инженер по радиационной защите</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="doctor">
                <label>Врач</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" name="biologist">
                <label>Экзобиолог</label>
            </div>
        </div>
        <div class="mb-3">
            <label class="d-block mb-1">Укажите пол</label>
            <div class="form-check">
                <input checked type="radio" class="form-check-input" name="gender" value="male">
                <label class="form-check-label">Мужской</label>
            </div>
            <div class="form-check">
                <input type="radio" class="form-check-input" name="gender" value="female">
                <label class="form-check-label">Женский</label>
            </div>
        </div>
        <div class="mb-3">
            <label class="d-block mb-1">Почему вы хотите принять участие в миссии?</label>
            <textarea name="why" class="w-100"></textarea>
        </div>
        <div class="mb-3">
            <label class="d-block mb-1">Приложите фотографию</label>
            <input class="form-control" type="file" name="photo">
        </div>

        <div class="mb-3">
            <input type="checkbox" class="form-check-input" name="ready_to_move">
            <label>Готовы остаться на Марсе?</label>
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</div>
</body>
</html>
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


@app.get("/astronaut_selection")
def astro_select():
    return REGISTRATION_FORM


@app.post("/handle-form")
def handle_form():
    occupations = []
    fields = {}
    for k, v in request.form.items():
        if k in OCCUPATIONS:
            occupations.append(k)
        else:
            fields[k] = v

    output = {
        "photo_added": bool(request.files["photo"]),
        "occupations": occupations,
        "other_fields": fields
    }
    pprint.pp(output)
    return output


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
