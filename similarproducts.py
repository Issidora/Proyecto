# =============================================================================
# Librerias

import pandas as pd
import numpy as np
from gensim.models import Word2Vec 

# =============================================================================
#Lee el dataframe con los datos de los clientes
df = pd.read_excel('Libro1.xlsx')


#Analisis del dataframe
print(df.shape)
print(df.head())





#Primero convertiremos los valores del Id producto en string 
df['id']=df['id'].astype(str)
#agrupamos a los usuarios según su numero de cliente 
clientes_1 = df["cliente"].unique().tolist()

# Cree una lista para almacenar las compras de cada uno de  los clientes y la llenamos
#con los códigos de los productos 
compras_de_clientes = []
for i in clientes_1:
    temp = df[df["cliente"] == i]["id"].tolist()
    compras_de_clientes.append(temp)
def aggregate_vectors(products):
    product_vec = []
    for i in products:
        try:
            product_vec.append(model[i])
        except KeyError:
            continue
        
    return np.mean(product_vec, axis=0)



#window: Distancia máxima entre la palabra actual y la predicha dentro de una oración.
#min_count:Ignora todas las palabras con una frecuencia total inferior a esta.
#workers:subprocesos de trabajo para entrenar el modelo 


#Creamos el modelo 
model = Word2Vec(min_count=1,size=300,workers=8,window = 100)

#Word2Vec requiere que construyamos la tabla de vocabulario 
vocab=model.build_vocab(compras_de_clientes, progress_per=200)
#progress_per:Indicates how many words to process before showing/updating the progress.

#Guardamos
model.save("word2vec.model")

#entrenamiento del modelo
model.train(compras_de_clientes, total_examples = model.corpus_count, 
            epochs=500, report_delay=1)
#lo entreno 50,500,1000,5000 veces
X = model[model.wv.vocab]

# =============================================================================
# resumen del modelo
#print(model)
#Word2Vec(vocab=1362, size=300, alpha=0.025)
#tamaño del vocabulario vocab=1362

# =============================================================================


#datarframe de los productos con su categoria
Productos = df[["id", "Grupo"]]
#diccionario que almacena todos los codigos de los productos y su categoria
productos_dict = Productos.groupby('id')['Grupo'].apply(list).to_dict()


#funcion para que me entregue 5 propductos similares a los que llevo
def mas_similares(v):

    ms1 = model.most_similar(v, topn= 6)[1:]
    
    nuevos_prod = []
    for j in ms1:
        out = (j[0],productos_dict[j[0]][0],j[1])
        nuevos_prod.append(out)
        
    return nuevos_prod 

#hacer funcion para que me entregue 5 predicciones
def prediccion(v):

    ms2 =model.predict_output_word(v, topn= 6)[1:]
    
    nuevos_produc = []
    for j in ms2:
        out = (j[0],productos_dict[j[0]][0],j[1])
        nuevos_produc.append(out)
        
    return nuevos_produc 




L=['H350120', 'Z273123', 'Z280111', 'Z282511', 'Z300042', 'Z304020', 'Z382512', 'H350120', 'H480220', 'L200211', 'R509226', 'R587104', 'S582124', 'Z215420', 'Z417655', 'Z432603', 'H350120', 'H380920', 'L200211', 'L325412']
np.array(L)

#Probando el codigo en la consola 
#prediccion(L)
#Out[2]: 
#[('Z304020', 'ASEO, HIGIENE Y OTROS', 0.1503102),
# ('Z215420', 'PAPELES TISSUE INSTITUCIONAL', 0.07874744),
# ('Z273123', 'ASEO, HIGIENE Y OTROS', 0.0736692),
# ('Z432603', 'PAPELES TISSUE INSTITUCIONAL', 0.071166635),
# ('Z280111', 'ASEO, HIGIENE Y OTROS', 0.062556654)]

#mas_similares(L)
#Out[3]: 
#[('U394785', 'SEGURIDAD INDUSTRIAL', 0.5008736848831177),
# ('U402439', 'PAPELES TISSUE INSTITUCIONAL', 0.499156653881073),
# ('S589820', 'LIBRERIA OFICINA', 0.4925268590450287),
# ('T001943', 'LIBRERIA OFICINA', 0.47304412722587585),
# ('Z274323', 'ASEO, HIGIENE Y OTROS', 0.47221261262893677)]




# =============================================================================
# me devuelve el producto,el código y el porcentaje de similitud 
