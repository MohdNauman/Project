
import numpy as np
from flask import Flask, request, jsonify
from flask import render_template 
import pickle
import sklearn

app = Flask(__name__)
model = pickle.load(open('model3.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict'):
    if request.method =='POST':
def predict():
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0])
    
    return render_template('index.html', prediction_text = 'Price {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    #For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output1 = prediction[0]
    return jsonify(output1)

if __name__ == '__main__' :
    app.run(debug=True)
    

