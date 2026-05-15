import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="SaaS Financial Dashboard", page_icon="📊", layout="wide")

st.title("🚀 SaaS Financial Dashboard - Phase 1")
st.markdown("---")

@st.cache_data
def load_sample_data():
    dates = pd.date_range(start='2026-05-01', periods=30, freq='D')

    amounts = []
    types = []
    categories = []

    # Revenue transactions
    for i in range(10):
        amounts.append(np.random.choice([49, 99, 199, 49, 99]))
        types.append('Revenue')
        categories.append('SaaS Revenue')

    # AWS expenses
    for i in range(5):
        amounts.append(-np.random.choice([35, 45, 55, 40]))
        types.append('Expense')
        categories.append('AWS')

    # Tools expenses
    for i in range(4):
        amounts.append(-np.random.choice([29, 35, 50, 20]))
        types.append('Expense')
        categories.append('Tools')

    # Marketing expenses
    for i in range(6):
        amounts.append(-np.random.choice([100, 150, 200, 75, 50]))
        types.append('Expense')
        categories.append('Marketing')

    # Hiring expenses
    for i in range(5):
        amounts.append(-np.random.choice([300, 400, 500, 200]))
        types.append('Expense')
        categories.append('Hiring')

    transactions = pd.DataFrame({
        'Date': dates[:len(amounts)],
        'Type': types,
        'Category': categories,
        'Amount': amounts
    })

    customers = pd.DataFrame({
        'Customer Name': [f'Customer {i}' for i in range(1, 16)],
        'Monthly Price': np.random.choice([49, 99, 199, 49, 99], 15),
        'Start Date': pd.date_range(start='2026-04-01', periods=15, freq='D')
    })

    return transactions, customers

transactions, customers = load_sample_data()

revenue = transactions[transactions['Type'] == 'Revenue']['Amount'].sum()
expenses = abs(transactions[transactions['Type'] == 'Expense']['Amount'].sum())
mrr = customers['Monthly Price'].sum()
avg_mrr = customers['Monthly Price'].mean()
total_customers = len(customers)

marketing_spend = expenses * 0.3
new_customers = max(1, int(total_customers * 0.2))
cac = marketing_spend / new_customers

monthly_churn = 0.02
customer_lifespan = 1 / monthly_churn
ltv = avg_mrr * customer_lifespan
ltv_cac_ratio = ltv / cac

last_30_days = datetime.now() - timedelta(days=30)
recent_expenses = abs(transactions[(transactions['Type'] == 'Expense') & (transactions['Date'] >= last_30_days)]['Amount'].sum())
recent_revenue = transactions[(transactions['Type'] == 'Revenue') & (transactions['Date'] >= last_30_days)]['Amount'].sum()
monthly_burn = recent_expenses - recent_revenue
cash_balance = 25000
runway = cash_balance / monthly_burn if monthly_burn > 0 else float('inf')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📈 MRR", f"${mrr:,.0f}")
with col2:
    st.metric("💰 CAC", f"${cac:,.0f}")
with col3:
    st.metric("💎 LTV", f"${ltv:,.0f}")
with col4:
    st.metric("🎯 LTV/CAC", f"{ltv_cac_ratio:.1f}x")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Expense Breakdown")
    expense_by_cat = transactions[transactions['Type'] == 'Expense'].groupby('Category')['Amount'].sum().abs()
    if len(expense_by_cat) > 0:
        fig = px.pie(values=expense_by_cat.values, names=expense_by_cat.index, title="Expenses by Category")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💵 Revenue vs Expenses")
    daily = transactions.groupby(['Date', 'Type'])['Amount'].sum().unstack().fillna(0)
    if 'Revenue' in daily.columns and 'Expense' in daily.columns:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=daily.index, y=daily['Revenue'], name='Revenue', line=dict(color='green', width=2)))
        fig.add_trace(go.Scatter(x=daily.index, y=-daily['Expense'], name='Expenses', line=dict(color='red', width=2)))
        fig.update_layout(height=400, title="Daily Revenue vs Expenses", xaxis_title="Date", yaxis_title="Amount ($)")
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("📊 Key Metrics Summary")
metrics_df = pd.DataFrame({
    'Metric': ['Total Revenue', 'Total Expenses', 'Net Cash Flow', 'Monthly Burn', 'Runway', 'MRR', 'CAC', 'LTV', 'LTV/CAC Ratio', 'Total Customers', 'Avg MRR/Customer'],
    'Value': [f"${revenue:,.0f}", f"${expenses:,.0f}", f"${revenue - expenses:,.0f}", f"${monthly_burn:,.0f}", f"{runway:.0f} months" if runway != float('inf') else "∞", f"${mrr:,.0f}", f"${cac:,.0f}", f"${ltv:,.0f}", f"{ltv_cac_cac_ratio:.1f}x", total_customers, f"${avg_mrr:,.0f}"]
})
st.dataframe(metrics_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.subheader("💡 Health Check")

if ltv_cac_ratio >= 3:
    st.success(f"✅ LTV/CAC Ratio: {ltv_cac_ratio:.1f}x (Healthy - Above 3x)")
else:
    st.warning(f"⚠️ LTV/CAC Ratio: {ltv_cac_ratio:.1f}x (Needs Improvement - Target > 3x)")

if monthly_burn < 10000:
    st.success(f"✅ Monthly Burn: ${monthly_burn:,.0f} (Under control)")
else:
    st.warning(f"⚠️ Monthly Burn: ${monthly_burn:,.0f} (High - Review expenses)")

if runway > 12:
    st.success(f"✅ Runway: {runway:.0f} months (Healthy)")
elif runway > 6:
    st.warning(f"⚠️ Runway: {runway:.0f} months (Monitor closely)")
else:
    st.error(f"🚨 Runway: {runway:.0f} months (Critical - Need fundraising)")

st.markdown("---")
st.success("✅ Phase 1 Complete! Dashboard is live.")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
