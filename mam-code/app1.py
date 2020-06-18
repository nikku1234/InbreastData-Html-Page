from flask import Flask, render_template
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib

app = Flask(__name__)

@app.route('/')
def hello_world():
    ### Generating X,Y coordinaltes to be used in plot
    data = numpy.load('Inbreastdata.npy')
    # print(type(data))
    # print(len(data))
    # print(data.shape)
    # print(data[0])
    # size= len(data)
    # print(size)
# for one file

# filename = "new-image"
# #Save as png
# img_name = filename +".png"
# matplotlib.image.imsave(img_name, data[0])
# print(filename + " was saved")

# for conversion of the files in .npy to .png
# for i in range(size):
#     filename = "image"+str(i)
#     img_name = filename +".png"
#     matplotlib.image.imsave("images/"+img_name, data[i],cmap="gray")
#     print(filename + " was saved")

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    # figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    result = data[0]
    return render_template('gallery1.html', result=result)

if __name__ == "__main__":
    # app.run(port=4555, debug=True)
    app.run()

