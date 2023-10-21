### Рекомендации по выполнению лабораторной работы №3

* Создать отображения таблиц из лабораторной работы №1 на классы
  * Создать экземпляр приложения app = Flask(__name__)
  * Создать сессию базы данных db = SQLAlchemy(app)
  * Создать классы Region(db.Model), CarTaxParam(db.Model), AreaTaxParam(db.Model)
  * Пример класса:
    ```python
        from flask import Flask
        from flask_sqlalchemy import SQLAlchemy

        app = Flask(__name__)
        db = SQLAlchemy(app)

        class Region(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String, nullable=False)
        
        new_region = Region(name='Новосибирск')
        db.session.add(new_region)
        
        all_regions = Region.query.all()
        for region in all_regions:
            print(region.name)
    
        filtered_regions = Region.query.filter(Region.name == 'Новосибирск')
    
        db.session.delete(new_region)
    ```
  * Эндпоинт (маршрут) не меняем (меняем только select и инсерты), только убираем взаимодействие с базой данных через psycopg2 
  * Сделать файл с тестами