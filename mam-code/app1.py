from flask import Flask, render_template
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)

@app.route('/')
def hello_world():
    ### Generating X,Y coordinaltes to be used in plot
    data = numpy.load('Inbreastdata.npy')

    # for one file

    # filename = "new-image"
    # #Save as png
    # img_name = filename +".png"
    # matplotlib.image.imsave(img_name, data[0])
# print(filename + " was saved")



    # X = numpy.linspace(0,10,30)
    # Y = X*X
    ### Generating The Plot
    plt.plot(data[0])

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    result = figdata_png
    return render_template('gallery1.html', result=result)

if __name__ == "__main__":
    app.run()
