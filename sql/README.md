# SQL Transformations

## Overview

This folder contains SQL scripts used to transform raw Google Trends data within BigQuery.

The transformation process follows a layered data architecture approach to ensure scalability, clarity, and analytical reliability.

---

## 🏗 Data Layers

### 🥉 Bronze Layer (Raw)

- Direct ingestion from CSV export  
- No transformations applied  
- Stores original fields as received from Google Trends  
- Acts as a source of truth  

---

### 🥈 Silver Layer (Cleaned & Structured)

- Standardized date formats  
- Extracted time dimensions (year, month, week)  
- Removed null or invalid records  
- Ensured consistent schema for downstream processing  

This layer prepares data for analytical modeling.

---

### 🥇 Gold Layer (Analytics-Ready)

- 4-week moving average calculation  
- Peak detection flags  
- Year-over-year comparison  
- Viral growth metrics  
- Derived analytical indicators  

This layer powers dashboards and advanced analysis.

---

## 📊 Key SQL Concepts Used

- Window functions  
- Partitioning and ordering  
- Rolling averages  
- Date extraction functions  
- Conditional logic for spike detection  

---

## 🚀 Future Enhancements

- Cross-country comparative modeling  
- Diffusion lag analysis  
- Multi-source aggregation logic  
- Automated materialized views  
