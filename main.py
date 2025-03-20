Creating a comprehensive route planning tool like "Eco-Navigator" that optimizes travel routes for minimal carbon footprint is a complex project that would typically involve several technologies and data sources. However, I'll provide you with a simplified version of such a tool using Python. We'll focus on structuring the program, performing basic operations, and adding error handling and comments. However, note that for a real-world application, you would need to integrate with APIs for real-time data and have access to datasets that provide details about public transport, traffic, and carpooling.

Below is a conceptual Python program. For the sake of simplicity, the program will use hypothetical functions to get real-time traffic, public transport, and carpooling data. These functions are placeholders for real integrations you would have in a production application.

```python
import random

# Hypothetical functions to get data. In a real implementation, these would be API calls.
def get_real_time_traffic_data(start, destination):
    # Simulate traffic data with random numbers for travel time in minutes
    return random.randint(30, 120)  # Simulating traffic delay time in minutes

def get_public_transport_options(start, destination):
    # Simulate public transport routes
    routes = [
        {'mode': 'Bus', 'duration': random.randint(40, 100)},
        {'mode': 'Train', 'duration': random.randint(35, 90)},
        {'mode': 'Subway', 'duration': random.randint(30, 80)}
    ]
    return routes

def get_carpool_options(start, destination):
    # Simulate carpool availability
    return random.choice([True, False])

# Function to calculate carbon footprint for each travel mode
def calculate_carbon_footprint(mode, duration):
    if mode == 'Car':
        return duration * 0.5  # Dummy factor for car emissions
    elif mode == 'Bus':
        return duration * 0.3  # Dummy factor for bus emissions
    elif mode == 'Train':
        return duration * 0.2  # Dummy factor for train emissions
    elif mode == 'Subway':
        return duration * 0.1  # Dummy factor for subway emissions

def eco_navigator(start, destination):
    try:
        # Step 1: Get real-time traffic data
        car_travel_time = get_real_time_traffic_data(start, destination)
        car_emissions = calculate_carbon_footprint('Car', car_travel_time)
        
        # Step 2: Get public transport options
        transport_options = get_public_transport_options(start, destination)
        
        # Step 3: Check carpooling options
        carpool_available = get_carpool_options(start, destination)
        
        # Plan routes with minimal carbon footprint
        best_option = {'mode': 'Car', 'emissions': car_emissions}
        
        # Compare with public transport options
        for option in transport_options:
            emissions = calculate_carbon_footprint(option['mode'], option['duration'])
            if emissions < best_option['emissions']:
                best_option = {'mode': option['mode'], 'emissions': emissions}

        # If carpool is available, assume it reduces emissions by 50%
        if carpool_available:
            carpool_emissions = car_emissions * 0.5
            if carpool_emissions < best_option['emissions']:
                best_option = {'mode': 'Carpool', 'emissions': carpool_emissions}
        
        return best_option

    except Exception as e:
        # Error handling
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    start_location = "A"
    destination_location = "B"
    
    best_route = eco_navigator(start_location, destination_location)
    if best_route:
        print(f"The best travel mode for minimal carbon footprint is: {best_route['mode']} with emissions: {best_route['emissions']} units")
    else:
        print("Failed to determine the best travel route.")
```

### Explanation
- **Data Retrieval**: The hypothetical functions `get_real_time_traffic_data`, `get_public_transport_options`, and `get_carpool_options` simulate getting data. In practice, these would connect to APIs or databases.
- **Error Handling**: A try-except block is used to handle potential errors gracefully.
- **Carbon Footprint Calculation**: The `calculate_carbon_footprint` function estimates emissions based on the travel mode and duration. This uses arbitrary emission factors for demonstration purposes.
- **Route Comparison**: The `eco_navigator` function compares different travel modes to find the one with the lowest emissions.
- **Main Functionality**: In the main block, we simulate a route planning scenario based on hypothetical data.

For a fully realized application, you would need access to real-time data APIs, integrate geographic information systems (GIS), and refine the carbon footprint calculation with accurate emission factors.