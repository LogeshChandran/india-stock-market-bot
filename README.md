# India Stock Market Analysis Bot

A comprehensive Python-based bot for analyzing Indian stocks using technical indicators, fundamental analysis, and news sentiment. Runs on GitHub Actions and generates detailed reports with visualizations and notifications.

## Features

- **Technical Analysis**
  - Moving Averages (SMA, EMA)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands
  - Stochastic Oscillator
  - ATR (Average True Range)
  - Support & Resistance Levels

- **Fundamental Analysis**
  - P/E Ratio
  - Earnings Per Share (EPS)
  - Dividend Yield
  - Market Cap
  - Book Value
  - ROE (Return on Equity)
  - Debt-to-Equity Ratio

- **News & Sentiment Analysis**
  - Real-time news fetching
  - Sentiment analysis
  - News scoring

- **Report Generation**
  - HTML reports with interactive charts
  - PDF exports
  - Data visualizations
  - Buy/Sell/Hold recommendations

- **Notifications**
  - Email alerts
  - Slack notifications
  - GitHub Issues integration

## Installation

```bash
git clone https://github.com/LogeshChandran/india-stock-market-bot.git
cd india-stock-market-bot
pip install -r requirements.txt
```

## Configuration

See `config.yaml` for configuration options.

## Running Locally

```bash
python main.py --stocks RELIANCE INFY TCS
```

## GitHub Actions

The bot runs automatically on a schedule. See `.github/workflows/` for workflow configurations.

## Output

- Reports are generated in `reports/` directory
- Visualizations are stored in `reports/visualizations/`
- Logs are maintained in `logs/` directory