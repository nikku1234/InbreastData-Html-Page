from flask import Flask, render_template
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64

### Generating X,Y coordinaltes to be used in plot
numpy.load('new-array.npy')
#need to check the data file
X = numpy.linspace(0,10,30)
Y = X*X
### Generating The Plot
plt.plot(X,Y)
### Saving plot to disk in png format
plt.savefig('example_plot.png')
### Rendering Plot in Html
figfile = BytesIO()
plt.savefig(figfile, format='png')
figfile.seek(0)
figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
result = figdata_png