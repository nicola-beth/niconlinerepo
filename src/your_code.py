from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    env_var = os.getenv('PAGER_DUTY_SECRET')
    print(env_var)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
