import os, time, redis

# Externalized configuration! Reads from environment variables
COTS_HOST = os.getenv("COTS_HOST", "localhost")
COTS_PORT = int(os.getenv("COTS_PORT", 6379))

r = redis.Redis(host=COTS_HOST, port=COTS_PORT)
print(f"Connected to COTS dummy! Ping response: {r.ping()}")