import models.lenet as lenet
import models.mlp as mlp
import models.cnn1 as cnn1
import models.cnn2 as cnn2
import models.cnn1 as cnn3


def get_model(name):
    if name == "lenet":
        return lenet.Model
    elif name == "mlp":
        return mlp.Model
    elif name == "cnn1":
        return cnn1.Model
    elif name == "cnn2":
        return cnn2.Model
    elif name == "cnn3":
        return cnn3.Model

