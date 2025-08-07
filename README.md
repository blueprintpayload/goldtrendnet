# GoldTrendNet

GoldTrendNet is a lightweight LSTM-based AI model designed to forecast short-term gold price trends using historical data. It serves as a foundation for building financial analytics tools in the precious metals domain.

## Features:
- Predict gold price 1–5 days ahead
- Visualize market trends
- Extendable to silver, platinum, and other assets
- Useful for Gold IRA comparison tools and investment calculators

## Example usage:
```python
from goldtrendnet import predict_gold_price

result = predict_gold_price(days=3)
print(f"Predicted gold price in 3 days: ${result}")