import pandas as pd
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS'u etkinleştir

EXCEL_FILE_PATH = '/Users/ibrahim/Desktop/My Work/ofis_otomasyon/form_data.xlsx' # bilgilerin kayıt edildiği excel
CSV_FILE_PATH = '/Users/ibrahim/Desktop/My Work/ofis_otomasyon/persons.csv'  # kişi önerisi alınacak excel bilgisi


@app.route('/kaydet', methods=['POST'])
def kaydet():
    try:
        # JSON verisini al
        data = request.get_json()
        print("Veri alındı:", data)  # Debug için eklenen satır

        # Verileri al
        name = data.get('name')
        giris = data.get('giris')
        cikis = data.get('cikis')
        departman = data.get('departman')
        durum = data.get('durum')

        # Eksik veri kontrolü
        if not all([name, giris, cikis, departman]):
            error_msg = 'Eksik veri'
            print(error_msg)  # Hata mesajını yazdır
            return jsonify({'success': False, 'error': error_msg}), 400

        # Form verisini Excel dosyasına kaydet
        save_form_data(name, giris, cikis, departman, durum)

        # Kişi adını CSV dosyasına kaydet
        save_person_name(name)

        return jsonify({'success': True})
    except Exception as e:
        print("Hata mesajı:", str(e))  # Hata mesajını yazdır
        return jsonify({'success': False, 'error': f'Hata: {str(e)}'}), 500


def save_form_data(name, giris, cikis, departman, durum):
    new_data = {
        'name': name,
        'giris': giris,
        'cikis': cikis,
        'departman': departman,
        'durum': durum
    }

    new_df = pd.DataFrame([new_data])

    try:
        if os.path.exists(EXCEL_FILE_PATH):
            with pd.ExcelFile(EXCEL_FILE_PATH) as xls:
                df = pd.read_excel(xls, sheet_name='Sheet1')
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_excel(EXCEL_FILE_PATH, index=False, sheet_name='Sheet1')
        else:
            new_df.to_excel(EXCEL_FILE_PATH, index=False, sheet_name='Sheet1')
    except Exception as e:
        print("Excel kaydetme hatası:", str(e))  # Excel kaydetme hatasını yazdır
        raise  # Hata oluşursa tekrar yakala


def save_person_name(name):
    new_df = pd.DataFrame({'name': [name]})

    try:
        if os.path.exists(CSV_FILE_PATH):
            df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8-sig')
            if name not in df['name'].values:
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_csv(CSV_FILE_PATH, index=False, encoding='utf-8-sig')
        else:
            new_df.to_csv(CSV_FILE_PATH, index=False, encoding='utf-8-sig')
    except Exception as e:
        print("CSV kaydetme hatası:", str(e))  # CSV kaydetme hatasını yazdır
        raise  # Hata oluşursa tekrar yakala


@app.route('/kisiler', methods=['GET'])
def kisiler():
    if os.path.exists(CSV_FILE_PATH):
        df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8-sig')
        names = df['name'].unique().tolist()
        return jsonify(names)
    else:
        return jsonify([])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

    #Macbbok kullanıları port numarasını 5001 ve üstü yapsın
