"""
Reference: https://towardsdatascience.com/confusion-matrix-for-your-multi-class-machine-learning-model-ff9aa3bf7826
"""

import datetime
import json
import os
import numpy as np


from src.load_data import Loader
from models.example import Model


def save_performance(model, loss):
    save_dir = model.save_dir
    with open(os.path.join(save_dir, "training.json"), "w") as file_out:
        json.dump({
            "name": model.name,
            "time": str(datetime.datetime.now()),
            "lr": model.lr,
            "batch_size": model.batch_size,
            "loss": loss
        }, file_out)


class Evaluator:
    def __init__(self, model):
        self.model = model

    def evalute_train(self, loader):
        classes = loader.classes


        training_evaluation = {
            "confusion_matrix": np.ndarray((len(classes), len(classes))),
            "Classes": classes,
            "Accuracy": [],
            "Classification Error": [],
            "Precision": [],
            "Recall": [],
            "Specificity": [],
            "F1-Score":[]
        }



if __name__ == "__main__":

    model = Model()
    loader = Loader(batch_size=model.batch_size)

    evaluator = Evaluator(model)
    evaluator.evaluate(train_loader=loader.train_loader, epochs=5)
