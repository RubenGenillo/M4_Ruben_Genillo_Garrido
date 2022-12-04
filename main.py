#Importa pandas y usa un alias para poder utilizar sus recursos
import pandas as pd
def main():
        #Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
        d = pd.read_csv("imdb_titulos.csv")
        print(d.head(), "\n")

        #Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
        d2 = pd.read_csv("imdb_elenco.csv")
        print(d2.head(), "\n")

        #Mostrar el número de registros del dataframe de titulos
        print("Número de registros del dataframe de titulos: ", len(d))

        #Mostrar el número de registros del dataframe de elenco
        print("Número de registros del dataframe de elenco: ", len(d2), "\n")

        #Mostrar las 5 peliculas más antiguas del listado de titulos
        print("Las 5 peliculas más antiguas son: \n", d.sort_values(by="year").head(), "\n")

        #Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
        print("Las peliculas que en el titulo tienen la palabra 'Dracula' son: \n", d[d["title"].str.contains("Dracula")], "\n")
        print("Y el número total de peliculas que coinciden con este requisito son: ", len(d[d["title"].str.contains("Dracula")]), "\n")

        #Mostrar los 10 titulos más comunes (que más se repiten)
        print("Los 10 titulos más comunes son: \n", d["title"].value_counts().head(10), "\n")

        #Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
        print("La primer pelicula hecha titulada 'Romeo and Juliet' es: \n", d[d["title"] == "Romeo and Juliet"].sort_values(by="year").head(1), "\n")

        #Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
        print("Las peliculas que contienen la palabra 'Exorcist' ordenadas de la más vieja a la más reciente son: \n", d[d["title"].str.contains("Exorcist")].sort_values(by="year"), "\n")

        #Mostrar cuantas peliculas fueron hechas en el año 1950
        print("El número de peliculas hechas en el año 1950 es:", len(d[d["year"] == 1950]), "\n")

        #Mostrar cuantas peliculas fueron hechas de 1950 a 1959
        print("El número de peliculas hechas de 1950 a 1959 es: \n", len(d[(d["year"] >= 1950) & (d["year"] <= 1959)]), "\n")

        #Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
        print("todos los roles o papeles que hubo en la pelicula 'The Godfather':\n", d2[d2["title"] == "The Godfather"]["character"], "\n")
        print("Y el número total de coincidencias es:", (d2[d2["title"] == "The Godfather"]["character"].duplicated()).sum(), "\n")

        #Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958   
        print("El elenco completo ordenado por la clasificacion 'n' de la pelicula 'Dracula' de 1958 es: \n", d2[(d2["title"] == "Dracula") & (d2["year"] == 1958)].sort_values(by="n")[["name","n"]], "\n")

        #Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas 
        print("El número de papeles de 'Bruce Wayne' han sido hechos en la historia de las peliculas es:", len(d2[d2["character"] == "Bruce Wayne"]), "\n")

        #Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
        print("El número de papeles que ha hecho Robert de Niro son:\n", len(d2[d2["name"] == "Robert De Niro"]["character"]), "\n")

        #Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
        print("Listado de papeles como protagonista (n=1) que tuvo el actor 'Charlton Heston' en la década de los 60's, ordenado por año de forma descendente: \n", d2[(d2["name"] == "Charlton Heston") & (d2["n"] == 1) & (d2["year"] >= 1960) & (d2["year"] <= 1969)].sort_values(by="year", ascending=False)[["character", "year"]], "\n")

        #Mostrar cuantos papeles para actores hubo en la década de los 50's
        print("El número de papeles para actores hubo en la década de los 50's fueron:", len(d2[d2["type"] == "actor"]["character"]))

        #Mostrar cuantos papeles para actrices hubo en la década de los 50's
        print("El número de papeles disponibles para actrices en el los años 50's:", len(d2[d2["type"] == "actress"]))

if __name__ == "__main__":
        main()