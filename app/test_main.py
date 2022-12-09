from fastapi.testclient import TestClient
from main import app
from fastapi import status

def test_crud_vacantes_ok():
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
                "Python": 5,
                "NoSQL": 3
                }
            ]
        }

    response = client.post(
        '/vacantes',
        json=vacante,
    )

    assert response.status_code == status.HTTP_200_OK, response.text
    data = response.json()
    assert data['position_name'] == vacante['position_name']
    assert data['company_name'] == vacante['company_name']
    assert data['salary'] == vacante['salary']
    assert data['currency'] == vacante['currency']
    assert data['vacancy_ink'] == vacante['vacancy_ink']
    assert data['required_skills'] == vacante['required_skills']
