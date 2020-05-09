import pyautogui
from PIL import Image,ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
def isCollide(data):
     #rectangle for bird
    for i in range(400, 650):
            for j in range(410, 540):
                  data[i, j] = 171
                  if  data[i, j] < 100:
                      hit("down")
                      return True
                    
    for i in range(400, 650):

            for j in range(500, 650):
               if  data[i, j] < 100:
                   hit("up")
                   return True
    return False





#def draw():
    


if __name__ == "__main__":
    print("Hey... Dino game about to start in 3 seconds....")
    time.sleep(3)
    hit('up')
    while True:

    
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            
        #print(asarray(image))
    '''
        #rectangle for cactus 
        for i in range(400, 650):

            for j in range(500, 650):
                 data[i, j] = 0
        #rectangle for bird
        for i in range(400, 650):
            for j in range(410, 540):
                  data[i, j] = 171
                    
        image.show()
        break
    
'''



       
    
        
        
        
       
        
               
                   

            
        


