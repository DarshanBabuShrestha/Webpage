import json
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage", layout="wide")



st.title("""[Namaste](https://en.wikipedia.org/wiki/Namaste) :wave:""")
st.subheader("Computer Science Undergraduate Student at University At Texas Arlington")
with st.container():
    st.write("---")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Education")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)




lottie_coding = load_lottiefile("education.json")
with st.container():
        st_lottie(
            lottie_coding,
            speed=5,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            # renderer="svg",  # canvas
            height=600 ,
            width=600,
            key=None,

)



with st.container():

    left_column, right_column = st.columns(2)
    with left_column:

        st.write("""
        - **University of Texas at Arlington** - Bachelor of Science in Computer Science (Current)
        - **Dallas College** - 01/22/2024 - 05/18/2024
        - **Tarrant County College** - 08/20/2023 - 12/18/2023
        - **Morehead State University** - Bachelor of Science in Computer Science (01/16/2023 - 05/12/2023)
        - **St. Xavier's School** - School Leaving Certificate (2009-2020)
        - **Ullens IB School** - International Baccalaureate Diploma (2020-2022)
        """)
with st.container():
    st.write("---")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("INVOLVMENT")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)




lottie_INVOLVMENT = load_lottiefile("INVOLVMENT.json")
st_lottie(
    lottie_INVOLVMENT,
    speed=5,
    reverse=False,
    loop=True,
    quality="low",  # medium ; high
    #renderer="svg",  # canvas
    height=125,
    width=125,
    key=None,
)
with st.container():

    left_column, right_column = st.columns(2)
    with left_column:

        st.write("""
        - [**Google Crash Course on Python** - 08/17/2021](https://drive.google.com/file/d/1QR1WRyM-p7Exldih8K62KznIKR1cUmWE/view)
        - [**IBM Python for Data Science, AI & Development** - 09/06/2021](https://drive.google.com/file/d/1o1l0gIlbr-8F6d76jrcRBKC-ItRBLFR2/view)
        - [**UC Davis SQL for Data Science** - 08/31/2021](https://drive.google.com/file/d/1JbCzajNhkC839cR7byVrqFxaYrA-XHYc/view)
        - [**University of Michigan Python Data Structures** - 08/19/2021](https://drive.google.com/file/d/1-JgMva6hDjlRpiOR3No3yzAtEJF6mN3q/view)
        """)

with st.container():
    st.write("---")

    st.header("Projects")
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


    lottie_project= load_lottiefile("project.json")  # replace link to local lottie file
    with st.container():
        st_lottie(
            lottie_project,
            speed=5,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            # renderer="svg",  # canvas
            height=450,
            width=450,
            key=None,

        )

    st.write("""
    - [**Stock Management System**](https://github.com/DarshanBabuShrestha/Stock-Management-System) - [**Video**](https://drive.google.com/file/d/1MvrCKeazEy1PMeuMeuQDZN2QJf4RMwrm/view)
    - [**Basic 2D Game**](https://github.com/DarshanBabuShrestha/IB-Game) - [**Video**](https://drive.google.com/file/d/1ZdSNCjxbaTxWc93GqeY7zGP-zU0Ra2Oz/view)
    """)

with st.container():
    st.write("---")
    st.header("Skills")
    st.write("""
    - **Programming Languages:** Python, C, Java
    - **Soft Skills:** Team Collaboration, Time Management, Problem Solving, Communication
    - **Technical Skills:** Debugging, Database Management, Mathematics
    """)

st.write("---")
st.write("Email: [dbs6231@mavs.uta.edu](mailto:dbs6231@mavs.uta.edu) | Phone: (682)-808-1166")
st.write("[LinkedIn](https://www.linkedin.com/in/darshan-shrestha-1076b3212/) | [GitHub](https://github.com/DarshanBabuShrestha)")
st.write("&copy; 2024 Darshan Babu Shrestha")
