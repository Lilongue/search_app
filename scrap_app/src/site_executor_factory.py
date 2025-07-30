from selenium.webdriver.common.by import By
import re
from selenium_handler import SeleniumHandler

class SiteExecutorFactory:
    @staticmethod
    def get_executor(url):
        if "yandex.ru/maps" in url:
            return MapsSeleniumSiteExecutor()  # + +
        elif "2gis.ru" in url:
            return TwogisSeleniumSiteExecutor()
        elif "zoon.ru" in url:
            return ZoonSeleniumSiteExecutor()
        elif "yell.ru" in url:
            return YellSeleniumSiteExecutor()
        elif "blizko.ru" in url:
            return BlizkoSeleniumSiteExecutor()
        elif "rusprofile.ru" in url:
            return RusProfileSeleniumSiteExecutor()
        elif "companies.rbc.ru" in url:
            return RbcSeleniumSiteExecutor()
        elif "vbankcenter.ru" in url:
            return VbankcenterSeleniumSiteExecutor()
        elif "list-org.com" in url:
            return ListOrgSeleniumSiteExecutor()
        elif "saby.ru" in url:
            return SabySeleniumSiteExecutor()
        elif "vk.com" in url:
            return VkSeleniumSiteExecutor()
        elif "e-ecolog.ru" in url:
            return EecologSeleniumSiteExecutor()
        elif "asktel.ru" in url:
            return AsktelSeleniumSiteExecutor()
        elif "bizly.ru" in url:
            return BizlySeleniumSiteExecutor()
        elif "sbis.ru" in url:
            return SbisSeleniumSiteExecutor()
        else:
            return SeleniumSiteExecutor()  # + +

class SeleniumSiteExecutor:
    """
    Класс для получения сайта с помощью Selenium WebDriver
    """
    def __init__(self):
        self.selenium_handler = SeleniumHandler()
        self.driver = None
    
    def get_site_info(self, url_link):
        try:
            self.driver = self.selenium_handler.get_interactive_driver(url_link)
            return self.driver.page_source, self._get_company_name(), self._get_inn_code()
        except Exception as e:
            print(f"Error getting site info for {url_link}: {e}")
            return None, None, None
        finally:
            # Clean up driver resources
            if self.selenium_handler:
                self.selenium_handler.cleanup_driver(self.driver)
            if self.driver:
                self.driver = None
    
    def _get_company_name(self):
        return None

    def _get_inn_code(self):
        return None


class MapsSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта yandex/maps
       """
       PHONE_CSS_CELECTOR = 'div.orgpage-phones-view__more'
       COMPANY_NAME_XPATH = '//h1[@itemprop="name"]'

       def get_site_info(self, url_link):
            try:
                self.driver = self.selenium_handler.get_interactive_driver(url_link)
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, self.PHONE_CSS_CELECTOR)
                except Exception as e:
                    print(f"Error fetching website {url_link}: {e}")
                    element = None
                if element and element.is_displayed() and element.is_enabled():
                    element.click()
                return self.driver.page_source, self._get_company_name(), self._get_inn_code()
            except Exception as e:
                print(f"Error getting site info for {url_link}: {e}")
                return None, None, None
            finally:
                if self.selenium_handler:
                    self.selenium_handler.cleanup_driver(self.driver)
                if self.driver:
                    self.driver = None
       
       def _get_company_name(self):
            if not self.driver.page_source:
                return None
            try:
                name_element = self.driver.find_element(By.XPATH, self.COMPANY_NAME_XPATH)
            except Exception as e:
                print(f"Error fetching website: {e}")
                name_element = None
            if name_element and name_element.is_displayed():
                return name_element.text
            return None

class TwogisSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта 2gis.ru
       """

       def get_site_info(self, url_link):
        try:
            self.driver = self.selenium_handler.get_interactive_driver(url_link)
            return self.driver.page_source, self._get_company_name(), self._get_inn_code()
        except Exception as e:
            print(f"Error getting site info for {url_link}: {e}")
            return str(e), None, None
        finally:
            # Clean up driver resources
            if self.selenium_handler:
                self.selenium_handler.cleanup_driver(self.driver)
            if self.driver:
                self.driver = None
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class ZoonSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта zoon
       """
       PHONE_CSS_CELECTOR = 'span.js-phone'
       COMPANY_NAME_XPATH = '//span[@itemprop="name"]'

       def get_site_info(self, url_link):
            try:
                self.driver = self.selenium_handler.get_interactive_driver(url_link)
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, self.PHONE_CSS_CELECTOR)
                    if element and element.is_displayed() and element.is_enabled():
                        element.click()
                except Exception as e:
                    print(f"Error fetching website {url_link}: {e}")
                return self.driver.page_source, self._get_company_name(), self._get_inn_code()
            except Exception as e:
                print(f"Error getting site info for {url_link}: {e}")
                return str(e), None, None
            finally:
                if self.selenium_handler:
                    self.selenium_handler.cleanup_driver(self.driver)
                if self.driver:
                    self.driver = None

       
       def _get_company_name(self):
            if not self.driver.page_source:
                return None
            try:
                name_element = self.driver.find_element(By.XPATH, self.COMPANY_NAME_XPATH)
            except Exception as e:
                print(f"Error fetching website: {e}")
                name_element = None
            if name_element and name_element.is_displayed():
                return name_element.text
            return None


class YellSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта yell.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None


class BlizkoSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта blizko.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None


class RusProfileSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта rusprofile.ru
       """
       COMPANY_NAME_XPATH = '//h1[@itemprop="name"]'
       COMPANY_INN_XPATH = '//span[@id="clip_inn"]'

       def get_site_info(self, url_link):
            self.driver.get(url_link)
            return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            if not self.driver.page_source:
                return None
            try:
                name_element = self.driver.find_element(By.XPATH, self.COMPANY_NAME_XPATH)
            except Exception as e:
                print(f"Error fetching website: {e}")
                name_element = None
            if name_element and name_element.is_displayed():
                return name_element.text
            return None
       
       def _get_inn_code(self):
            if not self.driver.page_source:
                return None
            try:
                inn_element = self.driver.find_element(By.XPATH, self.COMPANY_INN_XPATH)
            except Exception as e:
                print(f"Error fetching website: {e}")
                inn_element = None
            if inn_element and inn_element.is_displayed():
                return inn_element.text
            return None

class RbcSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта companies.rbc.ru
       """
       COMPANY_NAME_XPATH = '//h1[@class="company-headline__title"]/span'

       def get_site_info(self, url_link):
            self.driver.get(url_link)
            return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            if not self.driver.page_source:
                return None
            try:
                name_element = self.driver.find_element(By.XPATH, self.COMPANY_NAME_XPATH)
            except Exception as e:
                print(f"Error fetching website: {e}")
                name_element = None
            if name_element and name_element.is_displayed():
                return name_element.text
            return None



class VbankcenterSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта vbankcenter.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class ListOrgSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта list-org.com
       """
       COMPANY_NAME_XPATH = '//h1[@itemprop="name"]'
       COMPANY_INN_XPATH = '//span[@id="clip_inn"]'

    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            if not self.driver.page_source:
                return None
            try:
                head_elements = self.driver.find_elements(By.TAG_NAME, 'h1')
                if not head_elements:
                    return None
                name_element = head_elements[0]
            except Exception as e:
                print(f"Error fetching website: {e}")
                name_element = None
            if name_element and name_element.is_displayed():
                return name_element.text
            return None
       
       def _get_inn_code(self):
            if not self.driver.page_source:
                return None
            try:
                td_elements = self.driver.find_elements(By.TAG_NAME, 'td')
                if not td_elements:
                    return None
                for element in td_elements:
                    inn_value = self._find_inn(element.text)
                    if inn_value:
                        return inn_value
            except Exception as e:
                print(f"Error fetching website: {e}")
            return None
       
       def _find_inn(self, text):
            pattern = r"^(\d{10}|\d{12})\s*/\s*(\d{10}|\d{12})$"
 
            match = re.match(pattern, text)
            if match:
                return match.group(1)
            return None
        



class SabySeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта saby.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class VkSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта vk.com
       """
       def get_site_info(self, url_link):
            self.driver.get(url_link)
            return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class EecologSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта e-ecolog.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class AsktelSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта asktel.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class BizlySeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта bizly.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None

class SbisSeleniumSiteExecutor(SeleniumSiteExecutor):
       """
       Класс для получения сайта sbis.ru
       """
    #    def get_site_info(self, url_link):
    #         self.driver.get(url_link)
    #         return self.driver.page_source, self._get_company_name(), self._get_inn_code()
       
       def _get_company_name(self):
            return None
       
       def _get_inn_code(self):
            return None
