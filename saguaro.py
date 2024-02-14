# Favian Mokaya Imbera SCT211-0022/2021
# This program basically uses the fact that the cactus is structured into three parts from which have slightly similar structural designs.
# The default size of the cactus is 3 which should not be manipulated
# 
defaultsize = 3
cactus_size = 4 # Manipulating this value affects the size of the cactus

def spaces(num_spaces):
  print(" "*num_spaces, end="")
  
def leaf_extension(extension):
  if extension == "left":
    spaces(cactus_size-(1+(cactus_size-defaultsize)))
    print("x"*(cactus_size*2) + "X" + "~"*(cactus_size*2) + "X",end="")
  elif extension == "right":
    spaces((cactus_size*3)-(1+(cactus_size-defaultsize)))
    print("X" + "~"*(cactus_size*2) + "X" + "x"*(cactus_size*2))
  
      
def print_structuredPartOfCactus(part_of_cactus):
  if part_of_cactus == "top":
    print(" " + "x"*cactus_size + " ", end="")
    spaces(cactus_size)
    print(" " + "x"*(cactus_size*2) + " ")
    
    for i in range(1,(cactus_size*2)):
      print("X" + "-"*cactus_size + "X", end="")
      spaces(cactus_size)
      print("X" + "/"*i + "-"*((cactus_size*2)-i) + "X")
    leaf_extension("left")
    print(" "*(cactus_size-1)," " + "x"*cactus_size + " ")
    
  elif part_of_cactus == "middle":
    for i in range(1,(cactus_size*2)):
      spaces((cactus_size*3)-(1+(cactus_size-defaultsize)))
      print("X" + "-"*((cactus_size*2)-i) + "\\"*i + "X", end="")
      spaces(cactus_size)
      print("X" + "-"*cactus_size + "X")
    leaf_extension("right")
    
  elif part_of_cactus == "bottom":
      for i in range(cactus_size*2):
        spaces((cactus_size*3)-(1+(cactus_size-defaultsize)))
        print("X" + "~"*(cactus_size*2) + "X" )
  
def draw_saguaroCactus():
 print_structuredPartOfCactus("top")
 print_structuredPartOfCactus("middle")
 print_structuredPartOfCactus("bottom")    
  
draw_saguaroCactus()