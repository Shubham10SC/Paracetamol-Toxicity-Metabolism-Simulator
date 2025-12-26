# 🧪 Paracetamol Toxicity & Metabolism Simulator

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![C++](https://img.shields.io/badge/C%2B%2B-17-red)
![License](https://img.shields.io/badge/License-MIT-green)

### 🏥 Overview
A high-performance hybrid application that simulates the hepatotoxic effects of Paracetamol (Acetaminophen) overdose. 

This project demonstrates **High-Performance Computing (HPC)** by combining:
*   **C++ (Backend):** Handles complex kinetic calculations and liver depletion logic for maximum speed.
*   **Python (Frontend):** Uses Streamlit and RDKit for molecular visualization and interactive UI.

### 🧬 Key Features
*   **Real-time Metabolism Tracking:** Simulates the conversion of Paracetamol to the toxic metabolite **NAPQI**.
*   **Glutathione (GSH) Depletion:** Models the liver's defense mechanism against toxins using decay algorithms.
*   **Molecular Visualization:** Renders 2D chemical structures of Paracetamol and NAPQI dynamically.
*   **Risk Assessment:** Calculates toxic load scores to predict liver failure risks.

---

### 🚀 Installation & Usage

Since this project uses a custom C++ engine, you must compile the backend before running the app.

#### 1. Clone the Repository
```bash
git clone https://github.com/Shubham10SC/Paracetamol-Toxicity-Metabolism-Simulator.git
cd Paracetamol-Toxicity-Metabolism-Simulator


#### 2. Install Python Dependencies
```bash
pip install streamlit numpy matplotlib rdkit
```

#### 3. Compile the C++ Engine ⚙️
**For Linux / macOS / Termux:**
```bash
g++ -shared -o libengine.so -fPIC engine.cpp
```

**For Windows:**
```bash
g++ -shared -o libengine.dll engine.cpp
```

#### 4. Run the Application
```bash
streamlit run app.py
```

---

### 📂 Project Structure
| File | Description |
| :--- | :--- |
| `app.py` | Main Python application (UI & Logic Bridge) |
| `engine.cpp` | C++ Source code for toxicity calculations |
| `libengine.so` | Compiled binary (Linux/Android) |

### 🔬 Scientific Logic
The simulation uses a mathematical decay model where:
30715 GSH(t) = GSH_{initial} \times e^{-(k + \frac{Dose}{10000})t} 30715
Where *k* is the metabolic constant and *Dose* increases the rate of depletion.

---
**Created by Shubham10SC**
