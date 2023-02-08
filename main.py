#Api_key - IXcX32WXOjjvHDqgvbSpDrdlWHmh4h9C8EfXuzGa
#rover = 'curiosity'
#camera = 'fhaz'
#sol = '1000'
#request link f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key={Api_key}"

import os
import ezgmail
import requests

# TODO: Setup api keys along with environment variables
#setting up environment variables
#os.environ['Api_key'] = 

# TODO:
#download images?
#get stuff from the gui
def getImage(Api_key, rover, camera, sol):
    try:
        request_link =  "https://api.nasa.gov/mars-photos/api/v1/rovers/"+rover+"/photos?sol="+sol+"&camera="+camera+"&api_key="+Api_key
        res = requests.get(request_link).json()
        #res = {'photos': [{'id': 102693, 'sol': 1000, 'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG', 'earth_date': '2015-05-30', 'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active'}}, {'id': 102694, 'sol': 1000, 'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG', 'earth_date': '2015-05-30', 'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active'}}]}
        print(res)
        return res
    except:
        print("NASA API error")


#IT WORKS
def sendEmail(subject, message_body, recipients):
    os.chdir(r'/home/isocyanate/FreeMarsPics')
    ezgmail.init()
    try:
        ezgmail.send(recipients, subject, message_body)
    except:
        print("Error sending email")

Api_key = 'IXcX32WXOjjvHDqgvbSpDrdlWHmh4h9C8EfXuzGa'
rover = 'curiosity'
camera = 'rhaz'
sol = '1000'

#TODO: call function based on parameters
#given by the user in the gui
#sendEmail('Testing api', str(getImage(Api_key, rover, camera, sol)), 'aakm10304@gmail.com')
