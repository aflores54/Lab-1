#Adolfo Flores CS 2302 Dr. Olac Fuentes
#1:30 p.m. Last Edited 2/11 12:28 a.m.
import matplotlib.pyplot as plt #packages for drawing shapes
import numpy as np
import math 

def circle(center,rad):# general function for drawing circles
    n = int(4*rad*math.pi)# n establishes the circumfrance, t is creates the circular shape for x and y
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_squares1(ax,n,c,s,w):#generates squares at each square's corners
    if n>0:#'p' are the coordinates for square
        p = np.array([[c[0]-s*.5, c[1]-s*.5], [c[0]-s*.5, c[1]+s*.5], [c[0]+s*.5, c[1]+s*.5], [c[0]+s*.5, c[1]-s*.5], [c[0]-s*.5, c[1]-s*.5]])
        ax.plot(p[:,0],p[:,1],color='k')#creates square with 'p' coordinates
        if n > 1:
            for i in range(0,5):#recursive call for each of the 4 corners as new point for next square
                draw_squares1(ax,n-1,p[i],s*w,w)
                
def draw_circles2(ax,n,c,r,w):#generates circles that shrink to the left
    if n>0:
        x,y = circle(c,r)#calls the circle function for x, y values so ax.plot... can create circles
        ax.plot(x,y,color='k')
        draw_circles2(ax,n-1,[r*w,0],r*w,w)#changes the center and radius so circle moves and shrinks
        
def draw_brackets3(ax,n,o,l,w):#generates lines in a binary tree style bracket
    if n>0:
        p = np.array([[o[0],o[1]], [o[0]-l/(2*n),o[1]-l/n], [o[0],o[1]],[o[0]+l/(2*n),o[1]-l/n]])#picks points for lines
        ax.plot(p[:,0],p[:,1],color='k')#generates both left and right line from origin
        if n>1:
            draw_brackets3(ax,n-1,p[1],l*w,w)#sets left point as new origin, then right point as new origin
            draw_brackets3(ax,n-1,p[3],l*w,w)#like navigating a binary tree
    
def draw_circles4(ax,n,c,r,w):#generates 5 circles inside any given circle
    if n>0:#picks a center for each of the 5 circles
        p = np.array([[c[0],c[1]], [c[0]-2*(r*w),c[1]], [c[0]+2*(r*w),c[1]], [c[0],c[1]-2*(r*w)], [c[0],c[1]+2*(r*w)]])
        x,y = circle(c,r)
        ax.plot(x,y,color='k')
        if n > 1:
            for i in range(0,5):#recursive call with 'p' as new center
                draw_circles4(ax,n-1,p[i],r*w,w)
      
plt.close("all")#code for drawing functions on a graph 
fig, ax = plt.subplots() 
size = 100.0#general variables
center = [0.0,0.0]
shapes = False

while shapes != True:#code for input to pick which example to draw
    shape_choice = int(input('Enter problem choice 1, 2, 3, 4, or 0 to exit: '))
    if shape_choice == 1:
        example_choice = input('Enter example choice of 1; a, b, or c: ')
        if example_choice == 'a':
            draw_squares1(ax,2,center,size,.5)
            shapes = True
        elif example_choice == 'b':
            draw_squares1(ax,3,center,size,.5)
            shapes = True
        elif example_choice == 'c':
            draw_squares1(ax,4,center,size,.5)
            shapes = True
        else:
            print("choice is incorrect")
            
    elif shape_choice == 2:
        example_choice = input('Enter example choice of 2; a, b, or c: ')
        if example_choice == 'a':
            draw_circles2(ax, 10, [100,0], 100,.5)
            shapes = True
        elif example_choice == 'b':
            draw_circles2(ax, 50, [100,0], 100,.9)
            shapes = True
        elif example_choice == 'c':
            draw_circles2(ax, 100, [100,0], 100,.95)
            shapes = True
        else:
            print("choice is incorrect")
    
    elif shape_choice == 3:
        example_choice = input('Enter example choice of 3; a, b, or c: ')
        if example_choice == 'a':
            draw_brackets3(ax,2,[0,100],100,.4)
            shapes = True
        elif example_choice == 'b':
            draw_brackets3(ax,3,[0,100],100,.4)
            shapes = True
        elif example_choice == 'c':
            draw_brackets3(ax,4,[0,100],100,.4)
            shapes = True
        else:
            print("choice is incorrect")

    elif shape_choice == 4:
        example_choice = input('Enter example choice of 4; a, b, or c: ')
        if example_choice == 'a':
            draw_circles4(ax,3,center,size,.33)
            shapes = True
        elif example_choice == 'b':
            draw_circles4(ax,4,center,size,.33)
            shapes = True
        elif example_choice == 'c':
            draw_circles4(ax,5,center,size,.33)
            shapes = True
        else:
            print("choice is incorrect")
    elif shape_choice == 0:
            print("Program end")
            shapes = True
    else:
        print("choice is incorrect")
        
    ax.set_aspect(1.0)#code for drawing functions cont.
    ax.axis('off')
    plt.show()
    fig.savefig('squares.png')
    fig.savefig('circles.png')

