from flask import Flask, render_template_string, request
from markupsafe import escape
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'farol_solution_2026_safe')

INFO = {
    "whatsapp": "https://wa.me/18093041128?text=Hola%20Farol%20Solution,%20necesito%20una%20automatización",
    "email": "jose.colorvision@gmail.com"
}

HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farol Solution | Automatización</title>
    <style>
        body { background: #000; color: #fff; font-family: sans-serif; margin: 0; text-align: center; }
        header { padding: 50px 20px; border-bottom: 2px solid #ff8c00; }
        h1 { color: #ff8c00; margin: 0; font-size: 2rem; }
        .card { background: #111; margin: 20px; padding: 20px; border-radius: 15px; border: 1px solid #333; }
        .btn { display: block; background: #ff8c00; color: #000; padding: 20px; margin: 20px; border-radius: 10px; font-weight: bold; text-decoration: none; }
        input, textarea { width: 90%; padding: 15px; margin: 10px 0; border-radius: 8px; border: none; }
        button { width: 90%; padding: 15px; background: #fff; font-weight: bold; border-radius: 8px; border: none; }
    </style>
</head>
<body>
    <header><h1>🏮 FAROL SOLUTION</h1><p>Automatización de alto impacto</p></header>
    <div class="card"><h3>🚀 Servicios</h3><p>Webs Responsivas • Bots • Cloud</p></div>
    <a href="{{ info.whatsapp }}" class="btn">WHATSAPP DIRECTO</a>
    <form method="POST" style="padding:20px;">
        <input type="text" name="n" placeholder="Tu Nombre" required>
        <textarea name="p" placeholder="¿Qué necesitas?" required></textarea>
        <button type="submit">SOLICITAR CONSULTORÍA</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = escape(request.form.get('n'))[:50]
        return f"<body style='background:#000;color:#ff8c00;padding:50px;'><h2>¡Recibido {n}!</h2><p>Farol Solution te contactará.</p><a href='/' style='color:#fff;'>Volver</a></body>"
    return render_template_string(HTML, info=INFO)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
