# randompass
A random secure password generator
<br /><a href="https://randompass.herokuapp.com/">Live Demo</a><br />
<a href="https://randompass.herokuapp.com/"><img src="https://i.ibb.co/BV7ZSbY/Screenshot-from-2020-10-04-17-22-49.png" alt="Screenshot-from-2020-10-04-17-22-49" border="0"></a><br>
## Features
This idea was inspired by a series of videos on passwords made by Computherphile on their youtube channel. The general idea is to create passwords that are easy for humans to remember but hard for computers to crack. We really encourage you to watch the videos displayed on the website as they will explain why we need to pay more attention to the way we choose our passwords<br />
- 20.000 English Words: Picks 4 random words from a list of 20.000 english words separated by spaces. You can find the full list <a href="https://github.com/first20hours/google-10000-english/blob/master/20k.txt">here</a><br>
- Diceware: Picks 4 random words from a list of 7776 words, every word has a number assigned to it, the code throws a dice 5 times and based on the combination of those 5 numbers picks the word assigned to that number until 4 words form part of the password. You can learn more on the <a href="https://theworld.com/~reinhold/diceware.html">diceware site</a><br>
- API: Get a password via GET method to the endpoints declared on the site<br>

Example API call (Python)
```
import requests
import json

response = requests.get('https://randompass.herokuapp.com/api/diceware')
data = response.json()
print(data)
```
## Tools
- Django<br>
- Heroku
