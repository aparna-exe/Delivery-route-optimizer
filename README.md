# 🚚 RouteIQ — Dubai Delivery Optimizer

A high-performance logistics dashboard built for the **Algorithms Lab**. This project solves the **Traveling Salesman Problem (TSP)** using a **Greedy Nearest Neighbor** heuristic to optimize delivery routes across Dubai.

## 🌟 Key Features
- **Geocoding Engine**: Select areas like "Dubai Mall" or "Palm Jumeirah" without needing manual coordinates.
- **O(n²) Greedy Algorithm**: Efficiently calculates the shortest path between multiple stops.
- **Hamiltonian Cycle**: The route always starts and ends at the Warehouse (Dubai Internet City).
- **Live Map Visualization**: Interactive dark-mode map with dashed route lines (Polylines).
- **Traffic & Cost Engine**: Real-time recalculation of AED cost and travel time based on traffic density.

## 🛠️ Tech Stack
- **Backend**: Python 3 + Flask
- **Frontend**: Tailwind CSS (UI) + Leaflet.js (Mapping)
- **Algorithm**: Greedy Nearest Neighbor + Haversine Distance Formula

## 🚀 Setup for Collaborators
1. **Clone the repo**:
   ```bash
   git clone <your-repo-link>