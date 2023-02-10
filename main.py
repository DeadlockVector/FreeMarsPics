#Api_key - IXcX32WXOjjvHDqgvbSpDrdlWHmh4h9C8EfXuzGa

import os
import ezgmail
import requests
import shutil

# TODO: Setup api keys along with environment variables
#setting up environment variables
#os.environ['Api_key'] = 


def getImage(rover, camera, sol, Api_key = 'IXcX32WXOjjvHDqgvbSpDrdlWHmh4h9C8EfXuzGa'):
    
    #clearing directory
    path = '../FreeMarsPics/MarsPics/'
    for file_name in os.listdir(path):
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)

    #sending api request
    request_link =  "https://api.nasa.gov/mars-photos/api/v1/rovers/"+rover+"/photos?sol="+sol+"&camera="+camera+"&api_key="+Api_key
    res = requests.get(request_link).json()

    #adding image links
    #list images
    images = []
    print(res)
    for i in res['photos']:
        images.append(i['img_src'])

    #downloading images to directory
    #count just to name the images
    count = 1    
    for i in images:
        image = requests.get(i, stream = True)
        with open('../FreeMarsPics/MarsPics/'+'image'+str(count), 'wb') as f:
            shutil.copyfileobj(image.raw, f)
        print('Image sucessfully Downloaded')
        count += 1

    # TODO: In the future, implement resizing of the image
    # for file_name in os.listdir(path):
    #     file = path+file_name
    #     image = Image.open(file)
    #     image = image.resize((561, 481))
    #     image.save(file+'jpeg')
    #     os.remove(file)
        
#IT WORKS
# TODO: implement multiple recipients
def sendEmail(recipients, subject, message_body):
    #initializing ezgmail
    os.chdir(r'/home/isocyanate/FreeMarsPics')
    ezgmail.init()

    #getting paths of images
    attachments = []
    path = '../FreeMarsPics/MarsPics/'
    for image in os.listdir(path):
        attachments.append(path+image)

    #sending images
    try:
        ezgmail.send(recipients, subject, message_body, attachments=attachments)
        print("Sent mail")
    except:
        print("Error sending email")

#Api_key = 'IXcX32WXOjjvHDqgvbSpDrdlWHmh4h9C8EfXuzGa'
# rover = 'curiosity'
# camera = 'fhaz'
# sol = '1000'

#getImage(Api_key, rover, camera, sol)
#sendEmail('aakm10304@gmail.com', 'yoyoyooyo', 'hoiiiiiiiiiiii')