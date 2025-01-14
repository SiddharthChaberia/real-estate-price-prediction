from flask import Flask, request, jsonify
import util 

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response= jsonify({
        'locations': util.get_locations()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_prices', methods=['GET','POST'])
def predict_prices():
    sqft= float(request.form['sqft'])
    loc= request.form['location']
    bhk= int(request.form['bhk'])
    bath= int(request.form['bath'])
    response = jsonify({
        'predicted_price': util.get_predicted_value(sqft, loc, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=='__main__':
    print("Flask starting and setting up")
    util.load_artifacts()
    app.run()

