import streamlit as st

st.set_page_config(
    page_title="DigitalAIze",
    page_icon="🗃️",
)

st.write("# Welcome to 🗃️:blue[DigitalAIze]!")

st.markdown(
    """
    DigitalAIze is a set of Machine Learning solutions built with Streamlit,  
    aimed at facilitating Digital Transformation for Small Businesses   
    in communities with limited access to Information technology.
    
    """
)
    
multi = '''
**👈 Select a tool from the sidebar** to see what DigitalAIze has to offer.  
    Want to know more?   
    - Get details on how it works on [DigiTaLAIze GitHub repository](https://github.com/Bonam-M/DigitalAIze)  
    - Discover more via [Streamlit documentation](https://docs.streamlit.io/)  

    Keep using AI for good!

'''
st.markdown(multi)
