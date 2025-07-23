import requests
import os

def get_extension(image_url):
    extensions = ['.png', '.jpg', 'jpeg', '.svg', '.gif']
    for ext in extensions:
        if ext in image_url:
            return ext
    


def download_image(image_url , name , folder = None):
    ext = get_extension(image_url)
    if folder:
        image_name = f'{folder}/{name}{ext}'
    else:
        image_name = f'{name}{ext}'
    
    if os.path.isfile(image_name):
        raise Exception("File name already exists")

    try:
        image_content = requests.get(image_url).content
        with open(image_name , 'wb') as handler:
            handler.write(image_content)
            print(f" image with address : {image_url} downloaded sucssufuly.")
    except Exception as e:
        raise (f'Error {e}')
    
    
if __name__ == '__main__':
    img_url = input(": ")
    img_name = input(": ")
    download_image(img_url, img_name)

