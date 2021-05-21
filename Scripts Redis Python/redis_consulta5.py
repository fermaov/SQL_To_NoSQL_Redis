import redis

if __name__ == '__main__':
    
    r = redis.StrictRedis(
        host = 'localhost',
        port = 6379,
        decode_responses = True)

    listaF = r.keys("factura:*")
     
    for x in range(0,len(listaF)):
        existe = r.hexists(listaF[x],"salida")
        if not existe:
            numh = r.hget(listaF[x],"numero")
            tipo = r.hget("habitacion:" + numh,"tipo")
            precio = r.hget("precio:" + tipo,"precio")

            print(
                numh,
                tipo,
                precio
            )    



