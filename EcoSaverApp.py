from energy_monitoring import EnergyMonitor
from analytics import EnergyAnalytics
from recommendations import EnergyRecommendations
from eco_score import calculate_eco_score
from cost_savings_calculator import calculate_cost_savings

# Initialize the energy monitor, analytics, and recommendations
monitor = EnergyMonitor()
analytics = EnergyAnalytics()
recommendations = EnergyRecommendations()

# Main application loop
while True:
    # Monitor real-time energy consumption
    consumption_data = monitor.monitor_energy()

    # Analyze consumption data
    consumption_patterns = analytics.analyze_consumption(consumption_data)

    # Generate intelligent recommendations
    recommended_actions = recommendations.generate_recommendations(consumption_patterns)

    # Calculate potential cost savings
    savings_estimate = calculate_cost_savings(recommended_actions)

    # Calculate the EcoScore
    eco_score = calculate_eco_score(consumption_data)

    # Display recommendations, cost savings, and EcoScore to the user
    print("Recommended Actions: ", recommended_actions)
    print("Estimated Cost Savings: $", savings_estimate)
    print("EcoScore: ", eco_score)
