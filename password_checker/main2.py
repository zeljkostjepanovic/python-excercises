def strength(password):
    results = {}
    
    if len(password) >= 8:
        results["Length"] = "Pass"
    else:
        results["Length"] = "Fail"
    
    upper_lower = []
    
    for char in password:
        if char.isupper():
            upper_lower.append("upper")
        elif char.islower():
            upper_lower.append("lower")
        else:
            pass
        
    if all([x in upper_lower for x in ["lower","upper"]]):
        results["Upper_Lower"] = "Pass"
    else:
        results["Upper_Lower"] = "Fail"
        
    
    digits = []
    for char in password:
        if char.isdigit():
            digits.append("digit")
        else:
            digits.append("nodigit")

    if all([x in digits for x in ["digit","nodigit"]]):
        results["Digits"] = "Pass"
    else:
        results["Digits"] = "Fail"
    
    if "Fail" in results.values():
        return "Weak Password"
    else:
        return "Strong Password"
    
    
