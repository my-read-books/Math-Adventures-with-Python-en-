xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

transformation_matrix = [[0,-1],[1,0]]

def setup():
    global xscl, yscl
    size(600,600)
    #the scale factors for drawing on the grid:
    xscl= width/rangex
    yscl= -height/rangey
    noFill()
    
def draw():
    global xscl, yscl
    background(255) #white
    translate(width/2,height/2)
    grid(xscl, yscl)
    
    ang= map(mouseX, 0, width, 0, TWO_PI)
    rot_matrix = [[cos(ang),-sin(ang)],[sin(ang),cos(ang)]]
    fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]
    newmatrix = transpose(multmatrix(rot_matrix,transpose(fmatrix)))
    strokeWeight(2)
    stroke(0)
    #newmatrix = transpose(multmatrix(transformation_matrix, transpose(fmatrix)))
    graphPoints(fmatrix)
    stroke(255, 0, 0)
    graphPoints(newmatrix)

def transpose(a):
    '''Transposes matrix a'''
    output = []
    m = len(a)
    n = len(a[0])
    #create an n x m matrix
    for i in range(n):
        output.append([])
        for j in range(m):
        #replace a[i][j] with a[j][i]
            output[i].append(a[j][i])
    return output

def graphPoints(matrix):
    #draw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl,pt[1]*yscl)
    endShape(CLOSE)
    
def grid(xscl,yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    
def multmatrix(a,b):
    #Returns the product of matrix a and matrix b
    m = len(a) #number of rows in first matrix
    n = len(b[0]) #number of columns in second matrix
    newmatrix = []
    for i in range(m):
        row = []
        #for every column in b
        for j in range(n):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix
