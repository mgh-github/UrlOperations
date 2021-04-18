import requests
from bs4 import BeautifulSoup
import os
import uuid


# url = 'https://www.behance.net/harisnazar04f8'
newpath = r'C:\Users\Dell\Desktop\assignmentGit\ServerProject\asset'
if not os.path.exists(newpath):
    os.makedirs(newpath)

def imagedownload(url, folder):

    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    images = soup.find_all('img')
    i = 1
    for image in images:

        if len(image['alt'])==0:
            i=i+1
            name=i
        else:
            name= (image['alt'])
        name=str(name)
        link =(image['src'])
        with open(name.replace(' ', '-' ).replace('/', '') + '.jpeg', 'wb') as f:
            photo = requests.get(link)
            f.write(photo.content)

