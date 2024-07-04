import cv2
import os


directory= 'images'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')
    

for i in range(49,58):
    letter  = chr(i)
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')




import os
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             '1': len(os.listdir(directory+"/1")),
             '2': len(os.listdir(directory+"/2")),
             '3': len(os.listdir(directory+"/3")),
             '4': len(os.listdir(directory+"/4")),
             '5': len(os.listdir(directory+"/5")),
             '6': len(os.listdir(directory+"/6")),
             '7': len(os.listdir(directory+"/7")),
             '8': len(os.listdir(directory+"/8")),
             '9': len(os.listdir(directory+"/9")),
             'blank': len(os.listdir(directory+"/blank"))
             }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(48,48))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory+'1/'+str(count['1']))+'.png',frame)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(os.path.join(directory+'2/'+str(count['2']))+'.png',frame)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(os.path.join(directory+'3/'+str(count['3']))+'.png',frame)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(os.path.join(directory+'4/'+str(count['4']))+'.png',frame)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(os.path.join(directory+'5/'+str(count['5']))+'.png',frame)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(os.path.join(directory+'6/'+str(count['6']))+'.png',frame)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(os.path.join(directory+'7/'+str(count['7']))+'.png',frame)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(os.path.join(directory+'8/'+str(count['8']))+'.png',frame)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(os.path.join(directory+'9/'+str(count['9']))+'.png',frame)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(directory+'blank/' + str(count['blank']))+ '.jpg',frame)


    