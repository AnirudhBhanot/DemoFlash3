#!/usr/bin/env python3
"""Fix all NoneType comparison issues in strategic_context_engine.py"""

import re

def fix_none_comparisons():
    """Add None checks to all dict.get() comparisons"""
    
    with open('strategic_context_engine.py', 'r') as f:
        content = f.read()
    
    # Find all patterns like: if data.get("key", default) > value:
    pattern = r'if\s+data\.get\(([^)]+)\)\s*([><]=?)\s*([^:]+):'
    
    def replacement(match):
        get_expr = match.group(1)
        operator = match.group(2)
        value = match.group(3)
        
        # Extract the key name for variable naming
        key_match = re.search(r'"([^"]+)"', get_expr)
        if key_match:
            var_name = key_match.group(1).replace('_', '')[:15]
        else:
            var_name = "val"
        
        # Create safe comparison with None check
        return f'''val_{var_name} = data.get({get_expr})
        if val_{var_name} is not None and val_{var_name} {operator} {value}:'''
    
    # Apply the replacement
    modified = re.sub(pattern, replacement, content)
    
    # Also fix patterns without explicit None checks in other methods
    # Pattern: something.get(...) > value (not just data.get)
    pattern2 = r'if\s+(\w+)\.get\(([^)]+)\)\s*([><]=?)\s*([^:]+):'
    
    def replacement2(match):
        obj = match.group(1)
        get_expr = match.group(2)
        operator = match.group(3)
        value = match.group(4)
        
        # Don't replace if it's already fixed or has "is not None"
        if "is not None" in match.group(0):
            return match.group(0)
        
        # Extract key for variable name
        key_match = re.search(r'"([^"]+)"', get_expr)
        if key_match:
            var_name = key_match.group(1).replace('_', '')[:10]
        else:
            var_name = "temp"
            
        return f'''temp_{var_name} = {obj}.get({get_expr})
        if temp_{var_name} is not None and temp_{var_name} {operator} {value}:'''
    
    modified = re.sub(pattern2, replacement2, modified)
    
    # Write the fixed content
    with open('strategic_context_engine.py', 'w') as f:
        f.write(modified)
    
    print("Fixed NoneType comparison issues in strategic_context_engine.py")
    print("Restart the API server to apply changes.")

if __name__ == "__main__":
    fix_none_comparisons()