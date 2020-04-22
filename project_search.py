import requests

url = 'https://api.edamam.com/search?q=cheese&app_id=2ab24719&app_key=b72191d1937d2cfa6ccc312e1b7f12e1'
requests.get(url)

#ask user what they ingredient they are searching for

user_question = input('What ingredient are looking for?')
print(user_question)

# Create a function that makes a request to the Edamam API with the required ingredient aspart of the search query

url = 'https://api.edamam.com/search?q=cheese&app_id=2ab24719&app_key=b72191d1937d2cfa6ccc312e1b7f12e1'.format(user_question)
response = requests.get(url)
print(response)