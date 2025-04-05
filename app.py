import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

# Vérifier si le serveur est actif
@app.route('/api/alive', methods=['GET'])
def alive():
    """renvoie le message Alive si le serveur est en fonctionnement"""
    return jsonify({"message": "Alive"}), 200


# Liste de toutes les associations
@app.route('/api/associations', methods=['GET'])
def get_associations():
    """retourne lz liste de toutes les assos"""
    ids = associations_df['id'].tolist()
    return jsonify({"associations": ids}), 200

# Détails d'une association
@app.route('/api/association/<int:id>', methods=['GET'])
def get_association(id):
    """détails de l'asso donnée par son id"""
    assoc = associations_df[associations_df['id'] == id]
    if assoc.empty:
        return jsonify({"error": "Association not found"}), 404  # message d'erreur
    return jsonify(assoc.iloc[0].to_dict()), 200


# Liste de tous les événements
@app.route('/api/evenements', methods=['GET'])
def get_evenements():
    """liste des events d'une assos"""
    ids = evenements_df['id'].tolist()
    return jsonify({"evenements": ids}), 200


# Détails d’un événement
@app.route('/api/evenement/<int:id>', methods=['GET'])
def get_evenement(id):
    event = evenements_df[evenements_df['id'] == id]
    if event.empty:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(event.iloc[0].to_dict()), 200


# Événements d’une association
@app.route('/api/association/<int:id>/evenements', methods=['GET'])
def get_evenements_by_asso(id):
  pass
#pas compris


# Associations par type
@app.route('/api/associations/type/<type>', methods=['GET'])
def get_associations_by_type(type):
    pass
    # pas compris pour celle la 

if __name__ == '__main__':
    app.run(debug=False)
