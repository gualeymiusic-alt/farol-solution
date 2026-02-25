import os
from flask import Flask, render_template_string, request
from markupsafe import escape

app = Flask(__name__)

# Configuración de contacto
INFO = {
    "whatsapp": "https://wa.me/18093041128?text=Hola%20Farol%20Solution,%20necesito%20una%20automatización",
    "email": "jose.colorvision@gmail.com"
}

HTML_BASE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farol Solution | Automatización</title>
    <style>
        body { background: #000; color: #fff; font-family: sans-serif; margin: 0; text-align: center; }
        header { padding: 40px 20px; border-bottom: 3px solid #ff8c00; }
        h1 { color: #ff8c00; font-size: 2.2rem; margin: 0; letter-spacing: 2px; }
        .container { padding: 20px; max-width: 500px; margin: auto; }
        .card { background: #111; padding: 25px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; }
        .btn { display: block; background: #ff8c00; color: #000; padding: 18px; border-radius: 10px; font-weight: bold; text-decoration: none; margin: 15px 0; font-size: 1.1rem; }
        input, textarea { width: 100%; padding: 15px; margin: 10px 0; border-radius: 8px; border: 1px solid #444; background: #1a1a1a; color: #fff; box-sizing: border-box; }
        button { width: 100%; padding: 18px; background: #fff; color: #000; font-weight: bold; border-radius: 8px; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <header>
        <h1>🏮 FAROL SOLUTION</h1>
        <p>Expertos en Automatización de Procesos</p>
    </header>
    <div class="container">
        <div class="card">
            <h3>Soluciones Inteligentes</h3>
            <p>Bots, Integraciones y Desarrollo Web para tu negocio.</p>
        </div>
        <a href="{{ info.whatsapp }}" class="btn">SOLICITAR POR WHATSAPP</a>
        <form method="POST" class="card">
            <input type="text" name="n" placeholder="Tu Nombre" required>
            <textarea name="p" placeholder="¿En qué podemos ayudarte?" rows="4" required></textarea>
            <button type="submit">ENVIAR CONSULTA</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = escape(request.form.get('n'))[:50]
        return f"<body style='background:#000;color:#ff8c00;text-align:center;padding-top:100px;font-family:sans-serif;'><h2>¡Excelente {nombre}!</h2><p>Farol Solution ha recibido tu mensaje.</p><br><a href='/' style='color:#fff;'>Volver atrás</a></body>"
    return render_template_string(HTML_BASE, info=INFO)

if __name__ == "__main__":
    # CLAVE: Railway asigna el puerto mediante la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
