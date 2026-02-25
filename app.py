import os
from flask import Flask, render_template_string, request
from markupsafe import escape

app = Flask(__name__)

# Configuración de contacto
INFO = {
    "whatsapp": "https://wa.me/18093041128?text=Hola%20Farol%20Solution,%20necesito%20una%20automatización",
}

# HTML con Estrategia SEO integrada
HTML_BASE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Farol Solution | Automatización de Negocios en RD</title>
    <meta name="description" content="Farol Solution: Expertos en Chatbots de WhatsApp, automatización de ventas y procesos para empresas en República Dominicana. ¡Ahorra tiempo y dinero!">
    <meta name="keywords" content="automatización, chatbots whatsapp, bots de venta, eficiencia empresarial, Farol Solution, Santo Domingo, automatizar procesos">
    <meta name="author" content="Farol Solution">
    
    <meta property="og:title" content="Farol Solution | Agencia de Automatización">
    <meta property="og:description" content="Transformamos tu negocio con bots y procesos automáticos.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://farol-solution-production.up.railway.app">

    <style>
        body { background: #000; color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; text-align: center; }
        header { padding: 60px 20px; border-bottom: 4px solid #ff8c00; background: linear-gradient(to bottom, #111, #000); }
        h1 { color: #ff8c00; font-size: 2.5rem; margin: 0; text-transform: uppercase; letter-spacing: 2px; }
        .container { padding: 20px; max-width: 600px; margin: auto; }
        
        /* SEO Friendly Sections */
        .section-title { color: #ff8c00; margin-top: 40px; font-size: 1.6rem; text-transform: uppercase; border-bottom: 1px solid #333; display: inline-block; padding-bottom: 5px; }
        .info-card { background: #111; padding: 25px; border-radius: 15px; border-left: 5px solid #ff8c00; margin: 20px 0; text-align: left; transition: 0.3s; }
        .info-card:hover { background: #1a1a1a; transform: translateX(5px); }
        .info-card h3 { color: #ff8c00; margin-top: 0; font-size: 1.3rem; }
        .info-card p { color: #ccc; line-height: 1.6; font-size: 1rem; }

        .btn { display: block; background: #ff8c00; color: #000; padding: 20px; border-radius: 12px; font-weight: bold; text-decoration: none; margin: 30px 0; font-size: 1.2rem; box-shadow: 0 5px 20px rgba(255,140,0,0.4); }
        
        form { background: #111; padding: 30px; border-radius: 15px; border: 1px solid #333; margin-top: 30px; }
        input, textarea { width: 100%; padding: 15px; margin: 12px 0; border-radius: 8px; border: 1px solid #444; background: #000; color: #fff; box-sizing: border-box; font-size: 1rem; }
        button { width: 100%; padding: 20px; background: #fff; color: #000; font-weight: bold; border-radius: 10px; border: none; cursor: pointer; font-size: 1.1rem; transition: 0.3s; }
        button:hover { background: #ff8c00; color: #000; }
        
        footer { padding: 50px 20px; color: #555; font-size: 0.9rem; }
    </style>
</head>
<body>
    <header>
        <h1>🏮 FAROL SOLUTION</h1>
        <p style="color: #ff8c00; font-weight: bold; margin-top: 10px;">Liderando la Automatización en República Dominicana</p>
    </header>

    <div class="container">
        <h2 class="section-title">Servicios de Alta Eficiencia</h2>
        
        <div class="info-card">
            <h3>🤖 Chatbots para WhatsApp</h3>
            <p>Implementamos sistemas inteligentes que responden, filtran y venden por ti en la plataforma favorita de tus clientes en RD.</p>
        </div>

        <div class="info-card">
            <h3>⚙️ Flujos de Trabajo Automáticos</h3>
            <p>Conectamos tus herramientas para eliminar tareas repetitivas. Menos errores humanos, más rentabilidad para tu empresa.</p>
        </div>

        <a href="{{ info.whatsapp }}" class="btn">ASESORÍA POR WHATSAPP</a>

        <h2 class="section-title">Consulta Gratuita</h2>
        <p style="color: #888;">Impulsa tu negocio con tecnología de punta. Cuéntanos tu caso abajo.</p>
        
        <form method="POST">
            <input type="text" name="n" placeholder="Nombre completo o Empresa" required>
            <textarea name="p" placeholder="¿Qué proceso te gustaría automatizar hoy?" rows="4" required></textarea>
            <button type="submit">ENVIAR CONSULTA SEO-OPTIMIZADA</button>
        </form>
    </div>

    <footer>
        <p>&copy; 2026 Farol Solution | Santo Domingo Este, RD.</p>
        <p>Especialistas en Desarrollo y Automatización de Procesos.</p>
    </footer>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = escape(request.form.get('n'))[:50]
        return f"""
        <body style='background:#000;color:#ff8c00;text-align:center;padding-top:100px;font-family:sans-serif;'>
            <h2>¡Excelente elección, {nombre}!</h2>
            <p>Tu solicitud ha sido procesada. El equipo de Farol Solution te contactará.</p>
            <br>
            <a href='/' style='color:#fff; text-decoration:none; border:1px solid #fff; padding:10px; border-radius:5px;'>Volver al inicio</a>
        </body>
        """
    return render_template_string(HTML_BASE, info=INFO)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
