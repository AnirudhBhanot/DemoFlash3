import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import styles from './MichelinStrategicAnalysis.module.scss';
import useAssessmentStore from '../store/assessmentStore';

interface DynamicFrameworkAnalysis {
  framework_name: string;
  framework_id: string;
  category: string;
  analysis: any;
  fit_score: number;
  rationale: string[];
}

interface DynamicPhase1Data {
  executive_summary: string;
  frameworks_analysis: DynamicFrameworkAnalysis[];
  current_position_narrative: string;
  context: {
    industry: string;
    stage: string;
    key_challenges: string[];
    strategic_inflection: string;
  };
}

interface DynamicPhase1Response {
  startup_name: string;
  analysis_date: string;
  phase1: DynamicPhase1Data;
  frameworks_selected: string[];
}

export const MichelinDynamicAnalysis: React.FC = () => {
  const [activePhase, setActivePhase] = useState(1);
  const [phase1Data, setPhase1Data] = useState<DynamicPhase1Response | null>(null);
  const [phaseStatus, setPhaseStatus] = useState({
    phase1: 'idle' as 'idle' | 'loading' | 'completed' | 'error',
    phase2: 'idle' as 'idle' | 'loading' | 'completed' | 'error',
    phase3: 'idle' as 'idle' | 'loading' | 'completed' | 'error'
  });
  const [error, setError] = useState<string | null>(null);
  const [expandedFrameworks, setExpandedFrameworks] = useState<Set<string>>(new Set());

  const { data } = useAssessmentStore();

  const prepareStartupData = () => {
    return {
      startup_name: data.companyInfo?.companyName || 'Your Company',
      sector: data.companyInfo?.industry || 'saas_b2b',
      funding_stage: data.capital?.fundingStage || 'pre_seed',
      total_capital_raised_usd: data.capital?.totalFunding || 0,
      cash_on_hand_usd: data.capital?.cashOnHand || 0,
      monthly_burn_usd: data.capital?.monthlyBurn || 0,
      runway_months: data.capital?.runway || 12,
      team_size_full_time: data.people?.teamSize || 10,
      market_size_usd: data.market?.tamSize || 1000000000,
      market_growth_rate_annual: data.market?.marketGrowthRate || 20,
      competitor_count: data.market?.competitorCount || 10,
      market_share_percentage: data.market?.currentMarketShare || 0.1,
      customer_acquisition_cost_usd: data.market?.cac || 100,
      lifetime_value_usd: data.market?.ltv || 1000,
      monthly_active_users: data.market?.customerCount || 100,
      product_stage: data.advantage?.productStage || 'mvp',
      proprietary_tech: data.advantage?.proprietaryTech || false,
      patents_filed: data.advantage?.patentCount || 0,
      founders_industry_experience_years: data.people?.avgExperience || 5,
      b2b_or_b2c: data.companyInfo?.b2bOrB2c || 'B2B',
      key_challenges: [
        data.companyInfo?.mainChallenge || 'Achieving product-market fit',
        'Scaling customer acquisition',
        'Building competitive moat'
      ]
    };
  };

  const generatePhase1 = async () => {
    try {
      setPhaseStatus(prev => ({ ...prev, phase1: 'loading' }));
      setError(null);

      const response = await fetch('http://localhost:8001/api/michelin/dynamic/analyze/phase1', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ startup_data: prepareStartupData() }),
      });

      if (!response.ok) {
        throw new Error(`Phase 1 analysis failed: ${response.statusText}`);
      }

      const data = await response.json();
      setPhase1Data(data);
      setPhaseStatus(prev => ({ ...prev, phase1: 'completed' }));
    } catch (err) {
      console.error('Phase 1 analysis error:', err);
      setError(err instanceof Error ? err.message : 'Failed to generate Phase 1 analysis');
      setPhaseStatus(prev => ({ ...prev, phase1: 'error' }));
    }
  };

  const toggleFramework = (frameworkId: string) => {
    const newExpanded = new Set(expandedFrameworks);
    if (newExpanded.has(frameworkId)) {
      newExpanded.delete(frameworkId);
    } else {
      newExpanded.add(frameworkId);
    }
    setExpandedFrameworks(newExpanded);
  };

  const renderPhase1 = () => {
    if (!phase1Data) return null;
    const { phase1 } = phase1Data;

    return (
      <div className={styles.phaseContent}>
        <div className={styles.section}>
          <h3>Executive Summary</h3>
          <p className={styles.narrative}>{phase1.executive_summary}</p>
        </div>

        <div className={styles.section}>
          <h3>Strategic Context</h3>
          <div className={styles.contextGrid}>
            <div className={styles.contextItem}>
              <span>Industry:</span>
              <strong>{phase1.context.industry}</strong>
            </div>
            <div className={styles.contextItem}>
              <span>Stage:</span>
              <strong>{phase1.context.stage}</strong>
            </div>
            <div className={styles.contextItem}>
              <span>Strategic Inflection:</span>
              <strong>{phase1.context.strategic_inflection}</strong>
            </div>
          </div>
          <div className={styles.challenges}>
            <h4>Key Challenges:</h4>
            <ul>
              {phase1.context.key_challenges.map((challenge, idx) => (
                <li key={idx}>{challenge}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className={styles.section}>
          <h3>Framework Analysis</h3>
          {phase1.frameworks_analysis.map((fw, idx) => (
            <div key={fw.framework_id} className={styles.frameworkCard}>
              <div 
                className={styles.frameworkHeader} 
                onClick={() => toggleFramework(fw.framework_id)}
              >
                <div className={styles.frameworkInfo}>
                  <h4>{fw.framework_name}</h4>
                  <span className={styles.category}>{fw.category}</span>
                  <span className={styles.fitScore}>Fit Score: {fw.fit_score}%</span>
                </div>
                <span className={styles.toggle}>
                  {expandedFrameworks.has(fw.framework_id) ? '−' : '+'}
                </span>
              </div>
              
              {expandedFrameworks.has(fw.framework_id) && (
                <div className={styles.frameworkContent}>
                  <div className={styles.rationale}>
                    <h5>Why this framework:</h5>
                    <ul>
                      {fw.rationale.map((reason, ridx) => (
                        <li key={ridx}>{reason}</li>
                      ))}
                    </ul>
                  </div>
                  
                  <div className={styles.analysisContent}>
                    <h5>Analysis:</h5>
                    {typeof fw.analysis === 'object' ? (
                      <pre>{JSON.stringify(fw.analysis, null, 2)}</pre>
                    ) : (
                      <p>{fw.analysis}</p>
                    )}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className={styles.section}>
          <h3>Current Position Narrative</h3>
          <p className={styles.narrative}>{phase1.current_position_narrative}</p>
        </div>
      </div>
    );
  };

  return (
    <div className={styles.michelinAnalysis}>
      <div className={styles.header}>
        <h2>Dynamic Strategic Analysis</h2>
        <p>AI-powered framework selection based on your unique context</p>
      </div>

      <div className={styles.phaseNavigation}>
        <button
          className={`${styles.phaseButton} ${activePhase === 1 ? styles.active : ''}`}
          onClick={() => setActivePhase(1)}
        >
          <span className={styles.phaseNumber}>Phase 1</span>
          <span className={styles.phaseTitle}>Where Are We Now?</span>
        </button>
        <button
          className={`${styles.phaseButton} ${activePhase === 2 ? styles.active : ''}`}
          onClick={() => setActivePhase(2)}
          disabled={phaseStatus.phase1 !== 'completed'}
        >
          <span className={styles.phaseNumber}>Phase 2</span>
          <span className={styles.phaseTitle}>Where Should We Go?</span>
        </button>
        <button
          className={`${styles.phaseButton} ${activePhase === 3 ? styles.active : ''}`}
          onClick={() => setActivePhase(3)}
          disabled={phaseStatus.phase2 !== 'completed'}
        >
          <span className={styles.phaseNumber}>Phase 3</span>
          <span className={styles.phaseTitle}>How to Get There?</span>
        </button>
      </div>

      <AnimatePresence mode="wait">
        <motion.div
          key={activePhase}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -20 }}
          className={styles.phaseContainer}
        >
          {activePhase === 1 && (
            phaseStatus.phase1 === 'idle' ? (
              <div className={styles.phaseStart}>
                <h3>Ready to analyze your current position</h3>
                <p>We'll select the most relevant frameworks for your specific context</p>
                <button onClick={generatePhase1} className={styles.startButton}>
                  Start Analysis
                </button>
              </div>
            ) : phaseStatus.phase1 === 'loading' ? (
              <div className={styles.phaseLoading}>
                <div className={styles.spinner}></div>
                <h3>Analyzing Current Position...</h3>
                <p>Selecting optimal frameworks based on your context</p>
              </div>
            ) : phaseStatus.phase1 === 'error' ? (
              <div className={styles.phaseError}>
                <h3>Phase 1 Error</h3>
                <p>{error}</p>
                <button onClick={generatePhase1} className={styles.retryButton}>
                  Retry Analysis
                </button>
              </div>
            ) : (
              renderPhase1()
            )
          )}
        </motion.div>
      </AnimatePresence>
    </div>
  );
};