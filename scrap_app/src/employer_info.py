class EmployerInfo:
    """
    Класс для хранения информации о работодателе
    """
    def __init__(self, phone = None, email = None, site = None, organization_name = None, contact_person_name = None, code = None):
        self._phone = phone
        self._email = email
        self._site = site
        self._organization_name = organization_name
        self._contact_person_name = contact_person_name
        self._code = code

    def __str__(self):
        return f'Phone: {self._phone}, Email: {self._email}, Site: {self._site}, Organization Name: {self._organization_name}, Contact Person Name: {self._contact_person_name}, INN: {self._code}'

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, site):
        self._site = site

    @property
    def organization_name(self):
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        self._organization_name = organization_name

    @property
    def contact_person_name(self):
        return self._contact_person_name

    @contact_person_name.setter
    def contact_person_name(self, contact_person_name):
        self._contact_person_name = contact_person_name
    
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code
