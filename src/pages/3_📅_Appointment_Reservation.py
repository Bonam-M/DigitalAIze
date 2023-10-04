import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Dummy data for offices and appointments (replace with a database)
offices = {
    111: {"name": "Office JP", "location": "Johannesburg - Parkhurst"},
    222: {"name": "Office HCMC", "location": "Ho Chi Minh City - District 1"},
    333: {"name": "Office SJBE", "location": "San Jose - Barrio Escalante"},
    444: {"name": "Office MCDN", "location": "Montreal - Cote des Neiges"},
    # Add more offices and their details here
}

appointments = []

# Streamlit UI
st.set_page_config(
    page_title="Appointment Reservation",
    page_icon="📅",
)

st.title("📅 Appointment Reservation")

multi = '''
Manage your appointments with clients and partners easily    
with this prototype solution for small businesses. 

   
'''
st.markdown(multi)
# Office selection on the main page
selected_office = st.selectbox("Select Office", [office["name"] for office in offices.values()])

# Get office ID based on the selected name
office_id = [key for key, value in offices.items() if value["name"] == selected_office][0]

# Display the selected office's information
st.subheader("Office Information")
st.write(f"**Name:** {selected_office}")
st.write(f"**Location:** {offices[office_id]['location']}")

# Appointment reservation
st.header("Make an Appointment")

# Date selection
selected_date = st.date_input("Select a date", datetime.now())

# List of available time slots (example)
available_time_slots = ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"]

# Dropdown for selecting a time slot
selected_time = st.selectbox("Select a time", available_time_slots)

# User information
name = st.text_input("Your Name")
email = st.text_input("Your Email")
phone = st.text_input("Your Phone Number")

if st.button("Reserve Appointment"):
    # Validate user input
    if name and email and phone:
        # Check if the selected time slot is available (dummy check)
        is_available = True  # Replace with real availability check
        
        if is_available:
            # Format the selected date and time
            formatted_date = selected_date.strftime("%Y-%m-%d")
            
            # Add the appointment to the list (in-memory storage, replace with a database)
            appointments.append({
                "office_id": office_id,
                "date": formatted_date,
                "time": selected_time,
                "name": name,
                "email": email,
                "phone": phone,
            })
            st.success("Appointment reserved successfully!")
        else:
            st.error("Selected time slot is not available.")
    else:
        st.error("Please fill in all the required fields.")

# Display upcoming appointments for the selected office
st.header("Upcoming Appointments")

upcoming_appointments = []
for appointment in appointments:
    if appointment["office_id"] == office_id:
        upcoming_appointments.append(appointment)

if upcoming_appointments:
    upcoming_appointments_df = pd.DataFrame(upcoming_appointments)
    st.dataframe(upcoming_appointments_df)
else:
    st.warning("No upcoming appointments for this office.")

