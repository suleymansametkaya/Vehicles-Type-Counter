import mysql.connector as mysql
import datetime


database = mysql.connect(
  host="localhost",
  user="root", # Database kullanici adinizi giriniz
  password="YOUR_DATABASE_PASSWORD ", # Database sifrenizi giriniz
  database="YOUR_DATABASE_NAME" # Baglanilacak database adini giriniz
)

# Eger database yoksa olusturur
def databese_create():
    database_cursor = database.cursor()
    database_cursor.execute("CREATE TABLE IF NOT EXISTS vehicles_counts_log (id INT AUTO_INCREMENT PRIMARY KEY, otomobil_count INT NOT NULL, otobus_count INT NOT NULL, minibus_count INT NOT NULL, bisiklet_count INT NOT NULL, motor_count INT NOT NULL, kamyon_count INT NOT NULL, log VARCHAR(45))")
    database.commit()
    database_cursor.close()
    
# Database arac verilerini gonderir
def send_values(otomobil_count,otobus_count,minibus_count,bisiklet_count,motor_count,kamyon_count):
    database_cursor = database.cursor()
    sql = "INSERT INTO vehicles_counts_log (otomobil_count,otobus_count,minibus_count,bisiklet_count,motor_count,kamyon_count,log) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (otomobil_count,otobus_count,minibus_count,bisiklet_count,motor_count,kamyon_count,str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
    database_cursor.execute(sql, values)
    database.commit()
    database_cursor.close()
