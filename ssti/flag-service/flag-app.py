from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/secret')
def secret():
    return jsonify({"flag": "FLAG{s5t1_t3mpl4t3_1nj3ct10n_m4st3r3d!}"})

@app.route('/')
def index():
    return "Flag service running. The flag is hidden elsewhere."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
