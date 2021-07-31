import numpy as np
from PIL import Image


def softmax( x, ax=1 ):
    m = np.max( x, axis=ax, keepdims=True )#max per row
    p = np.exp( x - m )
    return ( p / np.sum(p,axis=ax,keepdims=True) )

def ml_softmax_test(title):

    W1 = np.load('W1.npy')
    W2 = np.load('W2.npy')

    im = Image.open(title)
    pixels = list(im.getdata())
    newPixels = [ pixels[x][0] for x in range(len(pixels)) ]
    newPixels.append(255)
    
    Z = np.cos(np.dot(newPixels, W1.T))
    
    W2= W2[:,1:]
    
    ytest = softmax( Z.dot(W2.T),0 )
    
    ttest = np.argmax(ytest, 0)
    return ttest
