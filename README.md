# Vehicles-Type-Counter

# <h2> Türkçe Açıklama </h2>
---
## <h4> Proje Amacı </h4>
Bu proje, otobanlar, AVM otoparkları gibi yerlerde araç türlerini tespit edip sayarak, bu verileri bir veritabanına kaydetmeyi amaçlamaktadır. Araç trafiğinin yoğun olduğu bu bölgelerde araç türlerinin belirlenmesi, hem trafik yönetimi hem de güvenlik açısından önemli faydalar sağlar. Sistem, anlık olarak araç tespiti yaparak belirli periyotlarda raporlar oluşturur ve veritabanına kaydeder.

## <h4> Projenin Amaçladığı Faydalar </h4>

- **Trafik yönetimi ve analiz**: Yoğun trafik alanlarında araç türlerinin (otomobil, kamyon, motosiklet, vb.) sayımı yapılarak trafik akışını optimize etmek için kullanılabilir.
- **Güvenlik önlemleri**: Otoparklarda ve otobanlarda şüpheli veya istenmeyen araçların tespiti kolaylaşır.
- **Ticari faydalar**: AVM'ler ve diğer büyük tesisler, araç trafiği analizlerine dayalı olarak park yerlerini daha verimli kullanabilir.
- **Veri analizi**: Sistem, veritabanında depolanan verilerle uzun vadeli trafik analizi yapılmasına olanak tanır.

## <h4> Projenin Çalışma Mantığı </h4>
Sistem, kamera akışlarından araç türlerini tespit eder ve bu verileri bir veritabanına kaydeder. Araçların tipi, giriş ve çıkış saatleri gibi bilgiler veritabanına otomatik olarak eklenir. Araçların sınıflandırılması makine öğrenimi modelleri ile yapılmaktadır ve sistem belirli aralıklarla veritabanını günceller. 

## <h4> Kurulum Adımları </h4>

### <h5> 1. Gerekli Kütüphaneleri Yükleyin </h5>
Terminal veya komut satırında aşağıdaki komutu çalıştırarak gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

### <h5> 2. Veritabanı Bağlantısı Kurun </h5>
- `database.py` dosyasındaki veritabanı bağlantı bilgilerini kendi ortamınıza göre güncelleyin.

### <h5> 3. Model Dosyasını Edinin </h5>
- Projede kullanılan model dosyasını doğru dizine eklediğinizden emin olun.

### <h5> 4. Projeyi Çalıştırın </h5> 
Projeyi başlatmak için terminalde aşağıdaki komutu çalıştırın:
```bash
python main.py
```

---

## <h4> Kullanıcılar İçin Önemli Notlar </h4> 

1. **Veritabanı bağlantısı**: 
   - Veritabanı yapılandırmalarınızı doğru yaptığınızdan emin olun.
2. **Model dosyası**:  
   - Araç tespit ve sınıflandırma işlemlerini gerçekleştiren model dosyasının doğru yerde olduğundan emin olun.

---

# <h2> English Description </h2>
---
## <h4> Project Purpose </h4>
This project aims to detect and count vehicle types in areas such as highways and mall parking lots, and record this data in a database. Identifying vehicle types in these high-traffic areas is crucial for both traffic management and safety. The system provides real-time vehicle detection, generates periodic reports, and stores the information in a database.

## <h4> Benefits of the Project </h4>

- **Traffic management and analysis**: By counting vehicle types (car, truck, motorcycle, etc.) in high-traffic areas, it helps optimize traffic flow.
- **Security measures**: Helps detect suspicious or unwanted vehicles in parking lots and highways.
- **Commercial benefits**: Malls and other large facilities can use traffic analysis to better manage their parking spaces.
- **Data analysis**: The system allows long-term traffic analysis using the data stored in the database.

## <h4> How the System Works </h4>
The system detects vehicle types from camera feeds and records the data in a database. Information such as vehicle type, entry, and exit times are automatically added to the database. Vehicle classification is done using machine learning models, and the system periodically updates the database.

## <h4> Installation Steps </h4>

### <h5> 1. Install the Required Libraries </h5>
Run the following command in the terminal to install the necessary libraries:
```bash
pip install -r requirements.txt
```

### <h5> 2. Set Up the Database Connection </h5>
- Update the database connection settings in the `database.py` file according to your environment.

### <h5> 3. Obtain the Model File </h5>
- Ensure that the model file used in the project is added to the correct directory.

### <h5> 4. Run the Project </h5> 
Run the following command in the terminal to start the project:
```bash
python main.py
```

---

## <h4> Important Notes for Users </h4>

1. **Database connection**: 
   - Make sure to properly configure the database settings.
2. **Model file**:  
   - Ensure that the model file for vehicle detection and classification is in the correct directory.
