from flask import Flask
import settings
from application import bootstrap
from db_seed import run_scripts
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(settings)
app.secret_key = 'super secret key'
cors = CORS(app)


for blueprint in bootstrap.blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':

    # create data for demo purpose
    run_scripts()

    app.run(
        host=app.config['HOST'],
        port=int(app.config['PORT']),
        debug=app.config['DEBUG']
    )
