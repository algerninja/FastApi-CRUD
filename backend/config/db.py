from pymongo import MongoClient

engine = MongoClient()
conn = engine["dashboard_sinco"]
