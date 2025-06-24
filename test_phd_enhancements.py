#!/usr/bin/env python3
"""
Test script for PhD Enhancement Integration
"""

import json
import requests
import asyncio
from datetime import datetime


def create_test_startup_data():
    """Create complete startup data for testing"""
    return {
        'startup_name': 'FLASH Platform',
        'sector': 'software',
        'industry': 'B2B SaaS/AI/ML',
        'product_description': 'AI-powered startup success prediction platform using ML models',
        'business_model': 'B2B SaaS subscription',
        'funding_stage': 'seed',
        'founders_count': 2,
        'total_capital_raised_usd': 2000000,
        'cash_on_hand_usd': 1200000,
        'monthly_burn_usd': 100000,
        'runway_months': 12,
        'team_size_full_time': 25,
        'market_size_usd': 50000000000,
        'market_growth_rate_annual': 25.0,
        'competitor_count': 10,
        'market_share_percentage': 0.5,
        'customer_acquisition_cost_usd': 1000.0,
        'lifetime_value_usd': 10000.0,
        'monthly_active_users': 5000,
        'product_stage': 'growth',
        'proprietary_tech': True,
        'patents_filed': 2,
        'founders_industry_experience_years': 10,
        'b2b_or_b2c': 'b2b',
        'burn_rate_usd': 100000.0,
        'investor_tier_primary': 'tier_2',
        'geographical_focus': 'global',
        'revenue_growth_rate': 150.0,
        'gross_margin': 75.0,
        'net_promoter_score': 45.0,
        'technology_readiness_level': 7,
        'has_strategic_partnerships': True,
        'customer_concentration': 15.0,
        'annual_revenue_usd': 1000000.0,
        'customer_count': 100
    }


def test_enhanced_framework_selection():
    """Test enhanced framework selection API"""
    print("\n" + "="*60)
    print("Testing Enhanced Framework Selection with PhD Enhancements")
    print("="*60)
    
    # Create simpler test data for framework selection
    test_data = {
        'startup_name': 'FLASH Platform',
        'sector': 'software',
        'stage': 'seed',
        'team_size': 25,
        'annual_revenue_usd': 1000000,
        'monthly_burn_usd': 100000,
        'cash_on_hand_usd': 1200000,
        'market_size_usd': 50000000000,
        'market_growth_rate_annual': 25,
        'customer_count': 100,
        'monthly_active_users': 5000,
        'lifetime_value_usd': 10000,
        'customer_acquisition_cost_usd': 1000,
        'product_stage': 'growth',
        'team_size_full_time': 25,
        'founders_industry_experience_years': 10,
        'geographical_focus': 'global',
        'proprietary_tech': True,
        'patents_filed': 2,
        'competitor_count': 10,
        'market_share_percentage': 0.5,
        'runway_months': 12,
        'max_frameworks': 3
    }
    
    try:
        response = requests.post(
            'http://localhost:8001/api/frameworks/enhanced/select',
            json=test_data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ API Call Successful")
            print(f"Methodology: {result.get('methodology', 'Unknown')}")
            print(f"Success: {result.get('success', False)}")
            print(f"Frameworks selected: {len(result.get('frameworks', []))}")
            
            # Check for PhD enhancements in the response
            frameworks = result.get('frameworks', [])
            phd_found = False
            
            for i, fw in enumerate(frameworks):
                print(f"\n📊 Framework {i+1}: {fw.get('name', fw.get('id', 'Unknown'))}")
                print(f"   Category: {fw.get('category', 'N/A')}")
                print(f"   Fit Score: {fw.get('fit_score', 0)}")
                
                # Check for academic insights (PhD enhancements)
                if 'customizations' in fw and 'academic_insights' in fw['customizations']:
                    print("   ✓ Academic insights present")
                    phd_found = True
                    
            if phd_found:
                print("\n✅ PhD Enhancements detected in response")
            else:
                print("\n⚠️  PhD Enhancements not visible in response (may be internal)")
                
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Details: {response.text[:500]}")
            
    except Exception as e:
        print(f"❌ Request failed: {str(e)}")


def test_michelin_enhanced_phase1():
    """Test Michelin Enhanced API Phase 1"""
    print("\n" + "="*60)
    print("Testing Michelin Enhanced Phase 1 with PhD Enhancements")
    print("="*60)
    
    startup_data = create_test_startup_data()
    
    try:
        response = requests.post(
            'http://localhost:8001/api/michelin/enhanced/analyze/phase1',
            json={'startup_data': startup_data},
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Michelin Enhanced Phase 1 API Call Successful")
            
            phase1 = result.get('phase1', {})
            
            # Check for framework interconnections (PhD feature)
            if 'framework_interconnections' in phase1:
                print("\n✅ Framework Interconnections Present (PhD Enhancement)")
                interconnections = phase1['framework_interconnections']
                print(f"   Primary Framework: {interconnections.get('primary_framework', 'N/A')}")
                
                if 'interconnections' in interconnections:
                    conn = interconnections['interconnections']
                    if 'synergistic' in conn and conn['synergistic']:
                        print(f"   Synergistic frameworks: {conn['synergistic']}")
                    if 'complementary' in conn and conn['complementary']:
                        print(f"   Complementary frameworks: {conn['complementary']}")
                    if 'conflicts' in conn and conn['conflicts']:
                        print(f"   Potential conflicts: {conn['conflicts']}")
            else:
                print("\n⚠️  Framework Interconnections not found in response")
            
            # Check BCG Matrix analysis
            if 'bcg_matrix_analysis' in phase1:
                bcg = phase1['bcg_matrix_analysis']
                print(f"\nBCG Matrix Position: {bcg.get('position', 'Unknown')}")
                print(f"Market Growth: {bcg.get('market_growth_rate', 'N/A')}")
                print(f"Market Share: {bcg.get('relative_market_share', 'N/A')}")
                
            # Check for strategic priorities
            if 'swot_analysis' in phase1:
                swot = phase1['swot_analysis']
                if 'strategic_priorities' in swot:
                    print(f"\nStrategic Priorities: {len(swot['strategic_priorities'])}")
                    
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Details: {response.text[:500]}")
            
    except Exception as e:
        print(f"❌ Request failed: {str(e)}")


def test_michelin_phase2_ml_opportunities():
    """Test Michelin Phase 2 for ML/AI opportunities"""
    print("\n" + "="*60)
    print("Testing Michelin Phase 2 - ML/AI Opportunities")
    print("="*60)
    
    startup_data = create_test_startup_data()
    
    # First get Phase 1 data
    print("Getting Phase 1 data first...")
    try:
        phase1_response = requests.post(
            'http://localhost:8001/api/michelin/enhanced/analyze/phase1',
            json={'startup_data': startup_data},
            timeout=60
        )
        
        if phase1_response.status_code != 200:
            print("❌ Phase 1 failed, cannot test Phase 2")
            return
            
        phase1_data = phase1_response.json()['phase1']
        
        # Now test Phase 2
        phase2_request = {
            'startup_data': startup_data,
            'phase1_insights': phase1_data
        }
        
        response = requests.post(
            'http://localhost:8001/api/michelin/enhanced/analyze/phase2',
            json=phase2_request,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Michelin Phase 2 API Call Successful")
            
            phase2 = result.get('phase2', {})
            
            # Check for ML/AI opportunities (PhD feature)
            if 'ml_ai_opportunities' in phase2:
                print("\n✅ ML/AI Opportunities Present (PhD Enhancement)")
                ml_opps = phase2['ml_ai_opportunities']
                
                if 'ml_applications' in ml_opps:
                    apps = ml_opps['ml_applications']
                    print(f"   ML Applications found: {len(apps)}")
                    for app in apps[:2]:  # Show first 2
                        print(f"\n   📊 Framework: {app.get('framework', 'N/A')}")
                        print(f"      Opportunity: {app.get('ml_opportunity', 'N/A')}")
                        print(f"      Expected Improvement: {app.get('expected_improvement', 'N/A')}")
            else:
                print("\n⚠️  ML/AI Opportunities not found in response")
                
        else:
            print(f"❌ Phase 2 API Error: {response.status_code}")
            print(f"Details: {response.text[:500]}")
            
    except Exception as e:
        print(f"❌ Request failed: {str(e)}")


def main():
    """Run all tests"""
    print(f"\nStarting PhD Enhancement Tests - {datetime.now().isoformat()}")
    
    # Check if server is running
    try:
        health = requests.get('http://localhost:8001/health')
        if health.status_code == 200:
            print("✅ API Server is healthy")
        else:
            print("❌ API Server health check failed")
            return
    except:
        print("❌ API Server is not running. Please start it first.")
        return
    
    # Run tests
    test_enhanced_framework_selection()
    test_michelin_enhanced_phase1()
    test_michelin_phase2_ml_opportunities()
    
    print("\n" + "="*60)
    print("PhD Enhancement Testing Complete")
    print("="*60)


if __name__ == "__main__":
    main()