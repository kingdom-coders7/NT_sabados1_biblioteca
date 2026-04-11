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
        libros.append(book)
        return libros