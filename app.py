import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    a=[]
    features[0]=2020-int(features[0])
    a.append(features[0])
    a.append(float(features[1]))
    a.append(int(features[2]))
    if features[3]=='Diesel':
        a.append(1)
        a.append(0)
    elif features[3]=='Petrol':
        a.append(0)
        a.append(1)
    else:
        a.append(0)
        a.append(0)
    if features[4]=='Dealer':
        a.append(0)
    else:
        a.append(1)
    if features[5]=="Mannual":
        a.append(1)
    else:
        a.append(0)
    a=[np.array(a)]
    #final_features = [np.array(features)]
    #prediction = model.predict(final_features)
    #output = round(prediction[0], 2)
    prediction = model.predict(a)
    output = round(prediction[0], 2)


    return render_template('index.html', prediction_text='You can sell your car for {} Lakhs'.format(output))


if __name__ == "__main__":
    app.run(debug=True)