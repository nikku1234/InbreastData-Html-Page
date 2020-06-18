# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib


app = Flask(__name__)

@app.route('/')
def hello():
    ### Generating X,Y coordinaltes to be used in plot
    # numpy.load('Inbreastdata.npy')
    data = numpy.load('Inbreastdata.npy')
    # print(type(data))
    # print(len(data))
    # print(data.shape)
    # print(data[0])
    size= len(data)
    # print(size)
    # X = numpy.linspace(0,10,30)
    # Y = X*X
    ### Generating The Plot
    # plt.plot(X,Y)
    ### Saving plot to disk in png format
    #plt.savefig('/home/AnandSatya/mysite/square_plot.png')
    for i in range(size):
        filename = "image"+str(i)
        img_name = filename +".png"
        matplotlib.image.imsave("images/"+img_name, data[i],cmap="gray")
        print(filename + " was saved")

    # ### Rendering Plot in Html
    # figfile = BytesIO()
    # plt.savefig(figfile, format='png')
    # figfile.seek(0)
    # figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    # result = figdata_png
    # return render_template('gallery1.html', result=result)
    return "Hello World!"

if __name__ == "__main__":
    app.run()