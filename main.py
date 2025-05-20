from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from validator import analizar_svg

app = FastAPI()

@app.post("/validar")
async def validar_svg(file: UploadFile = File(...)):
    contenido = await file.read()
    resultado = analizar_svg(contenido)
    return JSONResponse(content=resultado)
