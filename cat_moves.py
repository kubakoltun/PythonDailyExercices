def solution(start, finish):  
    moves = 0
    hasJumped = False
    
    for i in range (start, finish):
        hasJumped = False
        
        if ((start + 3)%2 == 0 and start+3 <= finish):
            start += 3
            moves += 1
            hasJumped = True
        elif (((start+3)%2 != 0) and start+3 <=finish):
            start += 3
            moves += 1
            hasJumped = True
        elif (hasJumped == False):
            start += 1
            moves += 1
            hasJumped = True
        if (start == finish):
            break
            
    
    return moves
