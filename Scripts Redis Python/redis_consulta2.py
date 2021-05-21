import redis

if __name__ == '__main__':
    
    r = redis.StrictRedis(
        host = 'localhost',
        port = 6379,
        decode_responses = True)

    listaS = r.keys("servicio:*")
    
    for x in range(0,len(listaS)):
        noms = r.hget(listaS[x],"descripcion")
        
        if noms == "restaurante":
            numreg = r.hget(listaS[x],"numreg")
            
            print(
                r.hget("empleado:" + numreg,"nombre")
            ) 
                  
            break
        



