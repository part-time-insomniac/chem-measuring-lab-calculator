glassware = [
    {
        "type": "100_bleaker",
        "mass_no_water": 115.25,
        "volume_of_water_added": [49.0, 50.0, 50.0],
        "mass_with_water": [157.88,158.43,159.64],
    },
    {
        "type": "100_cylinder",
        "mass_no_water": 45.81,
        "volume_of_water_added": [49.9, 50.0, 50.1],
        "mass_with_water": [94.61,95.18,95.86],
    },
    {
        "type": "25_flask",
        "mass_no_water": 23.74,
        "volume_of_water_added": [25.0, 25.0, 25.0],
        "mass_with_water": [49.28,49.31,49.36],
    },
    {
        "type": "10_cylinder",
        "mass_no_water": 38.45,
        "volume_of_water_added": [9.95, 10.05, 10.00],
        "mass_with_water": [45.61,45.76,45.63],
    },
]
dispenser = [
    {
        "type": "50_buret",
        "mass_no_water": 50.35,
        "init_vol": [0.00, 10.02, 19.98],
        "final": [10.02, 19.98, 31.0],
        "mass_with_water": [60.64,60.50,60.47],
    },
    {
        "type": "10_pipette",
        "mass_no_water": 50.43,
        "init_vol": [0.00, 0.00, 0],
        "final": [5.1, 5.1, 5.1],
        "mass_with_water": [56.82,55.48,55.42],
    },
]
results = []
for item in glassware:
    item_type = item
    mass_no = item["mass_no_water"]
    final_mass = []
    final_vol = []
    final_den = []
    for vol, mass in zip(item["volume_of_water_added"],item["mass_with_water"]):
        mass_water = mass - mass_no
        density = mass_water/vol
        final_mass.append(round(mass_water,4))
        final_vol.append(vol)
        final_den.append(round(density,4))
    results.append({
        "type": item_type,
        "mass_water_trials": final_mass,
        "volume_trials": final_vol,
        "density_trials": final_den
    })
for item in dispenser:
    item_type = item
    mass_no = item["mass_no_water"]
    final_mass = []
    final_voll = []
    final_den = []
    for in_vol, final_vol, mass in zip(item["init_vol"], item["final"], item["mass_with_water"]):
        mass_water = mass - mass_no
        vol = final_vol - in_vol
        density = mass_water/vol
        final_mass.append(round(mass_water,4))
        final_voll.append(vol)
        final_den.append(round(density,4))
    results.append({
        "type": item_type,
        "mass_water_trials": final_mass,
        "volume_trials": final_voll,
        "density_trials": final_den
    })
import pprint
pprint.pprint(results)

water_density = 0.988

accuracy_list = []
for item in results:
    avg_density = sum(item["density_trials"]) / len(item["density_trials"])
    percent_error = abs(avg_density - water_density) / water_density * 100
    accuracy_list.append({
        "type": item["type"]["type"],
        "avg_density_g_ml": round(avg_density, 4),
        "percent_error": round(percent_error, 4),
    })

accuracy_list.sort(key=lambda x: x["percent_error"])

pprint.pprint(accuracy_list)
