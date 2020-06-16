from flask import Flask, render_template
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)

@app.route('/')
def hello_world():
    ### Generating X,Y coordinaltes to be used in plot
    numpy.load('../Inbreastdata.npy')
    X = numpy.linspace(0,10,30)
    Y = X*X
    ### Generating The Plot
    plt.plot(X,Y)
    ### Saving plot to disk in png format
    #plt.savefig('/home/AnandSatya/mysite/square_plot.png')

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    result = figdata_png
    return render_template('gallery1.html', result=result)

if __name__ == "__main__":
    app.run(port=4555, debug=True)
