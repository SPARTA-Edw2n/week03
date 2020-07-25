from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'월-E'})
target_score = movie['star']
same_scores = list(db.movies.find({'star':target_score}))

for movie in same_scores:
    print(movie['title'])
    db.movies.update_many({'star':target_score},{'$set':{'star':0}})