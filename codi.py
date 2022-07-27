import streamlit as st
from streamlit_option_menu import option_menu

from datetime import datetime
import pandas as pd
import pymongo


# --------------- CONNECTO MONGO: Uses st.experimental_singleton to only run once ---------------
@st.experimental_singleton
def init_connection():
    return pymongo.MongoClient("mongodb://looming:012345@147.83.48.118/?authMechanism=DEFAULT") #"mongodb://xxxxxxxxxx:yyyyy/" on xxx... = ip públic del ordi al q es connecta // yy = port on esta el mongodb
    #"mongodb://looming:012345@147.83.48.118/ProbaConn"
    #"mongodb://147.83.48.118:27017/"
try:
    client = init_connection()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    st.error("Temps de connexio al MongoDB excedit. Temps: "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    st.error("Error al connectarse a MongoDB. Error: "+errorConexion)
except pymongo.errors.ConfigurationError as errorConfig:
    st.error("Error de configuracio de MongoDB. Error: "+errorConfig)
except pymongo.errors.OperationFailure as errorOperacio:
    st.error("Error d'operacio de MongoDB. Error: "+errorOperacio)
except pymongo.errors.InvalidURI as errorURI:
    st.error("Error de URI de MongoDB. Error: "+errorURI)
except pymongo.errors.PyMongoError as errorPyMongo:
    st.error("Error de PyMongo. Error: "+errorPyMongo)

st.info("s'ha connectat correctament a la base de dades")




db = client.ProbaConn.Eines1
buscar = db.find()
items = list(buscar)  # make hashable for st.experimental_memo
df = pd.DataFrame(items)
st.dataframe(df.head())

