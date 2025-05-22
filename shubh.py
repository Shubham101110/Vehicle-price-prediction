import streamlit as st
#st.set_page_config(page_title="Home Page")
st.set_page_config(
   #  page_title="Background Image Example",
    layout="wide"
)

# Adding CSS to set the background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Use the function and provide your image URL (local or online)
set_background("https://i.pinimg.com/originals/74/76/42/747642e2761d4a4dfdc1fa00925846d0.jpg")
# set_background("https://c0.wallpaperflare.com/preview/630/832/959/empty-white-concrete-pillared-parking-lot.jpg")

# Your Streamlit app content
#st.title("Welcome to My App")
# st.write("This app has a custom background image!")

from streamlit_option_menu import option_menu
import about,home,trending 

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='MACHINE LEARNING MODEL ',
                options=['Home','Trending','about'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "home":
            home.app()   
        if app == "trending":
            trending.app()        
        if app == 'about':
            about.app()    
          
             
    run()            
         
        
        

