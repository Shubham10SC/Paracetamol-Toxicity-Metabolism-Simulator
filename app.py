import streamlit as st
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Draw

# --- 1. SETUP THE C++ ENGINE ---
try:
    # Load the C++ tool we made
    lib = ctypes.CDLL('./libengine.so')
    # Tell Python that the function returns a decimal number (double)
    lib.calculate_risk.restype = ctypes.c_double
    lib.calculate_risk.argtypes = [ctypes.c_double, ctypes.c_double]
    cpp_loaded = True
except:
    cpp_loaded = False
    st.error("Could not load C++ Engine. Did you compile it?")

# --- 2. THE APP DESIGN ---
st.title("🧪 Paracetamol Toxicity Simulator")
st.caption("Powered by C++ (Kinetics), RDKit (Chem), and Python")

# Sidebar Inputs
st.sidebar.header("Patient Parameters")
dose = st.sidebar.slider("Paracetamol Dose (mg)", 0, 5000, 500, step=100)
gsh = st.sidebar.slider("Liver Glutathione Level (%)", 0, 100, 100)

# --- 3. MOLECULAR VISUALIZATION (RDKit) ---
st.subheader("1. Molecular Structures")
col1, col2 = st.columns(2)

with col1:
    st.write("**Paracetamol** (Safe)")
    mol_safe = Chem.MolFromSmiles("CC(=O)Nc1ccc(O)cc1")
    st.image(Draw.MolToImage(mol_safe), use_column_width=True)
    
with col2:
    st.write("**NAPQI** (Toxic Metabolite)")
    mol_toxic = Chem.MolFromSmiles("CC(=O)N=C1C=CC(=O)C=C1")
    st.image(Draw.MolToImage(mol_toxic), use_column_width=True)

# --- 4. SIMULATION ---
if cpp_loaded:
    # Call the C++ function
    risk_score = lib.calculate_risk(float(dose), float(gsh))
    
    st.subheader("2. Toxicity Analysis")
    
    # Display Risk Meter
    if risk_score == 0:
        st.success("✅ Safe: Liver neutralized the toxin.")
    elif risk_score < 100:
        st.warning(f"⚠️ Warning: Mild Liver Stress (Load: {risk_score:.1f})")
    else:
        st.error(f"☠️ DANGER: Hepatotoxicity Imminent (Load: {risk_score:.1f})")

    # --- 5. TIME-COURSE CHART (Math) ---
    st.subheader("3. Metabolism Over Time")
    
    # Fake complex math to visualize depletion curves
    time = np.linspace(0, 24, 100) # 24 hours
    initial_gsh = gsh
    
    # If dose is high, GSH drops fast
    decay_rate = 0.05 + (dose / 10000.0)
    gsh_over_time = initial_gsh * np.exp(-decay_rate * time)
    
    fig, ax = plt.subplots()
    ax.plot(time, gsh_over_time, color='green', label='Liver Glutathione')
    ax.axhline(y=30, color='red', linestyle='--', label='Critical Failure Line')
    ax.set_xlabel("Hours after ingestion")
    ax.set_ylabel("Glutathione %")
    ax.legend()
    
    st.pyplot(fig)

