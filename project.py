import json
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Digipodium", page_icon="lottiefiles/logoo.png", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Use Local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("lottiefiles/style.css")

# --- LOAD ASSETS ----\
lottie_coding = load_lottiefile("lottiefiles/coding.json")
lottie_evn = load_lottieurl("https://lottie.host/635196dc-3b37-4a9a-80b7-c1246c3d1735/J6oMSQgbEQ.json")
lottie_luffy = load_lottieurl("https://lottie.host/ddd6464b-7230-4d35-bc05-abe347d9ab18/Bb7GMsli7k.json")
lottie_kakashi = load_lottieurl("https://lottie.host/3d94fe1b-5ae8-4a73-ab1e-5885a974065d/l2Ng30Pty6.json")
lottie_trading = load_lottieurl("https://lottie.host/d56318dc-2f6d-4590-aec0-f3e0a5c938cb/pdOoMWKqGI.json")
img_dsa = Image.open("lottiefiles/dsa.jpg")
img_webapp = Image.open("lottiefiles/streamlitweb1.jpg")
img_logo = Image.open("lottiefiles/logoo.png")



#----- HEADER SECTION
with st.container():
    l,r = st.columns((1,14))
    with l:
        st.write("##")
        st.write("##")

        st.image(img_logo)
    with r:
        st.write("#")
        st.title("DIGIPODIUM")
with st.container():
    #st.image(img_logo)
    #st.title("DIGIPODIUM")
    st.write("---")
    st.subheader("What we are")
    st.write("Through specialities in a variety of topics, the platform Digipodium reaches out to its audiences to help them enrich their life.We are here to guarantee the best services in the most structured and methodical way possible. We take pleasure in having a highly motivated and assured crew that is committed to delivering and rises to challenges by keeping up with the most recent technological advancements.")
    st.write("[Learn More >](https://digipodium.com/about.php)")

# ---- WHAT I DO -----
with st.container():
    st.write("---")
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.title("Areas of Expertise")
        st.write("##")
        st.subheader("IT Training & Education")
        st.write("""IT Training Wing offers specialized training programs aligned with International Certification of Global Giants such as Oracle, Microsoft, Google, IBM, and others. Data Analytics, Java, Advanced Java, Python, Django, Android, Kotlin, IoT, Machine Learning, Advanced Machine Learning, Big Data, PHP, Advanced PHP, Angular,.NET, Cloud, and other training programs are provided. We recommend customized training programs for students that meet industry standards. This helps our young students keep on top of developing trends that are in tune with the numerous and ever-expanding job prospects.""")
        st.write("""**Our Key Resource Persons have proven track records in their respective fields of expertise. its vast knowledge base is backed up by international certifications, demonstrating its legitimacy and credibility.**""")
        
        st.write("## ")
        st.subheader("Digital Marketing")
        st.write("""
             - **Digital Marketing Training**
             - **Digital Marketing Solution**
                 """)
        st.write("Digital Marketing Training has programs from Associate Level to Master Level. All programs are mapped with Google and Hubspot Certifications. Training Programs are available on latest content of Digital Marketing Master Training Program, Online Advertising Using GOOGLE ADS, Search Engine Optimization (SEO), Web Analytics Using GOOGLE Analytics, Social Media Marketing (SMM), Content Marketing etc. Customized programs are available for students and professionals as per their requirement. Our Digital Marketing Solution team is here to provide solutions to corporates, small businesses, startups etc., related to online promotion and optimization techniques. **Our key resource person is a Google and Hubspot Certified Digital Marketing Professional.**")
        
        st.write('##')
        st.subheader('Event Management')
        st.write("""The Event Management coordinators provide a single roof solution to all your requirements and ensure a memorable and successful event finish. The events such as Conference, Inaugural functions, Seminar, Product Launch, College Festival, Felicitation ceremony Wedding, Live in Concerts, Birthday parties, Inter college events etc. **The key resource person has a 15 years experience** and has been leading a firm which has more than 50 years history in this field. She takes pride in handling events in a most creative and innovative style, so that each event has an identity and a memory exclusive. We thrive because we provide event management & planning , creating and building your dream event, theme development, concept based decors, sustainable services, dedicated staff and more.""")
    
    with right_col:
       
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st_lottie(lottie_coding, height=220, key="coding")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st_lottie(lottie_trading, height=190, key="trading")
        st.write("##")
        st.write("##")
        st.write("##")
        st_lottie(lottie_evn, height=180, key="evn")
       
# --- YOUTUBE ----
with st.container():
    st.write("---")
    st.header("Our Youtube Channel")
    st.markdown("[Visit...](https://www.youtube.com/@digipodium1604)")
    st.write("##")
    img_col,text_col = st.columns((1,2))
    with img_col:
        #insert img
        st.image(img_dsa)
        
    with text_col:
        st.subheader("Importance of Data structures and Algorithms")
        st.write(
            """ 
            DSA stands for Data Structures and Algorithms. They are important to learn because they help you to:
          -  Solve real-world problems efficiently and effectively
          -  Crack the interviews of top product-based companies
          -  Improve your programming skills and logic

           

            """
        )
        st.markdown("[Watch Video...](https://youtu.be/bpG1xtN_kq4)")

with st.container():
    
    st.write("##")
    img_col,text_col = st.columns((1,2))
    with img_col:
        st.image(img_webapp)
        
    with text_col:
        st.subheader("SQLalchemy + Python Tutorial (using Streamlit)")
        st.write(
            """ 
            If you want to create a streamlit project that connects to a database, you can use the st.experimental_connection function to access various data sources securely and easily. You can also use Streamlit’s secrets management to store your database credentials and other sensitive information.

           **You can also use other Python libraries to interact with databases, such as SQLAlchemy, pandas, or duckdb.**

            """
        )
        st.write("[Watch Video...](https://youtu.be/lIHGGcnCmFA)")
        

        # --- CONTACT ----
with st.container():
    st.write("---")       
    st.header("Get In Touch With US!")
    st.write("##")

            # Documentation: https://formsubmit.co/ !! change email !!
    contact_form = """
     <form action="https://formsubmit.co/strawHatsdigipodium@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
            """
    
    left_col,right_col = st.columns(2)
    with left_col:
            st.write(contact_form, unsafe_allow_html=True)
    with right_col:
            st_lottie(lottie_kakashi, height=200)
                


