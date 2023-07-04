def convert(feet,inches):
    """ Convert feet and inches to meters

    Args:
        feet,inches (integers or floats): takes two numbers
        
    Return:
        meters (float): feet and inches converted to meters 
    """
    try:
        meters = feet * 0.3048 + inches * 0.0254
        return meters
    except:
        return "Invalid input"
    
def parse(feet_inches):
    try:
        parts = feet_inches.split(" ")
        feet = float(parts[0])
        inches = float(parts[1])
        return {"feet": feet, "inches": inches}
    except:
        raise ValueError("Could not parse")