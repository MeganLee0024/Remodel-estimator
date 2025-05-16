
import streamlit as st

# Base costs per sqft
base_costs = {
    "Kitchen": {"Basic": 100, "Mid": 150, "High": 250},
    "Bathroom": {"Basic": 80, "Mid": 130, "High": 200},
    "Bedroom": {"Basic": 50, "Mid": 75, "High": 120},
    "Living Room": {"Basic": 60, "Mid": 90, "High": 140},
    "Basement": {"Basic": 70, "Mid": 110, "High": 170}
}

st.title("RemodelMate - Estimate Your Remodel")

# Step 1: Project Info
st.header("1. Project Info")
remodel_type = st.selectbox("Remodel Type", list(base_costs.keys()))
sqft = st.number_input("Square Footage", min_value=10)
material_quality = st.selectbox("Material Quality", ["Basic", "Mid", "High"])

base_cost = base_costs[remodel_type][material_quality]
material_total = base_cost * sqft

# Step 2: Labor Costs
st.header("2. Labor Costs")
labor_type = st.radio("How would you like to calculate labor?", ["Hourly", "Percentage"])
if labor_type == "Hourly":
    hourly_rate = st.number_input("Hourly Rate", value=50)
    hours = st.number_input("Estimated Hours", value=10)
    labor_total = hourly_rate * hours
else:
    labor_percent = st.slider("Labor % of Material", 0, 100, 30)
    labor_total = (labor_percent / 100) * material_total

# Step 3: Optional Upgrades
st.header("3. Optional Upgrades")
appliances = st.checkbox("New Appliances (+$2000)")
lighting = st.checkbox("Lighting Upgrade (+$1000)")
flooring = st.checkbox("New Flooring (+$5/sqft)")

upgrade_total = 0
if appliances:
    upgrade_total += 2000
if lighting:
    upgrade_total += 1000
if flooring:
    upgrade_total += 5 * sqft

# Step 4: Region Adjustment
st.header("4. Region Multiplier")
region_multiplier = st.slider("Regional Adjustment Multiplier", 0.5, 2.0, 1.0)

# Total Calculation
subtotal = material_total + labor_total + upgrade_total
adjusted_total = subtotal * region_multiplier

st.header("5. Estimate Summary")
st.markdown(f"**Material Cost**: ${material_total:,.2f}")
st.markdown(f"**Labor Cost**: ${labor_total:,.2f}")
st.markdown(f"**Upgrades**: ${upgrade_total:,.2f}")
st.markdown(f"**Regional Multiplier**: x{region_multiplier}")
st.markdown(f"### **Final Estimated Cost: ${adjusted_total:,.2f}**")

# Save/export options
st.download_button("Download Estimate as CSV", data=f"""
Type,{remodel_type}
Square Footage,{sqft}
Material Quality,{material_quality}
Material Cost,{material_total}
Labor Cost,{labor_total}
Upgrade Cost,{upgrade_total}
Region Multiplier,{region_multiplier}
Total Estimate,{adjusted_total}
""", file_name="remodel_estimate.csv")
