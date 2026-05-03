# MedLink IQ:Biological & Pharmaceutical Logistics Optimizer

## 🏥 Project Overview
**MedLink IQ** is a specialized logistics management system designed for the high-stakes environment of medical and pharmaceutical deliveries in Dubai. Unlike standard delivery routers, this system prioritizes life-saving assets (like organs and blood) over standard inventory (like pharmacy restocks) using a custom **Priority-Weighted Greedy Algorithm**.

The application provides a real-time command center interface where dispatchers can manage multiple medical destinations, assign priority levels to various medical assets, and optimize the delivery route based on urgency and live traffic density.

---

## 🚀 Key Features
* **Asset Categorization**: Specialized handling for Organs, Blood Units, Vaccines, and Emergency Medicines.
* **Priority-Weighted Routing**: A custom implementation of the Traveling Salesman Problem (TSP) heuristic that "weights" nodes based on medical urgency.
* **Dynamic Traffic Simulation**: Adjusts travel time and operational costs based on live traffic density sliders.
* **Hamiltonian Cycle Optimization**: Ensures the medical courier always begins and ends their route at the central Dubai Science Park (DSP) Hub.
* **Interactive Command Center**: Real-time map visualization using Leaflet.js with color-coded priority markers.

---

## 🧠 Algorithmic Logic (The DSA Part)
The core of this project is a **Weighted Greedy Heuristic**. 

### The Formula:
Standard greedy algorithms choose the next stop based strictly on the shortest physical distance ($d$). Our algorithm uses a **Bias Factor** ($B$):
$$Cost = d \times (Priority / 3)$$

* **Level 1 (Critical)**: Reduces the "apparent distance" by 66%, forcing the algorithm to visit these stops first.
* **Level 3 (Standard)**: Retains normal distance weighting.

This ensures that a hospital waiting for an organ transplant is prioritized, even if a pharmacy requiring a standard medicine restock is physically closer.

---

## 🛠️ Tech Stack
* **Backend**: Python / Flask
* **Frontend**: HTML5, Tailwind CSS, Leaflet.js (Mapping API)
* **Logic**: Haversine Formula (Great-circle distance calculation)
* **Version Control**: Git / GitHub

---

## 📈 Operational Stats
The system calculates three key metrics in real-time:
1.  **Total Distance**: Actual kilometers covered in the Hamiltonian cycle.
2.  **Est. Transit Time**: Calculated based on a 45km/h average city speed, adjusted by the traffic multiplier.
3.  **Priority Operational Cost**: A premium medical-grade pricing model (Base 20 AED + 8.5 AED/km).

---

## 👷 Setup Instructions
1. Clone the repository.
2. Install requirements: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the command center at `http://127.0.0.1:5000`
