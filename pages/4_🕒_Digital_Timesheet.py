import streamlit as st
import pandas as pd
from datetime import datetime

# Dummy data for employees and timesheets (replace with a database)
employees = {
    1: {"name": "Yacob Penda", "branch": "Branch C"},
    2: {"name": "John Doe", "branch": "Branch A"},
    3: {"name": "Dana Smith", "branch": "Branch B"},
    4: {"name": "Ajung Choi", "branch": "Branch C"},
    5: {"name": "Okedje Doumbe", "branch": "Branch B"},
    6: {"name": "Maud Klein", "branch": "Branch B"},
    7: {"name": "Hanh Hoang", "branch": "Branch A"},
    8: {"name": "Istas Catawanee", "branch": "Branch C"},
    9: {"name": "Tumaini Mwamba", "branch": "Branch B"},
    10: {"name": "Francisco Rodriguez", "branch": "Branch A"},

    # Add more employees and their details here
}

timesheets = []

# Streamlit UI
st.set_page_config(
    page_title="Digital Timesheet",
    page_icon="🕒",
)

st.title("🕒 Digital Timesheet")

multi = '''
**Get rid of paper timesheets** and simplify your process with **Digital Timesheet**  
A prototype solution for small businesses to easily 
keep track of the working hours of their employees and contractors. 

   
'''
st.markdown(multi)

# Employee selection on the main page
selected_employee = st.selectbox("Select Employee", [employee["name"] for employee in employees.values()])

# Get employee ID based on the selected name
employee_id = [key for key, value in employees.items() if value["name"] == selected_employee][0]

# Display the selected employee's information
st.subheader("Employee Information")
st.write(f"**Name:** {selected_employee}")
st.write(f"**Branch:** {employees[employee_id]['branch']}")

# Timesheet entry
st.header("Log Work Hours")
work_date = st.date_input("Date", datetime.now())
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
description = st.text_area("Work Description")

if st.button("Log Hours"):
    # Calculate total work hours
    start_datetime = datetime.combine(work_date, start_time)
    end_datetime = datetime.combine(work_date, end_time)
    total_hours = (end_datetime - start_datetime).total_seconds() / 3600  # Convert to hours
    
    # Add the timesheet entry to the list (in-memory storage, replace with a database)
    timesheets.append({
        "employee_id": employee_id,
        "date": work_date,
        "start_time": start_time,
        "end_time": end_time,
        "total_hours": total_hours,
        "description": description,
    })
    st.success("Hours logged successfully!")

# Display the employee's timesheet if it exists
st.header("Employee Timesheet")
timesheet_df = pd.DataFrame(timesheets)

if not timesheet_df.empty:
    filtered_timesheet = timesheet_df[timesheet_df["employee_id"] == employee_id]
    st.dataframe(filtered_timesheet)

    # Total hours worked by the employee
    total_worked_hours = filtered_timesheet["total_hours"].sum()
    st.write(f"Total Hours Worked: {total_worked_hours:.2f} hours")
else:
    st.warning("No timesheet entries found for this employee.")
