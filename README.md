# ============================================
# CREATE README.md FILE WITH CUSTOM NAME
# Run this in Google Colab or any Python environment
# ============================================

from datetime import datetime
import os

# ============================================
# OPTION 1: Save as "README.md" (Standard name)
# ============================================

readme_content = """# 🚀 SaaS Financial Dashboard - Phase 1

## 📋 Project Overview
This dashboard tracks key financial metrics for a SaaS startup including revenue, expenses, burn rate, and unit economics (CAC, LTV).

---

## 📁 Deliverables (3 Files)

| # | File Name | Purpose |
|---|-----------|---------|
| 1 | `Financial_Master_Sheet.xlsx` | Track all revenue, expenses, running balance, and burn rate |
| 2 | `Expense_Tracker.xlsx` | Categorized expenses (AWS, Tools, Marketing, Hiring) |
| 3 | `Initial_Metrics_Sheet.xlsx` | SaaS metrics: MRR, CAC, LTV, LTV/CAC ratio |

---

## 📊 Sample Data Summary

| Metric | Value |
|--------|-------|
| **Total Revenue** | $500 |
| **Total Expenses** | $850 |
| **Net Cash Flow** | -$350 |
| **Monthly Burn Rate** | $850 |
| **Runway** | ∞ (profitable) |
| **MRR** | $500 |
| **CAC** | $200 |
| **LTV** | $1,250 |
| **LTV/CAC Ratio** | 6.25x ✅ |

---

## 🛠️ How to Use These Files

### Step 1: Download the Excel files
- All 3 `.xlsx` files are in this repository
- Open them in Microsoft Excel, Google Sheets, or LibreOffice

### Step 2: Replace sample data
- Delete the example transactions
- Enter your actual bank/stripe exports
- Keep the column headers intact

### Step 3: Let formulas auto-calculate
- Running balance updates automatically
- Expense categorization works via dropdown filters
- Metrics sheet pulls from your data

---

## 📐 Formulas Used

### Financial Master Sheet
