from conexionBD import *

def crear(ususario_id,titulo,descripcion):
    try:
        cursor.execute("insert into notas(ususario:id,titulo,descripcion,fecha) values(%s,%s,%s,Now())",(ususario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where ususario_id=%s",(usuario_id,))
        lista=cursor.fetchall()
    except:
        return []
    

def cabiar(id,titulo,descripcion):
    try:
        cursor.execute("update notas set titulo=%s, descripcion=%s, fecha=Now()" \
        " where id=%s",(titulo,descripcion,id))
        conexion.commit()
        return True
    except:
        return False
    
def borrar(id):
    try:
        cursor.execute("delete from notas where id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False    