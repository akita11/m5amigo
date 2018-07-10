# Python script of generating Pads for M5stack base
def draw_rect(x1,y1,x2,y2,l):
    print("<rectangle x1=\""+str(x1)+"\" y1=\""+str(y1)+"\" x2=\""+str(x2)+"\" y2=\""+str(y2)+"\" layer=\""+str(l)+"\"/>")

def round(x):
    return(int(x * 100) / 100)

for i in range (1, 31, 1):
    if ((i-1) % 2) == 0:
        dx = 1
    else:
        dx = -1
    dy = int((i-1)/2)
    x1 = 6 - dx * 2.5 - 1.5
    y1 = 42.78 - 0.9  - dy * 2.54
    x2 = x1 + 3
    y2 = y1 + 1.8
    x1 = round(x1)
    y1 = round(y1)
    x2 = round(x2)
    y2 = round(y2)
    draw_rect(x1,y1,x2,y2,1)
    draw_rect(x1,y1,x2,y2,16)
    draw_rect(x1,y1,x2,y2,29)
    draw_rect(x1,y1,x2,y2,30)
    draw_rect(x1,y1,x2,y2,31)
    draw_rect(x1,y1,x2,y2,32)
    x = 6 - 1 * dx
    y = 42.78 - dy * 2.54
    x = round(x)
    y = round(y)
    print("<pad name=\"P$"+str(i)+"\" x=\""+str(x)+"\" y=\""+str(y)+"\" drill=\"0.35\"/>")
