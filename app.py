import os
from flask import Flask, render_template_string, request
from markupsafe import escape

app = Flask(__name__)

# Configuración de contacto
INFO = {
    "whatsapp": "https://wa.me/18093041128?text=Hola%20Farol%20Solution,%20necesito%20una%20automatización",
}

# HTML con Estrategia SEO y Publicaciones Motivadoras
HTML_BASE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Farol Solution | Automatización y Chatbots en RD</title>
    <meta name="description" content="Agencia líder en automatización de procesos y Chatbots inteligentes en República Dominicana. Optimizamos tu negocio para que vendas más con menos esfuerzo.">
    <meta name="keywords" content="Farol Solution, Automatización RD, Chatbots WhatsApp, Bots de ventas, Santo Domingo, Eficiencia empresarial">
    
    <meta property="og:title" content="🏮 Farol Solution: Tu Negocio en Piloto Automático">
    <meta property="og:description" content="¿Cansado de tareas manuales? Nosotros lo automatizamos.">
    <meta property="og:image" content="https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60">
    <meta property="og:url" content="https://farol-solution-production.up.railway.app">

    <style>
        body { background: #000; color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; text-align: center; }
        header { padding: 60px 20px; border-bottom: 5px solid #ff8c00; background: #050505; }
        h1 { color: #ff8c00; font-size: 2.5rem; margin: 0; text-transform: uppercase; letter-spacing: 4px; }
        .container { padding: 25px; max-width: 600px; margin: auto; }
        
        .section-title { color: #ff8c00; margin-top: 40px; font-size: 1.5rem; text-transform: uppercase; border-bottom: 2px solid #333; display: inline-block; padding-bottom: 5px; }
        
        /* Estilo de Publicaciones Informativas */
        .post { background: #111; padding: 25px; border-radius: 20px; border: 1px solid #222; margin: 25px 0; text-align: left; }
        .post h3 { color: #ff8c00; margin-top: 0; display: flex; align-items: center; }
        .post p { color: #aaa; line-height: 1.7; font-size: 1.05rem; }
        
        .btn { display: block; background: #ff8c00; color: #000; padding: 20px; border-radius: 15px; font-weight: bold; text-decoration: none; margin: 30px 0; font-size: 1.3rem; transition: 0.3s; box-shadow: 0 5px 20px rgba(255,140,0,0.4); }
        .btn:active { transform: scale(0.95); }
        
        form { background: #0a0a0a; padding: 30px; border-radius: 20px; border: 1px solid #ff8c00; margin-top: 40px; }
        input, textarea { width: 100%; padding: 15px; margin: 10px 0; border-radius: 10px; border: 1px solid #333; background: #000; color: #fff; box-sizing: border-box; font-size: 1rem; }
        button { width: 100%; padding: 20px; background: #fff; color: #000; font-weight: bold; border-radius: 10px; border: none; cursor: pointer; font-size: 1.2rem; }
        
        footer { padding: 60px 20px; color: #444; font-size: 0.9rem; }
    </style>
</head>
<body>
    <header>
        <h1>🏮 FAROL SOLUTION</h1>
        <p style="color: #888; letter-spacing: 1px;">Expertos en Eficiencia y Automatización</p>
    </header>

    <div class="container">
        <h2 class="section-title">Lo que tu negocio necesita</h2>

        <div class="post">
            <h3>🚀 Vende mientras duermes</h3>
            <p>Nuestros Chatbots de WhatsApp no solo responden, cierran ventas. Atiende a 100 clientes al mismo tiempo sin contratar más personal.</p>
        </div>

        <div class="post">
            <h3>💡 Cero Errores, Más Ganancia</h3>
            <p>Automatizamos tus facturas, inventarios y reportes. Deja de perder dinero en errores manuales y enfócate en crecer.</p>
        </div>

        <a href="{{ info.whatsapp }}" class="btn">ASESORÍA GRATIS POR WHATSAPP</a>

        <h2 class="section-title">Contáctanos</h2>
        <form method="POST">
            <input type="text" name="n" placeholder="Tu Nombre o Negocio" required>
            <textarea name="p" placeholder="¿Qué quieres automatizar hoy?" rows="4" required></textarea>
            <button type="submit">IMPULSAR MI NEGOCIO</button>
        </form>
    </div>

    <footer>
        <p>&copy; 2026 Farol Solution | Santo Domingo, República Dominicana.</p>
        <p>SEO Optimized for Dominican Businesses.</p>
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
            <h2>¡Recibido, {nombre}!</h2>
            <p>El Farol de la tecnología ya está trabajando en tu caso. Te escribiremos pronto.</p>
            <br>
            <a href='/' style='color:#fff; text-decoration:none; border:1px solid #fff; padding:10px; border-radius:5px;'>Volver</a>
        </body>
        """
    return render_template_string(HTML_BASE, info=INFO)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
