from flask import Flask, render_template, request, url_for, Markup, jsonify
import pickle
import pandas as pd
import numpy as np

 
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler

import pickle
from flask import Flask, render_template, request, send_from_directory


import os
import pandas as pd
 

app = Flask(__name__) #Initialize the flask App


@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')    
    
@app.route('/abstract')
def abstract():
    return render_template('abstract.html')
@app.route('/future')
def future():
    return render_template('future.html')    
    
@app.route('/index2')
def index2():
    return render_template('index2.html')
    
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df) 

@app.route('/landing_function')
 
def landing_function():
     
    stock_files = list(all_files.keys())

    return render_template('index.html',show_results="false", stocklen=len(stock_files), stock_files=stock_files, len2=len([]),
                           all_prediction_data=[],
                           prediction_date="", dates=[], all_data=[], len=len([]))

@app.route('/process', methods=['POST'])
def process():

    stock_file_name = request.form['stockfile']
    ml_algoritms = request.form.getlist('mlalgos')

    
    df = all_files[str(stock_file_name)]
    
    all_prediction_data, all_prediction_data, prediction_date, dates, all_data, all_data, all_test_evaluations = perform_training(str(stock_file_name), df, ml_algoritms)
    stock_files = list(all_files.keys())

    return render_template('index.html',all_test_evaluations=all_test_evaluations, show_results="true", stocklen=len(stock_files), stock_files=stock_files,
                           len2=len(all_prediction_data),
                           all_prediction_data=all_prediction_data,
                           prediction_date=prediction_date, dates=dates, all_data=all_data, len=len(all_data))
        

 

if __name__=='__main__':
    app.run(debug=True)
