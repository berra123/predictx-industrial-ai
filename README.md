# 🏭 PredictX Industrial AI Platform

**[TR]** Akıllı üretim tesisleri için geliştirilmiş yapay zeka destekli kestirimci bakım platformu.  
**[EN]** AI-powered predictive maintenance platform developed for smart manufacturing environments.

---

## 🇹🇷 Türkçe

### 📌 Proje Özeti
PredictX, gerçek zamanlı makine telemetri verilerini analiz ederek makine öğrenmesi ve anomali tespit algoritmaları sayesinde arızaları gerçekleşmeden önce tahmin eden yapay zeka destekli bir kestirimci bakım platformudur.  
Platform; plansız duruş sürelerini azaltmayı, bakım maliyetlerini optimize etmeyi ve ekipman güvenilirliğini artırmayı hedeflemektedir.

### 🚀 Öne Çıkan Özellikler

#### 🤖 Yapay Zeka Destekli Arıza Tahmini
- Makine Sağlık Skoru hesaplama
- Arıza risk tahmini
- Kalan Faydalı Ömür (RUL) öngörüsü
- Yapay zeka destekli bakım önerileri

#### 🚨 Akıllı Alarm Merkezi
- Gerçek zamanlı anomali tespiti
- Kural tabanlı ve makine öğrenmesi destekli alarm sistemi
- Çok seviyeli alarm yapısı (Düşük, Orta, Kritik)
- Alarm geçmişi ve olay takibi

#### 📧 Bildirim Sistemi
- Otomatik e-posta bildirimleri
- Alarm önceliğine göre dinamik yönlendirme
- Kritik olaylarda bakım ekiplerinin bilgilendirilmesi

#### 🛠 SAP PM İş Emri Simülasyonu
- Kritik alarmlarda otomatik iş emri oluşturma
- Öncelik bazlı ekip ataması
- ERP bakım süreçlerinin simülasyonu

#### 📊 Raporlama ve Analitik
- Geçmiş alarm analizi
- KPI ve bakım performans göstergeleri
- Operasyonel verimlilik takibi

### 🛠 Teknoloji Yığını

| Katman | Teknolojiler |
| :--- | :--- |
| **Backend & Arayüz** | Python, Streamlit |
| **Veritabanı** | PostgreSQL, Supabase, Psycopg2 |
| **Yapay Zeka** | Scikit-Learn, Predictive Analytics |
| **Bulut ve DevOps** | GitHub, Streamlit Community Cloud, Supabase |

---

## 🇬🇧 English

### 📌 Project Summary
PredictX is an AI-powered predictive maintenance platform that analyzes real-time machine telemetry data and predicts failures before they occur using machine learning and anomaly detection algorithms.  
The platform aims to reduce unplanned downtime, optimize maintenance operations, and improve equipment reliability.

### 🚀 Key Features

#### 🤖 AI Failure Prediction
- Machine Health Score calculation
- Failure risk estimation
- Remaining Useful Life (RUL) prediction
- AI-driven maintenance recommendations

#### 🚨 Intelligent Alarm Center
- Real-time anomaly detection
- Rule-based and ML-driven alert system
- Multi-level alarm structure (Low, Medium, Critical)
- Alarm history and event tracking

#### 📧 Notification System
- Automated email notifications
- Dynamic severity-based routing
- Maintenance team escalation workflows

#### 🛠 SAP PM Work Order Simulation
- Automatic work order generation
- Priority-based maintenance assignment
- ERP maintenance workflow simulation

#### 📊 Reporting & Analytics
- Historical alarm analysis
- Maintenance KPI monitoring
- Operational performance tracking

### 🛠 Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend & UI** | Python, Streamlit |
| **Database** | PostgreSQL, Supabase, Psycopg2 |
| **AI & Analytics**| Scikit-Learn, Predictive Analytics |
| **Cloud & DevOps**| GitHub, Streamlit Community Cloud, Supabase |

---

## 📐 Architecture & Workflow / Mimari ve İş Akışı

```mermaid
graph TD
    A[Telemetry Data / Telemetri Verisi] --> B[AI Engine / YZ Motoru]
    B --> C[Anomaly Detection / Anomali Motoru]
    C --> D[Intelligent Alarms / Akıllı Alarmlar]
    D --> E[Automated Notifications / Bildirimler]
    D --> F[SAP PM Work Order Simulation / İş Emri]
    F --> G[Event Timeline / Olay Zaman Çizelgesi]
    E --> G
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
    style G fill:#bfb,stroke:#333,stroke-width:2px