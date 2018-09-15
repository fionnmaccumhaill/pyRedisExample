import redis

redis_db = redis.StrictRedis(host="redis", port=6379, db=0)
print(redis_db.keys())

pydict = {"CT"="Connecticut", "OH"="Ohio", "TX" ="Texas"}
redis_db.set('CT', 'Connecticut')
redis_db.set('OH', 'Ohio')
print(redis_db.keys())

print( "Good bye!" )