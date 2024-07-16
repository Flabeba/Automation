import requests
import allure

class Company:

    def __init__(self, url):
        self.url = url
        
    @allure.step("Получаем токен авторизации")
    def get_token(self, user='bloom', password='fire-fairy'):
            creds = {
                'username': user,
                'password': password
            }
            resp = requests.post(f"{self.url}/auth/login", json=creds)
            return resp.json()["userToken"]

    @allure.step("Создаём компанию")
    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/company", json=company, headers=my_headers)
        return resp.json()

    @allure.step("Получаем список сотрудников")
    def get_list_employee(self, id):
        my_params = {
            "company": id
        }
        resp = requests.get(f"{self.url}/employee", params=my_params)
        return resp.json()

    @allure.step("Получаем данные сотрудника по ID")
    def get_employee_by_id(self, id_employee):
        resp = requests.get(f"{self.url}/employee/{id_employee}")
        return resp.json()

    @allure.step("Добавляем нового сотрудника")
    def add_new_employee(self, new_id, name, last_name):
        employee = {
            "id": 1,
            "firstName": name,
            "lastName": last_name,
            "middleName": "-",
            "companyId": new_id,
            "email": "test@test.ru",
            "url": "string",
            "phone": "89999999999",
            "birthdate": "2023-12-25T18:54:13.783Z",
            "isActive": 'true'
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/employee", headers=my_headers, json=employee)
        return resp.json()

    @allure.step("Обновление данных о сотруднике")
    def update_employee_info(self, id_employee, last_name, email):
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": True
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=my_headers, json=user_info)
        return resp.json()