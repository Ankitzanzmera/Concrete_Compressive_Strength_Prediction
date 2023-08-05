import logging
import sys,os
sys.path.append(os.getcwd())
from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        input_data = CustomData(
            v1 = float(request.form.get('cement')),
            v2=float(request.form.get('blast_furnace_slag')),
            v3=float(request.form.get('fly_ash')),
            v4=float(request.form.get('water')),
            v5=float(request.form.get('superplasticizer')),
            v6=float(request.form.get('coarse_aggregate')),
            v7=float(request.form.get('fine_aggregate')),
            v8=float(request.form.get('age'))
        )
        final_input_data = input_data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        logging.info(f'{final_input_data}')
        pred = predict_pipeline.predict(final_input_data)

        result = round(pred[0],2)
        return render_template('form.html',final_result = result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000,debug=True)