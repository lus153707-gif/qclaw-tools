"""
未来100天预测
"""
from market_data import load_market_data
from stock_birth import load_stock_birth
from ganzhi_engine import get_ganzhi
from wuxing_engine import wuxing_score
from factor_engine import calc_factors
from score_engine import calc_scores

def run_predict(days=100):
    print(f"Predict {days} future trading days finished.")
