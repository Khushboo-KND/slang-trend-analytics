# System Architecture

## 🧱 Phase 1 Architecture (Manual Pipeline)

The initial phase follows a controlled manual pipeline to validate data extraction, transformation logic, and dashboard integration before introducing automation.

### Workflow Steps

1. Extract data from Google Trends using Python (`pytrends`)
2. Save raw data locally as CSV
3. Upload raw dataset to BigQuery (Bronze Layer)
4. Transform data using SQL (Silver & Gold Layers)
5. Connect Looker Studio to analytics-ready tables
6. Build dashboard for visualization

This phase prioritizes correctness, clarity, and validation before scaling.

---

## 🚀 Planned Scalable Architecture (Future Phase)

Once the manual pipeline is validated, the system will transition to a fully automated architecture.

Cloud Scheduler (Trigger)

↓

Python Extraction Script

↓

BigQuery Raw Table (Bronze)

↓

SQL Transformations (Silver & Gold)

↓

Analytics Table

↓

Auto-Refreshing Dashboard


This enables continuous weekly ingestion and automated reporting.

---

## 🔄 Logical Data Flow

Google Trends

↓

Python (pytrends)

↓

Raw BigQuery Table

↓

SQL Transformations

↓

Analytics Table

↓

Looker Dashboard


---

## 🎯 Architectural Principles

- Layered data modeling (Bronze → Silver → Gold)
- Clear separation of extraction and transformation logic
- Scalability from manual validation to automated pipeline
- Analytics-ready outputs for visualization and insight generation
- Modular design to support multi-word and multi-country expansion
