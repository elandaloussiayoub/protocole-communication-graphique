import sys
import numpy as np
import random
import math
from string import ascii_lowercase
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from char_table import lang
from hamming import error_correction


sentence = input("enter the sentence to be converted :")
sen_array = list(sentence)
sen_bin = []
for i in sen_array:
  sen_bin.append('{0:06b}'.format(lang[i]))
sentence_bin = ''.join(sen_bin)
sen_with_errocC = error_correction(sentence_bin)
print(sen_bin)
print(sentence_bin)
print(sen_with_errocC)





def determine_qr_size(str):
  msg_len = len(str)
  oper_len  = 64 + 24
  size = 180
  if ( msg_len + oper_len < size) :
    ret = 16
  else :
    while size < 4700 :
      if msg_len + oper_len < size:
        # ret = 4*math.ceil(math.sqrt((size+88)*4/3)/4)
        a = int(math.sqrt(size + (4 - np.remainder(size, 4))))
        ret = a + (4 - np.remainder(a, 4))
        break
      size += 20
  return ret
final_size = determine_qr_size(sen_with_errocC)


qr_matrix = np.zeros(shape=(final_size,final_size))

def add_content(sentence):
  index = 0
  for i in range(final_size):
    for j in range(final_size):
      if(qr_matrix[i][j] == 0 and index<len(list(sentence))):
        qr_matrix[i][j] = int(sentence[index])
        index += 1

for i in range(final_size):
  for j in range(final_size):
    if i < final_size/4 and j < final_size/4 :
      qr_matrix[i][j] = -2 ;
    if i < final_size/4 and j >= final_size*3/4 :
      qr_matrix[i][j] = -2 ;
    if i >= final_size*3/4 and j < final_size/4 :
      qr_matrix[i][j] = -2 ;
    if i >= final_size*3/4 and j>= final_size*3/4 :
      qr_matrix[i][j] = -2 ;

def add_orientation():
  qr_matrix[math.floor(final_size*3/4 - 2)][0] = 2
  qr_matrix[math.floor(final_size*3/4 - 1)][0] = 2
  qr_matrix[math.floor(final_size*3/4 - 1)][1] = 2
  
  qr_matrix[0][math.floor(final_size*3/4 - 2)] = 2
  qr_matrix[0][math.floor(final_size*3/4 - 1)] = 2
  qr_matrix[1][math.floor(final_size*3/4 - 1)] = 2
  
  qr_matrix[math.floor(final_size*3/4 - 2)][math.floor(final_size - 1)] = 2
  qr_matrix[math.floor(final_size*3/4 - 1)][math.floor(final_size - 1)] = 2
  qr_matrix[math.floor(final_size*3/4 - 1)][math.floor(final_size - 2)] = 2

def add_timming():
  base = math.floor(final_size/2)
  for i in range(base - 4, base + 4):
    for j in range(base - 4, base + 4):
      qr_matrix[i][j] = -1
  qr_matrix[base-3][base-3] = 2
  qr_matrix[base-3][base-1] = 2
  qr_matrix[base-3][base+1] = 2
  qr_matrix[base-3][base+2] = 2
  qr_matrix[base-2][base-3] = 2
  qr_matrix[base-1][base+2] = 2
  qr_matrix[base]  [base-3] = 2
  qr_matrix[base+1][base+2] = 2
  qr_matrix[base+2][base-3] = 2
  qr_matrix[base+2][base-2] = 2
  qr_matrix[base+2]  [base] = 2
  qr_matrix[base+2][base+2] = 2


def seperators():
  # corner seperators
  qr_matrix[math.floor(final_size*3/4 - 3)][0] = -1
  qr_matrix[math.floor(final_size*3/4 - 3)][1] = -1
  qr_matrix[math.floor(final_size*3/4 - 2)][1] = -1
  qr_matrix[math.floor(final_size*3/4 - 2)][2] = -1
  qr_matrix[math.floor(final_size*3/4 - 1)][2] = -1
  
  qr_matrix[0][math.floor(final_size*3/4 - 3)] = -1
  qr_matrix[1][math.floor(final_size*3/4 - 3)] = -1
  qr_matrix[1][math.floor(final_size*3/4 - 2)] = -1
  qr_matrix[2][math.floor(final_size*3/4 - 2)] = -1
  qr_matrix[2][math.floor(final_size*3/4 - 1)] = -1
  
  qr_matrix[math.floor(final_size*3/4 - 3)][math.floor(final_size - 1)] = -1
  qr_matrix[math.floor(final_size*3/4 - 3)][math.floor(final_size - 2)] = -1
  qr_matrix[math.floor(final_size*3/4 - 2)][math.floor(final_size - 2)] = -1
  qr_matrix[math.floor(final_size*3/4 - 2)][math.floor(final_size - 3)] = -1
  qr_matrix[math.floor(final_size*3/4 - 1)][math.floor(final_size - 3)] = -1


def drawMatrix(ctx):
  for i in range(final_size):
    for j in range(final_size):
      if qr_matrix[i][j] == 0 :
        pass
      elif qr_matrix[i][j] == 1 :
        # color = "#%06x" % random.randint(0, 0xFFFFFF)
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#000000")
      elif qr_matrix[i][j] == 2 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#FF0000")
      elif qr_matrix[i][j] == 3 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#000000")
      # elif qr_matrix[i][j] == -1 :
      #   ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#808080")


def drawOutline(ctx, xsize, ysize):
  ctx.create_polygon( xsize/4   , 0,
                      xsize*3/4 , 0,
                      xsize*3/4 ,ysize/4, 
                      xsize     ,ysize/4,
                      xsize     ,ysize*3/4,
                      xsize*3/4 ,ysize*3/4,
                      xsize*3/4 ,ysize,
                      xsize/4   ,ysize ,
                      xsize/4   ,ysize*3/4,
                      0         ,ysize*3/4,
                      0         ,ysize/4 ,
                      xsize/4   ,ysize/4 ,
                      fill="#ffffff"
                      )

def drawLogo(ctx):
  img = Image.open("Logo-UCA.png")
  logo = ImageTk.PhotoImage(img)
  ctx.create_image(10,10, anchor= NW, image= logo)
  # img = tkinter.PhotoImage("Logo-UCA.png")
  # img = PhotoImg(Image.open("Logo-UCA.png"))
  # ctx.create_image((250,250), img)



# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = event.width/self.width
        hscale = event.height/self.height
        self.width = event.width
        self.height = event.height
        # rescale all the objects
        self.scale("all", 0, 0, wscale, hscale)


def main():
    root = Tk()
    root.title("CryptoCode")
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe, width= final_size*10, height= final_size*10)#, highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)
    
    drawOutline(mycanvas, final_size*10,final_size*10)

    add_orientation()
    add_timming()
    seperators()
    add_content(sen_with_errocC)

    drawMatrix(mycanvas)
    
    drawLogo(mycanvas)
    
    # Logo section
    # img = Image.open("Logo-UCA.png")
    img = Image.open("emojy.png")
    img = img.resize((40,40), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(img)
    mycanvas.create_image(final_size*10/2,final_size*10/2, anchor= CENTER, image= logo)
    
    # tag all of the drawn widgets
    root.mainloop()

if __name__ == "__main__":
    main()
