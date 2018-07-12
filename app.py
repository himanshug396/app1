from flask import Flask, render_template
import os
import io
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches



app = Flask(__name__,static_folder='static')


def get_plot(value):
    if(value=='bar'):
        bar_graph()
    png = pltToPng() # convert plot to SVG
    filename = 'image.png'
    # BASE_DIR = os.path.abspath("")
    # full_path = os.path.join(BASE_DIR,'static',filename)
    full_path = os.path.join('static',filename)
    with open(full_path, 'wb') as f:
        f.write(png)
    plt.cla()    #closes the plt buffer to reuse it
    image_url = full_path 
    return image_url

def pltToPng():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def bar_graph():
    vals = [59.69, 16, 9.94, 7.79, 5.68, 0.54]
    vals.reverse()
    X = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia']
    n = len(vals)
    width=0.8
    _X = np.arange(len(X))
    colors = ['green','blue','red','orange','black','yellow']
    plt.bar(range(n), X, align='center',color=colors)
    # for i in range(n):
    #     plt.bar(_X - width/2. + i/float(n)*width, vals[i],width=width/float(n),color = colors[i], align="edge")
    

    patches = []
    for i in range(n):
        patch = mpatches.Patch(color = colors[n-1-i],label=X[i])
        patches.append(patch)
    plt.legend(handles=patches)

    plt.ylabel('Pop Count')
    plt.title('Number of pop with country')

    plt.yticks(_X, vals) #for y-axis labels

    # plt.xticks(_X, X) #for x-axis labels



@app.route("/")
def main():
    bar_graph = get_plot('bar')
    return render_template('index.html',bar_graph=bar_graph)

if __name__ == "__main__":
    app.run(debug=True)





