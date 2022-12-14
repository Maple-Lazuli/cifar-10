
import os

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

from src.load_data import Loader


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(32 * 32 * 3, 200)
        self.fc2 = nn.Linear(200, 200)
        self.fc3= nn.Linear(200, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def verify_save_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


class Model:
    def __init__(self, name="mlp", save_dir="../results/", lr=0.001, batch_size=1000):
        self.net = Net()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.net.parameters(), lr=lr)

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.net.to(device=self.device)

        self.name = name
        verify_save_dir(os.path.join(save_dir, name))

        self.save_dir = os.path.join(save_dir, name)
        self.save_name = os.path.join(self.save_dir, f"{self.name}.pth")
        self.lr = lr
        self.batch_size = batch_size

    def step(self, inputs, labels):
        inputs = inputs.view(-1, 32*32*3)
        inputs = inputs.to(self.device)
        labels = labels.to(self.device)
        self.optimizer.zero_grad()

        # forward + backward + optimize
        outputs = self.net(inputs)
        loss = self.criterion(outputs, labels)
        loss.backward()
        self.optimizer.step()

        return loss.item()

    def loss(self, inputs, labels):
        inputs = inputs.view(-1, 32*32*3)
        inputs = inputs.to(self.device)
        labels = labels.to(self.device)
        outputs = self.net(inputs)
        loss = self.criterion(outputs, labels)
        return loss.item()

    def classify(self, inputs):
        inputs = inputs.view(-1, 32*32*3)
        inputs = inputs.to(self.device)
        return self.net(inputs)

    def save(self):
        torch.save(self.net.state_dict(), self.save_name)

    def load(self):
        self.net.load_state_dict(torch.load(self.save_name))


if __name__ == "__main__":
    model = Model()
    loader = Loader(batch_size=model.batch_size)

    total_loss = []
    for i, data in enumerate(loader.train_loader, 0):
        loss = model.step(data[0], data[1])
        total_loss.append(loss)
        print(loss)

    print(f"Epoch Loss: {np.mean(total_loss)}")
