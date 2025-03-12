import streamlit as st
import pandas as pd
import pymysql
import json


st.title("📊 Retail Order Analysis")

with open("queries.json", "r", encoding="utf-8") as f:
    queries = json.load(f)

tab1, tab2 = st.tabs(["📁 Set 1 (Q1–Q10)", "📂 Set 2 (Q11–Q20)"])

query_labels_set1 = [
    "1. Top 10 Highest Revenue Generating Products",
    "2. Top 5 Cities with Highest Profit Margins",
    "3. Total Discount Given for Each Category",
    "4. Average Sale Price per Product Category",
    "5. Region with Highest Average Sale Price",
    "6. Total Profit per Category",
    "7. Top 3 Segments with Highest Order Quantity",
    "8. Average Discount Percentage per Region",
    "9. Product Category with Highest Total Profit",
    "10. Total Revenue Generated Per Year"
]

query_labels_set2 = [
    "11. Monthly Sales Analysis",
    "12. Best-Performing Regions by Revenue",
    "13. Revenue % Contribution by Category",
    "14. Top Customer Segments by Revenue",
    "15. Profit Margin per Product Category",
    "16. Region with Highest Total Profit",
    "17. Product Performance Overview",
    "18. Impact of >20% Discount on Sales",
    "19. Top-Selling Products by Revenue",
    "20. Products with Highest Order Volume & Revenue"
]

with tab1:
    selected_label1 = st.selectbox("📋 Select a Query (Set 1)", query_labels_set1)
    query_index1 = query_labels_set1.index(selected_label1)
    selected_query1 = queries[query_index1]
    st.code(selected_query1, language="sql")

    if st.button("▶️ Run Query (Set 1)"):
        try:
            connection = pymysql.connect(
                host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
                user="2X5KUwsdnLEwrHQ.root",
                password="TjI9l52hFr0QUFmp",
                database="RetailAnalysis",
                ssl_verify_cert=True,
                ssl_verify_identity=True,
                ssl_ca=r"C:\Users\welcome\Downloads\isrgrootx1 (5).pem",
                cursorclass=pymysql.cursors.DictCursor
            )
            cursor = connection.cursor()
            cursor.execute(selected_query1)
            data = cursor.fetchall()
            df = pd.DataFrame(data)
            st.success("✅ Query executed successfully!")
            st.dataframe(df)
            cursor.close()
            connection.close()
        except Exception as e:
            st.error(f"❌ SQL Execution Error: {e}")

# --- Set 2 Tab ---
with tab2:
    selected_label2 = st.selectbox("📋 Select a Query (Set 2)", query_labels_set2)
    query_index2 = query_labels_set2.index(selected_label2) + 10 
    selected_query2 = queries[query_index2]
    st.code(selected_query2, language="sql")

    if st.button("▶️ Run Query (Set 2)"):
        try:
            connection = pymysql.connect(
                host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
                user="2X5KUwsdnLEwrHQ.root",
                password="TjI9l52hFr0QUFmp",
                database="RetailAnalysis",
                ssl_verify_cert=True,
                ssl_verify_identity=True,
                ssl_ca=r"C:\Users\welcome\Downloads\isrgrootx1 (5).pem",
                cursorclass=pymysql.cursors.DictCursor
            )
            cursor = connection.cursor()
            cursor.execute(selected_query2)
            data = cursor.fetchall()
            df = pd.DataFrame(data)
            st.success("✅ Query executed successfully!")
            st.dataframe(df)
            cursor.close()
            connection.close()
        except Exception as e:
            st.error(f"❌ SQL Execution Error: {e}")
