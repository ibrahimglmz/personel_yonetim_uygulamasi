personnel management application



---------[TR]---------
# Proje Rehberi

Bu proje, belirli bir Excel dosyasındaki verileri okuyarak bir CSV dosyasına yazma işlemini otomatikleştiren ve form verilerini web tarayıcısı ile işleyen bir uygulama içerir.

## Gereksinimler

Projenizi çalıştırmadan önce gerekli Python kütüphanelerini yüklemeniz gerekmektedir. Aşağıdaki komutları kullanarak gerekli kütüphaneleri yükleyebilirsiniz:

`
pip install openpyxl
pip install pandas
pip install selenium
pip install webdriver-manager




Dosya Yapısı

app.py
Bu dosya, Excel dosyasını okuyarak gerekli kişi adlarını CSV dosyasına yazma işlemini gerçekleştirir.

Yapmanız gerekenler:

1- person.csv adında bir Excel dosyası açın ve gerekli kişi adlarını "persons" adındaki kolona yazın.
2- csv_file_path değişkenine persons.csv dosyasının path adresini yazın.
3- "departmanlar" kısmını kişiselleştirin (örneğin: ML, Web, Siber Güvenlik, Bekçi, Güvenlik, Temizlik Personeli vb.).
selenium_client.py
Bu dosya, belirtilen HTML dosyasına erişir ve form verilerini web tarayıcısında işler.

Yapmanız gerekenler:

4- "html_file_path" değişkenine HTML dosyasının path adresini belirtin.
5- iOS cihaz kullanıyorsanız, localhost yerine Host 5001 adresini kullanın (5000 portu AirDrop ile çakışmaktadır).


calıştırma :
python3 app.py
python3 selenium_client.py



---------[EN]---------

# Project Guide

This project includes an application that automates the process of reading data from a specific Excel file and writing it to a CSV file, and handles form data through a web browser.

## Requirements

Before running the project, you need to install the required Python libraries. You can install the necessary libraries using the following commands:

```bash
pip install openpyxl
pip install pandas
pip install selenium
pip install webdriver-manager


File Structure

app.py
This file performs the task of reading the Excel file and writing the necessary names to the CSV file.

What you need to do:

Open an Excel file named person.csv and write the required names in the column named "persons".
Set the csv_file_path variable to the path of the persons.csv file.
Customize the "departments" section (e.g., ML, Web, Cybersecurity, Guard, Security, Cleaning Staff, etc.).
selenium_client.py
This file accesses the specified HTML file and processes form data in the web browser.

What you need to do:

Set the html_file_path variable to the path of the HTML file.
If you are using an iOS device, use the address Host 5001 instead of localhost (port 5000 conflicts with AirDrop).


Running the Project:
python3 app.py
python3 selenium_client.py




[TR ]Bu `README.md` dosyası, projenizin temel yapı taşlarını ve kullanım talimatlarını açıklayacaktır. Herhangi bir ek bilgi veya düzeltme isterseniz, lütfen belirtin!

[EN] This `README.md` file is the explicit program of the basic building blocks of your project and its operating instructions. If you would like any additional information or corrections, please let me know!

