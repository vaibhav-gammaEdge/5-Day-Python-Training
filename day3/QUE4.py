def create_student_profile(**kwargs):
    profile = {}
    
    for key, value in kwargs.items():
        profile[key] = value
        
    return profile
