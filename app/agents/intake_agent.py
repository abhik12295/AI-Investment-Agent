def suggest_strategy(horizon, risk):
    if horizon in ["1+ Year", "Months"] and risk in ["Low", "Medium"]:
        return "Long-term"
    
    elif horizon in ["Days", "Weeks"] and risk == "High":
        return "Swing"
    
    return "Hybrid"