import streamlit as st

st.title("Incident Report System")

# =======================
# INPUT FORM
# =======================
with st.form("incident_form"):

    client_name = st.text_input("Client Name")

    age = st.number_input(
        "Client Age",
        min_value=0,
        max_value=120,
        step=1
    )

    incident_type = st.selectbox(
        "Incident Type",
        [
            "Medical Emergency",
            "Injury",
            "Behavioral Incident",
            "Property Damage",
            "Other"
        ]
    )

    other_incident = ""

    if incident_type == "Other":
        other_incident = st.text_input("Please describe the 'Other' incident")

    severity_level = st.slider("Severity Level (0 - 10)", 0, 10, 0)

    submitted = st.form_submit_button("Submit Report")

# =======================
# PROCESS + OUTPUT
# =======================
if submitted:

    # Age group logic
    if age >= 18:
        age_group = "Adult"
    elif age >= 13:
        age_group = "Teen"
    else:
        age_group = "Child"

    # Risk level logic
    if severity_level >= 8:
        risk_level = "High Risk"
    elif severity_level >= 4:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    # Final incident type handling
    if incident_type == "Other":
        final_incident_type = other_incident
    else:
        final_incident_type = incident_type

    # =======================
    # REPORT OUTPUT
    # =======================
    st.markdown("## Incident Report")

    st.write(f"**Client Name:** {client_name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Age Group:** {age_group}")

    st.write("---")

    st.write(f"**Incident Type:** {final_incident_type}")

    st.write("---")

    st.write(f"**Severity Level:** {severity_level}")
    st.write(f"**Risk Level:** {risk_level}")

    st.success("Report submitted successfully!")