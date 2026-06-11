"""
Fundamental Analysis Module
Analyzes fundamental metrics of stocks
"""

import logging
from typing import Dict
from enum import Enum

logger = logging.getLogger(__name__)


class FundamentalRating(Enum):
    """Fundamental ratings"""
    EXCELLENT = "EXCELLENT"
    GOOD = "GOOD"
    FAIR = "FAIR"
    POOR = "POOR"
    VERY_POOR = "VERY POOR"


class FundamentalAnalyzer:
    """Perform fundamental analysis on stocks"""
    
    def __init__(self, config: dict):
        self.config = config
        self.fundamentals = config.get('fundamentals', {})
    
    def analyze(self, fundamentals: Dict, historical_price: float) -> Dict:
        """
        Perform complete fundamental analysis
        
        Args:
            fundamentals: Dictionary with fundamental metrics
            historical_price: Current stock price
            
        Returns:
            Dictionary with analysis and ratings
        """
        try:
            if not fundamentals:
                logger.warning("No fundamental data available")
                return {}
            
            analysis = {
                'valuation': self._analyze_valuation(fundamentals),
                'profitability': self._analyze_profitability(fundamentals),
                'financial_health': self._analyze_financial_health(fundamentals),
                'dividend': self._analyze_dividend(fundamentals),
                'growth': self._analyze_growth(fundamentals),
            }
            
            analysis['overall_rating'] = self._calculate_overall_rating(analysis)
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error in fundamental analysis: {str(e)}")
            return {}
    
    def _analyze_valuation(self, fundamentals: Dict) -> Dict:
        """Analyze valuation metrics"""
        try:
            pe_ratio = fundamentals.get('pe_ratio', 'N/A')
            forward_pe = fundamentals.get('forward_pe', 'N/A')
            pb_ratio = fundamentals.get('pb_ratio', 'N/A')
            pe_threshold = self.fundamentals.get('pe_ratio_threshold', 25)
            
            analysis = {
                'pe_ratio': pe_ratio,
                'forward_pe': forward_pe,
                'pb_ratio': pb_ratio,
            }
            
            # PE ratio evaluation
            if pe_ratio != 'N/A' and isinstance(pe_ratio, (int, float)):
                if pe_ratio < pe_threshold * 0.7:
                    analysis['pe_rating'] = 'UNDERVALUED'
                elif pe_ratio > pe_threshold * 1.3:
                    analysis['pe_rating'] = 'OVERVALUED'
                else:
                    analysis['pe_rating'] = 'FAIR'
            else:
                analysis['pe_rating'] = 'N/A'
            
            # PB ratio evaluation
            if pb_ratio != 'N/A' and isinstance(pb_ratio, (int, float)):
                if pb_ratio < 1:
                    analysis['pb_rating'] = 'UNDERVALUED'
                elif pb_ratio > 2:
                    analysis['pb_rating'] = 'OVERVALUED'
                else:
                    analysis['pb_rating'] = 'FAIR'
            else:
                analysis['pb_rating'] = 'N/A'
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing valuation: {str(e)}")
            return {}
    
    def _analyze_profitability(self, fundamentals: Dict) -> Dict:
        """Analyze profitability metrics"""
        try:
            roe = fundamentals.get('roe', 'N/A')
            roa = fundamentals.get('roa', 'N/A')
            net_margin = fundamentals.get('net_margin', 'N/A')
            operating_margin = fundamentals.get('operating_margin', 'N/A')
            eps = fundamentals.get('earnings_per_share', 'N/A')
            
            roe_threshold = self.fundamentals.get('roe_threshold', 15)
            
            analysis = {
                'roe': roe,
                'roa': roa,
                'net_margin': net_margin,
                'operating_margin': operating_margin,
                'eps': eps,
            }
            
            # ROE evaluation
            if roe != 'N/A' and isinstance(roe, (int, float)):
                if roe > roe_threshold:
                    analysis['roe_rating'] = 'EXCELLENT'
                elif roe > roe_threshold * 0.5:
                    analysis['roe_rating'] = 'GOOD'
                else:
                    analysis['roe_rating'] = 'POOR'
            else:
                analysis['roe_rating'] = 'N/A'
            
            # Net margin evaluation
            if net_margin != 'N/A' and isinstance(net_margin, (int, float)):
                margin_pct = net_margin * 100
                if margin_pct > 15:
                    analysis['margin_rating'] = 'EXCELLENT'
                elif margin_pct > 5:
                    analysis['margin_rating'] = 'GOOD'
                else:
                    analysis['margin_rating'] = 'FAIR'
            else:
                analysis['margin_rating'] = 'N/A'
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing profitability: {str(e)}")
            return {}
    
    def _analyze_financial_health(self, fundamentals: Dict) -> Dict:
        """Analyze financial health metrics"""
        try:
            debt_to_equity = fundamentals.get('debt_to_equity', 'N/A')
            current_ratio = fundamentals.get('current_ratio', 'N/A')
            quick_ratio = fundamentals.get('quick_ratio', 'N/A')
            de_threshold = self.fundamentals.get('debt_to_equity_threshold', 1.5)
            
            analysis = {
                'debt_to_equity': debt_to_equity,
                'current_ratio': current_ratio,
                'quick_ratio': quick_ratio,
            }
            
            # Debt to Equity evaluation
            if debt_to_equity != 'N/A' and isinstance(debt_to_equity, (int, float)):
                if debt_to_equity < de_threshold:
                    analysis['leverage_rating'] = 'HEALTHY'
                else:
                    analysis['leverage_rating'] = 'HIGH_LEVERAGE'
            else:
                analysis['leverage_rating'] = 'N/A'
            
            # Current ratio evaluation
            if current_ratio != 'N/A' and isinstance(current_ratio, (int, float)):
                if current_ratio > 1.5:
                    analysis['liquidity_rating'] = 'STRONG'
                elif current_ratio > 1:
                    analysis['liquidity_rating'] = 'ADEQUATE'
                else:
                    analysis['liquidity_rating'] = 'WEAK'
            else:
                analysis['liquidity_rating'] = 'N/A'
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing financial health: {str(e)}")
            return {}
    
    def _analyze_dividend(self, fundamentals: Dict) -> Dict:
        """Analyze dividend metrics"""
        try:
            dividend_yield = fundamentals.get('dividend_yield', 0)
            dividend_per_share = fundamentals.get('dividend_per_share', 0)
            payout_ratio = fundamentals.get('payout_ratio', 'N/A')
            div_threshold = self.fundamentals.get('dividend_yield_threshold', 2.5)
            
            analysis = {
                'dividend_yield': dividend_yield,
                'dividend_per_share': dividend_per_share,
                'payout_ratio': payout_ratio,
            }
            
            # Dividend yield evaluation
            if dividend_yield:
                if dividend_yield * 100 > div_threshold:
                    analysis['dividend_rating'] = 'HIGH_YIELD'
                elif dividend_yield > 0:
                    analysis['dividend_rating'] = 'GOOD'
                else:
                    analysis['dividend_rating'] = 'NO_DIVIDEND'
            else:
                analysis['dividend_rating'] = 'NO_DIVIDEND'
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing dividend: {str(e)}")
            return {}
    
    def _analyze_growth(self, fundamentals: Dict) -> Dict:
        """Analyze growth metrics"""
        try:
            earnings_growth = fundamentals.get('earnings_growth', 'N/A')
            revenue = fundamentals.get('revenue', 'N/A')
            revenue_per_share = fundamentals.get('revenue_per_share', 'N/A')
            
            analysis = {
                'earnings_growth': earnings_growth,
                'revenue': revenue,
                'revenue_per_share': revenue_per_share,
            }
            
            # Earnings growth evaluation
            if earnings_growth != 'N/A' and isinstance(earnings_growth, (int, float)):
                growth_pct = earnings_growth * 100
                if growth_pct > 20:
                    analysis['growth_rating'] = 'HIGH'
                elif growth_pct > 10:
                    analysis['growth_rating'] = 'MODERATE'
                elif growth_pct > 0:
                    analysis['growth_rating'] = 'LOW'
                else:
                    analysis['growth_rating'] = 'NEGATIVE'
            else:
                analysis['growth_rating'] = 'N/A'
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing growth: {str(e)}")
            return {}
    
    def _calculate_overall_rating(self, analysis: Dict) -> str:
        """Calculate overall fundamental rating"""
        try:
            score = 0
            max_score = 0
            
            # Valuation scoring
            valuation = analysis.get('valuation', {})
            if valuation.get('pe_rating') == 'UNDERVALUED':
                score += 2
                max_score += 2
            elif valuation.get('pe_rating') == 'FAIR':
                score += 1
                max_score += 2
            else:
                max_score += 2
            
            # Profitability scoring
            profitability = analysis.get('profitability', {})
            if profitability.get('roe_rating') == 'EXCELLENT':
                score += 2
                max_score += 2
            elif profitability.get('roe_rating') == 'GOOD':
                score += 1
                max_score += 2
            else:
                max_score += 2
            
            # Financial health scoring
            health = analysis.get('financial_health', {})
            if health.get('leverage_rating') == 'HEALTHY':
                score += 1.5
                max_score += 2
            elif health.get('liquidity_rating') == 'STRONG':
                score += 1.5
                max_score += 2
            else:
                max_score += 2
            
            # Dividend scoring
            dividend = analysis.get('dividend', {})
            if dividend.get('dividend_rating') in ['HIGH_YIELD', 'GOOD']:
                score += 1
                max_score += 1
            else:
                max_score += 1
            
            # Growth scoring
            growth = analysis.get('growth', {})
            if growth.get('growth_rating') in ['HIGH', 'MODERATE']:
                score += 2
                max_score += 2
            else:
                max_score += 2
            
            if max_score > 0:
                score_percentage = (score / max_score) * 100
                
                if score_percentage >= 80:
                    return FundamentalRating.EXCELLENT.value
                elif score_percentage >= 65:
                    return FundamentalRating.GOOD.value
                elif score_percentage >= 50:
                    return FundamentalRating.FAIR.value
                elif score_percentage >= 35:
                    return FundamentalRating.POOR.value
                else:
                    return FundamentalRating.VERY_POOR.value
            
            return FundamentalRating.FAIR.value
            
        except Exception as e:
            logger.error(f"Error calculating overall rating: {str(e)}")
            return FundamentalRating.FAIR.value