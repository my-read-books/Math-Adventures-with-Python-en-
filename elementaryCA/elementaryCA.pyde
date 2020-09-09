w = 3
rows = 1000
cols = 1000

def setup():
    global cells
    size(600, 600)
    
    cells = []
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0)
    cells[0][cols//2] = 1
    cells = generate()
    
#ruleset = [0,0,0,1,1,1,1,0]
ruleset = [0,1,0,1,1,0,1,0]

def draw():
    background(255)
    
    for i, cell in enumerate(cells):
        for j, v in enumerate(cell):
            if v == 1:
                fill(0)
            else:
                fill(255)
            rect(j*w - (cols * w - width) / 2, w * i, w, w)
            
def rules(a, b, c):
    return ruleset[7 - (4 * a + 2 * b + c)]

def generate():
    for i, row in enumerate(cells):
        for j in range(1, len(row) - 1):
            left = row[j-1]
            me = row[j]
            right = row[j+1]
            if i < len(cells)-1:
                cells[i+1][j] = rules(left, me, right)
    return cells
