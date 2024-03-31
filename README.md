Домашние задание от 25.03.24
"""
Создать базовый шаблон для интернет-магазина, 
содержащий общие элементы дизайна (шапка, меню, 
подвал), и дочерние шаблоны для страниц категорий 
товаров и отдельных товаров. 

Например, создать страницы "Одежда", "Обувь" и "Куртка", 
используя базовый шаблон
"""

Создан Базовый шаблон: templates/base.html
Дочерние шаблоны наследуют Базовый и переназначают блоки({% block title %} и {% block content %}:
templates/index.html
templates/about.html
templates/contacts.html
Так же создан шаблон новой страницы(templates/new_page.html) которая часто используется к примеру. 
Он наследует от базового шаблона templates/base.html в котором уже переназначены блоки({% block title %} и {% block content %}
И дочерений шаблон templates/new_page.html применяется уже в каталоге товара:
templates/cloth.html
templates/jacket.html
templates/shoes.html
