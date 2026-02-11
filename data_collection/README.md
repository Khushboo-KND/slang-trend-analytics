# Data Collection

## Overview

This folder contains scripts and logic used to extract Google Trends data using Python.

Data extraction is handled via the `pytrends` library, which provides programmatic access to Google Trends interest-over-time data.

---

## 📌 Data Source

- Platform: Google Trends  
- Access Method: Python (`pytrends`)  
- Data Type: Interest over time  
- Granularity: Weekly  

---

## 🎯 Phase 1 Scope

- **Word:** Karen  
- **Country:** United States (US)  
- **Search Type:** Web Search  
- **Time Range:** 2015–2025  

The goal in Phase 1 is to build a clean and reliable extraction process for a single word and geography before expanding the pipeline.

---

## 🚀 Future Expansion

- Multi-country tracking  
- Multi-source extraction (Web, YouTube, News)  
- Automated weekly ingestion  
- Parameterized scripts for multiple slang words  
- Integration with scheduled cloud workflows  

---

## 📂 Expected Outputs

- Raw CSV export files  
- Structured data ready for BigQuery ingestion  
- Logs for extraction timestamp (`pulled_at`) tracking  
