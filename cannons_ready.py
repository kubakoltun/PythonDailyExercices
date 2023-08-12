def cannons_ready(gunners):
    response = ''
    
    for i in gunners:
        if (gunners[i] == 'nay'):
           response = 'Shiver me timbers!'
        elif (response != 'Shiver me timbers!'):
            response = 'Fire!'
            
    return response
