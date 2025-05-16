
import streamlit as st

st.set_page_config(page_title="Remodel Estimator", layout="wide")
st.title("Remodel Cost Estimator")

# Client Info
st.sidebar.header("Client Information")
client_name = st.sidebar.text_input("Client Name")
project_address = st.sidebar.text_input("Project Address")
email = st.sidebar.text_input("Client Email")

# Project Details
st.header("Project Details")
project_type = st.selectbox("Remodel Type", ["Kitchen", "Bathroom", "Basement", "Full House"])
sq_ft = st.number_input("Square Footage", min_value=0)
quality = st.radio("Finish Quality", ["Basic", "Mid-Grade", "High-End"])
region = st.selectbox("Project Region", ["National Avg", "Utah", "California", "Texas", "New York"])

# Upgrades
st.subheader("Optional Upgrades")
appliances = st.checkbox("New Appliances")
flooring = st.checkbox("New Flooring")
lighting = st.checkbox("Lighting Upgrade")

# --- Pricing Data ---
base_costs = {
    "Kitchen": {"Basic": 100, "Mid-Grade": 150, "High-End": 200},
    "Bathroom": {"Basic": 80, "Mid-Grade": 120, "High-End": 180},
    "Basement": {"Basic": 60, "Mid-Grade": 90, "High-End": 130},
    "Full House": {"Basic": 110, "Mid-Grade": 160, "High-End": 210},
}

region_multipliers = {
    "National Avg": 1.0,
    "Utah": 0.95,
    "California": 1.2,
    "Texas": 0.98,
    "New York": 1.3,
}

upgrade_costs = {
    "Appliances": 3000,
    "Flooring": 5 * sq_ft,  # $5 per sq ft
    "Lighting": 1500,
}

# --- Calculation ---
material_cost = base_costs[project_type][quality] * sq_ft
region_adjusted_cost = material_cost * region_multipliers[region]

upgrade_total = 0
if appliances:
    upgrade_total += upgrade_costs["Appliances"]
if flooring:
    upgrade_total += upgrade_costs["Flooring"]
if lighting:
    upgrade_total += upgrade_costs["Lighting"]

labor_cost = 0.2 * (region_adjusted_cost + upgrade_total)
total_estimate = region_adjusted_cost + upgrade_total + labor_cost

# --- Display Results ---
st.subheader("Estimated Project Cost")
st.write(f"**Materials:** ${region_adjusted_cost:,.2f}")
st.write(f"**Upgrades:** ${upgrade_total:,.2f}")
st.write(f"**Labor (20%):** ${labor_cost:,.2f}")
st.success(f"**Total Estimate: ${total_estimate:,.2f}**")
