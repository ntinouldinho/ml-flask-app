import numpy as np
from PIL import Image
import keras


def softmax( x, ax=1 ):
    m = np.max( x, axis=ax, keepdims=True )#max per row
    p = np.exp( x - m )
    return ( p / np.sum(p,axis=ax,keepdims=True) )

def ml_softmax_test(title):

    W1 = np.load('W1.npy')
    W2 = np.load('W2.npy')

    im = Image.open(title)
    pixels = list(im.getdata())
    newPixels = [1-pixels[x][0]/255.0 for x in range(len(pixels)) ]
    newPixels.append(1.0)
    
    Z = np.cos(np.dot(newPixels, W1.T))
    
    W2= W2[:,1:]
    
    ytest = softmax( Z.dot(W2.T),0 )
    
    ttest = np.argmax(ytest, 0)
    return ttest

def cnn_test(title):
    mdl = keras.models.load_model('my_model')

    im = Image.open(title)
    pixels = list(im.getdata())
    newPixels =np.array([1-pixels[x][0]/255.0 for x in range(len(pixels)) ])
    newPixels = newPixels.reshape(1,28, 28)

    pred = mdl.predict([newPixels])

    return np.argmax(pred[0])
