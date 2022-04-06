import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_almost_equal
import os
from PIL import Image

# Helpers

def get_image_names(inputDir):
  """
  Function to get all of the image file names from a folder.
  
  Parameters
  ----------
  inputDir : str
      Input directory (with all of the images)
  
  Output
  ----------
  query_images : list
      List with all of the image file names.
  """
  query_images = []
  for filename in os.listdir('fb_post_images2'):
    if filename.endswith("jpg"): 
      query_images.append(filename)
  
  return query_images



def setAxes(ax, image, query = False, **kwargs):
    value = kwargs.get("value", None)
    if query:
        ax.set_xlabel("Query Image\n{0}".format(image), fontsize = 12)
    else:
        ax.set_xlabel("Similarity value {1:1.3f}\n{0}".format( image,  value), fontsize = 12)
    ax.set_xticks([])
    ax.set_yticks([])


def getSimilarImages(image, simNames, simVals):
    if image in set(simNames.index):
        imgs = list(simNames.loc[image, :])
        vals = list(simVals.loc[image, :])
        if image in imgs:
            assert_almost_equal(max(vals), 1, decimal = 5)
            imgs.remove(image)
            vals.remove(max(vals))
        return imgs, vals
    else:
        print("'{}' Unknown image".format(image))
 
        
def plotSimilarImages(image, similarNames, similarValues, inputDir, numRow=1, numCol=10):
    simImages, simValues = getSimilarImages(image, similarNames, similarValues)
    fig = plt.figure(figsize=(20, 20))
    
    # now plot the  most simliar images
    for j in range(0, numCol*numRow):
        ax = []
        if j == 0:
            img = Image.open(os.path.join(inputDir, image))
            ax = fig.add_subplot(numRow, numCol, 1)
            setAxes(ax, image, query = True)
        else:
            img = Image.open(os.path.join(inputDir, simImages[j-1]))
            ax.append(fig.add_subplot(numRow, numCol, j+1))
            setAxes(ax[-1], simImages[j-1], value = simValues[j-1])
        img = img.convert('RGB')
        plt.imshow(img)
        img.close()
    
    plt.show()