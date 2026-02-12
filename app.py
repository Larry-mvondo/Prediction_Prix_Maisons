import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load("Prediction_Prix_Maisons.pkl")

st.set_page_config(page_title="Prédiction Prix Maisons", page_icon="🏠", layout="centered")

st.title("🏠 Application de Prédiction du Prix des Maisons (Boston Housing)")

st.write("Entrez les caractéristiques de la maison pour obtenir une estimation du prix.")

# Saisie des variables
Taux_criminalite = st.number_input("Taux de criminalité", min_value=0.0, step=0.1)
Prop_terrains_resid = st.number_input("Proportion terrains résidentiels", min_value=0.0, step=0.1)
Prop_acres_indus = st.number_input("Proportion acres industriels", min_value=0.0, step=0.1)
Bordure_riviere = st.selectbox("Bordure rivière (CHAS)", [0, 1])  # 0 = Non, 1 = Oui
Concentration_NO2 = st.number_input("Concentration NO2", min_value=0.0, step=0.01)
Nb_pieces_logement = st.number_input("Nombre moyen de pièces par logement", min_value=1.0, step=0.1)
Prop_log_construits = st.number_input("Proportion logements construits avant 1940", min_value=0.0, step=1.0)
Dist_ponderees_emploi = st.number_input("Distances pondérées à l'emploi", min_value=0.0, step=0.1)
Accessibilite_autoroute = st.number_input("Accessibilité autoroutes", min_value=0.0, step=1.0)
Taux_impot_foncier = st.number_input("Taux d'imposition foncière", min_value=0.0, step=1.0)
Ratio_eleve_prof = st.number_input("Ratio élèves/professeurs", min_value=0.0, step=0.1)
Prop_noirs_ville = st.number_input("Proportion de noirs dans la ville", min_value=0.0, step=0.1)
Pourcentage_pop_inf = st.number_input("Pourcentage de population à faible revenu", min_value=0.0, step=0.1)



# Créer le DataFrame d'entrée (sans one-hot encore)
input_data = pd.DataFrame({
    "Taux_criminalite": [Taux_criminalite],
    "Prop_terrains_resid": [Prop_terrains_resid],
    "Prop_acres_indus": [Prop_acres_indus],
    "Concentration_NO2": [Concentration_NO2],
    "Nb_pieces_logement": [Nb_pieces_logement],
    "Prop_log_construits": [Prop_log_construits],
    "Dist_ponderees_emploi": [Dist_ponderees_emploi],
    "Accessibilite_autoroute": [Accessibilite_autoroute],
    "Taux_impot_foncier": [Taux_impot_foncier],
    "Ratio_eleve_prof": [Ratio_eleve_prof],
    "Prop_noirs_ville": [Prop_noirs_ville],
    "Pourcentage_pop_inf": [Pourcentage_pop_inf],
    "Bordure_riviere_1.0": [1 if Bordure_riviere == 1 else 0]
})



# S’assurer que toutes les colonnes attendues par le modèle existent
for col in model.feature_names_in_:
    if col not in input_data.columns:
        input_data[col] = 0

# Réordonner les colonnes
input_data = input_data[model.feature_names_in_]

# Bouton de prédiction
if st.button("Prédire le prix"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Prix estimé de la maison : **{prediction:.2f} k$**")

