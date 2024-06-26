import datetime
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

def test_add_new_employee():

    #Создать новую компанию
    name = "DONOR"
    descr = "magazin books"
    result = api.create_company(name, descr)
    new_id = result["id"]

    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # получить список сотруднико до...
    body = api.get_employees_list(companyId)
    len_before = len(body)

     # добавить нового сотрудника
    lastName = "Mazaeva"
    firstName = "Mia"
    middleName = "Aleksandrovna"
    email = "miya.mazaeva@mail.ru"
    url = "string"
    phone = "865423175266"
    birthdate = datetime.date.today().isoformat()
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]

    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["lastName"] == lastName
    assert body[-1]["firstName"] == firstName
    assert body[-1]["middleName"] == middleName
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == phone
    assert body[-1]["birthdate"] == birthdate
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():

    #Создать новую компанию
    name = "ООО Иванов"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    #Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']

    # получить список сотрудников новой компании до....
    body = api.get_employees_list(companyId)
    begin_list = len(body)

    # добавить нового сотрудника
    lastName = "Mazaeva"
    firstName = "Mia"
    middleName = "Alekseevna"
    email = "miya.mazaeva@mail.ru"
    url = "string"
    phone = "865423175456"
    birthdate = datetime.date.today().isoformat()
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]

    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1

    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    assert body[-1]["lastName"] ==  lastName
    assert body[-1]["firstName"] == firstName
    assert body[-1]["middleName"] == middleName
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  phone
    assert body[-1]["birthdate"] == birthdate
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():

    #Создать новую компанию
    name = "ИП Машинист"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # добавить нового сотрудника
    firstName = "irina"
    lastName = "Базарева"
    middleName = "alekseevna"
    email = "bazareva123@mail.ru"
    url = "string"
    phone = "865423175456"
    birthdate = datetime.date.today().isoformat()
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Козин"
    new_email = "bzreva123@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "bzreva123@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False

def test_delete_employee():

    #Создать новую компанию
    name = "ООО Стекло"
    descr = "промышленность"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # добавить нового сотрудника
    firstName = "Наталья"
    lastName = "Воронина"
    middleName = "Николаевна"
    email = "voronina123@mail.ru"
    url = "string"
    phone = "865423175789"
    birthdate = datetime.date.today().isoformat()
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]

    # удалить сотрудника
    del_emp = api.delete_employee(emp_id)

    # Проверить, что сотрудник был удален
    assert del_emp is not None, "Сотрудник не был удален"