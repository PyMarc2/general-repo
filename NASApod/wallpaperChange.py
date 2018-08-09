import urllib.request
import re
f = open('C:/Windows/Temp/00000001.jpg','w')
podPage = urllib.request.urlopen('https://www.nasa.gov/multimedia/imagegallery/iotd.html')
podPage = podPage.read()
print(podPage)
prefix = "https://www.nasa.gov"

imagesUrl = re.findall('/sites/default/files/styles/.+?', str(podPage))
print(imagesUrl)
print(len(imagesUrl))

# f.write()
# f.close()
