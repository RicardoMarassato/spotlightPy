from PIL import Image
from datetime import date, datetime, timedelta
import os
import shutil
import uuid


def createDirs():
    imgDir = "imgs"
    wallPapersDir = "wallpapers"
    imgParentDir = "./"
    profile = str(os.environ['USERPROFILE'])
    wallpaperParentDir = profile + "/desktop/"
    imgPath = os.path.join(imgParentDir, imgDir)
    wallPath = os.path.join(wallpaperParentDir, wallPapersDir)
    try:
        os.mkdir(imgPath)
        os.mkdir(wallPath)
    except:
        print("Dirs already created!")


def getImageSize(imgspath):
    path = "./imgs/" + imgspath
    img = Image.open(path)
    width, height = img.size
    return str(img.size)


def getImageModDate(img):
    imageModDate = os.path.getmtime(img)
    formatImageModDate = datetime.fromtimestamp(
        imageModDate).strftime("%m/%d/%y")
    return formatImageModDate


def copySpotlightImages():
    profile = str(os.environ['USERPROFILE'])
    imagesPath = profile + \
        "/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
    srcFiles = os.listdir(imagesPath)
    destPath = "./imgs/"

    for filename in srcFiles:
        fullFileName = os.path.join(imagesPath, filename)
        if os.path.isfile(fullFileName):
            shutil.copy(fullFileName, destPath)
    renameImages()


def renameImages():
    imagesPath = "./imgs/"
    srcFiles = os.listdir(imagesPath)
    destPath = "./imgs/"

    for filename in srcFiles:
        src = imagesPath + filename
        uniqueID = uuid.uuid4()
        dest = "img-" + str(uniqueID) + ".jpg"
        dest = destPath + dest
        os.rename(src, dest)
    getWallpapers()


def getWallpapers():
    imagesPath = "./imgs/"
    srcFiles = os.listdir(imagesPath)
    profile = str(os.environ['USERPROFILE'])
    destPath = profile + "/Desktop/wallpapers/"
    for filename in srcFiles:
        if getImageSize(filename) == "(1080, 1920)" or getImageSize(filename) == "(1920, 1080)":
            print("Copied file = " + filename)
            fullFileName = os.path.join(imagesPath, filename)
            if os.path.isfile(fullFileName):
                shutil.copy(fullFileName, destPath)
        else:
            #print("Not supported!")
            pass
    cleanImgFolder()


def cleanImgFolder():
    imagesPath = "./imgs/"
    for filename in os.listdir(imagesPath):
        file_path = os.path.join(imagesPath, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def main():
    createDirs()
    copySpotlightImages()


if __name__ == "__main__":
    main()
