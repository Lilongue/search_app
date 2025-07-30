from bs4 import BeautifulSoup
import re
from employer_info import EmployerInfo
from site_executor_factory import SiteExecutorFactory


class SiteInfoExtractor:
    """
    Класс для извлечения информации о работодатели из переданного сайта
    """
    _processed_content = ""
    _company_name = None
    _inn_code = None


    def __init__(self):
        pass

    def get_site_info(self, url_link):
        siteExecutor = SiteExecutorFactory.get_executor(url_link)

        try:
            site, company_name, inn_code = siteExecutor.get_site_info(url_link)
            self._company_name = company_name
            self._inn_code = inn_code
            soup = BeautifulSoup(site, 'html.parser')
            cleaned_html = '\n'.join([line for line in soup.stripped_strings])
            self._processed_content = cleaned_html.strip()
            return self._processed_content
        except Exception as e:
            return f"Error fetching website: {e}"

    def extract_employer_info(self, employer_info: EmployerInfo):
        extracted_info = EmployerInfo()
        extracted_info.phone = self._extract_phone(employer_info.phone) or self._extract_phone_variously(employer_info.phone)
        extracted_info.email = self._extract_email(employer_info.email)
        extracted_info.site = self._extract_site(employer_info.site)
        extracted_info.organization_name = self._company_name or self._extract_organization_name(employer_info.organization_name)
        extracted_info.contact_person_name = self._extract_contact_person_name(employer_info.contact_person_name)
        extracted_info.code = self._inn_code or self._extract_code(employer_info.code)
        return extracted_info

    def _extract_phone(self, phone):
        if not phone:
            return phone
        found_index = self._processed_content.find(phone)

        if found_index != -1:
            return phone
        return None
    
    def _extract_phone_variously(self, phone):
        if not phone:
            return phone
        info_extractor = InfoExtractor(self._processed_content)
        found_phones = info_extractor.extract_phones()
        for found_phone in found_phones:
            if info_extractor.normalize_phone(found_phone) == info_extractor.normalize_phone(phone):
                return found_phone
        return None


    def _extract_email(self, email):
        if not email:
            return email
        found_index = self._processed_content.find(email)

        if found_index != -1:
            return email
        return None


    def _extract_site(self, site):
        if not site:
            return site
        found_index = self._processed_content.find(site)

        if found_index != -1:
            return site
        return None

    def _extract_organization_name(self, organization_name):
        if not organization_name:
            return organization_name
        info_extractor = InfoExtractor(self._processed_content)
        return info_extractor.extract_organization_name(organization_name)


    def _extract_contact_person_name(self, contact_person_name):
        if not contact_person_name:
            return contact_person_name
        found_index = self._processed_content.find(contact_person_name)

        if found_index != -1:
            return contact_person_name
        return None
    
    def _extract_code(self, code):
        info_extractor = InfoExtractor(self._processed_content)
        return info_extractor.extract_code()


class InfoExtractor:
    def __init__(self, text):
        self._text = text
    
    def extract_phones(self):
        """
        Извлекаем все телефонные номера из текста.
        Регулярное выражение ищет номера в различных форматах.
        """
        # This regex finds numbers in formats like +7(123)456-78-90, (123)456-78-90, 123-45-67, 123-4567
        phone_regex = r"((?:\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}|\d{3}[\s-]?\d{4}|\d{3}[\s-]?\d{2}[\s-]?\d{2})"
        return re.findall(phone_regex, self._text)

    def extract_emails(self):
        """
        Извлекаем все email из текста
        """
        email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        return re.findall(email_regex, self._text)

    def extract_sites(self):
        pass

    def extract_organization_name(self, organization_name):
        if not organization_name:
            return organization_name
        lower_text = self._text.lower()
        found_index = lower_text.find(organization_name.lower())
        if found_index != -1:
            return self._text[found_index:found_index + len(organization_name)]
        clean_name = re.sub(r'[^a-zA-Z0-9\sа-яА-Я]', '', organization_name).lower()
        clean_name = ' '.join(clean_name.split())
        found_index = lower_text.find(clean_name)
        if found_index != -1:
            return self._text[found_index:found_index + len(clean_name)]
        return None

    def extract_contact_person_name(self):
        pass

    def normalize_phone(self, phone):
        """
        Takes a phone number in any format and returns a string containing only
        digits, with a leading '+' if it was present in the input string.
        All whitespace and other symbols are removed.
        """
        if not phone:
            return phone
        # Remove all non-digit characters
        cleaned_phone = re.sub(r'\D', '', phone)
        if phone.strip().startswith('+'):
            return '+' + cleaned_phone
        if phone.strip().startswith('8'):
            return '+7' + cleaned_phone[1:]
        return cleaned_phone
    
    def extract_code(self):
        inn_code_regexp = r'ИНН\s+(\d{10}|\d{12})'
        codes = re.findall(inn_code_regexp, self._text)
        if len(codes) > 0:
            return codes[0]
        return None




if __name__ == '__main__':
    employer_info = EmployerInfo()
    employer_info.phone = "8 (921) 962-15-09"
    employer_info.site = "nastroenie-dental.ru"
    employer_info.organization_name = "ООО \"Настроение\""
    site_info_extractor = SiteInfoExtractor()
    website_url = input("Enter the website URL: ")
    site_info = site_info_extractor.get_site_info(website_url)
    # print(site_info)
    extracted_info = site_info_extractor.extract_employer_info(employer_info)
    print(extracted_info)
