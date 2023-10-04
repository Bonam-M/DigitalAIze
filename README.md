# DigitalAIze
 A set of ML tools to facilitate Digital Transformation for Small Businesses from communities with limited access to Information Technology.

## Try it now!
 Open [DigitalAIze WebApp](https://digitalaize.streamlit.app) and discover all the ML tools available.

## What tools are included in DigitalAIze?

<div style="text-align: center;">
  <img
  src="testdata/digital-documents-readme-pic.jpg"
  alt="MRAW image"
  title="Optional title"
  width="360" 
  height="300"
  style="margin: 0 auto;">
</div>

The following ML tools are available on DigitalAIze :
- **Handwritten to Text** : this app leverages Google Cloud Vision API
to extract text from a picture of a handwritten document.
- **Data Visualization** : this app helps to visualize the distribution of 
numerical data from a csv or Excel file.
- **Appointment Reservation** : a prototype online form to set up appointments 
with clients and partners.
- **Digital Timesheet** : a prototype to log the working hours of employees and contractors.


## How does it work?
The solution was built using [Streamlit](https://streamlit.io/) .  
During the process [UNdata](http://data.un.org/Explorer.aspx) was used for testing.

All the tools were built only using python libraries such as:
- _PyMuPDF_ to convert PDF files into images.
- _pandas_ to save data from csv files into an appropriate dataframe.
- _seaborn_ to display data visualization such as histogram and line chart.
- _datetime_ to handle appointment days and schedules in a 24h timeframe.
- and more

## What can you find in this repo?
- The main streamlit app _DigitalAIze.py_ that contains all the tools described above.
- The _requirement.txt_ file that lists all the required packages to run the app.
- The UX theme configuration with color code in _.streamlit_ folder.
- In the _testdata_ folder: files of various formats (csv, xlsx, pdf, png) that can be used to test the app.
- And of course of dash of my creativity...

## Keep using AI for social good
And change the world one ML solution at a time.
