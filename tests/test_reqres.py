import allure
import requests

from config import BASE_URL
from src.schemas.get_users_model import GetUsersResponse, GetSingleUserModel
from src.schemas.registration_user_model import RegistrationUserResponse, AuthorizationUserResponse
from src.schemas.update_user_model import UpdateUserResponse
from tests.data.users_bodies import body_registration_user, body_update_user
from tests.utils.log_util import log_response


@allure.story("Получение списка пользователей из метода GET /users")
@allure.tag("POSTITVE")
def test_get_users():
    with allure.step("Получаем список пользователей"):
        response = requests.get(url=f"{BASE_URL}/users")
    
    assert response.status_code == 200
    GetUsersResponse(**response.json())
    log_response(response)


@allure.story("Создание нового пользователя методом POST /register")
@allure.tag("POSITIVE")
def test_create_user():
    with allure.step("Создаем нового пользователя"):
        response = requests.post(url=f"{BASE_URL}/register", json=body_registration_user)
    
    assert response.status_code == 200
    RegistrationUserResponse(**response.json())
    log_response(response)


@allure.story("Обновление пользователя методом PUT /users")
@allure.tag("POSITIVE")
def test_update_user():
    with allure.step("Обновляем пользователя"):
        response = requests.put(url=f"{BASE_URL}/users/2", json=body_update_user)
    
    assert response.status_code == 200
    UpdateUserResponse(**response.json())
    log_response(response)


@allure.story("Удаление пользователя методом DELETE /users")
@allure.tag("POSITIVE")
def test_delete_user():
    user_id = 2
    with allure.step(f"Удаляем пользователя с id = {user_id}"):
        response = requests.delete(url=f"{BASE_URL}/users/{user_id}")
    
    assert response.status_code == 204
    log_response(response)


@allure.story("Авторизация пользователя")
@allure.tag("POSITIVE")
def test_success_login():
    with allure.step("Пользователь авторизуется"):
        response = requests.post(url=f"{BASE_URL}/login", json=body_registration_user)
    
    assert response.status_code == 200
    AuthorizationUserResponse(**response.json())
    log_response(response)


@allure.story("Получение данных о конкретном пользователе")
@allure.tag("POSITIVE")
def test_get_single_user():
    user_id = 2
    with allure.step(f"Получаем данные о пользователе с id = {user_id}"):
        response = requests.get(url=f"{BASE_URL}/users/{user_id}")
    
    assert response.status_code == 200
    GetSingleUserModel(**response.json())
    log_response(response)


@allure.story("Авторизация пользователя")
@allure.tag("NEGATIVE")
def test_error_login():
    with allure.step("Пользователь авторизуется"):
        response = requests.post(url=f"{BASE_URL}/login", json={"email": "peter@klaven"})
    
    assert response.status_code == 400
    assert response.json().get("error") == "Missing password"
    log_response(response)


@allure.story("Получение данных о конкретном пользователе")
@allure.tag("NEGATIVE")
def test_error_get_single_user():
    user_id = 23
    with allure.step(f"Получаем данные о пользователе с id = {user_id}"):
        response = requests.get(url=f"{BASE_URL}/users/{user_id}")
    
    assert response.status_code == 404
    log_response(response)
