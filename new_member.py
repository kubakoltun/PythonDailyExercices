def open_or_senior(data):
    status = []
    for i in range (len(data)): 
        for j in range (len(data[i])):
           
            print(data[i][j], j)
            if (j == 0):
                if(data[i][j] >= 55):
                    print('wiekw')
                    oldEnough = True
                else:
                    oldEnough = False
            elif (j == 1):
                if(data[i][j] > 7):
                    print('skillw')
                    handiEnough = True
                else:
                    handiEnough = False
            
        if(oldEnough == True and handiEnough == True):
                print('ww, sw')
                status.append('Senior')
        else:
                status.append('Open')
                
        print(status)
                    
            
    return status
