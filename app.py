import os
from flask import Flask, render_template_string, request
from markupsafe import escape

app = Flask(__name__)

INFO = {
    "whatsapp": "https://wa.me/18093041128?text=Hola%20Farol%20Solution,%20quiero%20empezar%20mi%20automatizacion",
}

HTML_BASE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farol Solution | Automatización y Chatbots RD</title>
    
    <meta name="description" content="Expertos en eficiencia empresarial y Chatbots en República Dominicana.">
    <meta property="og:title" content="🏮 Farol Solution: Tu Agencia de Automatización">
    <meta property="og:image" content="https://images.unsplash.com/photo-1551434678-e076c223a692?w=500">

    <style>
        body { background: #000; color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; text-align: center; }
        header { padding: 40px 20px; border-bottom: 4px solid #ff8c00; background: #0a0a0a; }
        h1 { color: #ff8c00; margin: 0; letter-spacing: 2px; text-transform: uppercase; font-size: 1.8rem; }
        .container { padding: 15px; max-width: 500px; margin: auto; }
        
        .section-title { color: #ff8c00; margin-top: 30px; font-size: 1.3rem; text-transform: uppercase; }
        
        /* TARJETAS DE SERVICIOS Y PRECIOS */
        .card { background: #111; border: 1px solid #333; border-radius: 15px; padding: 20px; margin: 15px 0; text-align: left; position: relative; }
        .card.premium { border: 2px solid #ff8c00; box-shadow: 0 0 15px rgba(255,140,0,0.2); }
        .card h3 { margin-top: 0; color: #ff8c00; }
        .price { font-size: 1.8rem; font-weight: bold; margin: 10px 0; }
        .features { padding-left: 15px; color: #bbb; font-size: 0.9rem; }
        .features li { margin-bottom: 8px; }

        /* PUBLICACIONES / MOVIMIENTO */
        .post { background: #070707; border-left: 4px solid #ff8c00; padding: 15px; border-radius: 5px; margin: 10px 0; text-align: left; font-size: 0.95rem; }
        .date { color: #ff8c00; font-size: 0.75rem; font-weight: bold; display: block; margin-bottom: 5px; }

        .btn { display: block; background: #ff8c00; color: #000; padding: 18px; border-radius: 10px; font-weight: bold; text-decoration: none; margin-top: 15px; text-align: center; font-size: 1.1rem; }
        
        form { background: #111; padding: 20px; border-radius: 15px; border: 1px solid #222; margin-top: 30px; }
        input, textarea { width: 100%; padding: 12px; margin: 8px 0; border-radius: 8px; border: 1px solid #333; background: #000; color: #fff; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #fff; color: #000; font-weight: bold; border-radius: 8px; border: none; font-size: 1.1rem; }
    </style>
</head>
<body>
    <header><h1>🏮 FAROL SOLUTION</h1><p style="color:#666; margin:5px 0 0 0;">Liderando la eficiencia en RD</p></header>

    <div class="container">
        <h2 class="section-title">Novedades del Farol</h2>
        <div class="post">
            <span class="date">HOY - 25 FEB 2026</span>
            <p><strong>✅ Actualización:</strong> Optimizamos los tiempos de respuesta. ¡Bots ahora 2x más rápidos!</p>
        </div>

        <h2 class="section-title">Planes y Soluciones</h2>
        
        <div class="card">
            <h3>Bot de Inicio</h3>
            <p>Ideal para negocios pequeños.</p>
            <div class="price">RD$ 4,900<small>/mes</small></div>
            <ul class="features">
                <li>Respuestas 24/7</li>
                <li>Menú interactivo</li>
                <li>Redirección a WhatsApp</li>
            </ul>
            <a href="{{ info.whatsapp }}" class="btn">ORDENAR BÁSICO</a>
        </div>

        <div class="card premium">
            <span style="background:#ff8c00; color:#000; font-size:0.7rem; padding:3px 8px; border-radius:5px; position:absolute; top:10px; right:10px; font-weight:bold;">RECOMENDADO</span>
            <h3>Sistema Full-Auto</h3>
            <p>Tu negocio en piloto automático.</p>
            <div class="price">RD$ 12,500<small>/mes</small></div>
            <ul class="features">
                <li>Integración con Inventarios</li>
                <li>Cobros por Azul/Pop/PayPal</li>
                <li>IA con memoria de clientes</li>
            </ul>
            <a href="{{ info.whatsapp }}" class="btn">ORDENAR PRO</a>
        </div>

        <h2 class="section-title">Consulta Personalizada</h2>
        <form method="POST">
            <input type="text" name="n" placeholder="Nombre / Empresa" required>
            <textarea name="p" placeholder="¿Qué quieres automatizar?" rows="3" required></textarea>
            <button type="submit">SOLICITAR COTIZACIÓN</button>
        </form>
    </div>

    <footer style="padding:40px; color:#333; font-size:0.8rem;">
        FAROL SOLUTION &copy; 2026 | Santo Domingo, RD.
    </footer>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = escape(request.form.get('n'))[:50]
        return f"<body style='background:#000;color:#ff8c00;text-align:center;padding-top:100px;font-family:sans-serif;'><h2>¡Excelente, {nombre}!</h2><p>Farol Solution analizará tu solicitud de inmediato.</p><br><a href='/' style='color:#fff; border:1px solid #fff; padding:10px; border-radius:5px; text-decoration:none;'>Volver</a></body>"
    return render_template_string(HTML_BASE, info=INFO)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
