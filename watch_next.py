#import spacy 

import spacy

nlp = spacy.load(
    'en_core_web_md')

#defined lists needed to allow similarity comparison between given string and movie description in text file

movie_list_read_in = []
similarity_list = []
static_movie_list = []

#read in movies.txt file and append the string into movie_list_read_in

file = open("movies.txt","r")
user = file.read()
print(user)
for i in user:
    movie_list_read_in.append(i)

#movie I will use to find most similar in list with
planet_hulk = "Will he save their word or destroy it? When Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunatetly, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
planet_hulk_1 = nlp(planet_hulk)

#for statement that allows spacy to run the similarity comparison, the numbers are then appened to similarity_list
for token in movie_list_read_in:
    token = nlp(token).similarity(planet_hulk_1)
    similarity_list.append(token)

#static list of films and their descriptions is set up to identify which number in similarity list relates to it
for i in user:
    static_movie_list.append(i.split("\n"))

#final for statement that identifies the max value in similarity list and it's position in the list. This position is then used to call upon the movies name and description from the static_movie_list
x = len(similarity_list)
for i in range(x):
    if similarity_list[i] == max(similarity_list):
         print(f"The most similar film to Planet Hulk is: \n {static_movie_list[i]}")