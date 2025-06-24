#!/usr/bin/env python3
"""Fix None comparison issues in strategic_context_engine.py"""

import re

def fix_none_comparisons():
    with open('strategic_context_engine.py', 'r') as f:
        content = f.read()
    
    # Pattern to find potentially problematic get() calls with comparisons
    # This will match things like: data.get("key", 0) > value
    pattern = r'(data\.get\([^)]+\))\s*([><]=?)\s*(\d+|[a-zA-Z_]+(?:\.[a-zA-Z_]+)*)'
    
    def replace_func(match):
        get_call = match.group(1)
        operator = match.group(2)
        value = match.group(3)
        
        # Extract the variable name from get call
        var_match = re.search(r'get\("([^"]+)"', get_call)
        if var_match:
            var_name = var_match.group(1).replace('_', '')[:10]  # Short name
        else:
            var_name = "val"
        
        # Create safe comparison
        return f"({get_call} or 0) {operator} {value}"
    
    # Apply the fix
    fixed_content = re.sub(pattern, replace_func, content)
    
    # Write back
    with open('strategic_context_engine.py', 'w') as f:
        f.write(fixed_content)
    
    print("Fixed None comparison issues in strategic_context_engine.py")

if __name__ == "__main__":
    fix_none_comparisons()