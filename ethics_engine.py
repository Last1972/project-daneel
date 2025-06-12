# Simple ethics engine for v0.5

def check_ethics(prompt: str) -> str:
    lowered = prompt.lower()
    
    if any(bad in lowered for bad in ["hack", "kill", "lie", "manipulate", "steal"]):
        return "refused"
    
    if any(ambiguous in lowered for ambiguous in ["secret", "bypass", "cheat"]):
        return "clarify_needed"
    
    return "allowed
