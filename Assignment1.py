#Name: Angeli anak david
#Matric Number: BS19110452
#Course: SC32303 Image Processing
#Lecturer: Prof. Madya Abdullah Bade
#Assignment 1

from tkinter import *
from PIL import ImageTk,Image
import cv2
import colorsys
import numpy as np

class MainWindow:
    def __init__(self,wind):
        
        global myimage
        
        self.win=wind
        wind.title("Main Window")
        wind.geometry("400x200")
        wind.configure(bg="pink")
        wind.iconbitmap("image demo/blender.ico")
        
        self.Widget(wind)
        
    
    #Main Menu
    def Widget(self, wind):
        
        myLabel=Label(wind,text="Simple Image Editor", bg="yellow")
        myLabel.config(font =("Courier", 14))
        myLabel.pack()
        
        btn=Button(wind, text="Image Load", command=self.opensecwin)
        btn.pack()
        
        btn1=Button(wind, text="Image Resize & Save", command=self.openthirdwin)
        btn1.pack()
        
        btn2=Button(wind, text="Convert Color", command=self.openfourthwin)
        btn2.pack()
        
        btn3=Button(wind, text="Shape in Image", command=self.primitiveshape)
        btn3.pack()       
        
        btn4=Button(wind, text="Exit", command=wind.destroy, bg="red")
        btn4.pack()
        
    #Load Images
    def opensecwin(self):
    
        global myimage
        
        top=Toplevel()
        top.iconbitmap("image demo/blender.ico")
        
        mylabel=Label(top,text="Sticth Picture").pack()
        myimage=ImageTk.PhotoImage(Image.open("image demo/main.png"))
        mylabel1=Label(top,image=myimage).pack()
        
        #rotate image
        btn1=Button(top, text="Rotate image 180", command=self.rotate_image)
        btn1.pack()
        btn2=Button(top, text="Rotate image 90", command=self.rotate_image1)
        btn2.pack()
        btn3=Button(top, text="Rotate image 60", command=self.rotate_image2)
        btn3.pack()
        
        #translate image
        btn4=Button(top, text="Translate image", command=self.translate_image)
        btn4.pack()
        
        
        btnTop=Button(top,text="Close",command=top.destroy, bg="red")
        btnTop.pack()
        
        
    #rotate images 180
    def rotate_image(self):
        
        global myimage
        
        top=Toplevel()
        top.iconbitmap("image demo/blender.ico")
        mylabel=Label(top,text="Rotate Picture").pack()
        Original_Image = Image.open("image demo/main.png")
         
        # Rotate Image By 180 Degree
        rotated_image1 = Original_Image.rotate(180)
        
        rotated_image1.show()
        
        
        #rotate images 90
    def rotate_image1(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Rotate windows")
        top.iconbitmap("image demo/blender.ico")
        mylabel=Label(top,text="Rotate Picture").pack()
        Original_Image = Image.open("image demo/main.png")
         
        # Rotate Image By 90 Degree
        rotated_image1 = Original_Image.rotate(90)
        
        rotated_image1.show()
        
        #rotate images 60
    def rotate_image2(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Rotate windows")
        top.iconbitmap("image demo/blender.ico")
        mylabel=Label(top,text="Rotate Picture").pack()
        Original_Image = Image.open("image demo/main.png")
         
        # Rotate Image By 60 Degree
        rotated_image1 = Original_Image.rotate(60)
        
        rotated_image1.show()
        
    #Translate image
        
    def translate_image(self):
        global myimage
        
        top=Toplevel()
        top.title("Translate windows")
        top.iconbitmap("image demo/blender.ico")
        
        mylabel=Label(top,text="Sticth Picture").pack()
        
        image = cv2.imread("image demo/main.png")
  
        # Store height and width of the image
        height, width = image.shape[:2]
          
        quarter_height, quarter_width = height / 4, width / 4
          
        T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
          
        # We use warpAffine to transform
        # the image using the matrix, T
        img_translation = cv2.warpAffine(image, T, (width, height))
        cv2.imshow('Translation', img_translation)
    
    #Resize image    
    def openthirdwin(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Resize windows")
        top.iconbitmap("image demo/blender.ico")
        
        mylabel=Label(top,text="Sticth Picture").pack()
        myimage=ImageTk.PhotoImage(Image.open("image demo/main.png"))
        mylabel1=Label(top,image=myimage).pack()

        btnTop=Button(top,text="Resize Image",command=self.resizeImage)
        btnTop.pack()
        
    
    #Resize image or scalling
    def resizeImage(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Resize windows")
        top.iconbitmap("image demo/blender.ico")
        
        mylabel=Label(top,text="Sticth Picture").pack()
        
        img = Image.open("image demo/main.png")
        resized_img = img.resize((300, 100))
        resized_img.save("resized_image2.png")
        
        mylabel1=Label(top,image=myimage).pack()
        
        btnTop=Button(top, text="Close", command=top.destroy)
        btnTop.pack()
        
    #Change Color
    def openfourthwin(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Convert Color windows")
        top.iconbitmap("image demo/blender.ico")
        
        mylabel=Label(top,text="Sticth Picture").pack()
        myimage=ImageTk.PhotoImage(Image.open("image demo/main.png"))
        mylabel1=Label(top,image=myimage).pack()

        btnTop11=Button(top,text="RGB to Gray",command=self.graycolor, bg="yellow")
        btnTop11.pack()
        
        btnTop12=Button(top,text="RGB to HSV",command=self.hsvcolor, bg="purple")
        btnTop12.pack()
        
        btnTop13=Button(top,text="RGB to GAUSSIAN BLUR",command=self.gaussianblur, bg="yellow")
        btnTop13.pack()
        
        btnTop14=Button(top,text="RGB to SHARPEN",command=self.sharpen, bg="purple")
        btnTop14.pack()
        
        btnTop1=Button(top,text="Close",command=top.destroy, bg="red")
        btnTop1.pack()
        
        
    #Grey Color
    def graycolor(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Gray Color windows")
        top.iconbitmap("image demo/blender.ico")
        mylabel=Label(top,text="Gray Picture").pack()
        image = cv2.imread("image demo/main.png")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Gray image', gray)
        
        
    #HSV Color 
    def hsvcolor(self):
        
        global myimage
        
        top=Toplevel()
        top.title("HSV Color windows")
        top.iconbitmap("image demo/blender.ico")
        image=cv2.imread("image demo/main.png")
        hsvImage=cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        
        cv2.imshow('HSV image', hsvImage)
        
    def gaussianblur(self):

        global myimage
        
        top=Toplevel()
        top.title("GaussBlur Color windows")
        top.iconbitmap("image demo/blender.ico")
        mylabel=Label(top,text="Gray Picture").pack()
        image = cv2.imread("image demo/main.png")
        gausBlur = cv2.GaussianBlur(image, (5,5),0)
        
        cv2.imshow('GausBlur image', gausBlur)
            
    def sharpen(self):
        
        global myimage

        top=Toplevel()
        top.title("Sharpen Color windows")
        top.iconbitmap("image demo/blender.ico")
        mylabel=Label(top,text="Sharpen Picture").pack()
        image = cv2.imread("image demo/main.png")
        
        kernel=np.array([[0,-1,1],[-1,5,-1],[0,-1,0]])
        sharpen = cv2.filter2D(image, -1, kernel)
        
        cv2.imshow('Sharpen image',sharpen)
    
        
    #Primitive shape
    def primitiveshape(self):
        
        global myimage
        
        top=Toplevel()
        top.title("Primitive windows")
        top.configure(bg="pink")
        top.iconbitmap("image demo/blender.ico")
        btnTop1=Button(top,text="Circle",command=self.Circle)
        btnTop1.pack()
        btnTop2=Button(top,text="Rectangle",command=self.rectangle)
        btnTop2.pack()
        btnTop2=Button(top,text="Text",command=self.text)
        btnTop2.pack()
        btnTop=Button(top,text="Close",command=top.destroy, bg="red")
        btnTop.pack()
        
    def Circle(self):
        global myimage
        
        top=Toplevel()
        top.iconbitmap("image demo/blender.ico")
        
        image=cv2.imread("image demo/main.png")
        # Creating circle
        cv2.circle(image, (100, 100), 80, (255, 0, 0), 3)
         
        cv2.imshow('Circle', image)
        
    def rectangle(self):
        global myimage
        
        top=Toplevel()
        top.iconbitmap("image demo/blender.ico")
        
        image=cv2.imread("image demo/main.png")
        # Creating rectangle
        cv2.rectangle(image, (20, 20), (200, 100), (0, 255, 0), 5)
         
        cv2.imshow('Rectangle', image)
        
    def text(self):
        
        top=Toplevel()
        top.iconbitmap("image demo/blender.ico")
        # Creating a black image with 3
        # channels RGB and unsigned int datatype
        img = np.zeros((400, 400, 3), dtype = "uint8")
         
        # writing text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Name: Angeli anak David', (50, 50),
                    font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img, 'Matric Number: BS19110452', (20, 90),
                    font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
         
        cv2.imshow('dark', img)
        
                  
        # Create text widget and specify size.
        T = Text(top, height = 5, width = 52)
        T.pack()
    
def main():
    root=Tk()
    win=MainWindow(root)
    root.mainloop()
    
if __name__=="__main__":
    main()
