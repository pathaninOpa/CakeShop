from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import time

class MongoServer:
    def __init__(self, uri):
        self.client = MongoClient(uri, server_api = ServerApi('1'))
        self.db = None

    #Timeout for 60 seconds
    def connect(self, timeout = 60 * 1000):
        start = time.time()
        try:
            self.client.admin.command('ping', maxTimeMS = timeout)
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print('Connection failed: ', e)
        finally:
            print(f'Time taken: {(time.time() - start)}s', )

if __name__ == "__main__":
    env_file = "server/.env"
    if os.path.exists(env_file):
        load_dotenv(env_file)
        mongo_key = os.getenv("MONGO_KEY")
        uri = f"mongodb+srv://master:{mongo_key}@cluster0.symdeqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        MongoServer(uri).connect()
    else:
        print(f"{env_file} does not exist")