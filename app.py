from flask import Flask, render_template, request
from pymongo import MongoClient
import logging
import ssl

# Configure logging
logging.basicConfig(level=logging.DEBUG)
# Enable SSL debugging
ssl_logger = logging.getLogger('ssl')
ssl_logger.setLevel(logging.DEBUG)


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
    try:
        if request.method == 'POST':
            data = request.form.get('data')
            logging.debug(f"Received data: {data}")
            collection.insert_one({'data': data})
            logging.info("Item added successfully!")
            return 'Item added successfully!', 200
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run()
