import streamlit as st
import pandas as pd
import numpy as np
import pickle
from urllib.request import urlopen
import lime
from lime import lime_tabular
import streamlit.components.v1 as components
import plotly.figure_factory as ff
import altair as alt
import matplotlib.pyplot as plt
import dill
import plotly.graph_objects as go
import plotly.express as px
#https://lime-ml.readthedocs.io/en/latest/lime.html?highlight=explain_instance#lime.lime_tabular.LimeTabularExplainer.explain_instance
# Load Dataframe
df = pd.read_csv("Base_Client.csv",index_col=0)
print(df.shape)

#load modele
model = pickle.load(open('credit.pkl','rb'))

# Load Scaler
file_scaler=open('file_scale.dat','rb')
std_scale=pickle.load(file_scaler)
file_scaler.close()

#load de notre explainer
file_explain=open('Explainer.dat','rb')
explainer=dill.load(file_explain)
file_explain.close()

#liste des identifiants
liste_id = df['SK_ID_CURR'].values

#affichage formulaire
st.title('Dashboard Scoring Credit')
st.markdown("Prédictions de scoring client, notre seuil de choix est de 40 %")
id_input = st.number_input(label='Veuillez saisir l\'identifiant d\'un client:',format="%i", value=0)
if id_input not in liste_id:
    st.write("L'identifiant client n'est pas bon")


elif (int(id_input) in liste_id):
    i = df['SK_ID_CURR']==id_input
    Y = df[i]
    Y = Y.drop(['SK_ID_CURR'], axis=1)



#transformation des données
    num = np.array(std_scale.transform(Y))

#afficher les données
    st.subheader('Les données du client')
    st.write(id_input)
    st.write(Y)


# importer le modele et l'appliquer
    pr = model.predict_proba(num)[:, 1]
    if pr > 0.4:
        prevision= 'Rejet de la demande de crédit'

    else :
        prevision= 'Acceptation de la demande de crédit'
    #affichage prévision
    st.subheader('Le statut de la demande de crédit')
    st.write(prevision)
    st.subheader('Le pourcentage de scoring du client')
    st.write((pr[0]*100).round(0))

    #interprétabilité
    st.subheader('Interprétabilité de notre prévision')
    exp = explainer.explain_instance(data_row=num.reshape(1,Y.shape[1])[0], \
                                     predict_fn=model.predict_proba)

    components.html(exp.as_html(), height=800)
    exp.as_list()


    #graphique
    #tickers=Y.columns
    #print(tickers)
    st.sidebar.subheader('Exploration des caractéristiques du client')
    #dropdown=st.multiselect('Choisir une variable du client',tickers)
    select_box=st.sidebar.multiselect(label='Features',options=Y.columns)
    plt.figure()
    fig1 = px.bar(Y, x=select_box)
    st.plotly_chart(fig1)
    #fig1.show()
    st.sidebar.subheader("Exploration des caractéristiques de l'ensemble des clients")
    select_box1 = st.sidebar.multiselect(label='Features', options=df.columns)
    fig2 = px.histogram(df, x=select_box1,nbins=50)
    st.plotly_chart(fig2)
    #fig2.show()

    # graphique deux variables quantitatives
    st.sidebar.subheader("Analyse Bivariée des caractéristiques de nos clients")
    select_box2 = st.sidebar.selectbox(label='Axe des abscisses', options=df.columns)
    select_box3 = st.sidebar.selectbox(label='Axe des ordonnées', options=df.columns)
    fig3 = px.scatter(df, x=select_box2, y=select_box3)
    st.plotly_chart(fig3)