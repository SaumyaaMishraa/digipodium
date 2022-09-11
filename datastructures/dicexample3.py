#pprint changes the order where as thr print does not change the order
from pprint import pprint
movies= {}
#[''] for adding a single value in set
movies['sholay']='2 friens fight with gabbar'
movies['inception']='no summary available'
print(movies)

#adding multiple
movies.update(
  ironman='man builds a suit that is not iron',
  hulk='gaint green man ',
  batman= 'man dressed as a bat')
movies.pop('sholay')

#updatemovies
movies['inception']='dream with in dream with recursion logic'
#update2
movies['batman']+=' and fight with villans'
pprint (movies)

