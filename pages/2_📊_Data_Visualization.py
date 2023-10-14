import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow as pa
import pyarrow.parquet as pq

# Streamlit UI
st.set_page_config(
    page_title="Data Visualization",
    page_icon="📊",
)
st.title("📊 Data Visualization")

st.markdown(
    """
    Use this Machine Learning solution to visualize the distribution of numerical data  
    from a csv, xls or xslx file.    
    """
)
multi = '''
**👇 Follow the instructions below** to visualize the distribution of your data.  
    Download and use these files from UNdata for a quick demo  
    - This file for [Multidimensional Poverty Index](http://data.un.org/DocumentData.aspx?id=488)  
    - The [Ratio of school attendance of orphans to school attendance of non-orphans](http://data.un.org/Data.aspx?d=SOWC&f=inID%3a35)  
    - Statistics for [Percentage of individuals using the Internet](http://data.un.org/Data.aspx?d=ITU&f=ind1Code%3aI99H)  
    Or use your own files and try it out!  
      

'''
st.markdown(multi)

# Upload a file (Excel or CSV)
uploaded_file = st.file_uploader("Upload a file", type=["xls", "xlsx", "csv"])

if uploaded_file is not None:
    try:
        file_extension = uploaded_file.name.split(".")[-1].lower()

        # Read the uploaded file into a DataFrame based on the file extension
        if file_extension in ["xls", "xlsx"]:
            df = pd.read_excel(uploaded_file)
        elif file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        
        # Check if the DataFrame is empty
        if df.empty:
            st.error("Error: The DataFrame is empty. Please check your file and try again.")
        else:
             # Display the first ten rows of the DataFrame
            st.subheader("First Ten Rows of the DataFrame")
            st.write(df.head(10))

        # Allow the user to select two columns for visualization
        selected_column1 = st.selectbox("Select the First Column", df.columns)
        selected_column2 = st.selectbox("Select the Second Column", df.columns)

        # Convert all columns to float, handling non-convertible data as 'NaN'
        df = df.apply(pd.to_numeric, errors='coerce')

        # Create a histogram for the first selected column
        fig1, ax1 = plt.subplots()
        sns.histplot(data=df, x=selected_column1, kde=True, ax=ax1)
        ax1.set_xlabel(selected_column1)
        ax1.set_ylabel("Frequency")
        st.subheader(f"Histogram for {selected_column1}")
        st.pyplot(fig1)

        # Create a line chart for the second selected column
        fig2, ax2 = plt.subplots()
        sns.lineplot(data=df, x=df.index, y=selected_column2, ax=ax2)
        ax2.set_xlabel("Index")
        ax2.set_ylabel(selected_column2)
        st.subheader(f"Line Chart for {selected_column2}")
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error: {str(e)}")




