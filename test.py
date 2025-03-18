import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_page_load(driver, timeout=30):
    """Ожидание полной загрузки страницы"""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get("https://nexign.com/ru")
        wait_for_page_load(driver)

        try:
            products_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Продукты и решения']")))
            products_button.click()
            wait_for_page_load(driver)
        except Exception as e:
            print(f"Ошибка перехода в раздел: {str(e)}")
            driver.quit()
            return

        try:
            it_tools_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Инструменты для ИТ-команд')]"))
            )
            it_tools_button.click()
            wait_for_page_load(driver)

        except Exception as e:
            print(f"Ошибка перехода в подменю: {str(e)}")
            driver.quit()
            return

        try:
            nexign_nord_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Nexign Nord')]"))
            )
            nexign_nord_button.click()
            wait_for_page_load(driver)
            time.sleep(2)

        except Exception as e:
            print(f"Ошибка перехода в Nexign Nord: {str(e)}")
            driver.quit()
            return

        # Проверка успешного перехода
        print("Успешно перешли в раздел Nexign Nord")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
