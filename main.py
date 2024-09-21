import streamlit as st

# Function to calculate ATRIA Bleeding Risk Score
def calculate_atria(age, anemia, renal_disease, hypertension, prior_bleeding):
    score = 0
    
    # Age points
    if age >= 75:
        score += 3
    
    # Anemia
    if anemia == 'Yes':
        score += 3
    
    # Renal Disease
    if renal_disease == 'Yes':
        score += 3
    
    # Hypertension
    if hypertension == 'Yes':
        score += 1
    
    # Prior Bleeding
    if prior_bleeding == 'Yes':
        score += 1
    
    return score

# Streamlit App Description
st.title("ATRIA Bleeding Risk Score Calculator")
st.write("""
This app calculates the ATRIA (Anticoagulation and Risk Factors in Atrial Fibrillation) Bleeding Risk Score. The ATRIA score is used to assess the risk of bleeding in patients with atrial fibrillation who are undergoing anticoagulation therapy.
""")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=60)
anemia = st.selectbox("Do you have a history of anemia?", ["No", "Yes"])
renal_disease = st.selectbox("Do you have a history of severe renal disease?", ["No", "Yes"])
hypertension = st.selectbox("Do you have a history of hypertension?", ["No", "Yes"])
prior_bleeding = st.selectbox("Do you have a history of prior bleeding?", ["No", "Yes"])

# Calculate ATRIA Score
if st.button("Calculate ATRIA Score"):
    atria_score = calculate_atria(age, anemia, renal_disease, hypertension, prior_bleeding)
    st.write(f"ATRIA Bleeding Risk Score: {atria_score}")
    
    # Display risk category based on score
    if atria_score == 0:
        st.write("Low risk of bleeding.")
    elif 1 <= atria_score <= 3:
        st.write("Moderate risk of bleeding.")
    else:
        st.write("High risk of bleeding.")
