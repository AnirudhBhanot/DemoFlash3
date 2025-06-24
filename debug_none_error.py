#!/usr/bin/env python3
"""Debug the NoneType comparison error"""

import asyncio
from strategic_context_engine import StrategicContextEngine

async def test_context_building():
    """Test context building with minimal data"""
    engine = StrategicContextEngine()
    
    test_data = {
        "startup_name": "TestCo",
        "stage": "seed",
        "sector": "saas_b2b",
        "team_size": 10,
        "revenue": 100000,
        "growth_rate": 50,
        "key_challenges": ["unit economics"]
    }
    
    try:
        context = await engine.build_company_context(test_data)
        print("✅ Context built successfully!")
        print(f"Company: {context.company_name}")
        print(f"Industry: {context.industry}")
        print(f"Stage: {context.stage}")
    except Exception as e:
        print(f"❌ Error building context: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_context_building())