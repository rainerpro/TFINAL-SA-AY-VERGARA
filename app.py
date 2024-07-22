from flask import Flask, render_template, request, redirect, url_for
from programa.usuario import Usuario
from programa.transf import realizar_transferencia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']
        nombre_completo = request.form['nombre_completo']
        num_cedula = request.form['num_cedula']
        saldo_inicial = float(request.form['saldo_inicial'])
        
        Usuario.registrar_usuario(nombre_usuario, contrasena, nombre_completo, num_cedula, saldo_inicial)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        # Extrae y maneja los datos necesarios para la transferencia aquí
        realizar_transferencia()
        return redirect(url_for('index'))
    return render_template('transfer.html')

if __name__ == "__main__":
    app.run(debug=True)
