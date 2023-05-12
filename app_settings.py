import streamlit as st
import base64


def app_settings():

    """
    Returns:
        Dictionary: Dictionary with value of the App's title, icon, layout and style.
    """
        
    title='MovieMatch'
    icon = '🎞'
    layout = 'wide'

    hide_st_style = '''
                    <style>
                    #MainMenu {visibility: hidden;}
                    header {visibility: hidden;}
                    footer {visibility: hidden;}
                    footer:after {
                        content:'Copyright @2023: Jeshua Cespedes'; 
                        visibility: visible;
                        display: block;
                        position: relative;
                        padding: 5px;
                        top: 2px;
                        color: white;
                        }
                   
                    </style>
                    '''
    
    hyperlink_settings = '''
                        <style>
                        /* unvisited link */
                        a:link {
                            color: #ccc;
                        }
                        /* visited link */
                        a:visited {
                            color: #F6BA6F;
                        }
                        /* mouse hover link */
                        a:hover {
                            color: #00FFCA;
                        }
                        /* selected link */
                        a:active {
                            color: #800000;
                        }
                        </style>
                        '''

    return {'title':title,'icon':icon,'layout':layout,'style':hide_st_style,'hyperlink_settings':hyperlink_settings}


def add_bg_from_url():
    '''
    Adds background from an image URL

    From : My Data Talk
    https://levelup.gitconnected.com/how-to-add-a-background-image-to-your-streamlit-app-96001e0377b2
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://e1.pxfuel.com/desktop-wallpaper/675/583/desktop-wallpaper-oled-black-and-blue-gradient-i-oled-black.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Example use:    
#add_bg_from_url() 


def add_bg_from_local(image_file):
    '''
    Adds background from an image file.

    From : My Data Talk
    https://levelup.gitconnected.com/how-to-add-a-background-image-to-your-streamlit-app-96001e0377b2
    '''

    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Example use:
#add_bg_from_local('fondo-abstracto-textura.jpg') 

