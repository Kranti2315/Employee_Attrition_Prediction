# import streamlit as st
# import pandas as pd
# import pickle

# # ---------------- PAGE CONFIG ---------------- #

# st.set_page_config(
#     page_title="Employee Attrition Dashboard",
#     page_icon=" ",
#     layout="wide"
# )

# # ---------------- LOAD MODEL ---------------- #

# model = pickle.load(open("employee_model.pkl", "rb"))

# # ---------------- CUSTOM CSS ---------------- #

# st.markdown("""
# <style>

# .stApp{
# background:#0f172a;
# }

# .block-container{
# padding-top:1rem;
# padding-bottom:1rem;
# max-width:1300px;
# }

# /* Header */

# .title{
# font-size:42px;
# font-weight:bold;
# color:white;
# }

# .subtitle{
# font-size:18px;
# color:#cbd5e1;
# margin-top:-10px;
# }

# /* Sidebar */

# section[data-testid="stSidebar"]{
# background:#111827;
# }

# .sidebar-card{
# background:#1e293b;
# padding:18px;
# border-radius:12px;
# color:white;
# margin-bottom:15px;
# text-align:center;
# }

# .sidebar-card h2{
# color:#60a5fa;
# }

# /* KPI Cards */

# .metric-card{
# background:linear-gradient(135deg,#2563eb,#1d4ed8);
# padding:20px;
# border-radius:15px;
# color:white;
# text-align:center;
# box-shadow:0px 5px 15px rgba(0,0,0,.4);
# }

# .metric-title{
# font-size:17px;
# }

# .metric-value{
# font-size:34px;
# font-weight:bold;
# }

# /* Form Card */

# .form-card{
# background:#1e293b;
# padding:20px;
# border-radius:15px;
# box-shadow:0px 5px 10px rgba(0,0,0,.3);
# }

# /* Predict Button */

# div.stButton > button{
# width:100%;
# background:#2563eb;
# color:white;
# border-radius:12px;
# height:55px;
# font-size:22px;
# font-weight:bold;
# border:none;
# }

# div.stButton > button:hover{
# background:#1d4ed8;
# }

# /* Result Card */

# .success{
# background:#14532d;
# padding:25px;
# border-radius:15px;
# text-align:center;
# font-size:30px;
# font-weight:bold;
# color:white;
# }

# .danger{
# background:#7f1d1d;
# padding:25px;
# border-radius:15px;
# text-align:center;
# font-size:30px;
# font-weight:bold;
# color:white;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- SIDEBAR ---------------- #

# with st.sidebar:

#     st.image(
#         "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
#         width=130
#     )

#     st.markdown("##HR Analytics")

#     st.markdown("""
# <div class="sidebar-card">
# <h2>Employee Attrition</h2>

# Predict whether an employee is likely to leave the company using Machine Learning.
# </div>
# """, unsafe_allow_html=True)

#     st.markdown("""
# <div class="sidebar-card">
#  Dataset<br><br>
# 5000 Employees
# </div>
# """, unsafe_allow_html=True)

#     st.markdown("""
# <div class="sidebar-card">
#  Best Model<br><br>
# Random Forest
# </div>
# """, unsafe_allow_html=True)

#     st.markdown("""
# <div class="sidebar-card">
#   Developed Using

# Python

# Scikit-Learn

# Streamlit
# </div>
# """, unsafe_allow_html=True)

# # ---------------- HEADER ---------------- #

# st.markdown(
# """
# <div class="title">
#   Employee Attrition Prediction Dashboard
# </div>
# """,
# unsafe_allow_html=True
# )

# st.markdown(
# """
# <div class="subtitle">
# Predict whether an employee is likely to leave the company using Machine Learning.
# </div>
# """,
# unsafe_allow_html=True
# )

# st.write("")

# # ---------------- KPI CARDS ---------------- #

# c1,c2,c3,c4 = st.columns(4)

# with c1:

#     st.markdown("""
# <div class="metric-card">
# <div class="metric-title">
#   Accuracy
# </div>

# <div class="metric-value">
# 96.2%
# </div>
# </div>
# """, unsafe_allow_html=True)

# with c2:

#     st.markdown("""
# <div class="metric-card">
# <div class="metric-title">
#   Best Model
# </div>

# <div class="metric-value">
# Random Forest
# </div>
# </div>
# """, unsafe_allow_html=True)

# with c3:

#     st.markdown("""
# <div class="metric-card">
# <div class="metric-title">
#   Dataset
# </div>

# <div class="metric-value">
# 5000+
# </div>
# </div>
# """, unsafe_allow_html=True)

# with c4:

#     st.markdown("""
# <div class="metric-card">
# <div class="metric-title">
#   Target
# </div>

# <div class="metric-value">
# Attrition
# </div>
# </div>
# """, unsafe_allow_html=True)

# st.write("")
# st.markdown("---")
# # =====================================================
# # EMPLOYEE INFORMATION
# # =====================================================

# st.markdown("##Employee Information")

# left, right = st.columns(2)

# # ---------------- LEFT COLUMN ---------------- #

# with left:

#     age = st.number_input(
#         "Age",
#         min_value=18,
#         max_value=65,
#         value=30
#     )

#     gender = st.selectbox(
#         "Gender",
#         ["Male","Female"]
#     )

#     years_at_company = st.number_input(
#         "Years at Company",
#         0,50,5
#     )

#     job_role = st.selectbox(
#         "Job Role",
#         [
#             "Education",
#             "Finance",
#             "Healthcare",
#             "Media",
#             "Technology"
#         ]
#     )

#     monthly_income = st.number_input(
#         "Monthly Income",
#         1000,
#         100000,
#         30000
#     )

#     work_life_balance = st.selectbox(
#         "Work Life Balance",
#         [
#             "Poor",
#             "Fair",
#             "Good",
#             "Excellent"
#         ]
#     )

#     job_satisfaction = st.selectbox(
#         "Job Satisfaction",
#         [
#             "Low",
#             "Medium",
#             "High",
#             "Very High"
#         ]
#     )

#     performance_rating = st.selectbox(
#         "Performance Rating",
#         [
#             "Below Average",
#             "Average",
#             "High",
#             "Low"
#         ]
#     )

#     number_of_promotions = st.number_input(
#         "Number of Promotions",
#         0,10,0
#     )

#     overtime = st.selectbox(
#         "Overtime",
#         [
#             "Yes",
#             "No"
#         ]
#     )

#     distance_from_home = st.number_input(
#         "Distance From Home",
#         1,100,10
#     )

# # ---------------- RIGHT COLUMN ---------------- #

# with right:

#     education_level = st.selectbox(
#         "Education",
#         [
#             "High School",
#             "Associate Degree",
#             "Bachelor's Degree",
#             "Master's Degree",
#             "PhD"
#         ]
#     )

#     marital_status = st.selectbox(
#         "Marital Status",
#         [
#             "Single",
#             "Married",
#             "Divorced"
#         ]
#     )

#     number_of_dependents = st.number_input(
#         "Dependents",
#         0,10,1
#     )

#     job_level = st.selectbox(
#         "Job Level",
#         [
#             "Entry",
#             "Mid",
#             "Senior"
#         ]
#     )

#     company_size = st.selectbox(
#         "Company Size",
#         [
#             "Small",
#             "Medium",
#             "Large"
#         ]
#     )

#     company_tenure = st.number_input(
#         "Company Tenure (Months)",
#         1,500,24
#     )

#     remote_work = st.selectbox(
#         "Remote Work",
#         [
#             "Yes",
#             "No"
#         ]
#     )

#     leadership = st.selectbox(
#         "Leadership Opportunities",
#         [
#             "Yes",
#             "No"
#         ]
#     )

#     innovation = st.selectbox(
#         "Innovation Opportunities",
#         [
#             "Yes",
#             "No"
#         ]
#     )

#     company_reputation = st.selectbox(
#         "Company Reputation",
#         [
#             "Poor",
#             "Fair",
#             "Good",
#             "Excellent"
#         ]
#     )

#     employee_recognition = st.selectbox(
#         "Employee Recognition",
#         [
#             "Low",
#             "Medium",
#             "High",
#             "Very High"
#         ]
#     )

# st.write("")
# st.markdown("---")

# predict = st.button("Predict Employee Attrition")

# st.markdown("---")
# if predict:

#     # ---------------- INPUT DATA ---------------- #

#     input_data = pd.DataFrame({

#         "age": [age],
#         "gender": [gender],
#         "years_at_company": [years_at_company],
#         "job_role": [job_role],
#         "monthly_income": [monthly_income],
#         "work-life_balance": [work_life_balance],
#         "job_satisfaction": [job_satisfaction],
#         "performance_rating": [performance_rating],
#         "number_of_promotions": [number_of_promotions],
#         "overtime": [overtime],
#         "distance_from_home": [distance_from_home],
#         "education_level": [education_level],
#         "marital_status": [marital_status],
#         "number_of_dependents": [number_of_dependents],
#         "job_level": [job_level],
#         "company_size": [company_size],
#         "company_tenure_(in_months)": [company_tenure],
#         "remote_work": [remote_work],
#         "leadership_opportunities": [leadership],
#         "innovation_opportunities": [innovation],
#         "company_reputation": [company_reputation],
#         "employee_recognition": [employee_recognition]

#     })

#     # ---------------- PREDICTION ---------------- #

#     prediction = model.predict(input_data)[0]

#     probability = None

#     if hasattr(model, "predict_proba"):
#         probability = model.predict_proba(input_data)[0]

#     st.write("")
#     st.markdown("##Prediction Dashboard")

#     left, right = st.columns([2, 1])

#     # ---------------- LEFT COLUMN ---------------- #

#     with left:

#         if prediction == 0:
#             st.success("##Employee is likely to STAY")
#         else:
#             st.error("##Employee is likely to LEAVE")

#         if probability is not None:

#             stay_prob = probability[0] * 100
#             leave_prob = probability[1] * 100

#             st.write("###Confidence")

#             st.metric("Stayed", f"{stay_prob:.2f}%")
#             st.progress(stay_prob / 100)

#             st.metric("Left", f"{leave_prob:.2f}%")
#             st.progress(leave_prob / 100)

#     # ---------------- RIGHT COLUMN ---------------- #

#     with right:

#         st.info("###Employee Summary")

#         st.write(f"**Age:** {age}")
#         st.write(f"**Gender:** {gender}")
#         st.write(f"**Job Role:** {job_role}")
#         st.write(f"**Monthly Income:** ₹{monthly_income}")
#         st.write(f"**Experience:** {years_at_company} Years")
#         st.write(f"**Overtime:** {overtime}")

#     st.markdown("---")

#     st.subheader("Employee Details")

#     st.dataframe(input_data, use_container_width=True)

#     csv = input_data.to_csv(index=False).encode("utf-8")

#     st.download_button(
#         "Download Employee Details",
#         data=csv,
#         file_name="employee_details.csv",
#         mime="text/csv"
#     )





import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Employee Attrition Prediction System",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("employee_model.pkl")

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
padding-left:2rem;
padding-right:2rem;
}

body{
background:#f4f7fb;
}

.main-title{
font-size:38px;
font-weight:700;
color:white;
}

.sub-title{
font-size:18px;
color:white;
margin-bottom:25px;
}

.card{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0px 4px 12px rgba(0,0,0,.08);
margin-bottom:15px;
}

div[data-testid="stMetric"]{
background:#1E293B;
padding:20px;
border-radius:12px;
border:1px solid #334155;
text-align:center;
}

div[data-testid="stMetricLabel"]{
color:#CBD5E1;
font-size:16px;
font-weight:600;
}

div[data-testid="stMetricValue"]{
color:white;
font-size:28px;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("Employee Attrition")

    st.markdown("---")

    st.write("Machine Learning Project")

    st.info("""
Best Model

Logistic Regression
""")

    st.markdown("---")

    st.write("Technologies")

    st.write("""
• Python

• Scikit-Learn

• Streamlit

• Pandas

• Joblib
""")

    st.markdown("---")

    st.success("Ready for Prediction")

# ---------------- HEADER ---------------- #

st.markdown(
"""
<div class='main-title'>
Employee Attrition Prediction System
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='sub-title'>
Predict whether an employee is likely to stay or leave the organization using a trained Machine Learning model.
</div>
""",
unsafe_allow_html=True
)
# ---------------- KPI CARDS ---------------- #

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Model", "Logistic Regression")

with c2:
    st.metric("Target", "Attrition")

with c3:
    st.metric("Prediction", "Stay / Leave")

with c4:
    st.metric("Deployment", "Streamlit")

st.write("")

# ---------------- TABS ---------------- #

tab1, tab2 = st.tabs(
    [
        "Single Employee Prediction",
        "Batch CSV Prediction"
    ]
)

# ============================================================
# TAB 1
# ============================================================

with tab1:

    st.markdown("## Employee Information")

    left, right = st.columns(2)

    # ---------------- LEFT COLUMN ---------------- #

    with left:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=70,
            value=30
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

        years_at_company = st.number_input(
            "Years at Company",
            min_value=0,
            max_value=40,
            value=5
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
            min_value=1000,
            max_value=100000,
            value=25000
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
                "Low",
                "Average",
                "High"
            ]
        )

        number_of_promotions = st.number_input(
            "Number of Promotions",
            min_value=0,
            max_value=15,
            value=1
        )

        overtime = st.selectbox(
            "Overtime",
            [
                "No",
                "Yes"
            ]
        )

        distance_from_home = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=100,
            value=10
        )
            # ---------------- RIGHT COLUMN ---------------- #

    with right:

        education_level = st.selectbox(
            "Education Level",
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
            "Number of Dependents",
            min_value=0,
            max_value=10,
            value=1
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
            min_value=1,
            max_value=500,
            value=60
        )

        remote_work = st.selectbox(
            "Remote Work",
            [
                "No",
                "Yes"
            ]
        )

        leadership = st.selectbox(
            "Leadership Opportunities",
            [
                "No",
                "Yes"
            ]
        )

        innovation = st.selectbox(
            "Innovation Opportunities",
            [
                "No",
                "Yes"
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

    predict = st.button(
        "Predict Employee Attrition",
        use_container_width=True
    )

    if predict:

        input_data = pd.DataFrame({

            "age":[age],
            "gender":[gender],
            "years_at_company":[years_at_company],
            "job_role":[job_role],
            "monthly_income":[monthly_income],
            "work-life_balance":[work_life_balance],
            "job_satisfaction":[job_satisfaction],
            "performance_rating":[performance_rating],
            "number_of_promotions":[number_of_promotions],
            "overtime":[overtime],
            "distance_from_home":[distance_from_home],
            "education_level":[education_level],
            "marital_status":[marital_status],
            "number_of_dependents":[number_of_dependents],
            "job_level":[job_level],
            "company_size":[company_size],
            "company_tenure_(in_months)":[company_tenure],
            "remote_work":[remote_work],
            "leadership_opportunities":[leadership],
            "innovation_opportunities":[innovation],
            "company_reputation":[company_reputation],
            "employee_recognition":[employee_recognition]

        })

        prediction = model.predict(input_data)[0]

        probability = None

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_data)[0]
        st.write("")

        st.markdown("## Prediction Dashboard")

        col1, col2 = st.columns([2,1])

        # =====================================
        # LEFT SIDE
        # =====================================

        with col1:

            if prediction == 0:

                st.success("Employee is likely to STAY")

            else:

                st.error("Employee is likely to LEAVE")

            if probability is not None:

                stay_prob = probability[0] * 100
                leave_prob = probability[1] * 100

                st.write("")

                st.subheader("Prediction Confidence")

                confidence = max(stay_prob, leave_prob)

                st.progress(int(confidence))

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "Stay Probability",
                        f"{stay_prob:.2f}%"
                    )

                with c2:

                    st.metric(
                        "Leave Probability",
                        f"{leave_prob:.2f}%"
                    )

        # =====================================
        # RIGHT SIDE
        # =====================================

        with col2:

            st.subheader("Employee Summary")

            st.write(f"Age : {age}")

            st.write(f"Gender : {gender}")

            st.write(f"Job Role : {job_role}")

            st.write(f"Experience : {years_at_company} Years")

            st.write(f"Monthly Income : ₹ {monthly_income:,}")

            st.write(f"Overtime : {overtime}")

            st.write(f"Work Life Balance : {work_life_balance}")

            st.write(f"Job Satisfaction : {job_satisfaction}")

        st.write("")

        st.markdown("---")

        st.subheader("Employee Input Data")

        st.dataframe(
            input_data,
            use_container_width=True
        )

        csv = input_data.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="Download Employee Details",

            data=csv,

            file_name="employee_details.csv",

            mime="text/csv",

            use_container_width=True
        )
        # ==========================================================
# TAB 2 : BATCH CSV PREDICTION
# ==========================================================

with tab2:

    st.markdown("## Batch Employee Attrition Prediction")

    st.write(
        "Upload a cleaned employee dataset to predict attrition for multiple employees."
    )

    uploaded_file = st.file_uploader(
        "Upload Employee CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(uploaded_file)

            st.success("CSV Uploaded Successfully")

            st.write("### Uploaded Dataset")

            st.dataframe(
                df.head(),
                use_container_width=True
            )

            st.write("")

            st.info("Predicting Employee Attrition...")

            prediction = model.predict(df)

            prediction = [
                "Stayed" if i == 0 else "Left"
                for i in prediction
            ]

            df["Prediction"] = prediction

            st.success("Prediction Completed Successfully")

            stayed = (df["Prediction"]=="Stayed").sum()
            left = (df["Prediction"]=="Left").sum()

            c1,c2,c3 = st.columns(3)

            with c1:
                st.metric(
                    "Total Employees",
                    len(df)
                )

            with c2:
                st.metric(
                    "Stayed",
                    stayed
                )

            with c3:
                st.metric(
                    "Left",
                    left
                )

            st.write("")

            st.subheader("Prediction Results")

            st.dataframe(
                df,
                use_container_width=True
            )

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(

                label="Download Prediction CSV",

                data=csv,

                file_name="Employee_Predictions.csv",

                mime="text/csv",

                use_container_width=True

            )

        except Exception as e:

            st.error("Prediction Failed")

            st.exception(e)
            st.markdown("---")

st.markdown(
"""
<div style='text-align:center;
padding:15px;
color:gray;
font-size:15px;'>

Employee Attrition Prediction System

Developed using Python, Scikit-Learn, Streamlit and Machine Learning

</div>
""",
unsafe_allow_html=True
)