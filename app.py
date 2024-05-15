from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# Replace '<password>' with your actual password
client = MongoClient("mongodb+srv://morsewallace254:whoami@cluster0.5pxkesk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["dreamteam"]
collection = db["dreamteam_collection"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_item():
    if request.method == 'POST':
        data = request.form.get('data')
        collection.insert_one({'data': data})
        return 'Item added successfully!', 200

if __name__ == '__main__':
    app.run()
