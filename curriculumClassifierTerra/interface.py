import streamlit as st
import pandas as pd
import numpy as np
#import pydeck as pdk
import plotly.express as px
#import mysql.connector



st.title("Covid Detector")
st.markdown("Datos del usuario")

st.header("Datos generales")

nombre = st.text_input("Nombre completo del usuario", '-')


# #mandar todos los datos a SQL, no se si sea la manera de decir que cuando piquen
# #el boton se mande los datos
# if botonGuardar: 
#     try:
  
#     #aqui se guarda la conexion con tu base de datos de sql
#         cnx = mysql.connector.connect(user='root', password='Iyzkw3927', host='127.0.0.1', database='covidDetector', auth_plugin='mysql_native_password')
#         cursor = cnx.cursor()

#         #solo es importante la coma al final cuando es un sólo elemento 
#         query_data = (1,)
        
        
#         query_dataPersona = ( nombre, edad)
#         # lastID, nombre, edad
#         #no es necesario poner el idPersona porque se autoincrementa al añadir valores a la columna
#         #siempre es %s  para pasar una referencia
#         queryPersona = (f"insert into persona (nombre, edad) values( %s, %s) ;")
        
#         #primero debes ejecutar persona para que exista la foreign key que se compartirá
#         cursor.execute(queryPersona, query_dataPersona)

#         #obtener el idPersona para ponerlo en historial
#         queryID = (f"select idPersona from persona;")
#         cursor.execute(queryID)
#         #list comprenhension, vas a guardar el ultimo id de luz para de ahí insertar más
#         lastID = [result[0] for result in cursor][-1]


       
#         #ORDEN: idHistorial, idPersona, edadRiesgo, diabetes, hipertension, eRespiratorias
#         #fiebre, perdidaOlfato, dificultadRespiratoria, eGastro
        
#         query_dataHistorial = (lastID, lastID, edadRiesgoBool, diabetesBool, hipertensionBool, eRespiratorias, fiebreBool, olfatoBool, dificultadRespiratoriaBool, eGastro )
#         queryHistorial = (f"insert into historial values( %s, %s, %s, %s, %s,%s,%s,%s,%s,%s ) ;")

#         cursor.execute(queryHistorial, query_dataHistorial)

#         st.write("si se pudo")
#         #para hacer cambios en database 
#         cnx.commit()

    # except mysql.connector.Error as err:
    # #si hay un error ocurrira esto
    # #en caso de que se niegue el acceso a la base de datos
    #     if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your user name or password")
    #         #si no existe la base de datos
    #     elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
        
    # finally:
    # #esto se hará si o sí 
    #     if 'cnx' in locals() or 'cnx' in globals():
    #         cnx.close()