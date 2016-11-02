import markov
import regex
import random

# states
name_list = list()
for line in open('./text/first_names.txt'):
    line = line.strip()
    name_list.append(line)
for i in range(1):
    random_name_0 = random.choice(name_list)
    random_name_1 = random.choice(name_list)
    random_name_2 = random.choice(name_list)
# last names
text_last_names = open("./text/last_names.txt").read()
line_last_names = text_last_names.strip()
model = markov.build_model(line_last_names, 2)
markov_last_names = markov.generate(model, 2)

full_list_last_names = ''.join(markov_last_names)
list_last_names = full_list_last_names.split()

# parties
text_parties = open("./text/parties.txt").read()
line_parties = text_parties.strip()
model = markov.build_model(line_parties, 2)
markov_parties = markov.generate(model, 2)

full_list_parties = ''.join(markov_parties)
list_parties = full_list_parties.split()

# cities
text_cities = open("./text/cities.txt").read()
line_cities = text_cities.strip()
model = markov.build_model(line_cities, 2)
markov_cities = markov.generate(model, 2)

full_list_cities = ''.join(markov_cities)
list_cities = full_list_cities.split()

# states
state_list = list()
for line in open('./text/states.txt'):
    line = line.strip()
    state_list.append(line)
for i in range(1):
    random_state_0 = random.choice(state_list)
    random_state_1 = random.choice(state_list)
    random_state_2 = random.choice(state_list)

# markov count
def count_letters(word):
    return len(word) - word.count(' ')

# final list _ last names
final_list_last_names = []
for line in list_last_names:
    if (10 > count_letters(line) > 4) and (line.istitle() is True):
        final_list_last_names.append(line)

# final list _ parties
final_list_parties = []
for line in list_parties:
    if (15 > count_letters(line) > 4) and (line.istitle() is True):
        final_list_parties.append(line)

# final list _ cities
final_list_cities = []
for line in list_cities:
    if (12 > count_letters(line) > 4) and (line.istitle() is True):
        final_list_cities.append(line)

print
print "---------------OFFICIAL GENERAL ELECTION BALLOT---------------"
print
print "YOU MAY USE PEN (BLACK OR BLUE) OR PENCIL."
print "TO ENSURE YOUR VOTE COUNTS, COMPLETELY FILL IN THE OVAL (*) TO THE LEFT OF THE RESPONSE OF YOUR CHOICE."
print
print
print " (    )   " + random_name_0 + " " + final_list_last_names[0]
print "          " + final_list_parties[0] + " Party"
print "          " + final_list_cities[0] + ", " + random_state_0
print
print " (    )   " + random_name_1 + " " + final_list_last_names[1]
print "          " + final_list_parties[1] + " Party"
print "          " + final_list_cities[1] + ", " + random_state_1
print
print " (    )   " + random_name_2 + " " + final_list_last_names[2]
print "          " + final_list_parties[2] + " Party"
print "          " + final_list_cities[2] + ", " + random_state_2
print
print
