from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def file_upload():
    return request.get_data()

if __name__ == "__main__":
    app.run(debug=True)