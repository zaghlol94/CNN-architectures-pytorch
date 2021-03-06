import torch
import torch.nn as nn


class LeNet(nn.Module):
    def __init__(self, in_channel, num_classes):
        super(LeNet, self).__init__()
        self.relu = nn.ReLU()
        self.pool = nn.AvgPool2d(kernel_size=(2, 2), stride=(2, 2))
        self.conv1 = nn.Conv2d(in_channels=in_channel, out_channels=6, kernel_size=(5, 5), stride=(1, 1), padding=(0, 0))
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=(5, 5), stride=(1, 1), padding=(0, 0))
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=120, kernel_size=(5, 5), stride=(1, 1), padding=(0, 0))
        self.fc1 = nn.Linear(120, 84)
        self.fc2 = nn.Linear(84, num_classes)

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.pool(x)
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = self.relu(self.conv3(x))  # num_of examples x 120 x 1 x 1
        x = x.reshape(x.shape[0], -1)  # num_of examples x 120
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# test
data = torch.randn(64, 3, 32, 32)
model = LeNet(in_channel=3, num_classes=10)
print(model(data).shape)
