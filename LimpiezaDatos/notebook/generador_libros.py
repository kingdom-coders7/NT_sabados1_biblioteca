import pandas as pd
import random

data = []

for _ in range(100):

    book = {
        "id_books": random.randint(1000,9999),
        "title": f"Libro {_}",
        "author": random.choice(["Borges", "Asimov", "Cortázar"]),
        "editor": random.choice(["Planeta", "Norma"]),
        "pages": random.randint(100,1200),
        "id_gender": random.randint(1,12),
        "id_stand": random.randint(0,3)
    }

    data.append(book)

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)

print("CSV generado")