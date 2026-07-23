import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon=" ",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open("employee_model.pkl", "rb"))

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp{
background:#0f172a;
}

.block-container{
padding-top:1rem;
padding-bottom:1rem;
max-width:1300px;
}

/* Header */

.title{
font-size:42px;
font-weight:bold;
color:white;
}

.subtitle{
font-size:18px;
color:#cbd5e1;
margin-top:-10px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:#111827;
}

.sidebar-card{
background:#1e293b;
padding:18px;
border-radius:12px;
color:white;
margin-bottom:15px;
text-align:center;
}

.sidebar-card h2{
color:#60a5fa;
}

/* KPI Cards */

.metric-card{
background:linear-gradient(135deg,#2563eb,#1d4ed8);
padding:20px;
border-radius:15px;
color:white;
text-align:center;
box-shadow:0px 5px 15px rgba(0,0,0,.4);
}

.metric-title{
font-size:17px;
}

.metric-value{
font-size:34px;
font-weight:bold;
}

/* Form Card */

.form-card{
background:#1e293b;
padding:20px;
border-radius:15px;
box-shadow:0px 5px 10px rgba(0,0,0,.3);
}

/* Predict Button */

div.stButton > button{
width:100%;
background:#2563eb;
color:white;
border-radius:12px;
height:55px;
font-size:22px;
font-weight:bold;
border:none;
}

div.stButton > button:hover{
background:#1d4ed8;
}

/* Result Card */

.success{
background:#14532d;
padding:25px;
border-radius:15px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;
}

.danger{
background:#7f1d1d;
padding:25px;
border-radius:15px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=130
    )

    st.markdown("##HR Analytics")

    st.markdown("""
<div class="sidebar-card">
<h2>Employee Attrition</h2>

Predict whether an employee is likely to leave the company using Machine Learning.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="sidebar-card">
 Dataset<br><br>
5000 Employees
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="sidebar-card">
 Best Model<br><br>
Random Forest
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="sidebar-card">
  Developed Using

Python

Scikit-Learn

Streamlit
</div>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
"""
<div class="title">
  Employee Attrition Prediction Dashboard
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="subtitle">
Predict whether an employee is likely to leave the company using Machine Learning.
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- KPI CARDS ---------------- #

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""
<div class="metric-card">
<div class="metric-title">
  Accuracy
</div>

<div class="metric-value">
96.2%
</div>
</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="metric-card">
<div class="metric-title">
  Best Model
</div>

<div class="metric-value">
Random Forest
</div>
</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="metric-card">
<div class="metric-title">
  Dataset
</div>

<div class="metric-value">
5000+
</div>
</div>
""", unsafe_allow_html=True)

with c4:

    st.markdown("""
<div class="metric-card">
<div class="metric-title">
  Target
</div>

<div class="metric-value">
Attrition
</div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("---")
# =====================================================
# EMPLOYEE INFORMATION
# =====================================================

st.markdown("##Employee Information")

left, right = st.columns(2)

# ---------------- LEFT COLUMN ---------------- #

with left:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    years_at_company = st.number_input(
        "Years at Company",
        0,50,5
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Education",
            "Finance",
            "Healthcare",
            "Media",
            "Technology"
        ]
    )

    monthly_income = st.number_input(
        "Monthly Income",
        1000,
        100000,
        30000
    )

    work_life_balance = st.selectbox(
        "Work Life Balance",
        [
            "Poor",
            "Fair",
            "Good",
            "Excellent"
        ]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    performance_rating = st.selectbox(
        "Performance Rating",
        [
            "Below Average",
            "Average",
            "High",
            "Low"
        ]
    )

    number_of_promotions = st.number_input(
        "Number of Promotions",
        0,10,0
    )

    overtime = st.selectbox(
        "Overtime",
        [
            "Yes",
            "No"
        ]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        1,100,10
    )

# ---------------- RIGHT COLUMN ---------------- #

with right:

    education_level = st.selectbox(
        "Education",
        [
            "High School",
            "Associate Degree",
            "Bachelor's Degree",
            "Master's Degree",
            "PhD"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

    number_of_dependents = st.number_input(
        "Dependents",
        0,10,1
    )

    job_level = st.selectbox(
        "Job Level",
        [
            "Entry",
            "Mid",
            "Senior"
        ]
    )

    company_size = st.selectbox(
        "Company Size",
        [
            "Small",
            "Medium",
            "Large"
        ]
    )

    company_tenure = st.number_input(
        "Company Tenure (Months)",
        1,500,24
    )

    remote_work = st.selectbox(
        "Remote Work",
        [
            "Yes",
            "No"
        ]
    )

    leadership = st.selectbox(
        "Leadership Opportunities",
        [
            "Yes",
            "No"
        ]
    )

    innovation = st.selectbox(
        "Innovation Opportunities",
        [
            "Yes",
            "No"
        ]
    )

    company_reputation = st.selectbox(
        "Company Reputation",
        [
            "Poor",
            "Fair",
            "Good",
            "Excellent"
        ]
    )

    employee_recognition = st.selectbox(
        "Employee Recognition",
        [
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

st.write("")
st.markdown("---")

predict = st.button("Predict Employee Attrition")

st.markdown("---")
if predict:

    # ---------------- INPUT DATA ---------------- #

    input_data = pd.DataFrame({

        "age": [age],
        "gender": [gender],
        "years_at_company": [years_at_company],
        "job_role": [job_role],
        "monthly_income": [monthly_income],
        "work-life_balance": [work_life_balance],
        "job_satisfaction": [job_satisfaction],
        "performance_rating": [performance_rating],
        "number_of_promotions": [number_of_promotions],
        "overtime": [overtime],
        "distance_from_home": [distance_from_home],
        "education_level": [education_level],
        "marital_status": [marital_status],
        "number_of_dependents": [number_of_dependents],
        "job_level": [job_level],
        "company_size": [company_size],
        "company_tenure_(in_months)": [company_tenure],
        "remote_work": [remote_work],
        "leadership_opportunities": [leadership],
        "innovation_opportunities": [innovation],
        "company_reputation": [company_reputation],
        "employee_recognition": [employee_recognition]

    })

    # ---------------- PREDICTION ---------------- #

    prediction = model.predict(input_data)[0]

    probability = None

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0]

    st.write("")
    st.markdown("##Prediction Dashboard")

    left, right = st.columns([2, 1])

    # ---------------- LEFT COLUMN ---------------- #

    with left:

        if prediction == 0:
            st.success("##Employee is likely to STAY")
        else:
            st.error("##Employee is likely to LEAVE")

        if probability is not None:

            stay_prob = probability[0] * 100
            leave_prob = probability[1] * 100

            st.write("###Confidence")

            st.metric("Stayed", f"{stay_prob:.2f}%")
            st.progress(stay_prob / 100)

            st.metric("Left", f"{leave_prob:.2f}%")
            st.progress(leave_prob / 100)

    # ---------------- RIGHT COLUMN ---------------- #

    with right:

        st.info("###Employee Summary")

        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Job Role:** {job_role}")
        st.write(f"**Monthly Income:** ₹{monthly_income}")
        st.write(f"**Experience:** {years_at_company} Years")
        st.write(f"**Overtime:** {overtime}")

    st.markdown("---")

    st.subheader("Employee Details")

    st.dataframe(input_data, use_container_width=True)

    csv = input_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Employee Details",
        data=csv,
        file_name="employee_details.csv",
        mime="text/csv"
    )