import pandas as pd
import random


data = []

for _ in range(100):

    stand = {

        "id_stand": random.choice([
            "EST001",
            "EST002",
            "EST003"
        ]),

        "location": random.choice([
            "Fundamentos",
            "Desarrollo Web y Móvil",
            "Ciencia de Datos y Arquitectura"
        ])
    }

    data.append(stand)


df = pd.DataFrame(data)

df.to_csv("stands.csv", index=False)

print("CSV generado")