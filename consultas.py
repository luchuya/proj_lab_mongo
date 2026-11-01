"""
Asignatura: SGDI
Práctica 2:
Autores: XXXXXXXXXXXXXXX

Declaración de integridad
Declaramos que esta solución es fruto exclusivamente de nuestro trabajo 
personal. No hemos sido ayudados por ninguna otra persona o sistema automático
ni hemos obtenido la solución de fuentes externas, y tampoco hemos compartido 
nuestra solución con otras personas de manera directa o indirexcta. 
Declaramos además que no hemos realizado de manera deshonesta ninguna otra 
actividad que pueda mejorar nuestros resultados ni perjudicar los resultados 
de los demás.
"""
import pymongo
from bson.objectid import ObjectId

MONGO_URI = "mongodb://localhost:27017/"
mongoclient = pymongo.MongoClient(MONGO_URI)
mongoclient.server_info()  # Comprobar la conexión
#print("Conexión exitosa")

def usuario_peliculas(mongoclient, user_id, n):
    db = mongoclient["sgdi_pr2"]
    return db.usuarios.find(
        {"_id": user_id},
        {"email": 1, "visualizaciones": {"$slice": n}}
    )


# def usuarios_gustos(mongoclient, gustos, n):
#     ...

  
# def usuario_sexo_edad(mongoclient, sexo, edad_min, edad_max ):
#     ...

    
# def usuarios_apellidos(mongoclient, ):
#     ...
    
    
# def pelicula_prefijo(mongoclient, prefijo):
#     ...
    

# def usuarios_gustos_numero(mongoclient, n):
#     ...
    

# def usuarios_vieron_pelicula(mongoclient, id_pelicula, inicio, fin):
#     ...

