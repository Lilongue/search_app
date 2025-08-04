from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import tempfile


class SeleniumHandler:
    def __init__(self):
        self.driver_path = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')

    def get_interactive_driver(self, url):
        """
        Получить интерактивный экземпляр WebDriver для URL

        Args:
            url (str): URL для навигации

        Returns:
            webdriver.Chrome: Интерактивный экземпляр WebDriver

        Raises:
            Exception: Если создание драйвера не удалось
        """
        user_data_dir = None

        try:
            user_data_dir = tempfile.mkdtemp()

            # Configure Chrome options
            options = webdriver.ChromeOptions()
            options.add_argument(f'--user-data-dir={user_data_dir}')
            options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-popup-blocking')
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')

            # Initialize WebDriver
            driver = webdriver.Chrome(service=Service(self.driver_path), options=options)

            driver.get(url)

            driver._user_data_dir = user_data_dir
            driver._cleanup_required = True

            return driver

        except Exception as e:
            if user_data_dir:
                import shutil
                try:
                    shutil.rmtree(user_data_dir)
                except Exception as e:
                    print(f"Failed to remove user data directory {user_data_dir}: {e}")
            raise Exception(f"Failed to create interactive driver for URL {url}: {str(e)}")

    def cleanup_driver(self, driver):
        """
        Очистить ресурсы для экземпляра WebDriver

        Args:
            driver: Экземпляр WebDriver для очистки
        """
        if driver and hasattr(driver, '_cleanup_required') and driver._cleanup_required:
            try:
                driver.quit()
            except Exception as e:
                print(f"Failed to quit driver {driver}: {e}")

            if hasattr(driver, '_user_data_dir') and driver._user_data_dir:
                import shutil
                try:
                    shutil.rmtree(driver._user_data_dir)
                except Exception as e:
                    print(f"Failed to remove user data directory {driver._user_data_dir}: {e}")

    def scrape_url(self, url):
        """
        Скрапить URL с помощью Selenium Chrome WebDriver

        Args:
            url (str): URL для скрапинга

        Returns:
            str: HTML-контент страницы

        Raises:
            Exception: Если скрапинг не удается
        """
        driver = None
        user_data_dir = None

        try:
            user_data_dir = tempfile.mkdtemp()

            # Configure Chrome options
            options = webdriver.ChromeOptions()
            options.add_argument(f'--user-data-dir={user_data_dir}')
            options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19')
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')

            driver = webdriver.Chrome(service=Service(self.driver_path), options=options)

            driver.get(url)
            html = driver.page_source

            return html

        except Exception as e:
            raise Exception(f"Failed to scrape URL {url}: {str(e)}")
        finally:
            if driver:
                driver.quit()
            if user_data_dir:
                import shutil
                try:
                    shutil.rmtree(user_data_dir)
                except Exception as e:
                    print(f"Failed to remove user data directory {user_data_dir}: {e}")
