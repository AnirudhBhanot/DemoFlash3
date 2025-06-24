#!/usr/bin/env python3
"""
Merge generated framework tags with existing database
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_tags_database import create_framework_tags_database
from generated_framework_tags import GENERATED_TAGS

def merge_tags():
    """Merge generated tags with existing tags"""
    
    # Get existing tags
    existing_tags = create_framework_tags_database()
    print(f"Existing tags: {len(existing_tags)}")
    
    # Merge with generated tags
    merged_tags = existing_tags.copy()
    
    # Add generated tags that don't exist
    added_count = 0
    for framework_id, tags in GENERATED_TAGS.items():
        if framework_id not in merged_tags:
            merged_tags[framework_id] = tags
            added_count += 1
    
    print(f"Added {added_count} new tags")
    print(f"Total tags after merge: {len(merged_tags)}")
    
    return merged_tags

def write_merged_database(merged_tags):
    """Write the merged tags back to the database file"""
    
    # Read the current file
    with open("framework_intelligence/framework_tags_database.py", "r") as f:
        lines = f.readlines()
    
    # Find where to insert the new tags
    insert_line = None
    for i, line in enumerate(lines):
        if "return tags_db" in line:
            insert_line = i
            break
    
    if insert_line is None:
        print("Error: Could not find insertion point")
        return
    
    # Generate code for new tags
    new_tag_code = []
    
    # Get existing framework ids
    existing_ids = create_framework_tags_database().keys()
    
    for framework_id, tags in sorted(GENERATED_TAGS.items()):
        if framework_id not in existing_ids:
            new_tag_code.append(f"\n    # {framework_id.replace('_', ' ').title()}\n")
            new_tag_code.append(f'    tags_db["{framework_id}"] = FrameworkTags(\n')
            new_tag_code.append(f'        temporal_stages=[{", ".join(f"TemporalStage.{s}" for s in tags.temporal_stages)}],\n')
            new_tag_code.append(f'        problem_archetypes=[{", ".join(f"ProblemArchetype.{p}" for p in tags.problem_archetypes)}],\n')
            new_tag_code.append(f'        decision_contexts=[{", ".join(f"DecisionContext.{d}" for d in tags.decision_contexts)}],\n')
            new_tag_code.append(f'        data_requirements=[{", ".join(f"DataRequirement.{r}" for r in tags.data_requirements)}],\n')
            new_tag_code.append(f'        complexity_tier=ComplexityTier.{tags.complexity_tier},\n')
            new_tag_code.append(f'        outcome_types=[{", ".join(f"OutcomeType.{o}" for o in tags.outcome_types)}],\n')
            new_tag_code.append(f'        industry_contexts=[{", ".join(f"IndustryContext.{i}" for i in tags.industry_contexts)}],\n')
            new_tag_code.append(f'        typical_users={tags.typical_users},\n')
            new_tag_code.append(f'        team_size_min={tags.team_size_min},\n')
            new_tag_code.append(f'        team_size_max={tags.team_size_max},\n')
            new_tag_code.append(f'        time_to_value_days={tags.time_to_value_days},\n')
            new_tag_code.append(f'        durability_months={tags.durability_months},\n')
            new_tag_code.append(f'        ease_of_use={tags.ease_of_use},\n')
            new_tag_code.append(f'        actionability={tags.actionability},\n')
            new_tag_code.append(f'        accuracy={tags.accuracy},\n')
            new_tag_code.append(f'        strategic_impact={tags.strategic_impact},\n')
            new_tag_code.append(f'        requires_facilitator={tags.requires_facilitator},\n')
            new_tag_code.append(f'        requires_software={tags.requires_software},\n')
            new_tag_code.append(f'        has_variants={tags.has_variants},\n')
            new_tag_code.append(f'        keywords={{{", ".join(f'"{k}"' for k in sorted(tags.keywords))}}}\n')
            new_tag_code.append('    )\n')
    
    # Insert the new code
    lines[insert_line:insert_line] = new_tag_code
    
    # Write back
    with open("framework_intelligence/framework_tags_database_merged.py", "w") as f:
        f.writelines(lines)
    
    print(f"Merged database written to framework_tags_database_merged.py")

if __name__ == "__main__":
    merged_tags = merge_tags()
    write_merged_database(merged_tags)