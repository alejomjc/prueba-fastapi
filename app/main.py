from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional, List, Dict
from uuid import uuid4 as uuid


app = FastAPI()
vacantes = []
usuarios = []


class RequiredSkills(BaseModel):
    Python: Optional[int] = 1
    NoSQL: Optional[int] = 2


class Vacante(BaseModel):
    position_name: str = "Python Dev"
    company_name: str = "Test company"
    salary: float = 9999999
    currency: str = "COP"
    vacancy_id: Optional[str] = "autofilled"
    vacancy_ink: str = "https://www.test.com"
    required_skills : List[RequiredSkills]


class Usuario(BaseModel):
    user_id: Optional[str] = "autofilled"
    first_name: str = "Test Name"
    last_name: str = "Test Last Name"
    email: str = "un.test.no.hace.mal@gmail.com"
    years_previous_experience: int = 5
    skills: List[RequiredSkills]


@app.get('/')
def read_root():
    return RedirectResponse(url="/docs/")


# Inicio de bloque Vacantes


@app.get('/vacantes')
def get_vacantes():
    return  vacantes


@app.post('/vacantes')
def save_vacante(vacante: Vacante):
    vacante.vacancy_id =  str(uuid())
    vacantes.append(vacante.dict())
    return {"respuesta": "OK"}


@app.get('/vacante/{vacancy_id}')
def get_vacante(vacancy_id: str):
    for vacante in vacantes:
        if vacante['vacancy_id'] == vacancy_id:
            return  vacante
    raise HTTPException(status_code=404, detail="Vacante no encontrada")


@app.put('/vacante/{vacancy_id}')
def update_vacante(vacancy_id: str, nuevoVacante: Vacante):
    for index, vacante in enumerate(vacantes):
        if vacante['vacancy_id'] == vacancy_id:
            vacantes[index]["position_name"] = nuevoVacante.position_name
            vacantes[index]["company_name"] = nuevoVacante.company_name
            vacantes[index]["salary"] = nuevoVacante.salary
            vacantes[index]["currency"] = nuevoVacante.currency
            vacantes[index]["vacancy_ink"] = nuevoVacante.vacancy_ink
            vacantes[index]["required_skills"] = nuevoVacante.required_skills
            return {"message": "OK"}
    raise HTTPException(status_code=404, detail="Vacante no encontrada")


@app.delete('/vacante/{vacancy_id}')
def delete_vacante(vacancy_id: str):
    for index, vacante in enumerate(vacantes):
        if vacante['vacancy_id'] == vacancy_id:
            vacantes.pop(index)
            return {"message": "OK"}
    raise HTTPException(status_code=404, detail="Vacante no encontrada")


# Fin de bloque Vacantes

# Inicio de bloque Usuarios


@app.get('/usuarios')
def get_usuarios():
    return  usuarios


@app.post('/usuarios')
def save_usuario(usuario: Usuario):
    usuario.user_id =  str(uuid())
    usuarios.append(usuario.dict())
    return {"respuesta": "OK"}


@app.get('/usuario/{user_id}')
def get_usuario(user_id: str):
    for usuario in usuarios:
        if usuario['user_id'] == user_id:
            return  usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.put('/usuario/{user_id}')
def update_usuario(user_id: str, nuevoUsuario: Usuario):
    for index, usuario in enumerate(usuarios):
        if usuario['user_id'] == user_id:
            usuarios[index]["first_name"] = nuevoUsuario.first_name
            usuarios[index]["last_name"] = nuevoUsuario.last_name
            usuarios[index]["email"] = nuevoUsuario.email
            usuarios[index]["years_previous_experience"] = nuevoUsuario.years_previous_experience
            usuarios[index]["skills"] = nuevoUsuario.skills
            return {"message": "OK"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete('/usuario/{user_id}')
def delete_usuario(user_id: str):
    for index, usuario in enumerate(usuarios):
        if usuario['user_id'] == user_id:
            usuarios.pop(index)
            return {"message": "OK"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# Inicio de bloque Usuarios

# Consulta de vacantes por usuarios


@app.get('/usuario/{user_id}')
def get_vacantes_por_usuario(user_id: str):
    vacantes_disponibles = []
    usuario_buscado = ''
    for usuario in usuarios:
        if usuario['user_id'] == user_id:
            usuario_buscado = usuario

    if usuario_buscado:
        for user_skill in usuario_buscado['Skills']:
            for vacante in vacantes:
                for required_skill in vacante['RequiredSkills']:
                    if user_skill == required_skill:
                        vacantes_disponibles.append(vacante)

        if vacantes_disponibles:
            return vacantes_disponibles
        else:
            return {"mensaje": "No hay ninguna vacante a la que pueda aplicar"}
        
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
