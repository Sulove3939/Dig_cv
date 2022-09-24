
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sulav Adhikari"
PAGE_ICON = ":wave:"
NAME = "Sulav Adhikari"
DESCRIPTION = """
A highly detail-oriented and self-motivated Finance professional. Abilty to perform exceptional data analysis and
quantitative taks with the help of tools such as Excel, VBA, PowerBi and Python to enhance productivity and assist enterprises by supporting data-driven decision-making.

"""
EMAIL = "Sulove3939@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCxdAZkNP77ATNoRMGJd5I6A",
    "LinkedIn": "https://www.linkedin.com/in/sulav-adhikari-12ab2790/",
    "GitHub": "https://github.com/Sulove3939",
    "Twitter": "",
}
PROJECTS = {
    "🏆 NDIS Service Booking Tool (Service Agreement Printer) - Complete solution of the NDIS service booking using Excel and VBA - Exports Agreement on PDF and DOCX format": "https://www.youtube.com/watch?v=jPwgX-RMmfE&t=7s",
    "🏆 Desktop Application - To keep the record of the terminated employees": "https://www.youtube.com/watch?v=e-BKERT34A4",
    "🏆 Revenue and Payroll Dashboard - Excel Pivot Tables and charts comparing Revenue and payroll": "https://www.youtube.com/channel/UCxdAZkNP77ATNoRMGJd5I6A",
    "🏆 Income and Expense Report - PowerBI Visulization of the databases": "https://www.youtube.com/channel/UCxdAZkNP77ATNoRMGJd5I6A",


}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=280)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    # --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 years of experince in NDIS claiming, NDIS fund management and Payroll
- ✔️ Strong hands on experience and knowledge in Excel, VBA and PowerBI
- ✔️ Great understanding of Accounting standards and softwares
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (streamlit, Pandas), MS Excel, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Tableau
- 📚 Accounting: Xero, Microsoft Dynamics, Myob
- 🗄️ Payroll: Xero, CloudPayroll
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Finance Manager | Prospect-Hill**")
st.write("05/2021 - Present")
st.write(
    """
- ► Supervision of the finance team
- ► Process payroll and report payroll taxes for the organization
- ► Tax Reporting
- ►	Claiming Wages subsidies
- ►	Complete financial reports, lead the month-end closing process and conduct monthly financial forecast.
- ►	Respond to financial enquiries, gathering and interpreting data
- ►	Conduct internal audits such as wage reviews and NDIS Billing
- ►	Reconciliations & Liaise with NDIS, CoS & participant families when required.
- ►	Manage and train staff when necessary
- ►	Provide secretarial support requiring the exercise of sound judgment, initiative, confidentiality, and sensitivity in the performance of work.
- ►	Preparation of ROC (Roster of Care) and NDIS point of contact.

"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Accounts Receivable | Aruma**")
st.write("04/2020 - 05/2021")
st.write(
    """
- ► Manual claims onto the NDIA myplace Portal.
- ► Key point of looking after daily banking transactions.
- ►	Checking service booking of the participants if enough funds available.
- ► Posting daily payment allocation processes.
- ► Debt collection.
- ► Processing refunds and maintaining journal entries in appropriate accounts

"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Accounts Assistant | Proacc Australia**")
st.write("03/2019 - 12/2019")
st.write(
    """
- ► Preparation of BAS and Tax return documents
- ►	Preparation of bank reconciliation statements
- ►	Looking after administration and handling queries of all the clients.
- ►	Data import processes between software.
- ►	Posting daily payment allocation processes.

"""
)
# --- JOB 4
st.write("#")
st.write("🚧", "**Education Counseller | 3Bees Education and Migration**")
st.write("06/2018 - 12/2018")
st.write(
    """
- ►	Coordinating new partnerships with agents.
- ►	Student enrolment recruitment.
- ►	Coordinating translation and interpreting services.
- ►	Monitoring student performance and providing feedback for improvement.
- ►	Reviewing and recommending improvements to instructional material.

"""
)
# --- JOB 6
st.write("#")
st.write("🚧", "**Sales Assistant | Vintage Cellars**")
st.write("01/2018 - 12/2019")
st.write(
    """
- ►	Helping customers choose between the company's array of goods and services, process payments and maintain a high level of customer service.
- ►	Answering a high volume of queries over the phone and via email.
- ►	Filling, scanning, drafting documents, mailing, minute taking etc.
- ►	Data entry into the internal databases.
- ►	Ad-hoc duties.


"""
)
# --- JOB 7
st.write("#")
st.write("🚧", "**Bartender | The Roosevelt**")
st.write("10/2016 - 12/2017")
st.write(
    """
- ►	Bartending
- ►	Built customer confidence by actively listening to their preference and giving appropriate recommendation.
- ►	Inventory management on the weekly basis
- ►	Processing deliveries and organizing the cellar stock level.
- ►	Balanced the needs of multiple customers simultaneously in a fast-paced environment.
- ►	Reconciliation of registers



"""
)
# --- Education ---
st.write("#")
st.subheader("Education")
st.write("---")

# --- Education 1
#st.write("#")
st.write("📗", "**CPA | CPA**")
st.write("06/2021 - Current")

#st.write("#")
st.write("📘", "**Master of Porfessional Accounting | Holmes Institute**")
st.write("2016 - 2019")

#st.write("#")
st.write("‍📙", "**Bachelor of Business administration | Tribhuwan University**")
st.write("2012 - 2016")

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sulav Adhikari"
PAGE_ICON = ":wave:"
NAME = "Sulav Adhikari"
DESCRIPTION = """
A highly detail-oriented and self-motivated Finance professional. Abilty to perform exceptional data analysis and
quantitative taks with the help of tools such as Excel, VBA, PowerBi and Python to enhance productivity and assist enterprises by supporting data-driven decision-making.

"""
EMAIL = "Sulove3939@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCxdAZkNP77ATNoRMGJd5I6A",
    "LinkedIn": "https://www.linkedin.com/in/sulav-adhikari-12ab2790/",
    "GitHub": "https://github.com/Sulove3939",
    "Twitter": "",
}
PROJECTS = {
    "🏆 NDIS Service Booking (Service Agreement Printer) - Complete solution of the NDIS service booking using Excel and VBA - Exports Agreement on PDF and DOCX format": "https://www.youtube.com/watch?v=jPwgX-RMmfE&t=7s",
    "🏆 Desktop Application - To keep the record of the terminated employees": "https://www.youtube.com/watch?v=e-BKERT34A4",
    "🏆 Revenue and Payroll Dashboard - Excel Pivot Tables and charts comparing Revenue and payroll": "https://www.youtube.com/channel/UCxdAZkNP77ATNoRMGJd5I6A",
    "🏆 Income and Expense Report - PowerBI Visulization of the databases": "https://www.youtube.com/channel/UCxdAZkNP77ATNoRMGJd5I6A",


}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=280)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    # --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 years of experince in NDIS claiming, NDIS fund management and Payroll
- ✔️ Strong hands on experience and knowledge in Excel, VBA and PowerBI
- ✔️ Great understanding of Accounting standards and softwares
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (streamlit, Pandas), MS Excel, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Tableau
- 📚 Accounting: Xero, Microsoft Dynamics, Myob
- 🗄️ Payroll: Xero, CloudPayroll
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Finance Manager | Prospect-Hill**")
st.write("05/2021 - Present")
st.write(
    """
- ► Supervision of the finance team
- ► Process payroll and report payroll taxes for the organization
- ► Tax Reporting
- ►	Claiming Wages subsidies
- ►	Complete financial reports, lead the month-end closing process and conduct monthly financial forecast.
- ►	Respond to financial enquiries, gathering and interpreting data
- ►	Conduct internal audits such as wage reviews and NDIS Billing
- ►	Reconciliations & Liaise with NDIS, CoS & participant families when required.
- ►	Manage and train staff when necessary
- ►	Provide secretarial support requiring the exercise of sound judgment, initiative, confidentiality, and sensitivity in the performance of work.
- ►	Preparation of ROC (Roster of Care) and NDIS point of contact.

"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Accounts Receivable | Aruma**")
st.write("04/2020 - 05/2021")
st.write(
    """
- ► Manual claims onto the NDIA myplace Portal.
- ► Key point of looking after daily banking transactions.
- ►	Checking service booking of the participants if enough funds available.
- ► Posting daily payment allocation processes.
- ► Debt collection.
- ► Processing refunds and maintaining journal entries in appropriate accounts

"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Accounts Assistant | Proacc Australia**")
st.write("03/2019 - 12/2019")
st.write(
    """
- ► Preparation of BAS and Tax return documents
- ►	Preparation of bank reconciliation statements
- ►	Looking after administration and handling queries of all the clients.
- ►	Data import processes between software.
- ►	Posting daily payment allocation processes.

"""
)
# --- JOB 4
st.write("#")
st.write("🚧", "**Education Counseller | 3Bees Education and Migration**")
st.write("06/2018 - 12/2018")
st.write(
    """
- ►	Coordinating new partnerships with agents.
- ►	Student enrolment recruitment.
- ►	Coordinating translation and interpreting services.
- ►	Monitoring student performance and providing feedback for improvement.
- ►	Reviewing and recommending improvements to instructional material.

"""
)
# --- JOB 6
st.write("#")
st.write("🚧", "**Sales Assistant | Vintage Cellars**")
st.write("01/2018 - 12/2019")
st.write(
    """
- ►	Helping customers choose between the company's array of goods and services, process payments and maintain a high level of customer service.
- ►	Answering a high volume of queries over the phone and via email.
- ►	Filling, scanning, drafting documents, mailing, minute taking etc.
- ►	Data entry into the internal databases.
- ►	Ad-hoc duties.


"""
)
# --- JOB 7
st.write("#")
st.write("🚧", "**Bartender | The Roosevelt**")
st.write("10/2016 - 12/2017")
st.write(
    """
- ►	Bartending
- ►	Built customer confidence by actively listening to their preference and giving appropriate recommendation.
- ►	Inventory management on the weekly basis
- ►	Processing deliveries and organizing the cellar stock level.
- ►	Balanced the needs of multiple customers simultaneously in a fast-paced environment.
- ►	Reconciliation of registers



"""
)
# --- Education ---
st.write("#")
st.subheader("Education")
st.write("---")

# --- Education 1
#st.write("#")
st.write("📗", "**CPA | CPA**")
st.write("06/2021 - Current")

#st.write("#")
st.write("📘", "**Master of Porfessional Accounting | Holmes Institute**")
st.write("2016 - 2019")

#st.write("#")
st.write("‍📙", "**Bachelor of Business administration | Tribhuwan University**")
st.write("2012 - 2016")

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
>>>>>>> 96ab8e2a2234b8004d5768ed0b9da0951d4b5788
