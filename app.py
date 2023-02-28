# import main Flask class and request object
from flask import Flask, request
from flask_cors import CORS, cross_origin
from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from id_label_map import *

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = None
processor = None

@app.before_first_request
def before_first_request():
    # This method will setup the dataframe and model
    # if we run the application using the flask command
    global model, processor

    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("eeshclusive/captionary-BLIP")

@app.route('/')
def home():
    return("Captionary API")
@app.route('/score')
def score():
    image_url = request.args.get('image_url')
    id = request.args.get('id')
    global model
    global processor
    image = Image.open(requests.get(image_url, stream = True).raw)
    inputs = processor(images=image, return_tensors="pt")
    pixel_values = inputs.pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    score = int(generated_caption == id_label_map[id])
    
    return str(score)

if __name__ == '__main__':
    # This method will setup the dataframe and model
    # if we run the application using the python3 command
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("eeshclusive/captionary-BLIP")
    # run app in debug mode on port 8082
    app.run(debug=True, port=8000, host='0.0.0.0')