import requests

def download(url, name, ext):
    img=requests.get(url)
    if ext=='jpg':
        img_option=open(name + '.' + 'jpg', 'wb')
    if ext=='png':
        img_option=open(name + '.' + 'png', 'wb')
    if ext=='gif':
        img_option=open(name + '.' + 'gif', 'wb')
    img_option.write(img.content)
    img_option.close()
    print(f'Successfully saved the image as {name}.{ext}!')