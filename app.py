from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# WAREHOUSE: Dubai Science Park (Central Medical Hub)
WAREHOUSE = {"name": "DSP Med-Hub", "lat": 25.0617, "lng": 55.2472}

# REGISTERED DUBAI HOSPITALS & PHARMACIES
HOSPITALS = {
    "Rashid Hospital": {"lat": 25.2497, "lng": 55.3090},
    "Latifa Hospital": {"lat": 25.2046, "lng": 55.3204},
    "Mediclinic Parkview": {"lat": 25.0564, "lng": 55.2505},
    "Aster Pharmacy": {"lat": 25.0770, "lng": 55.1380},
    "Zulekha Hospital": {"lat": 25.2718, "lng": 55.3622},
    "King's College Hospital": {"lat": 25.1014, "lng": 55.2592},
    "Al Zahra Hospital": {"lat": 25.1154, "lng": 55.1963},
    "Life Pharmacy": {"lat": 25.1955, "lng": 55.2760}
}

def haversine(p1, p2):
    """Calculates the distance between two lat/lng points in KM."""
    R = 6371 
    dlat, dlng = math.radians(p2['lat']-p1['lat']), math.radians(p2['lng']-p1['lng'])
    a = math.sin(dlat/2)**2 + math.cos(math.radians(p1['lat'])) * math.cos(math.radians(p2['lat'])) * math.sin(dlng/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

@app.route('/')
def index():
    return render_template('index.html', hospitals=sorted(HOSPITALS.keys()))

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    selected_stops = data.get('stops', [])
    traffic = float(data.get('traffic', 1.0))
    
    nodes = []
    for s in selected_stops:
        name = s['name']
        if name in HOSPITALS:
            nodes.append({
                "name": name, 
                "lat": HOSPITALS[name]['lat'], 
                "lng": HOSPITALS[name]['lng'], 
                "priority": int(s['priority']),
                "supply": s['supply']
            })

    if not nodes: return jsonify({"error": "No items"}), 400

    # DSA Logic: Priority-Weighted Greedy Heuristic
    unvisited = nodes[:]
    current = WAREHOUSE
    path = [WAREHOUSE]
    total_dist = 0
    
    while unvisited:
        # Priority 1 reduces effective distance, making it the 'greediest' choice
        nearest = min(unvisited, key=lambda x: haversine(current, x) * (x['priority'] / 3.0))
        total_dist += haversine(current, nearest)
        path.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    # Complete Hamiltonian Cycle
    total_dist += haversine(current, WAREHOUSE)
    path.append(WAREHOUSE)
    
    final_dist = total_dist * traffic
    return jsonify({
        "path": path,
        "distance": round(final_dist, 2),
        "time": round((final_dist / 45) * 60), 
        "cost": round(20 + (final_dist * 8.5), 2) # Base fee + Medical transport rate
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)