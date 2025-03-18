import streamlit as st

st.title("UNIT CONVERTER 🔄")
st.write("Effortlessly convert units with just a few clicks! 🚀")

conversion_type = st.radio("Choose a type", ["Length", "Temperature"])

value = st.number_input("Enter value", min_value=0.0)

if conversion_type == "Length":
    units = {"Meters": 1, "Kilometers": 1000, "Centimeter": 0.01}
    from_unit = st.selectbox("From", units.keys())
    to_unit = st.selectbox("To", units.keys())
    result = value * (units[to_unit] / units[from_unit])
    st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.radio("From", ["Celsius", "Fahrenheit"])
    to_unit = st.radio("To", ["Celsius", "Fahrenheit"])
    if from_unit == to_unit:
        result = value
    elif from_unit == "Celsius":
        result = (value * 9/5) + 32
    else:
        result = (value - 32) * 5/9
    st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")
