import requests

def download(url, name, ext):
    img=requests.get(url)
    if ext=='jpg':
        img_option=open(name + '.' + 'jpg', 'wb')
    elif ext=='png':
        img_option=open(name + '.' + 'png', 'wb')
    img_option.write(img.content)
    img_option.close()
    print(f'Successfully saved the image as {name}.{ext}!')