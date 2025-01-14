import pickle
import json 
import numpy as np

__locations=None
__model=None
__data_columns=None

def get_predicted_value(sqft, loc, bhk, bath):
    try: 
        ind += __data_columns.index(loc.lower())
    except:
        ind = -1
    
    df=np.zeros(len(__data_columns))
    df[0]=sqft
    df[2]=bhk 
    df[1]=bath
    if ind>=0:
        df[ind]=1
    
    return round(__model.predict([df])[0], 2)

def load_artifacts():
    print("Artifact Loading Started")
    global __data_columns
    global __model
    global __locations

    with open('server/artifacts/columns.json', 'r', encoding='utf-8') as f:
        __data_columns = json.load(f)['columns']
        __locations=__data_columns[3:]

    if __model is None:
        with open('server/artifacts/bangalore_price_predict_model.pickle', 'rb') as f:
            __model=pickle.load(f)
    
    print("Artifact Loading Completed")

def get_locations():
    return __locations

def get_columns():
    return __data_columns

if __name__=='__main__':
    load_artifacts()
    print(get_locations())
    
    print(get_predicted_value(1000,'varthur', 2, 2))