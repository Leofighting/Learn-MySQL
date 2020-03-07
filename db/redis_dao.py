import redis

# 建立redis连接池
try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        password="123qwe",
        db=1,
        max_connections=20
    )
except Exception as e:
    print(e)
