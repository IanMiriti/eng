🔗 Canlı Demo Linki   
https://baihvh6z3srni6cmuruicv.streamlit.app/   
   
GITHUB REPOSITORY LINK - https://github.com/IanMiriti/eng   
 Additional DEMO future Website : https://property-art.lovable.app/   
  
  
    
AI SPARK HACKATHON – YATIRIM DANIŞMANI PROJESİ   
Takım: Engineers   
Tema: Yapay Zekâ Modelleri   
    
1.	Problem Yorumlama (10 Puan)   
Bizden istenen problem neydi?   
Hackathon kapsamında bizden, İstanbul konut piyasasına yönelik veri odaklı bir Yatırım Danışmanı sistemi geliştirmemiz istendi. Amaç yalnızca konut fiyatı tahmin etmek değil, adil piyasa değerini (Fair Value) hesaplayarak bunu ilan fiyatı ile karşılaştırmak ve kullanıcıya yatırım kararı sunmaktı.   
Problemi nasıl yorumladık?   
Problemi şu şekilde tanımladık:   
“Sabit gelirli ve kredi kullanabilen alıcıların, 2020 İstanbul konut piyasasında bir ilanın fırsat mı, normal mi yoksa pahalı mı olduğunu anlayabilmesini sağlayan karar destek sistemi geliştirmek.”   
Uyum sağladığımız temel kısıtlar   
•	Sadece 2020 verisi kullanıldı   
•	Available for Loan = Yes filtresi zorunlu olarak uygulandı   
•	Gelecek yıllara (2025 vb.) yönelik fiyat tahmini yapılmadı   
  Ham bir regresyon problemi, gerçek hayata uygun bir  
  
2.	Veri Analizi – EDA (15 Puan)   
EDA’nın amacı   
•	Fiyat dağılımını anlamak   
•	Aykırı değerleri incelemek   
•	Metrekare (m²) etkisinin baskınlığını görmek   
•	Konum, oda sayısı ve bina yaşının fiyat üzerindeki etkisini analiz etmek Elde edilen önemli içgörüler   
•	Konut fiyatları sağa çarpık (right-skewed) bir dağılım göstermektedir   
•	Ham veride m², fiyatı aşırı derecede domine etmektedir   
•	Konum ve yapı özellikleri, toplam fiyattan çok metrekare başına değer üzerinden etkilidir   
Görselleştirme   
•	Krediye uygun konutlar filtrelendikten sonra fiyat dağılımı görselleştirildi   
•	Modelin yanlış kitleyi öğrenmesi engellendi   
  Sonuç:  EDA, doğrudan feature engineering stratejimizi şekillendirdi.   
  
3.	Veri Ön İşleme (15 Puan)   
Temizleme işlemleri   
•	Fiyat alanlarından TL , nokta ve virgüller kaldırıldı   
•	Sayısal alanlar numerik tipe dönüştürüldü   
•	Kritik kolonlarda (Price, Gross m², Net m²) eksik veriler çıkarıldı   
Zorunlu filtreleme   
•	Sadece krediye uygun (Available for Loan = Yes) konutlar kullanıldı   
Özellik seçimi (Feature Selection)   
•	Gürültü yaratan kolonlar çıkarıldı:   
•	Neighborhood (aşırı detaylı)   
•	İlan tarihleri (2020 modeli için anlamsız)   
Özellik Mühendisliği (Yenilikçi Yaklaşım)   
Tespit edilen problem   
•	Model yalnızca m²’ye odaklanıyor, konum ve kaliteyi yeterince öğrenemiyordu   
Geliştirdiğimiz çözüm   
•	Target Encoding uygulandı   
•	İlçe, oda sayısı ve bina yaşı için:   
•	Ortalama fiyat   
•	Metrekare başına ortalama fiyat (PPGSM)   
Bu sayede model: - Bölgesel değerleri - Yapı kalitesini - Piyasa verimliliğini öğrenebildi   
    
4.	Model / Yöntem Seçimi (15 Puan)   
Seçilen model: XGBoost Regressor Neden   
XGBoost?   
•	Tabular verilerde yüksek başarı   
•	Doğrusal olmayan ilişkileri öğrenebilme   
•	Çok sayıda özelliği etkin kullanabilme   
•	Overfitting’e karşı dayanıklılık   
Değerlendirilen alternatifler   
•	Linear Regression  yetersiz   
•	Random Forest  tuning maliyeti yüksek   
Model yapılandırması   
•	500 ağaç   
•	Kontrollü derinlik   
•	Düşük öğrenme oranı   
    
5.	Model Performansı (20 Puan)   
Değerlendirme stratejisi   
•	%80 eğitim – %20 test ayrımı   
•	Kullanılan metrikler:   
•	R² Skoru   
•	RMSE (TL cinsinden hata)   
Metriklerin önemi   
•	R²  Piyasa dinamiklerinin ne kadar iyi öğrenildiğini gösterir   
•	RMSE  Gerçek parasal hata miktarını ifade eder   
Yorumlama   
•	Yüksek R², güçlü öğrenme anlamına gelir   
•	RMSE, ortalama konut fiyatına oranlanarak yorumlandı   
Overfitting farkındalığı   
•	Gizli test setine erişim yok   
•	Hard-coded tahmin yok   
  
6.	Yenilikçilik (10 Puan)   
Projemizi yenilikçi yapan noktalar   
1.	Metrekare Verimliliği Yaklaşımı   
2.	Tahmin değil karar üretme   
3.	%10 toleranslı piyasa mantığı   
 
4.	Yatırımcı dostu çıktı tasarımı   
  Sonuç:  Klasik fiyat tahmininin ötesine geçildi.   
  
7.	Uygulanabilirlik (10 Puan)   
Gerçek hayata uygunluk   
•	Sabit gelirli alıcılar için tasarlandı   
•	Kullanımı basit   
•	Uzmanlık gerektirmez   
Kullanım senaryoları   
•	Ev alıcıları   
•	Yatırımcılar   
•	Emlak danışmanları   
Ölçeklenebilirlik   
•	Yeni verilerle yeniden eğitilebilir   
 
•	Diğer şehirler için uyarlanabilir   
  Sonuç:  Gerçek dünyada kullanılabilir bir çözüm.   
  
8.	Sunum & Anlatım (5 Puan)   
Arayüz   
•	Streamlit tabanlı sade tasarım   
•	Tek tıkla analiz   
Çıktılar   
•	İlan fiyatı   
•	Adil değer   
•	Normal fiyat aralığı   
•	Yatırım tavsiyesi   
Demo hazır   
•	Canlı link   
•	Kurulum gerektirmez   
    
9.	Deployment & Sürekli Erişim (Referans)   
Kullanılan platform Streamlit  Community Cloud Neden  
önemli?   
•	Colab geçicidir   
•	Yarışma canlı demo ister   
Deployment adımları   
1.	Tüm dosyalar Colab’dan alındı   
2.	GitHub reposuna yüklendi   
3.	Streamlit Cloud’a bağlandı   
4.	Otomatik kurulum ve yayın   
Sonuç   
•	7/24 erişilebilir   
•	Kalıcı URL   
    
10.	Genel Değerlendirme   
Bu proje: - Problemi doğru tanımlar - Güçlü veri bilimi yöntemleri kullanır - Yenilikçi bir bakış açısı sunar - Gerçek hayatta çalışır bir ürün ortaya koyar   
Bu bir model değil, bir Yatırım Danışmanıdır.   
    
Teşekkürler 🙏   
ADDITIONALLY  
  
🤖 Talk to AI Investment Advisor  
Buyers can click the “Talk to AI Investment Advisor” button at the bottom of the  DEMO website to instantly access our AI model. The AI analyzes property details and compares the listing price with real market data to advise whether the home is an investment opportunity, fairly priced, or overpriced, helping buyers make confident, data-driven decisions before purchasing.  
🔗  Website: https://property-art.lovable.app  
🔗 AI Advisor: https://baihvh6z3srni6cmuruicv.streamlit.app/  
  
  






# 🏡 AI-Powered Real Estate Investment Advisor

**AI Spark Hackathon 2025**
**Team: Engineers**

🔗 **Live Application:**
[https://baihvh6z3srni6cmuruicv.streamlit.app/](https://baihvh6z3srni6cmuruicv.streamlit.app/)

🔗 **GitHub Repository:**
[https://github.com/IanMiriti/eng](https://github.com/IanMiriti/eng)

---

## 📌 Project Overview

This project is an **AI-powered Investment Advisor** designed to help users determine whether a house listing in **Istanbul (2020 market)** represents a:

* ✅ **Good Investment Opportunity**
* ⚖️ **Fair / Normal Deal**
* ❌ **Overpriced Property**

Instead of only predicting house prices, the system calculates a **Fair Market Value** and compares it with the **listing price**, providing a **clear investment recommendation**.

This approach directly follows the **AI Spark Hackathon problem statement**.

---

## 🎯 Problem Statement

The Istanbul real estate market shows **high price inconsistency**, making it difficult for fixed-income buyers to decide whether a house is worth its price.

### Our Goal:

To build a **data-driven decision support system** that:

1. Learns 2020 housing market dynamics
2. Predicts a fair property value
3. Classifies listings as **Opportunity / Normal / Expensive**

---

## 📊 Dataset

* **File:** `hackathon_train_set.csv`
* **Year:** 2020
* **Key Constraint Applied:**
  Only properties with
  **`Available for Loan = Yes`**
  were used, as required by the competition rules.

---

## 🧹 Data Preprocessing

### Cleaning

* Removed currency symbols (`TL`), dots, and commas
* Converted price and area fields to numeric values
* Removed rows with missing critical values

### Feature Selection

* Dropped noisy or redundant columns (e.g., neighborhood, advertisement dates)

---

## 🧠 Feature Engineering (Key Innovation)

### Problem Identified

Raw models tend to **over-rely on square meters (m²)** and fail to capture **location quality and market efficiency**.

### Our Solution

We introduced **Target Encoding + Price-per-Area Ratios**:

For key categorical features:

* **District**
* **Number of Rooms**
* **Building Age**

We created:

* Average price per group
* Average **price per gross square meter (PPGSM)**

This allowed the model to learn:

* Neighborhood value
* Structural quality
* Market efficiency

---

## 🤖 Model Selection

### Chosen Model: **XGBoost Regressor**

**Why XGBoost?**

* Excellent performance on tabular data
* Captures non-linear relationships
* Robust against overfitting
* Handles high-dimensional encoded features well

### Evaluation Metrics

* **R² Score**
* **RMSE (Root Mean Squared Error)**

These metrics were selected to ensure both **technical accuracy** and **real-world interpretability**.

---

## 📈 Decision Logic (Business Layer)

Prediction alone is not enough.

We apply a **±10% tolerance margin** around the predicted fair value:

| Condition                        | Classification |
| -------------------------------- | -------------- |
| Listing Price < Fair Value − 10% | 🌟 Opportunity |
| Listing Price within ±10%        | ⚖️ Normal      |
| Listing Price > Fair Value + 10% | 💸 Expensive   |

This reflects **real-world negotiation margins** used in property investment.

---

## 🌐 Web Application (Streamlit)

The system is deployed as an interactive **Streamlit web app** where users can:

* Enter property features
* Input the listing price
* Instantly receive an investment recommendation

### Key Features

* Clean and simple UI
* Real-time predictions
* Clear, investor-friendly output
* No technical knowledge required

---

## 🚀 Deployment (Permanent Access)

The application is **permanently deployed** using **Streamlit Community Cloud**.

### Deployment Steps

1. Exported trained model and app files from Google Colab
2. Uploaded all files to a public GitHub repository
3. Connected the repository to Streamlit Cloud
4. Automatic build using `requirements.txt`
5. App launched with a permanent public URL

✅ No local machine required
✅ 24/7 availability
✅ Fully demo-ready for hackathon evaluation

---

## 📁 Project Structure

```
eng/
├── app.py                      # Streamlit application
├── house_price_model.joblib    # Trained XGBoost model
├── feature_columns.joblib      # Feature blueprint
├── requirements.txt            # Dependencies
├── notebooks/                  # Training notebooks
└── PRESENTATION_REPORT.txt     # Hackathon presentation report
```

---

## 🏆 Hackathon Evaluation Alignment

| Criterion              | Covered |
| ---------------------- | ------- |
| Problem Interpretation | ✅       |
| Data Analysis (EDA)    | ✅       |
| Data Preprocessing     | ✅       |
| Model Selection        | ✅       |
| Model Performance      | ✅       |
| Innovation             | ✅       |
| Applicability          | ✅       |
| Presentation           | ✅       |

---

## 👥 Team

**Team Name:** Engineers

This project was developed as part of the **AI Spark Hackathon**, following all competition rules and constraints.

---

## 📌 Final Note

This is **not just a machine learning model**.
It is a **real-world investment advisor** built with:

* Strong data science principles
* Clear business logic
* Practical usability
* Transparent and reproducible code
