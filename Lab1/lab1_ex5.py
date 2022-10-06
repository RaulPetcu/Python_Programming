def print_spiral(row, col, arr):
    top = 0
    bottom = row-1
    left = 0
    right = col - 1 

    direction = 0
    
    while (top <= bottom and left <=right):    
        if direction ==0:
            for i in range(left,right+1):
                print (arr[top][i], end="")

            top +=1
            direction = 1

        elif direction ==1:
            for i in range(top,bottom+1):
                print (arr[i][right], end="")

            right -=1 
            direction = 2
            
        elif direction ==2:
            for i in range(right,left-1,-1):
                print (arr[bottom][i], end="")

            bottom -=1
            direction = 3
            
        elif direction ==3:
            for i in range(bottom,top-1,-1):
                print (arr[i][left], end="")
            left +=1
            direction = 0

matrix = [  ['f', 'i', 'r', 's'],
            ['n', '_', 'l', 't'], 
            ['o', 'b', 'a', '_'], 
            ['h', 't', 'y', 'p']  ]

print_spiral(4, 4, matrix)