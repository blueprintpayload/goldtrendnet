import torch
import torch.nn as nn

class GoldTrendNet(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2):
        super(GoldTrendNet, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out