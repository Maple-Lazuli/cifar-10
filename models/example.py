"""
Source: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

This is the example CNN taken from the tutorial for pytorch
"""
import datetime
import os
import shutil

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

from src.load_data import Loader


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1)  # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def verify_save_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


class Model:
    def __init__(self, name="example", save_dir="../results/example", lr=0.001, batch_size=1000):
        self.net = Net()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.net.parameters(), lr=lr)

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.net.to(device=self.device)

        self.name = f"{name}-{str(datetime.datetime.now())}"
        verify_save_dir(save_dir)
        self.save_dir = save_dir
        self.save_name = os.path.join(save_dir, self.name)
        self.lr = lr
        self.batch_size = batch_size

    def step(self, inputs, labels):
        inputs = inputs.to(self.device)
        labels = labels.to(self.device)
        self.optimizer.zero_grad()

        # forward + backward + optimize
        outputs = self.net(inputs)
        loss = self.criterion(outputs, labels)
        loss.backward()
        self.optimizer.step()

        return loss.item()

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
