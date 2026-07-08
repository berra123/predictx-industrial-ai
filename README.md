# 🏭 PredictX Industrial AI Platform

AI-powered Predictive Maintenance Platform for Smart Manufacturing.

PredictX is an Industry 4.0 focused predictive maintenance platform developed for paper manufacturing environments. The platform monitors machine telemetry in real time, detects anomalies, predicts potential failures and provides actionable maintenance insights to reduce downtime and improve operational efficiency.

---

## 🚀 Features

* 📡 Real-time Telemetry Monitoring
* 🤖 AI-based Failure Prediction
* 🚨 Hybrid Andon Monitoring
* 📈 Live Telemetry Charts
* 🏭 Pulper Digital Twin
* 📊 Reports & Analytics
* 🕒 Event Timeline
* 🎛️ Demo Controller
* 🧠 Scenario Engine
* 🗄️ MySQL Integration
* 🔗 GitHub Integration

---

## 🛠️ Technologies

### Backend

* Python

### Frontend

* Streamlit

### Database

* MySQL

### Visualization

* Plotly

### Data Processing

* Pandas

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
predictx
│
├── app_pages
│   ├── dashboard.py
│   ├── executive.py
│   ├── pulper.py
│   ├── alarms.py
│   ├── reports.py
│   └── settings.py
│
├── components
│   ├── executive_kpis.py
│   ├── executive_charts.py
│   ├── executive_summary.py
│   ├── executive_insights.py
│   ├── factory_overview.py
│   ├── pulper_twin.py
│   ├── ai_diagnosis.py
│   ├── maintenance_panel.py
│   ├── event_timeline.py
│   ├── live_charts.py
│   ├── demo_controller.py
│   ├── andon_panel.py
│   └── ai_prediction.py
│
├── services
│   ├── prediction_engine.py
│   ├── anomaly_detector.py
│   ├── alarm_engine.py
│   ├── ai_engine.py
│   └── event_engine.py
│
├── database
│   ├── connection.py
│   ├── read_repository.py
│   ├── prediction_repository.py
│   ├── prediction_read_repository.py
│   ├── alarm_repository.py
│   ├── alarm_read_repository.py
│   ├── event_repository.py
│   ├── event_read_repository.py
│   └── dashboard_repository.py
│
├── assets
├── data
├── data_sources
├── models
├── utils
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📋 Current Modules

| Module              | Status |
| ------------------- | ------ |
| Dashboard           | ✅ 100% |
| Executive Dashboard | ✅ 100% |
| Pulper Digital Twin | 🟡 97% |
| Reports             | 🟡 95% |
| Alarm Center        | 🟡 90% |
| Database Layer      | ✅ 100% |

Overall Project Completion: **~95%**

---

## 🗄️ Database Schema

### telemetry

Stores machine telemetry data.

| Field       |
| ----------- |
| id          |
| timestamp   |
| machine     |
| status      |
| current     |
| temperature |
| vibration   |
| torque      |
| speed       |

### predictions

Stores AI prediction results.

| Field             |
| ----------------- |
| id                |
| timestamp         |
| machine           |
| ai_risk           |
| predicted_failure |
| remaining_life    |
| confidence        |
| recommendation    |

### alarms

Stores generated alarms.

| Field       |
| ----------- |
| id          |
| timestamp   |
| machine     |
| alarm_level |
| alarm_type  |
| description |

### events

Stores operational events and historical activities.

| Field       |
| ----------- |
| id          |
| timestamp   |
| event_type  |
| title       |
| description |

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/berra123/predictx-industrial-ai.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

* OPC-UA Integration
* PLC Data Collection
* MES Integration
* SAP Integration
* Real Factory Telemetry Connection
* XGBoost Predictive Model
* Remaining Useful Life Estimation
* REST API
* Multi-Machine Support
* Cloud Deployment

---

## 🏭 Industrial Vision

PredictX aims to support the transition from reactive maintenance to predictive maintenance strategies by combining Artificial Intelligence, Digital Twin technologies and Industrial IoT concepts in a single platform.

The long-term vision is to create an intelligent industrial assistant capable of monitoring factory equipment, predicting failures and optimizing maintenance operations in real time.

---

## 👩‍💻 Developer

**Berragül Çulha**

Industrial Engineering Student

PredictX is an Industry 4.0 and Artificial Intelligence portfolio project focused on predictive maintenance solutions for manufacturing systems.
