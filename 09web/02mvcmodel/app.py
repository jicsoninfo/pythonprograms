from flask import Flask
from views import sll_view
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register the views blueprint
app.register_blueprint(sll_view)

@app.route('/')
def home():
    return "Welcome to the Linked List API!"

if __name__ == '__main__':
    app.run(debug=True)


#pip freeze > requirement.txt