from flask import Flask,render_template,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['POST','GET'])
def mainServer():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('index.html')

if(__name__ == "__main__"):
    app.run(debug=True)