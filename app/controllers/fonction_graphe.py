import json
import matplotlib.pyplot as plt


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def create_graphs_from_json(data):
    # Créer les graphiques en fonction des données JSON
    # (Votre implémentation de cette fonction)

    # Chemin vers le fichier JSON contenant les données
    file_path = "app\\data\\global_metrics.json"

# Charger les données JSON à partir du fichier
    data = load_json_data(file_path)

# Créer les graphiques à partir des données JSON
    create_graphs_from_json(data)
