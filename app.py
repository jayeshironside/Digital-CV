from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jaykumar"
PAGE_ICON = "📋"
NAME = "Jay Kumar"
DESCRIPTION = """
A passionate Data Analyst working as a Business Analyst.
"""
EMAIL = "jaykumar25012001@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jaykumar-m-41a0b31ab/",
    "GitHub": "https://github.com/jayeshironside",
}
PROJECTS = {
    "Langchain Apps - Created chatbots & useful applications.": "https://github.com/jayeshironside/Langchain_Projects.git",
    "Spotify Wrapped - Spotify streaming history analysis.": "https://github.com/jayeshironside/Spotify-Streaming-history-analysis.git",
    "Gmail - Analyse inbox and sent mails trend.": "https://github.com/jayeshironside/Gmail_Analysis.git",
    "Youtube Wrapped - Youtube watch history analysis.": "https://github.com/jayeshironside/Youtube-Wrapped.git",
    "Whatsapp - Whatsapp chat history analysis.": "https://github.com/jayeshironside/Whatsapp-chat-analysis.git",
}
CERTIFICATES = {
    "Python Programming": "https://drive.google.com/file/d/13iXqXMHjFDJt9FaoJhjTFmMGldJkPO0e/view?usp=sharing",
    "Introduction to Pandas": "https://drive.google.com/file/d/1H1Fb7GuSNwzqUTZb7-y9FpzQ4it_mY1n/view?usp=sharing",
    "Data Visualization": "https://drive.google.com/file/d/1ztF65bSdTBwvAZ-_n4lcNtcbe6a49Saq/view?usp=sharing",
    "Machine Learning with Python": "https://drive.google.com/file/d/1HytPWp4hhgORterAiwuCLI0eLr8dAHaV/view?usp=sharing",
    "Business analysis basics": "https://drive.google.com/file/d/1VG0t5PjPQAbECDIMCNPRfOYZSSCRMr36/view?usp=drivesdk",
    "Introduction to Business analysis": "https://drive.google.com/file/d/1VDNyGN1u2WlQ26vn8gjoGosvSNcn76QY/view?usp=drivesdk",
    "Master Lancgain": "https://www.udemy.com/certificate/UC-e4519b6f-d279-44b5-9353-9ae178b21fe4/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)
    

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA), gap="small")
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    col_list = f"<div class='center-align'><a href='{link}'>🔗 {platform}</a></div>"
    cols[index].markdown(col_list, unsafe_allow_html=True)

# --- About me ---
st.write('\n')
st.subheader("About me")
st.write(
    """
- ✔️ Expereinced in extracting actionable insights from data.
- ✔️ Strong hands on experience and knowledge in Python and Excel.
- ✔️ Good understanding of ML & LL models and its related frameworks.
- ✔️ Expert in understanding the client's requirements and delivering the projects.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Langhchain), SQL.
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Matplotlib, Seaborn.
- 📚 Modeling: Large language models, Logistic & linear regression, decition tree.
- 💻 Designing: HTML, CSS, Bootstrap, Streamlit.
- 🗄️ Databases: MongoDB, MySQL.
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Business Analyst | Naapbooks Limited**")
st.write("01/2023 - Present")
st.write(
    """
- ► Communicating and documenting project requirements.
- ► Mapping processes and developing use cases.
- ► Managing projects and ensuring quality through testing.
- ► Utilizing data analysis to identify trends and patterns for informed decision-making.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Sr. Client service executive | Aqkode healthcare Solutions Pvt. Ltd.**")
st.write("09/2021 - 01/2023")
st.write(
    """
- ► Senior Client Service Executive in the US healthcare industry.
- ► Managed account receivables and handled rejection, denial, and payment issues.
- ► Conducted eligibility verification audits and improved revenue cycle management.
- ► Maintained timely, accurate, and satisfactory client communication.
- ► Utilized strong analytical skills for complex problem-solving and patient eligibility verification.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**AR Executive | CrystalVoxx global LLP**")
st.write("12/2020 - 09/2021")
st.write(
    """
- ► Managed account receivables, rejections, and denial management.
- ► Utilized strong analytical and problem-solving skills.
- ► Identified and resolved complex payment issues.
- ► Improved revenue cycle management.
"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
certificates_list = list(CERTIFICATES.items())
cols = st.columns(2)
for index, (certificate, link) in enumerate(certificates_list):
    with cols[index % 2]:
        st.write(f"🥇 [{certificate}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"🎯 [{project}]({link})")
