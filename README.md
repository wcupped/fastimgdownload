# Fast Image Downloader (fastimgdownload)

# How to install
```
pip install fastimgdownload
```

# Example code
```
from fastimgdownload import *

download('https://cdn.discordapp.com/attachments/1228709121902116874/1259918361953964153/0708_1.gif?ex=669010e9&is=668ebf69&hm=20a361d002731fca57049bf71d12b9d2744c1b565ceb78c19c55014c1f3fe9e7&', 
         'wtfisthislmfao', 'png')
```

# Explanation
### Fast Image Downloader (FID) uses module requests but FID simplifies the download of image from the internet. For example, we get the url of the image. We're importing the library and then calling the function 'download' and in the brackets we paste parameters:
### Url (str or var), the name of image that will be saved (str or var) and extension (str or var). There are two of them right now (jpg, png)

# Description

Python module that uses requests module to simplify the downloading of image (PyPI: https://pypi.org/project/fastimgdownload/)
