#include <cmath>

extern "C" {
    // A simple simulation of how liver glutathione (GSH) fights NAPQI
    // dose: mg of paracetamol
    // gsh_level: percentage of healthy liver function
    double calculate_risk(double dose, double gsh_level) {
        
        // NAPQI production (approx 5-10% of paracetamol becomes toxic)
        double napqi_produced = dose * 0.10;
        
        // Liver defense capacity
        double defense_capacity = gsh_level * 5.0; 
        
        // Calculate remaining toxic NAPQI
        double toxic_load = napqi_produced - defense_capacity;
        
        if (toxic_load < 0) {
            return 0.0; // Liver handled it safely
        } else {
            return toxic_load; // This is the damage value
        }
    }
}

