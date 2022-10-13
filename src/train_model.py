import datetime
import json
import os

import numpy as np

from src.load_data import Loader
from models.example import Model


def save_training_performance(model, loss):
    save_dir = model.save_dir
    with open(os.path.join(save_dir, "training.json"), "w") as file_out:
        json.dump({
            "name": model.name,
            "time": str(datetime.datetime.now()),
            "lr": model.lr,
            "batch_size": model.batch_size,
            "loss": loss
        }, file_out)


class Trainer:
    def __init__(self, model):
        self.model = model

    def train(self, train_loader, epochs):

        total_loss = []
        for epoch in range(epochs):
            epoch_loss = []
            for batch_idx, data_target in enumerate(train_loader):
                data = data_target[0]
                target = data_target[1]
                loss = self.model.step(data, target)
                epoch_loss.append(loss)

            epoch_loss = np.mean(epoch_loss)
            print(f"Epoch {epoch+1} loss {epoch_loss}")
            total_loss.append(epoch_loss)

        save_training_performance(self.model, total_loss)

        model.save()


if __name__ == "__main__":

    model = Model()
    loader = Loader(batch_size=model.batch_size)

    trainer = Trainer(model)
    trainer.train(train_loader=loader.train_loader, epochs=5)
