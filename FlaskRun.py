from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'flask test~~~~ 이주애 화이팅~'

if __name__ == '__main__':
    app.run('0.0.0.0', port=27017, debug=True)