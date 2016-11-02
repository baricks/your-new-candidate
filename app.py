import httplib, urllib, base64
import requests, json, sys
import markov, regex, random
from twython import Twython
from apscheduler.schedulers.blocking import BlockingScheduler

# Twitter authentication

APP_KEY = 'YOUR-KEY-HERE'
APP_SECRET = 'YOUR-SECRET-HERE'
ACCESS_TOKEN = 'YOUR-TOKEN-HERE'
ACCESS_SECRET = 'YOUR-SECRET-HERE'

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# Bing authentication

# Bing API key
BING_API_KEY = "YOUR-KEY-HERE"

# Generate the content of the tweet

# states
name_list = list()
for line in open('./text/first_names.txt'):
    line = line.strip()
    name_list.append(line)
for i in range(1):
    random_name = random.choice(name_list)

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
model = markov.build_model(line_parties, 3)
markov_parties = markov.generate(model, 3)

full_list_parties = ''.join(markov_parties)
list_parties = full_list_parties.split()

# states
state_list = list()
for line in open('./text/states.txt'):
    line = line.strip()
    state_list.append(line)
for i in range(1):
    random_state = random.choice(state_list)

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
    if (15 > count_letters(line) > 3) and (line.istitle() is True):
        final_list_parties.append(line)

# Bing image search by candidate name
full_name = random_name + " " + final_list_last_names[0]
search_name = full_name + " headshot"

# Search bing using final_party keyword and grab first result

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': BING_API_KEY,
}

params = urllib.urlencode({
    # Request parameters
    'q': search_name,
    'count': '1',
    'offset': '0',
    'mkt': 'en-us',
    'safeSearch': 'Moderate',
})

try:
    conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    # print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

d = json.loads(data)
# pprint(d)
print

if len(d["value"][0]) is 0:
    imgURL = d["value"][0]["contentUrl"]
else:
    imgURL = d["similarTerms"][0]["thumbnail"]

# download URL

# download the image
f = open('speedtest.png','wb')
f.write(urllib.urlopen(imgURL).read())
f.close()
# read the saved image
imagen =  open('speedtest.png', 'rb')
# upload it
image_ids = twitter.upload_media(media=imagen)

# Get the word count
def count_letters(word):
    return len(word) - word.count(' ')

# Construct the tweet
line1 = full_name
line2 = final_list_parties[0] + " " + final_list_parties[1] + " Party"
line3 = random_state
full_sentence = line1 + "\n" + line2 + "\n" + line3

# def cron_job():
if len(full_sentence) < 140:
# send the tweet
    twitter.update_status(status=full_sentence, media_ids=[image_ids['media_id']])
    sys.exit()
else: print "too long"

# scheduler = BlockingScheduler()
# scheduler.add_job(cron_job, 'interval', minutes=30)
# scheduler.start()
