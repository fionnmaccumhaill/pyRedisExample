import redis

redis_db = redis.StrictRedis(host="redis", port=6379, db=0)
print(redis_db.keys())

redis_db.set('CT', 'Connecticut')
redis_db.set('OH', 'Ohio')
print(redis_db.keys())

ctstr = redis_db.get("CT").decode("utf-8")
print(ctstr)

print( "Good bye!" )