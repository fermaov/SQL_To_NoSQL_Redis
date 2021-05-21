import redis

if __name__ == '__main__':
    
    r = redis.StrictRedis(
        host = 'localhost',
        port = 6379,
        decode_responses = True)

    listaE = r.keys("empleado:*")
    
    for x in range(0,len(listaE)):
        nome = r.hget(listaE[x],"nombre")

        if nome == "Jorge Alonso Alonso":
            cods = r.hget(listaE[x],"cods")
            numreg = r.hget("servicio:" + cods,"numreg")
            
            print(
                r.hget("empleado:" + numreg,"nombre")
            ) 
                  
            break
        



