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
def predict_pipeline():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            v1 = float(request.form.get('cement')),
            v2=float(request.form.get('cementblast_furnace_slag')),
            v3=float(request.form.get('fly_ash')),
            v4=float(request.form.get('water')),
            v5=float(request.form.get('superplasticizer')),
            v6=float(request.form.get('coarse_aggregate')),
            v7=float(request.form.get('fine_aggregate')),
            v8=float(request.form.get('age'))
        )
        final_input_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_input_data)

        results = round(pred[0],2)
        return render_template('form.html',final_result = results)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000,debug=True)