"""
主入口
"""
from backtest import run_backtest
from predict import run_predict

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--backtest', action='store_true', help='Run historical backtest')
    parser.add_argument('--predict', action='store_true', help='Run future prediction')
    parser.add_argument('--start', type=str, default='2010-01-01')
    parser.add_argument('--end', type=str, default='2026-06-10')
    parser.add_argument('--days', type=int, default=100)
    args = parser.parse_args()

    if args.backtest:
        run_backtest(args.start, args.end)
    if args.predict:
        run_predict(args.days)
