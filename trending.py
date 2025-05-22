import pandas as pd 
import numpy as np 
import pickle as pk 
import streamlit as st



model = pk.load(open('model.pkl','rb'))

st.header('SECOND HAND CAR PRICE PREDICTION SYSTEM')

# Your Streamlit app content
st.title("Enter your vehicle details")
#st.write("This is how you add a background image!")

cars_data = pd.read_csv('C:\\Users\\dell\\OneDrive\\Pictures\\Documents\\Car price prediction system\\new car\\Cardetails.csv')
st.sidebar.title ("TEAM ENCRYPTION A.I")
st.sidebar.text_input("YOUR EMAIL ADDRESS")
st.sidebar.text_input("PASSWORD")
st.sidebar.button("SUBMIT")
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
cars_data['name'] = cars_data['name'].apply(get_brand_name)
#st.file_uploader("upload car image in front and back && both side && interiorer")

name = st.selectbox('SELECT CAR MODEL', cars_data['name'].unique())
#brandmodel = st.selectbox ('Select car model')
brandmodel = st.selectbox ('Select car model',["MODEL TYPE","maruti Alto K10", 'Maruti Alto 800',"_Maruti Celerio","_Maruti S-Presso",
                                               "Maruti Swift" ," Maruti Baleno", "Maruti Wagon R" ,"Maruti Dzire" ,"Maruti Ciaz","Maruti Invic","maruti Breza",
                                               "Maruti artica", "Grand Vitara","Maruti Brezza","Maruti Grand Vitara",
"Maruti Jimny","Maruti Fronx EV","Maruti Ertiga","Maruti XL6","Maruti Eeco","Maruti Super Carry","Toyota Urban Cruiser Hyryder","Toyota Urban Cruiser Taisor",
"Toyota Fortuner",
"Toyota Fortuner Legender",
"Toyota Hilux",
"Toyota Innova Crysta",
"Toyota Innova Hycross",
"Toyota Rumion",
"Toyota Vellfire",
"maze","City","City e:HEV","Jazz","WR-V","Civic","Accord",
"R-V",
"BR-V","A3","A4","A6","A8","Q2","Q3","Q5","Q7","Q8","e-tron","e-tron GT","RS e-tron GT","TT","R8"
])

year = st.slider('Car Manufactured Year', 1994,2024)
km_driven = st.slider('No of kms Driven', 11,200000)
fuel = st.selectbox('Fuel type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller  type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission type', cars_data['transmission'].unique())
owner = st.selectbox('Seller  type', cars_data['owner'].unique())
mileage = st.slider('Car Mileage', 10,40)
engine = st.slider('Engine CC', 700,5000)
max_power = st.slider('Max Power', 0,200)
seats = st.slider('No of Seats', 5,10)


if st.button("Predict"):
    input_data_model = pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],
    columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
    
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],
                           [1,2,3,4,5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2], inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai','Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                          [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                          ,inplace=True)
    
    car_price = model.predict(input_data_model)
    st.balloons()


    st.markdown('Car Price is going to be '+ str(car_price[0]))

