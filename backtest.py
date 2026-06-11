"""
历史回测引擎
"""
from market_data import load_market_data
from stock_birth import load_stock_birth
from ganzhi_engine import get_ganzhi
from wuxing_engine import wuxing_score
from factor_engine import calc_factors
from score_engine import calc_scores

def run_backtest(start_date, end_date):
    market_data = load_market_data(start_date, end_date)
    stock_data = load_stock_birth()
    market_data, stock_data = calc_factors(market_data, stock_data)
    market_data, stock_data = calc_scores(market_data, stock_data)
    print("Backtest finished.")
