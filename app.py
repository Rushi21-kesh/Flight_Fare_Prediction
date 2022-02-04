import streamlit as st
import pickle
import pandas as pd
import datetime

#set backround image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://blog.air.irctc.co.in/wp-content/uploads/2019/11/bg.jpg")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True)

global model
df = pd.read_excel('Data_Train.xlsx')

def import_model():
    model = pickle.load(open("D:flight_rf.pkl", "rb"))
    return model

st.title('✈️ Flight Fare Prediction  ✈')
st.markdown("### Filter Flight ")

# take inputs from user
date = st.date_input('Date Of Journey', datetime.datetime.now())

dep_time = st.text_input('Departure Time (HH : MM) ','00:00')
dep_time = pd.to_datetime(dep_time)
# Dep_Hour = st.slider('Hour : ', 0, 24)
# Dep_Min = st.slider("Minute : ", 0, 59)

# arrival_time = st.time_input('Arrival Time',datetime.datetime.now() + datetime.timedelta(hours = 1))
arrival_time = st.text_input("Arrival Time (HH : MM) ",'00:00')
arrival_time = pd.to_datetime(arrival_time)

ar = ['Choose_Airline']
ar.extend(list(df['Airline'].unique()))
airline = st.selectbox('Airline',ar,key=1)

s = ['Choose_Source']
s.extend(list(df['Source'].unique()))
source = st.selectbox('Source',s)

des = ['Choose_Destination']
try:
    des.extend(list(df['Destination'].unique()))
    des.remove(source)
    destination = st.selectbox('Destination',des,key='Choose')
except:
    des.extend(list(df['Destination'].unique()))
    destination = st.selectbox('Destination', des,key='Choose')

stops = st.selectbox('No of Stop',range(5),key=10)

# setting parameters
Total_Stops = stops
Journey_day = date.day
Journey_month = date.month
Dep_Hour = dep_time.hour
Dep_Min = dep_time.minute
Arrival_Hour = arrival_time.hour
Arrival_Min = arrival_time.minute
Duration_Hours = abs(Arrival_Hour - Dep_Hour)
Duration_Mins = abs(Arrival_Min - Dep_Min)

# OneHot Encoding for Airline
if (airline == 'Jet Airways'):
    Jet_Airways = 1
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'IndiGo'):
    Jet_Airways = 0
    IndiGo = 1
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Air India'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 1
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Multiple carriers'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 1
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'SpiceJet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 1
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Vistara'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 1
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'GoAir'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 1
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Multiple carriers Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 1
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Jet Airways Business'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 1
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Vistara Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 1
    Trujet = 0

elif (airline == 'Trujet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 1

else:
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

# onehot encoding for source
if (source == 'Delhi'):
    s_Delhi = 1
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0

elif (source == 'Kolkata'):
    s_Delhi = 0
    s_Kolkata = 1
    s_Mumbai = 0
    s_Chennai = 0

elif (source == 'Mumbai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 1
    s_Chennai = 0

elif (source == 'Chennai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 1

else:
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0


# OneHot for Destination
if (destination == 'Cochin'):
    d_Cochin = 1
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (destination == 'Delhi'):
    d_Cochin = 0
    d_Delhi = 1
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (destination == 'New_Delhi'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 1
    d_Hyderabad = 0
    d_Kolkata = 0

elif (destination == 'Hyderabad'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 1
    d_Kolkata = 0

elif (destination == 'Kolkata'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 1

else:
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

# prediction
if st.button("   Predict Fare   "):
    try:
        model = import_model()
        prediction = model.predict([[
            Total_Stops, Journey_day, Journey_month, Dep_Hour, Dep_Min, Arrival_Hour, Arrival_Min, Duration_Hours,
            Duration_Mins,
            Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
            Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy,
            s_Chennai, s_Delhi, s_Kolkata, s_Mumbai,
            d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata, d_New_Delhi
        ]])

        output = round(prediction[0])
    except:
        output = 0000
    st.markdown(f"##### Predicted Fare is : {output} INR")