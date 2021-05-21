import redis
import psycopg2


if __name__ == '__main__':
    
    r = redis.StrictRedis(
        host = 'localhost',
        port = 6379,
        decode_responses = True)

    try:
        conexion = psycopg2.connect(host="localhost", database="hotel", user="postgres", password="1EESC998")
        cur = conexion.cursor()

        #LLENADO DE CLIENTE
        cur.execute("SELECT dni, nombre, apellidos, \
            domicilio, telefono FROM cliente")

        for dni, nombre, apellidos, domicilio, telefono in cur.fetchall():
            r.hset("cliente:" + dni,"dni",dni)
            r.hset("cliente:" + dni,"nombre",nombre)
            r.hset("cliente:" + dni,"apellidos",apellidos)
            r.hset("cliente:" + dni,"domicilio",domicilio)
            r.hset("cliente:" + dni,"telefono",telefono)
        print ("Se migró la tabla cliente")

        #LLENADO DE PRECIO
        cur.execute("SELECT tipo, precio FROM precio")

        for tipo, precio in cur.fetchall():
            r.hset("precio:" + tipo,"tipo",tipo)
            r.hset("precio:" + tipo,"precio",precio)
        print ("Se migró la tabla precio")

        #LLENADO DE FORMAPAGO
        cur.execute("SELECT forma, comision FROM formapago")

        for forma, comision in cur.fetchall():
            r.hset("formapago:" + forma,"forma",forma)
            r.hset("formapago:" + forma,"comision",comision)
        print ("Se migró la tabla formapago")

        #LLENADO DE HABITACION
        cur.execute("SELECT numero, superficie, bar, terraza, puedesupletoria, tipo FROM habitacion")

        for numero, superficie, bar, terraza, puedesupletoria, tipo in cur.fetchall():
            r.hset("habitacion:" + str(numero),"numero",numero)
            r.hset("habitacion:" + str(numero),"superficie",superficie)
            r.hset("habitacion:" + str(numero),"bar",bar)
            r.hset("habitacion:" + str(numero),"terraza",terraza)
            r.hset("habitacion:" + str(numero),"puedesupletoria",puedesupletoria)
            r.hset("habitacion:" + str(numero),"tipo",tipo)
        print ("Se migró la tabla habitacion")

        #LLENADO DE SERVICIO
        cur.execute("SELECT cods, descripcion, costeinterno, numreg FROM servicio")

        for cods, descripcion, costeinterno, numreg in cur.fetchall():
            r.hset("servicio:" + str(cods),"cods",cods)
            r.hset("servicio:" + str(cods),"descripcion",descripcion)
            r.hset("servicio:" + str(cods),"costeinterno",costeinterno)
            r.hset("servicio:" + str(cods),"numreg",numreg)
        print ("Se migró la tabla servicio")

        #LLENADO DE EMPLEADO
        cur.execute("SELECT numreg, nombre, incorporacion, sueldo, cods FROM empleado")

        for numreg, nombre, incorporacion, sueldo, cods in cur.fetchall():
            r.hset("empleado:" + str(numreg),"numreg",numreg)
            r.hset("empleado:" + str(numreg),"nombre",nombre)
            r.hset("empleado:" + str(numreg),"incorporacion",str(incorporacion))
            if sueldo is not None:
                r.hset("empleado:" + str(numreg),"sueldo",sueldo)
            if cods is not None:
                r.hset("empleado:" + str(numreg),"cods",cods)
        print ("Se migró la tabla empleado")
        
        #LLENADO DE PROVEEDOR
        cur.execute("SELECT nif, nombre, direccion, numreg FROM proveedor")

        for nif, nombre, direccion, numreg in cur.fetchall():
            r.hset("proveedor:" + nif,"nif",nif)
            r.hset("proveedor:" + nif,"nombre",nombre)
            r.hset("proveedor:" + nif,"direccion",direccion)
            r.hset("proveedor:" + nif,"numreg",numreg)
        print ("Se migró la tabla proveedor")

        #LLENADO DE FACTURA
        cur.execute("SELECT codigof, entrada, salida, dni, numero, supletoria, forma, total FROM factura")

        for codigof, entrada, salida, dni, numero, supletoria, forma, total in cur.fetchall():
            r.hset("factura:" + str(codigof),"codigof",codigof)
            r.hset("factura:" + str(codigof),"entrada",str(entrada))
            if salida is not None:
                r.hset("factura:" + str(codigof),"salida",str(salida))
            r.hset("factura:" + str(codigof),"dni",dni)
            r.hset("factura:" + str(codigof),"numero",numero)
            r.hset("factura:" + str(codigof),"supletoria",supletoria)
            r.hset("factura:" + str(codigof),"forma",forma)
            if total is not None:
                r.hset("factura:" + str(codigof),"total",total)
        print ("Se migró la tabla factura")

        #LLENADO DE FACTURA PROVEEDOR
        cur.execute("SELECT codfp, fecha, importe, nif, numreg FROM factura_prov")

        for codfp, fecha, importe, nif, numreg in cur.fetchall():
            r.hset("factura_prov:" + str(codfp),"codfp",codfp)
            if fecha is not None:
                r.hset("factura_prov:" + str(codfp),"fecha",str(fecha))
            r.hset("factura_prov:" + str(codfp),"importe",importe)
            r.hset("factura_prov:" + str(codfp),"nif",nif)
            r.hset("factura_prov:" + str(codfp),"numreg",numreg)
        print ("Se migró la tabla factura_prov")

        #LLENADO DE RESERVA
        cur.execute("SELECT dni, numero, entrada, salida FROM reserva")

        for dni, numero, entrada, salida in cur.fetchall():
            r.hset("reserva:" + dni + ":" + str(numero),"dni",dni)
            r.hset("reserva:" + dni + ":" + str(numero),"numero",numero)
            r.hset("reserva:" + dni + ":" + str(numero),"entrada",str(entrada))
            r.hset("reserva:" + dni + ":" + str(numero),"salida",str(salida))
        print ("Se migró la tabla reserva")

        #LLENADO DE LIMPIEZA
        cur.execute("SELECT numreg, numero, fecha FROM limpieza")

        for numreg, numero, fecha in cur.fetchall():
            r.hset("limpieza:" + str(numreg) + ":" + str(numero) + ":" + str(fecha),"numreg",numreg)
            r.hset("limpieza:" + str(numreg) + ":" + str(numero) + ":" + str(fecha),"numero",numero)
            r.hset("limpieza:" + str(numreg) + ":" + str(numero) + ":" + str(fecha),"fecha",str(fecha))
        print ("Se migró la tabla limpieza")

        #LLENADO DE INCLUYE
        cur.execute("SELECT codigof, cods, coste, fecha FROM incluye")

        for codigof, cods, coste, fecha in cur.fetchall():
            r.hset("incluye:" + str(codigof) + ":" + str(cods) + ":" + str(fecha),"codigof",codigof)
            r.hset("incluye:" + str(codigof) + ":" + str(cods) + ":" + str(fecha),"cods",cods)
            r.hset("incluye:" + str(codigof) + ":" + str(cods) + ":" + str(fecha),"coste",coste)
            r.hset("incluye:" + str(codigof) + ":" + str(cods) + ":" + str(fecha),"fecha",str(fecha))
        print ("Se migró la tabla incluye")

        #LLENADO DE USA
        cur.execute("SELECT cods, servicio_cods, fecha FROM usa")

        for cods, servicio_cods, fecha in cur.fetchall():
            r.hset("usa:" + str(cods) + ":" + str(servicio_cods) + ":" + str(fecha),"cods",cods)
            r.hset("usa:" + str(cods) + ":" + str(servicio_cods) + ":" + str(fecha),"servicio_cods",servicio_cods)
            r.hset("usa:" + str(cods) + ":" + str(servicio_cods) + ":" + str(fecha),"fecha",str(fecha))
        print ("Se migró la tabla incluye")

        conexion.close()

    except psycopg2.Error as e:
        print("ocurrió un error: ", e)


    