from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def start_driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Tarayıcıyı arka planda çalıştırmak isterseniz
    webdriver_service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=webdriver_service, options=chrome_options)

def main():
    driver = start_driver()

    try:
        # HTML dosyasının yolunu belirtin
        cwd = os.getcwd()
        html_file_path = f"file://{os.path.join(cwd, 'index.html')}"

        # HTML dosyasını tarayıcıda açın
        driver.get(html_file_path)

        # Formu doldur ve "Kayıt Et" düğmesine tıklayın
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name"))).send_keys(" ")
        driver.find_element(By.ID, "day").send_keys(" ")
        driver.find_element(By.ID, "month").send_keys(" ")
        driver.find_element(By.ID, "giris").send_keys(" ")
        driver.find_element(By.ID, "cikis").send_keys(" ")

        # "Kayıt Et" butonuna tıklayın
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Kayıt Et']"))).click()

        # Uyarı penceresinin açık olmasını bekle ve kapat
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Uyarı metni: {alert_text}")
            alert.accept()
            print("Uyarı kabul edildi.")
        except Exception as e:
            print(f"Uyarı bulunamadı veya kapatılamadı: {e}")

        # Sunucu yanıtını kontrol etme
        time.sleep(2)  # Sunucunun yanıt vermesi için kısa bir süre bekle

    finally:
        # Tarayıcıyı kapatmadan önce kullanıcıya tarayıcı penceresini inceleme süresi verin
        input("Tarayıcıyı kapatmak için Enter'a basın...")
        driver.quit()

if __name__ == "__main__":
    main()