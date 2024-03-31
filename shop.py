from flask import Flask, render_template

app = Flask(__name__) # создание объекта приложения

@app.route('/') # декоратор маршрутизации запросов
def index():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это главная страница Интернет магазина</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашими товарами</p>')
    context = {'text': _text_info, 'title': 'Главная страница'}
    return render_template('index.html', **context)

@app.route('/about/') # декоратор маршрутизации запросов
def about():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница о нас</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете узнать о нас больше</p>')
    context = {'text': _text_info, 'title': 'О Нас'}
    return render_template('about.html', **context)

@app.route('/contacts/') # декоратор маршрутизации запросов
def contacts():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница контактов</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете связаться с нами</p>')
    context = {'text': _text_info, 'title': 'Контакты'}
    return render_template('contacts.html', **context)

@app.route('/cloth/') # декоратор маршрутизации запросов
def cloth():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница одежды</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашей одеждой</p>')
    context = {'text': _text_info, 'title': 'Одежда'}
    return render_template('cloth.html', **context)

@app.route('/shoes/') # декоратор маршрутизации запросов
def shoes():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница обуви</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашей обувью</p>')
    context = {'text': _text_info, 'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/jacket/') # декоратор маршрутизации запросов
def jacket():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница курток</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашими куртками</p>')
    context = {'text': _text_info, 'title': 'Куртки'}
    return render_template('jacket.html', **context)

if __name__ == '__main__':
    app.run(debug=True) # запуск приложения
