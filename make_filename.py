# for leetcode problem
def make(title):
    
    num, name = title.split(".")
    name = name.strip().lower().replace(" ", "-")
    
    return f"lc-{num}-{name}.py"
    
    
    
