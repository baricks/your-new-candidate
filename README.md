#Description
Your New Candidate is a Twitter bot that generates names of new presidential candidates, names of their parties, and a recent headshot. The bot lives here: https://twitter.com/yrcandidate

#How it works
The script generates names of candidates using a Markov chain based on lists of current U.S. senators/house reps. It generates party names using a Markov chain based on a list of third parties in the U.S. It then searches for a headshot on Bing using the candidate name.

#Dependencies/Packages
After setting up a virtual environment, install twython using pip.

#Notes
After registering for API keys from both Twitter and Bing, copy and paste your credentials where noted. Then run "python app.py" from a local server.
