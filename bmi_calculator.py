import streamlit as st

# App Title
st.set_page_config(page_title="Body Mass Index Calculator", page_icon="💪", layout="centered")

st.markdown(
    "<h1 style='text-align: center; '>Body Mass Index Calculator</h1>",
    unsafe_allow_html=True,
)

st.write("Use this calculator to check your **Body Mass Index (BMI)** based on your weight and height.")

# User Inputs
st.markdown("### Enter your details:")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)

with col2:
    st.markdown("**Height**")
    feet = st.number_input("Feet", min_value=0, max_value=8, step=1)
    inches = st.number_input("Inches", min_value=0, max_value=11, step=1)

# Button to calculate Body Mass Index
if st.button("Calculate Body Mass Index"):
    # Convert height to meters
    total_inches = (feet * 12) + inches
    height_m = total_inches * 0.0254  # 1 inch = 0.0254 meters

    if height_m > 0:
        body_mass_index = weight / (height_m ** 2)

        # Display result
        st.markdown(
            f"<h3 style='text-align: center; color: #117A65;'>Your Body Mass Index is: {body_mass_index:.2f}</h3>",
            unsafe_allow_html=True,
        )

        # Interpretation based on Body Mass Index ranges
        if body_mass_index < 18.5:
            st.warning("⚠️ You are **Underweight**. Consider a balanced diet and professional advice.")
        elif 18.5 <= body_mass_index < 24.9:
            st.success("✅ You are in the **Healthy** range. Keep maintaining your lifestyle!")
        elif 25 <= body_mass_index < 29.9:
            st.info("ℹ️ You are **Overweight**. Consider regular exercise and a healthy diet.")
        else:
            st.error("❌ You are **Obese**. Medical consultation is highly recommended.")
    else:
        st.error("Please enter a valid height in feet and inches.")
