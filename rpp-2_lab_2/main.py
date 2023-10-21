from flask import Flask

from api.routes.add_route import bp as add_bp
from api.routes.fetch_route import bp as fetch_bp
from api.routes.update_route import bp as update_bp

app = Flask(__name__)
app.register_blueprint(add_bp)
app.register_blueprint(fetch_bp)
app.register_blueprint(update_bp)

if __name__ == '__main__':
    app.run()
