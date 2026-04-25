import random

def simular_libros(numLibros):
    
    #Semilla de datos
    listaLibros=["Codigo limpio", "Fundamentos de programación en C#", "Python 3", "Javascript en un fin de semana", "C++ practico"]

    listaAutores=["Brian W.", "Luis Joyanes Aguilar", "Ricardo W.", "Hadley Wickham", "Jesús Ormaza"]

    listaEditores=["O’Reilly Media", "Packt Publishing", "Apress (Springer)", "McGraw-Hill Education", "Anaya Multimedia"]

    listadDeCodigos=["SBN123", "SBN001", "SBN423", "SBN879", "SBN400"]


    libros=[]

    for _ in range(numLibros):
        book={
            "id_books": random.choice(listadDeCodigos),
            "title":random.choice(listaLibros),
            "author":random.choice(listaAutores),
            "editor":random.choice(listaEditores),
            "pages":random.randint(100, 1200),
            "id_gender":random.randint(1, 12),
            "id_stand":random.randint(0,3)
        }

        #Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.1:
            book["id_books"] = random.choice([None, 0,1])
            book["title"] = " " + book["title"] + " "
        elif probabilidadError < 0.25:
            book["author"] = None
        elif probabilidadError < 0.4:
            book["id_books"] = book["id_books"].lower()
            book["pages"] = random.choice([-1, -10])
            book["id_stand"] = None 
            book["id_gender"] = None
        elif probabilidadError < 0.7:
            book["author"] = random.choice(["batman", "un humano", "??"])
        elif probabilidadError < 0.9:
            book["editor"] = random.choice(["colanta", "sony", "cocacola"])
        libros.append(book)
        
    return libros