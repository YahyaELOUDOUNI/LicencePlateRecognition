import streamlit as st
import os
import subprocess
from moviepy import VideoFileClip

# Titre de l'application
st.title("Système de Reconnaissance de Plaques - YOLOv8")

# Section de téléchargement de la vidéo
st.subheader("Téléchargez votre vidéo")
uploaded_file = st.file_uploader("Glissez-déposez ou cliquez pour télécharger une vidéo", type=["mp4"])

# Fonction pour exécuter des scripts Python
def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
        st.success(f"Exécution de {script_name} terminée avec succès.")
    except subprocess.CalledProcessError as e:
        st.error(f"Erreur lors de l'exécution de {script_name} : {e}")

if uploaded_file is not None:
    # Sauvegarder la vidéo téléchargée temporairement
    input_path = "./uploaded_video.mp4"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.success("Vidéo téléchargée avec succès !")

    # Étape 1 : Détection initiale
    st.subheader("Étape 1 : Détection et extraction initiales")
    try:
        os.rename(input_path, "sample.mp4")  # Renommer la vidéo téléchargée en "sample.mp4" pour correspondre à main.py
        st.write("Traitement de la vidéo en cours...")
        run_script("main.py")  # Appeler le script main.py
    except Exception as e:
        st.error(f"Erreur lors de la détection initiale : {e}")

    # Étape 2 : Interpolation des données manquantes
    st.subheader("Étape 2 : Interpolation des données manquantes")
    try:
        st.write("Interpolation des données...")
        run_script("add_missing_data.py")  # Appeler le script add_missing_data.py
    except Exception as e:
        st.error(f"Erreur lors de l'interpolation des données : {e}")

    # Étape 3 : Génération de la vidéo finale
    st.subheader("Étape 3 : Génération de la vidéo finale")

    def verify_and_convert_video(input_path, output_path):
        """Vérifie et convertit la vidéo au format compatible si nécessaire."""
        try:
            clip = VideoFileClip(input_path)
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            return True
        except Exception as e:
            return False, str(e)

    try:
        st.write("Traitement en cours ...")
        run_script("visualize.py")  # Appeler le script visualize.py
        output_path = "out.mp4"

        if os.path.exists(output_path):
            # Vérifiez si la vidéo est lisible et convertissez-la si nécessaire
            converted = verify_and_convert_video(output_path, "output_converted.mp4")
            if converted == True:
                st.success("Vidéo finale générée et convertie avec succès !")
                st.video("output_converted.mp4")  # Afficher la vidéo convertie
                # Option pour télécharger la vidéo convertie
                with open("output_converted.mp4", "rb") as file:
                    st.download_button(
                        label="Télécharger la vidéo finale",
                        data=file,
                        file_name="output_converted.mp4",
                        mime="video/mp4"
                    )
            else:
                st.error(f"Erreur lors de la conversion de la vidéo : {converted[1]}")
        else:
            st.error("Fichier 'out.mp4' introuvable après la visualisation.")
    except Exception as e:
        st.error(f"Erreur lors de la génération de la vidéo finale : {e}")
