from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()  # app FastAPI

# Redirigir la raíz "/" a "/docs"
@app.get("/", include_in_schema=False)  # no aparece en la documentación
def root():
    return RedirectResponse(url="/docs")
