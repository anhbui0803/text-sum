from flask import Flask, render_template, request

from transformers import pipeline


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST', 'GET'])
def getSummary():
    body = request.form['data']
    body = 'summarize: ' + body
    summarizer = pipeline('summarization', model='buianh0803/text-sum-2')
    result = summarizer(body)[0]['summary_text']
    return render_template('summary.html', result=result)
