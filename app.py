from flask import Flask, request
import  joblib
import numpy


MODEL_PATH='models/modelxgb.pkl'


app = Flask(__name__)

model=joblib.load(MODEL_PATH)


@app.route('/prediction_test',methods = ['GET'])
def prediction():  # put application's code here
    args = request.args
    floor = args.get('floor', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    kitchen_area = args.get('kitchen_area', default=-1, type=float)
    living_area = args.get('living_area', default=-1, type=float)
    agent_fee = args.get('agent_fee', default=-1, type=float)
    price_per_sq_m = args.get('price_per_sq_m', default=-1, type=float)
    house_price_sqm_median_cleaned=args.get('house_price_sqm_median_cleaned', default=-1, type=int)
    days_exposition = args.get('days_exposition', default=-1, type=int)
    price_for_rent = args.get('price_for_rent', default=-1, type=float)

    x=numpy.array([floor,rooms,area,kitchen_area,living_area,agent_fee,price_per_sq_m,house_price_sqm_median_cleaned,
                   days_exposition,price_for_rent]).reshape(1,-1)
    result=model.predict(x)

    return str(result[0])



if __name__ == '__main__':
    app.run(debug=True,port=5444,host='0.0.0.0') #port specification with port = ...
