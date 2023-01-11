#import spacy 

import spacy

nlp = spacy.load(
    'en_core_web_md')

#defined lists needed to allow similarity comparison between movie description and movies.txt file

movie_list_read_in = []
similarity_list = []
static_movie_list = []

#read in movies.txt file and append the string into movie_list_read_in

file = open("movies.txt","r")
user = file.readlines()
for i in user:
    movie_list_read_in.append(i)

#movie description used to compare against movies.txt
planet_hulk = "Will he save their word or destroy it? When Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunatetly, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
planet_hulk_1 = nlp(planet_hulk)

#for statement that allows SpaCy to run the similarity comparison, the numbers are then appened to similarity_list
for token in movie_list_read_in:
    token = nlp(token).similarity(planet_hulk_1)
    similarity_list.append(token)

#a copy of movies.txt is split into static_movie_list so each movie holds it's own value in the list 
for i in user:
    static_movie_list.append(i.split("\n"))

#final for statement that identifies the max value in similarity list and it's position in the list. This position is then used to call upon the movies name and description from the static_movie_list
x = len(similarity_list)
for i in range(x):
    if similarity_list[i] == max(similarity_list):
         print(f"The most similar film to Planet Hulk is: \n {static_movie_list[i]}")