#import opencv library
import cv2
#import numpy
import numpy as np
#import image function from keras
from keras.preprocessing import image
#import load_model from keras
from keras.models import load_model
#import Client from twilio API
from twilio.rest import Client
#import playsound package
from playsound import playsound
#load the saved model
model = load_model(r'forest12.h5')
#define video
video = cv2.VideoCapture(0)
#define the featues
name = ['forest', 'with fire']

while(1):
    success, frame = video.read()
    cv2.imwrite("image.jpg", frame)
    img = image.load_img("image.jpg", target_size = (128,128,3))
    x = image.img_to_array(img) 
    x = np.expand_dims(x,axis=0)
    pred = model.predict(x)
    p = pred[0]
    print(pred)
    #cv2.putText(frame, "predicted class = "+str(name[p]), (100,100),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
    pred=model.predict(x)
    
    
    if pred[0]==1:
        #twilio account ssid
        account_sid = 'ACa56e34d497b8c093a5dae951558a788d'
        #twilio account authentication token
        auth_token= 'e4420b51bb0bfda074318faebd0fb251'
        client = Client (account_sid, auth_token)
        message = client.messages \
        .create(
         body='Forest Fire is detected, stay alert',
        #use twilio free number
        from_=' +16075363542',
        #to number
        to='+919944629265')
        print(message.sid)
        print('sms send!')
        playsound(r'C:\Users\Smart\Downloads\buzzer-or-wrong-answer-20582.mp3')
    else:
        print("No Danger")
        #break
    cv2.imshow("image",frame)
    if cv2.waitKey(1)&0xFF == ord('a'):
      break

video.release()
cv2.destroyAllWindows()