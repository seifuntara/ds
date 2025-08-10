import streamlit as st

# Page Title
st.set_page_config(page_title="CV")

# Header
htp = "https://github.com/seifuntara/ds/blob/master/newfolder/profile.jpg"
st.image(htp)
st.title("Untara, Muhammad Seif Robbani")
st.write("📍 Jakarta, Indonesia | 📧 seif30100@gmail.com | 📱 +62 81234361773 | 💼 [LinkedIn](https://linkedin.com/in/seifuntara)")
st.markdown("---")

# Summary
st.subheader("Summary")
st.write("Business Analyst/Technology Consultant with hands-on experience in analytics, data management and system process optimisation. Teamwork oriented, able to learn and adapt quickly in new environment.")

# Skills
st.subheader("Skills")
st.write("Data Management | Business Process Flow | Stakeholder Management | SQL | Python | Tableau | Power BI")

# Experience
st.subheader("Experience")
st.markdown("**Business Analyst | Traveloka, Jakarta** (Jan 2024 – May 2025)")
st.write(
    """
    - Designed and optimised business process flows for internal invoicing system integration
    - Collaborated with multiple stakeholders to gather requirements and identify automation opportunities
    - Performed internal testing, handled data issues in system processeds and led sprint planning 
    """
)
st.markdown("**Technology Consultant | Ernst & Young, Jakarta** (Aug 2022 – Dec 2023)")
st.write(
    """
    - Conducted IT Strategic Planning (ITSP) for Data Architecture of a multi finance company
    - Conducted Digital Maturity Assessment (DMA) and IT compliance review of a private Bank  
    - Conducted IT Due Diligence of a multi finance company to identify risks and ensure smooth IT integration post-acquisition
    """
)
st.markdown("**Data Management Analyst Intern | Pertamina Hulu Mahakam, Balikpapan** (Jan 2020 – Feb 2020)")
st.write(
    """
    - Developed a free alternative to a paid daily performance report using SSRS
    - Improved Power BI dashboards design to enable monthly and yearly Drilling KPI monitoring 
    """
)

# Education
st.subheader("Education")
st.write(
    """
    - **MSc Business Analytics, Nanyang Technological University**, Singapore (2025/08-Present)
    - **BSc Artificial Intelligence and Computer Science, University of Birmingham**, UK (2020/08-2022/06)
    - **BSc in Computer Science, Universitas Gadjah Mada**, Indonesia (2018/08-2022/06)
    """
)





