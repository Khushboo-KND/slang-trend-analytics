# Slang Trend Diffusion Analytics

## 📌 Project Objective

This project analyzes how internet slang evolves over time using Google Trends data and builds a scalable data pipeline to track cultural virality.

The project begins with a single slang term ("Karen") and gradually expands into multi-country, multi-source diffusion modeling to understand how language spreads across geographies and platforms.

---

## 🎯 Phase 1 (MVP Scope)

- **Word:** Karen  
- **Country:** United States  
- **Source:** Web Search  
- **Time Range:** 2015–2025  
- **Granularity:** Weekly  

---

## 🛠 Tech Stack

- Python (pytrends)
- BigQuery
- Advanced SQL (window functions, moving averages)
- Looker Studio
- GitHub (version control)
- Cloud Scheduler (future phase)
- PySpark (future phase)

---

## 🏗 Architecture Overview

Google Trends

↓

Python Extraction (pytrends)

↓

BigQuery - Raw Layer (Bronze)

↓

SQL Transformations (Silver & Gold Layers)

↓

Analytics Table

↓

Dashboard (Looker Studio)

---

## 📊 Planned Analytical Features

- Interest-over-time tracking  
- 4-week moving average smoothing  
- Peak detection logic  
- Event-based spike annotation  
- Cross-country diffusion modeling (future phase)  
- Multi-source comparison (Web, News, YouTube)  

---

## 🚀 Future Enhancements

- Automated weekly data ingestion  
- Viral score calculation  
- Time-to-peak analysis  
- Diffusion classification modeling  
- Blog documentation of findings and insights  

---

## 📈 Long-Term Vision

Build a cultural analytics framework that quantifies how slang words spread, peak, decline, and diffuse across countries and media sources using scalable data engineering and analytical modeling.

