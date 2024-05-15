from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
# Replace '<password>' with your actual password
client = MongoClient("mongodb+srv://morsewallace254:<password>@cluster0.isxlant.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["your_database_name"]
collection = db["your_collection_name"]

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    collection.insert_one(data)
    return 'Item added successfully!', 200

if __name__ == '__main__':
    app.run()
