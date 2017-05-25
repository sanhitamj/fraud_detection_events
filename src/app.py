from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Flask root'

#define website
@app.route('/hello', methods=['GET'])   #map web page to address with decorator
def index():
    return 'Hello, World!'

#define website
@app.route('/score', methods=['POST'])   #map web page to address with decorator
def index():
    name = request.form.get('name')     #Use request.form instead of request.args if using POST to enter info
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
