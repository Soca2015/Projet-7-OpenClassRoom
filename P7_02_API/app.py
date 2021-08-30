from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import RobustScaler
from io import StringIO
import os
from os.path import join, dirname, realpath
import lime
from lime import lime_tabular
from pathlib import Path
import matplotlib.pyplot as plt
from wtforms.fields import StringField
from wtforms import Form,TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms.widgets import TextArea

app=Flask(__name__)
#load model
model = pickle.load(open('credit.pkl','rb'))
# Load Scaler
file_scaler=open('file_scale.dat','rb')
std_scale=pickle.load(file_scaler)
file_scaler.close()
#load imputer  variable AMT numerique
file_medianAMT=open('file_imputerAMT.dat','rb')
median_AMT=pickle.load(file_medianAMT)
file_medianAMT.close()
#load imputer variable EXT
file_medianEXT=open('file_imputerEXT.dat','rb')
median_EXT=pickle.load(file_medianEXT)
file_medianEXT.close()
#load imputer categorique type occupation
file_occupation=open('file_imputeroccupation.dat','rb')
Occupation=pickle.load(file_occupation)
file_occupation.close()
#load imputer categorique type organisation
file_organisation=open('file_imputerorga.dat','rb')
occupation=pickle.load(file_organisation)
file_organisation.close()
#load imputer categorique type
file_type=open('file_imputertype.dat','rb')
type_cat=pickle.load(file_type)
file_type.close()


@app.route('/',methods=["GET"])

def hello_word():
    return render_template("index.html")


# Load Dataframe
df = pd.read_csv("Base_Client.csv",index_col=0)

print(df.columns)



@app.route('/',methods=["POST"])
def predict():
    for x in request.form.values():
        Identifiant = int(x)
    print(Identifiant)
    print(type(Identifiant))
    print(df.columns)
    print(df.head())
    #print(df['SK_ID_CURR'].dtypes)
    if Identifiant in df['SK_ID_CURR'].values:

        i=df['SK_ID_CURR'] == Identifiant

        Y = df[i]
        Y = Y.drop(['SK_ID_CURR'], axis=1)
        num = np.array(std_scale.transform(Y))
        pr = model.predict_proba(num)[:, 1]

        if pr > 0.4:
            classification = 'Rejet de la demande de crédit'


        else:
            classification = 'Acceptation de la demande de crédit'

    return render_template('index.html', valeur=(pr[0]*100).round(0),prediction=classification)
    #return render_template('index.html', prediction=classification)





#@app.route('/')
#@app.route('/', methods=['POST'])

#@app.route('/')
#@app.route('/index')

'''

def interpretation ():
    exp = " "
    for x in request.form.values():
        Identifiant = int(x)
    #ID = int(Identifiant)
    #class_names = {0: 'Client Fiable', 1: 'Client Pas Fiable'}
    X1 = df[df['SK_ID_CURR'] == Identifiant]
    #print('ID client: {}'.format(ID))
    #print('Classe réelle : {}'.format(class_names[X1['LABELS'].values[0]]))

    # print('Temps initialisation : ', time.time() - start_time)
    # start_time = time.time()
    X1 = X1.drop(['SK_ID_CURR'], axis=1)
    dataframe = df.drop(['SK_ID_CURR'], axis=1)
    explainer = lime_tabular.LimeTabularExplainer(
        training_data=np.array(std_scale.transform(dataframe)),
        feature_names=dataframe.columns,
        training_labels=dataframe.columns.tolist(),
        verbose=1,
        random_state=20,
        mode='classification')
    exp = explainer.explain_instance(data_row=X1.sort_index(axis=1).iloc[0:1, :].to_numpy().ravel(), \
                                     predict_fn=model.predict_proba)
    #exp.save_to_file('output_filename.html')
    #exp = exp.as_html()
    

    plt.savefig(exp,
                format="png",
                dpi=150,
                bbox_inches='tight')
    dataToTake = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    #return render_template('index.html', exp=exp)
    return render_template("index.html", user_image=print(exp))
'''


if __name__ == "__main__":
    app.run(port=5000,debug=True)