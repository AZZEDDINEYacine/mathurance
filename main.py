import pandas as pd

data_path = "data/Mathurance Hackathon/Base de Données MATHURANCE.xlsm"

def xlsm_to_csv(path):
    data = pd.read_excel(path)
    data.to_csv("data/data.csv")

xlsm_to_csv(data_path)