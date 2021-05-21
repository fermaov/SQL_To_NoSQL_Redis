import redis

if __name__ == '__main__':
    
    r = redis.StrictRedis(
        host = 'localhost',
        port = 6379,
        decode_responses = True)

    listaE = r.keys("empleado:*")
     
    for x in range(0,len(listaE)):
        
        existe = r.hexists(listaE[x],"cods")
        if existe:
            cods = r.hget(listaE[x],"cods")
            noms = r.hget("servicio:" + cods,"descripcion")
        else:
            noms = "None"
        print(
            r.hget(listaE[x],"numreg"),
            "\t",
            r.hget(listaE[x],"nombre"),
            "\t",
            r.hget(listaE[x],"incorporacion"),
            "\t",
            r.hget(listaE[x],"sueldo"),
            "\t",
            noms
        )    



