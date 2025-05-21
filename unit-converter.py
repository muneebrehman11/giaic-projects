import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.title("🔄 Universal Unit Converter")

# Category selection
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Conversion dictionaries
length_units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
weight_units = {"Grams": 1, "Kilograms": 1000, "Pounds": 453.592}
temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Input section
st.markdown("### Enter value and select units:")

value = st.number_input("Value", min_value=0.0, format="%.4f")

# Unit conversion logic
if category == "Length":
    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))

    result = value * length_units[from_unit] / length_units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))

    result = value * weight_units[from_unit] / weight_units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)

    def convert_temperature(val, from_u, to_u):
        if from_u == to_u:
            return val
        if from_u == "Celsius":
            if to_u == "Fahrenheit":
                return (val * 9/5) + 32
            elif to_u == "Kelvin":
                return val + 273.15
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return (val - 32) * 5/9
            elif to_u == "Kelvin":
                return (val - 32) * 5/9 + 273.15
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return val - 273.15
            elif to_u == "Fahrenheit":
                return (val - 273.15) * 9/5 + 32

    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
