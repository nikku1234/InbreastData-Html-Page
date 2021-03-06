import numpy
from numpy import savetxt
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
from PIL import Image   

### Generating X,Y coordinaltes to be used in plot
data = numpy.load('../Inbreastdata.npy')
print(type(data))
print(len(data))
print(data.shape)
print(data[0])
size= len(data)
print(size)
# for one file

# filename = "new-image"
# #Save as png
# img_name = filename +".png"
# matplotlib.image.imsave(img_name, data[0])
# print(filename + " was saved")

# for conversion of the files in .npy to .png
for i in range(size):
    filename = "image"+str(i)
    img_name = filename +".png"
    matplotlib.image.imsave("images/"+img_name, data[i],cmap="gray")
    print(filename + " was saved")

# for conversion of the files in .npy to plt images
for i in range(size):
    X = numpy.linspace(i,10,30)
    Y = X*X
    ### Generating The Plot
    plt.plot(X,Y)
    filename = "image_plot"+str(i)
    img_name = filename +".png"
    ### Saving plot to disk in png format
    plt.savefig("plots/"+filename+'.png')




# # savetxt('data.csv', data, delimiter=',')
# # numpy.savetxt('data.txt',data, delimiter=' ')
# X = numpy.linspace(0,10,30)
# Y = X*X
# ### Generating The Plot
# plt.plot(X,Y)
# ### Saving plot to disk in png format
# plt.savefig('plt.png')

### Rendering Plot in Html
figfile = BytesIO()
plt.savefig(figfile, format='png')
figfile.seek(0)
figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
result = figdata_png