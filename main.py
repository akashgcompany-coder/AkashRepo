import streamlit as st
import pandas as pd

st.title("CSV Uploader and Data Explorer")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    
    preview_option = st.radio("Choose preview mode:", ("Head (first 5 rows)", "Full data"))
    if preview_option == "Head (first 5 rows)":
        st.dataframe(df.head())
    else:
        st.dataframe(df)
    
    if st.checkbox("Show summary statistics"):
        st.write(df.describe())
    
    st.write("Filter rows by column value")
    columns = df.columns.tolist()
    
    if columns:
        selected_column = st.selectbox("Select column to filter", columns)
        unique_values = df[selected_column].dropna().unique()
        selected_values = st.multiselect("Select values to keep", unique_values)
        
        if selected_values:
            filtered_df = df[df[selected_column].isin(selected_values)]
            st.write(f"Filtered Data (rows: {len(filtered_df)})")
            st.dataframe(filtered_df)
else:
    st.info("Please upload a CSV file to get started.")
