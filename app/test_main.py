from fastapi.testclient import TestClient
from main import app
from fastapi import status

# Inicio de Test para CRUD de vacantes

def test_create_vacantes_ok():
    client = TestClient(app)

    vacante = {
            "position_name": "Senior Developer",
            "company_name": "Google",
            "salary": 8500000,
            "currency": "COP",
            "vacancy_id": "autofilled",
            "vacancy_ink": "https://www.google.com/jobs",
            "required_skills": [
                {
                "NoSQL": 3,
                "PostgresSQL": 1,
                "GIT": 1
                }
            ]
        }

    response = client.post(
        '/vacantes',
        json=vacante,
    )

    assert response.status_code == status.HTTP_200_OK, response.text


def test_get_vacantes_ok():
    client = TestClient(app)

    response = client.get(
        '/vacantes'
    )

    assert response.status_code == status.HTTP_200_OK, response.text


def test_get_one_vacante_ok():
    client = TestClient(app)

    response = client.get(
        '/vacantes'
    )
    
    new_response = client.get(
        '/vacante/{0}'.format(response.json()[0]["vacancy_id"])
    )

    assert new_response.status_code == status.HTTP_200_OK, new_response.text
    assert new_response.json()["vacancy_id"] == response.json()[0]["vacancy_id"]


def test_update_one_vacante_ok():
    client = TestClient(app)

    response = client.get(
        '/vacantes'
    )

    vacante = {
            "position_name": "Junior",
            "company_name": "Test company",
            "salary": 9999999,
            "currency": "COP",
            "vacancy_id": "autofilled",
            "vacancy_ink": "https://www.test.com",
            "required_skills": [
                {
                "Python": 1,
                "NoSQL": 2,
                "PostgresSQL": 3,
                "GIT": 3
                }
            ]
        }
    
    new_response = client.put(
        '/vacante/{0}'.format(response.json()[0]["vacancy_id"], json=vacante)
    )

    assert new_response.status_code == status.HTTP_200_OK


def test_delete_one_vacante_ok():
    client = TestClient(app)

    response = client.get(
        '/vacantes'
    )
    
    new_response = client.delete(
        '/vacante/{0}'.format(response.json()[0]["vacancy_id"])
    )

    assert new_response.status_code == status.HTTP_200_OK, new_response.text

# Fin de Test para CRUD de vacantes

# Inicio de Test para CRUD de usuarios


def test_create_usuarios_ok():
    client = TestClient(app)

    usuario = {
                "first_name": "Alejandro",
                "last_name": "Cepeda",
                "email": "alejomjc2011@gmail.com",
                "years_previous_experience": 5,
                "skills": [
                    {
                    "Python": 5,    
                    "NoSQL": 0,
                    "PostgresSQL": 5,
                    "GIT": 5
                    }
                ]
            }

    response = client.post(
        '/usuarios',
        json=usuario,
    )

    assert response.status_code == status.HTTP_200_OK, response.text


def test_get_usuarios_ok():
    client = TestClient(app)

    response = client.get(
        '/usuarios'
    )

    assert response.status_code == status.HTTP_200_OK, response.text



def test_get_one_usuario_ok():
    client = TestClient(app)

    response = client.get(
        '/usuarios'
    )
    
    new_response = client.get(
        '/usuario/{0}'.format(response.json()[0]["user_id"])
    )

    assert new_response.status_code == status.HTTP_200_OK, new_response.text
    assert new_response.json()["user_id"] == response.json()[0]["user_id"]


def test_update_one_usuario_ok():
    client = TestClient(app)

    response = client.get(
        '/usuarios'
    )

    usuario = {
                "first_name": "Alejandro",
                "last_name": "Cepeda",
                "email": "alejomjc2011@gmail.com",
                "years_previous_experience": 5,
                "skills": [
                    {
                    "Python": 5,    
                    "NoSQL": 1,
                    "PostgresSQL": 5,
                    "GIT": 5
                    }
                ]
            }
    
    new_response = client.put(
        '/usuario/{0}'.format(response.json()[0]["user_id"], json=usuario)
    )

    assert new_response.status_code == status.HTTP_200_OK, new_response.text


def test_delete_one_usuario_ok():
    client = TestClient(app)

    response = client.get(
        '/usuarios'
    )
    
    new_response = client.delete(
        '/usuario/{0}'.format(response.json()[0]["user_id"])
    )

    assert new_response.status_code == status.HTTP_200_OK, new_response.text

