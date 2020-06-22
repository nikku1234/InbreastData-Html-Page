
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

hists = os.listdir('../computation_files/images')
hists = ['..computation_files/images/' + file for file in hists]
print(hists)
    # return render_template('gallery1.html', hists = hists)
    # http://127.0.0.1:5000/static/%7B%7Bhist%7D%7D