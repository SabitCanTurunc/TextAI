from flask import Flask, render_template, request, redirect, url_for
from data_processing import analyze_text, save_to_database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        analysis_result = analyze_text(text)
        save_to_database(text, analysis_result)
        return render_template('result.html', text=text, analysis_result=analysis_result)

@app.route('/return_to_index', methods=['GET'])
def return_to_index():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
