import torch
from model import GoldTrendNet

def predict_gold_price(days=3):
    model = GoldTrendNet()
    model.eval()
    dummy_input = torch.randn(1, 30, 1)  # Simulate 30 days of historical data
    with torch.no_grad():
        prediction = model(dummy_input)
    return round(prediction.item(), 2)