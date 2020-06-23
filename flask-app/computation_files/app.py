from flask import Flask, render_template
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# import computation
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    hists = os.listdir('../computation_files/static/images')
    hists = ['images/' + file for file in hists]
    print(hists)
    return render_template('gallery1.html', hists = hists)
    # image_names = os.listdir('images')
    # image_names = ['images/' + file for file in image_names]
    # #image_names = os.listdir('flask-app/computation_files/images')
    # # render_template('gallery1.html', image_name=image_names)
    # return render_template('gallery1.html', image_name=image_names)

if __name__ == "__main__":
    app.run()
