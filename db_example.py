from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

forties = list(db.users.find({'age':40}))
##print(all_users[0])  # 0번째 결과값을 보기
#print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기

for user in forties:  # 반복문을 돌며 모든 결과값을 보기
    print(user)

dumbles = db.users.find_one({'name':'덤블도어'})

print(dumbles)

dumbles_filterid =  db.users.find_one({'name':'덤블도어'},{'_id':False})
print(dumbles_filterid)

db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})

user = db.users.find_one({'name': '덤블도어'})
print(user)

db.users.delete_one({'name':'론'})
user = db.users.find_one({'name':'론'})
print(user)