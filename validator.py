from openai import OpenAI
import os
import base64

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analizar_svg(svg_bytes):
    b64_svg = base64.b64encode(svg_bytes).decode("utf-8")
    mensaje = {
        "role": "user",
        "content": [
            {"type": "text", "text": "Validá esta ilustración SVG según las reglas de Andes Ilustraciones. Respondé con el formato de checklist."},
            {"type": "image", "image_url": {"url": f"data:image/svg+xml;base64,{b64_svg}"}}
        ]
    }
respuesta = client.chat.completions.create(
    model="gpt-4-vision",
        messages=[mensaje],
        max_tokens=1000
    )
    return {"respuesta": respuesta.choices[0].message.content}
