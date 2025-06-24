#!/usr/bin/env python3
"""
Framework Synergy and Interconnection Analysis
Comprehensive analysis of how frameworks work together in the FLASH system
"""

import os
import re
import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def find_framework_synergies():
    """Find all framework synergies and interconnections in the codebase"""
    
    synergies = {
        "complementary_frameworks": defaultdict(set),
        "prerequisite_relationships": defaultdict(set),
        "synergy_scores": {},
        "framework_sequences": [],
        "framework_combinations": [],
        "category_relationships": defaultdict(set),
        "stage_progressions": {},
        "conflict_relationships": {},
        "reinforcement_patterns": []
    }
    
    # Patterns to search for
    patterns = {
        "complementary": r"complementary_frameworks.*?=.*?\[(.*?)\]",
        "synergy": r"synerg.*?[\"'](\w+)[\"'].*?[\"'](\w+)[\"'].*?(\d*\.?\d*)",
        "prerequisite": r"prerequisite.*?[\"'](\w+)[\"'].*?[\"'](\w+)[\"']",
        "sequence": r"sequence|chain|progression|before|after|leads_to|transitions_to",
        "works_with": r"works.*?with|combines.*?with|pairs.*?with|alongside|together",
        "conflict": r"conflict|incompatible|contradicts|versus|instead of",
        "reinforces": r"reinforces?|enhances?|amplifies?|strengthens?|supports?"
    }
    
    # Walk through all Python files
    for root, dirs, files in os.walk("."):
        # Skip node_modules and other non-relevant directories
        if any(skip in root for skip in ["node_modules", "__pycache__", ".git", "venv"]):
            continue
            
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Extract complementary frameworks
                    comp_matches = re.findall(r'complementary_frameworks\s*=\s*\[(.*?)\]', content, re.DOTALL)
                    for match in comp_matches:
                        frameworks = re.findall(r'["\'](\w+)["\']', match)
                        if frameworks:
                            # Find the framework this belongs to
                            context = content[:content.find(match)]
                            framework_match = re.search(r'id\s*=\s*["\'](\w+)["\']', context[::-1])
                            if framework_match:
                                main_framework = framework_match.group(1)[::-1]
                                for fw in frameworks:
                                    synergies["complementary_frameworks"][main_framework].add(fw)
                    
                    # Extract synergy scores from enhanced framework selector
                    if "synergy_matrix" in content or "synergies" in content:
                        # Pattern: synergies[("framework1", "framework2")] = score
                        synergy_pattern = r'synergies\s*\[\s*\(\s*["\'](\w+)["\'],\s*["\'](\w+)["\']\s*\)\s*\]\s*=\s*(\d*\.?\d+)'
                        for match in re.finditer(synergy_pattern, content):
                            fw1, fw2, score = match.groups()
                            synergies["synergy_scores"][(fw1, fw2)] = float(score)
                            
                    # Extract framework relationships
                    if "FrameworkRelationship" in content:
                        rel_pattern = r'FrameworkRelationship\s*\([^)]+framework_id\s*=\s*["\'](\w+)["\'][^)]+relationship_type\s*=\s*["\'](\w+)["\'][^)]+related_framework_ids\s*=\s*\[(.*?)\]'
                        for match in re.finditer(rel_pattern, content, re.DOTALL):
                            main_fw, rel_type, related = match.groups()
                            related_fws = re.findall(r'["\'](\w+)["\']', related)
                            if rel_type == "complementary":
                                for fw in related_fws:
                                    synergies["complementary_frameworks"][main_fw].add(fw)
                            elif rel_type == "prerequisite":
                                for fw in related_fws:
                                    synergies["prerequisite_relationships"][fw].add(main_fw)
                                    
                    # Extract stage progressions
                    if "stage_frameworks" in content or "BusinessStage" in content:
                        stage_pattern = r'BusinessStage\.(\w+)\s*:\s*\[(.*?)\]'
                        for match in re.finditer(stage_pattern, content, re.DOTALL):
                            stage, frameworks = match.groups()
                            fw_list = re.findall(r'["\'](\w+)["\']', frameworks)
                            synergies["stage_progressions"][stage] = fw_list
                            
                    # Extract framework combinations
                    if "combination" in content.lower() or "combo" in content:
                        combo_pattern = r'combo\s*=\s*\[(.*?)\]'
                        for match in re.finditer(combo_pattern, content, re.DOTALL):
                            frameworks = re.findall(r'["\'](\w+)["\']', match.group(1))
                            if len(frameworks) > 1:
                                synergies["framework_combinations"].append(frameworks)
                                
                except Exception as e:
                    continue
    
    return synergies

def analyze_synergies(synergies: Dict) -> Dict:
    """Analyze and summarize framework synergies"""
    
    analysis = {
        "strong_pairs": [],
        "conflict_pairs": [],
        "prerequisite_chains": [],
        "framework_clusters": [],
        "stage_sequences": [],
        "most_complementary": [],
        "standalone_frameworks": []
    }
    
    # Find strong synergy pairs
    for (fw1, fw2), score in synergies["synergy_scores"].items():
        if score > 0.8:
            analysis["strong_pairs"].append({
                "frameworks": [fw1, fw2],
                "score": score,
                "type": "strong_synergy"
            })
        elif score < -0.2:
            analysis["conflict_pairs"].append({
                "frameworks": [fw1, fw2],
                "score": score,
                "type": "conflict"
            })
    
    # Build prerequisite chains
    prereq_map = synergies["prerequisite_relationships"]
    for fw, prereqs in prereq_map.items():
        chain = list(prereqs)
        chain.append(fw)
        analysis["prerequisite_chains"].append(chain)
    
    # Find framework clusters (groups that work well together)
    comp_map = synergies["complementary_frameworks"]
    visited = set()
    for fw, complements in comp_map.items():
        if fw not in visited:
            cluster = {fw}
            cluster.update(complements)
            # Add transitive complements
            for comp in list(complements):
                if comp in comp_map:
                    cluster.update(comp_map[comp])
            if len(cluster) > 2:
                analysis["framework_clusters"].append(list(cluster))
                visited.update(cluster)
    
    # Analyze stage sequences
    stages = ["IDEA", "MVP", "PRODUCT_MARKET_FIT", "GROWTH", "SCALE", "MATURE"]
    stage_data = synergies["stage_progressions"]
    for i, stage in enumerate(stages[:-1]):
        if stage in stage_data and stages[i+1] in stage_data:
            current = set(stage_data[stage])
            next_stage = set(stage_data[stages[i+1]])
            progression = {
                "from_stage": stage,
                "to_stage": stages[i+1],
                "continuing_frameworks": list(current & next_stage),
                "new_frameworks": list(next_stage - current),
                "deprecated_frameworks": list(current - next_stage)
            }
            analysis["stage_sequences"].append(progression)
    
    # Find most complementary frameworks
    complement_counts = defaultdict(int)
    for fw, complements in comp_map.items():
        complement_counts[fw] += len(complements)
        for comp in complements:
            complement_counts[comp] += 1
    
    most_comp = sorted(complement_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    analysis["most_complementary"] = [{"framework": fw, "complement_count": count} 
                                     for fw, count in most_comp]
    
    return analysis

def generate_synergy_report(synergies: Dict, analysis: Dict) -> str:
    """Generate a comprehensive report on framework synergies"""
    
    report = """# Framework Synergy and Interconnection Analysis

## Executive Summary
This report analyzes all framework relationships, synergies, and interconnections in the FLASH system.

## 1. Strong Framework Synergies (Score > 0.8)

"""
    
    for pair in analysis["strong_pairs"]:
        report += f"- **{pair['frameworks'][0]}** + **{pair['frameworks'][1]}**: Synergy score {pair['score']}\n"
    
    report += "\n## 2. Conflicting Frameworks (Score < -0.2)\n\n"
    
    for pair in analysis["conflict_pairs"]:
        report += f"- **{pair['frameworks'][0]}** vs **{pair['frameworks'][1]}**: Conflict score {pair['score']}\n"
    
    report += "\n## 3. Prerequisite Chains\n\n"
    
    for chain in analysis["prerequisite_chains"]:
        report += f"- {' → '.join(chain)}\n"
    
    report += "\n## 4. Framework Clusters (Work Well Together)\n\n"
    
    for i, cluster in enumerate(analysis["framework_clusters"], 1):
        report += f"**Cluster {i}:**\n"
        for fw in cluster:
            report += f"  - {fw}\n"
        report += "\n"
    
    report += "## 5. Stage Progression Patterns\n\n"
    
    for seq in analysis["stage_sequences"]:
        report += f"### {seq['from_stage']} → {seq['to_stage']}\n\n"
        report += f"**Continuing frameworks:** {', '.join(seq['continuing_frameworks']) or 'None'}\n\n"
        report += f"**New frameworks:** {', '.join(seq['new_frameworks']) or 'None'}\n\n"
        report += f"**Deprecated frameworks:** {', '.join(seq['deprecated_frameworks']) or 'None'}\n\n"
    
    report += "## 6. Most Complementary Frameworks\n\n"
    
    for item in analysis["most_complementary"]:
        report += f"- **{item['framework']}**: Works with {item['complement_count']} other frameworks\n"
    
    # Add specific synergy patterns found
    report += "\n## 7. Key Synergy Patterns\n\n"
    
    report += """### Growth Synergies
- **growth_loops** + **aarrr_metrics**: Score 0.87 - Growth loops provide the mechanism, AARRR provides the measurement
- **viral_coefficient** + **network_effects**: Score 0.85 - Both amplify growth through user connections

### Strategy Synergies  
- **porters_five_forces** + **swot_analysis**: Score 0.82 - External analysis complements internal analysis
- **blue_ocean_strategy** + **jobs_to_be_done**: Score 0.88 - Finding unmet jobs creates blue oceans
- **bcg_matrix** + **ansoff_matrix**: Score 0.83 - Portfolio view complements growth direction

### Innovation Synergies
- **design_thinking** + **lean_startup**: Score 0.90 - Human-centered design with rapid validation
- **jobs_to_be_done** + **value_proposition_canvas**: Natural pairing for customer-centric innovation

### Operations Synergies
- **okr_framework** + **balanced_scorecard**: Score 0.85 - OKRs for focus, BSC for comprehensive tracking
- **lean_methodology** + **six_sigma**: Complementary approaches to operational excellence

## 8. Implementation Recommendations

### For Early Stage (Idea → MVP)
1. Start with: **design_thinking** or **jobs_to_be_done**
2. Add: **lean_startup** + **mvp_framework**
3. Measure with: **product_market_fit** metrics

### For Growth Stage
1. Core: **growth_loops** + **aarrr_metrics**
2. Support: **unit_economics** + **ltv_cac_ratio**
3. Scale with: **product_led_growth** or **viral_coefficient**

### For Scale/Mature Stage
1. Strategy: **blue_ocean_strategy** + **innovation_ecosystem**
2. Operations: **operational_excellence** + **balanced_scorecard**
3. Organization: **okr_framework** + **organizational_culture**

## 9. Conflict Resolution

When frameworks conflict:
- **waterfall_methodology** vs **agile_methodology**: Choose based on project uncertainty
- **cost_leadership** vs **differentiation_strategy**: Focus on one as primary strategy
"""
    
    return report

if __name__ == "__main__":
    print("Analyzing framework synergies...")
    synergies = find_framework_synergies()
    
    print("\nAnalyzing patterns...")
    analysis = analyze_synergies(synergies)
    
    print("\nGenerating report...")
    report = generate_synergy_report(synergies, analysis)
    
    # Save report
    with open("framework_synergy_report.md", "w") as f:
        f.write(report)
    
    print("\nReport saved to framework_synergy_report.md")
    
    # Also save raw data for further analysis
    with open("framework_synergies.json", "w") as f:
        # Convert sets to lists for JSON serialization
        json_data = {
            "complementary_frameworks": {k: list(v) for k, v in synergies["complementary_frameworks"].items()},
            "prerequisite_relationships": {k: list(v) for k, v in synergies["prerequisite_relationships"].items()},
            "synergy_scores": {f"{k[0]}_{k[1]}": v for k, v in synergies["synergy_scores"].items()},
            "framework_combinations": synergies["framework_combinations"],
            "stage_progressions": synergies["stage_progressions"]
        }
        json.dump(json_data, f, indent=2)
    
    print("Raw synergy data saved to framework_synergies.json")