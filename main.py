from PIL import Image
import math
import os


mul = 1.05
border = 10
pageType = "A4"
polaroidNumber = 0

backgroundColor = (240, 240, 240)
canvasDimensions = [int(353*mul), int(403*mul)]

imageDimension = int(298*mul)

pageDimensions = {
    "A4" : {
        "width" : 1123,
        "height": 1584,
        "xMax": 3,
        "yMax": 3
    }
}

imagePaths = os.listdir("input/")

polaroids = []
pages = []

xBorder = (pageDimensions[pageType]["width"] - (pageDimensions[pageType]["xMax"] * (canvasDimensions[0] + border)))/2
yBorder = (pageDimensions[pageType]["height"] - (pageDimensions[pageType]["yMax"] * (canvasDimensions[1] + border)))/2


# we make the image
def makePolaroidObject(imagePath):
    canvas  = Image.new(mode = "RGB", size = (canvasDimensions[0], canvasDimensions[1]), color=backgroundColor)
    actualPicture = Image.open("input/" + imagePath).resize((imageDimension, imageDimension), ).copy()
    canvas.paste(actualPicture, (19, 19))
    return canvas
    

for imagePath in imagePaths:
    polaroids.append(makePolaroidObject(imagePath))


#number of pages loop
numberOfPages = math.ceil(len(polaroids)/(pageDimensions[pageType]["yMax"] * pageDimensions[pageType]["xMax"]))
for i in range(numberOfPages):
    page = Image.new(mode="RGB", size=(pageDimensions[pageType]["width"], pageDimensions[pageType]["height"]), color="white")
    try:
        for y in range(pageDimensions[pageType]["yMax"]):
            for x in range(pageDimensions[pageType]["xMax"]):
                xCoordinate = x * (canvasDimensions[0] + border) + int(xBorder)
                yCoordinate = y * (canvasDimensions[1] + border) + int(yBorder)
                page.paste(polaroids[polaroidNumber], (xCoordinate, yCoordinate))
                polaroidNumber+=1
    except:
        print()
    page.save("output/"+str(i) + ".png", format="png")
    pages.append(page)