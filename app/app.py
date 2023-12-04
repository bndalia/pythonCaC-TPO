from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerAuto import *
#from flask_cors import CORS

#Para subir archivo tipo foto al servidor
import os
from werkzeug.utils import secure_filename 


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app
#CORS(app)

msg  =''
tipo =''


#Creando mi decorador para el home, el cual retornara la Lista de Autos
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaAutos())


#RUTAS
@app.route('/registrar-auto', methods=['GET','POST'])
def addAuto():
    return render_template('public/acciones/add.html')


 
#Registrando nuevo auto
@app.route('/auto', methods=['POST'])
def formAddAuto():
    if request.method == 'POST':
        marca               = request.form['marca']
        modelo              = request.form['modelo']
        year                = request.form['year']
        color               = request.form['color']
        puertas             = request.form['puertas']
        combustible         = request.form['combustible']
        
        
        if(request.files['foto'] !=''):
            file     = request.files['foto'] #recibiendo el archivo
            nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
            resultData = registrarAuto(marca, modelo, year, color, puertas, combustible, nuevoNombreFile)
            if(resultData ==1):
                return render_template('public/layout.html', miData = listaAutos(), msg='El Registro fue un éxito', tipo=1)
            else:
                return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto', tipo=1)   
        else:
            return render_template('public/layout.html', msg = 'Debe cargar una foto', tipo=1)
            


@app.route('/form-update-auto/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateAuto(id)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaAutos(), msg='No existe el auto', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaAutos(), msg = 'Metodo HTTP incorrecto', tipo=1)          
 
   
  
@app.route('/ver-detalles-del-auto/<int:idAuto>', methods=['GET', 'POST'])
def viewDetalleAuto(idAuto):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelAuto(idAuto) #Funcion que almacena los detalles del auto
        
        if resultData:
            return render_template('public/acciones/view.html', infoAuto = resultData, msg='Detalles del Auto', tipo=1)
        else:
            return render_template('public/acciones/layout.html', msg='No existe el Auto', tipo=1)
    return redirect(url_for('inicio'))
    

@app.route('/actualizar-auto/<string:idAuto>', methods=['POST'])
def  formActualizarAuto(idAuto):
    if request.method == 'POST':
        marca           = request.form['marca']
        modelo          = request.form['modelo']
        year            = request.form['year']
        color           = request.form['color']
        puertas         = request.form['puertas']
        combustible        = request.form['combustible']
        
        #Script para recibir el archivo (foto)
        if(request.files['foto']):
            file     = request.files['foto']
            fotoForm = recibeFoto(file)
            resultData = recibeActualizarAuto(marca, modelo, year, color, puertas, combustible, fotoForm, idAuto)
        else:
            fotoAuto  ='sin_foto.jpg'
            resultData = recibeActualizarAuto(marca, modelo, year, color, puertas, combustible, fotoAuto, idAuto)

        if(resultData ==1):
            return render_template('public/layout.html', miData = listaAutos(), msg='Datos del auto actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/layout.html', miData = listaAutos(), msg='No se pudo actualizar', tipo=1)


#Eliminar auto
@app.route('/borrar-auto', methods=['GET', 'POST'])
def formViewBorrarAuto():
    if request.method == 'POST':
        idAuto         = request.form['id']
        nombreFoto      = request.form['nombreFoto']
        resultData      = eliminarAuto(idAuto, nombreFoto)

        if resultData ==1:

            return render_template('public/layout.html', miData = listaAutos(), msg='Registro eliminado con éxito', tipo=1)    
            #return jsonify([1])
            #return jsonify(["respuesta", 1])
        else:
            msg ='No se elimino el registro'
            return render_template('public/layout.html', miData = listaAutos(), msg='No se pudo eliminar registro', tipo=1) 
            #return jsonify([0])




def eliminarAuto(idAuto='', nombreFoto=''):
        
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur              = conexion_MySQLdb.cursor(dictionary=True)
    
    cur.execute('DELETE FROM autos WHERE id=%s', (idAuto,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount #retorna 1 o 0
    #print(resultado_eliminar)
    
    basepath = os.path.dirname (__file__) 
    url_File = os.path.join (basepath, 'static/assets/fotos_autos', nombreFoto)
    os.remove(url_File) #Borrar foto desde la carpeta
  
    

    return resultado_eliminar



def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/assets/fotos_autos', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

       
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)