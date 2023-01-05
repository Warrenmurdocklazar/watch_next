import spacy

nlp = spacy.load(
    'en_core_web_md')

movie_list = []
list_1 = []

file = open("movies.txt","r")
user = file.readlines()

for i in user:
    movie_list.append(i.split("\n"))

planet_hulk = "Will he save their word or destroy it? When Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunatetly, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
planet_hulk_1 = nlp(planet_hulk)


for token in movie_list:
    token = nlp(token).similarity(planet_hulk_1)
    print(token)

x = 0
for i in list_1:
    if i == max(list):
        print(f"The most similar film is,{movie_list[x]}")
    x +=1