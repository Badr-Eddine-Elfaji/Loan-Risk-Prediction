import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn 


# Load the saved model and scaler
with open('gb_model.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

model = loaded_data["model"]
scaler = loaded_data["scaler"]

# Set up the App Header
st.title("Application de Prédiction du Risque")
st.write("""
Cette application prédit le niveau de risque basé sur les caractéristiques du client.
""")

# Create Sidebar for User Input
st.sidebar.header("Caractéristiques du Client")
def user_input():
    # Use two columns inside the sidebar
    col_a, col_b = st.sidebar.columns(2)
    
    with col_a:
        st.caption("🔢 Numériques")
        a1 = st.slider('A1', 13.75, 80.25, 31.56) # Min-Max
        a2 = st.slider('A2', 0.0, 28.0, 4.75)     
        a3 = st.slider('A3', 0.0, 2000.0, 184.01) 
        a4 = st.slider('A4', 0.0, 100000.0, 5.0)  

    with col_b:
        st.caption("🗂️ Catégories")
        a5 = st.selectbox('A5', ('g', 'p', 'gg'))
        a6 = st.selectbox('A6', ('c', 'q', 'w', 'i', 'aa', 'ff', 'k', 'cc', 'x', 'm', 'd', 'e', 'j', 'r'))
        a7 = st.selectbox('A7', ('v', 'h', 'bb', 'ff', 'j', 'z', 'dd', 'n', 'o'))

    data = {
        'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
        'A5': a5, 'A6': a6, 'A7': a7
    }
    return pd.DataFrame(data, index=[0])

# Process the Input Data
df_input = user_input()

st.subheader("Données saisies par l'utilisateur :")
st.write(df_input)

# --- Apply the same data transformation ---

# Load raw data to ensure all categorical dummy columns match training
df_raw = pd.read_excel("Risque_data.xlsx")
X_raw = df_raw.drop('Risque', axis=1)

# Step A: Winsorizing
df_input['A1'] = np.clip(df_input['A1'], 13.75, 60.37) 
df_input['A2'] = np.clip(df_input['A2'], 0.0, 16.62)
df_input['A3'] = np.clip(df_input['A3'], 0.0, 560.0)
df_input['A4'] = np.clip(df_input['A4'], 0.0, 990.0)

# Step B: Log Transformation
num_cols = ['A1', 'A2', 'A3', 'A4']
df_input[num_cols] = np.log1p(df_input[num_cols])

# Step C: One-Hot Encoding & Alignment
df_encoded = pd.get_dummies(df_input)
X_final = df_encoded.reindex(columns=pd.get_dummies(X_raw).columns, fill_value=0)

# Step D: Robust Scaling
X_scaled = scaler.transform(X_final)

# Make Prediction
if st.button('Prédire le Risque'):
    prediction = model.predict(X_scaled)
    prediction_proba = model.predict_proba(X_scaled)

    st.subheader("Résultat de la Prédiction :")
    risk_label = "Risque Elevé" if prediction[0] == 1 else "Risque Faible"
    
    if prediction[0] == 1:
        st.error(f"Le niveau de risque est : **{risk_label}**")
    else:
        st.success(f"Le niveau de risque est : **{risk_label}**")
    
    st.write(f"Confiance : **{np.max(prediction_proba) * 100:.2f}%**")