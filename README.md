# GoldTrendNet

**GoldTrendNet** is an experimental AI project for forecasting market trends, combining multiple models: one based on historical price data (LSTM), and another based on textual signal interpretation (Replicate). The goal is to provide flexible tools for evaluating gold price movements and broader market sentiment.

---

## 📈 Model 1: Gold Price Forecasting (LSTM)

This model is trained on historical gold price data and uses a Long Short-Term Memory (LSTM) neural network to predict future values.

### 🔧 Usage

```python
from keras.models import load_model
import numpy as np

model = load_model('gold_price_model.h5')
input_data = np.array([[...]])
prediction = model.predict(input_data)
print(prediction)
