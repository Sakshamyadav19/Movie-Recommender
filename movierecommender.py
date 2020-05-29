import requests
import json
import os

def recommend(movieName):
    baseurl='https://tastedive.com/api/similar'
    params_d = {}
    params_d['q']= movieName
    params_d['k']='373171-Sam-UW1YNP5R'
    params_d['type']= 'movies'
    params_d['limit'] = '5'
    resp = requests.get(baseurl, params=params_d)
    data=json.loads(resp.text)
    for x in range(0,5):
      print(data['Similar']['Results'][x]['Name'])
      
def info(name):
  url='http://www.omdbapi.com/'
  par={}
  par['apikey']='d817e6ac'
  par['t']=name
  resp=requests.get(url,params=par)
  data=json.loads(resp.text)
  print('imdbRating:',data['imdbRating'])
  print('Awards:',data['Awards'])
  print('Plot:',data['Plot'])

os.system('clear')
while True:
    try:
        movie=input('Enter Movie:')
        info(movie)
    except:
        os.system('clear')
        continue
    else:
        break
print('===========')
print('Recommedations')
try:
    recommend(movie)
except:
    print("OOPS! Unable to find Recommendations for this Movie...")

