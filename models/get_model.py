import models.example as example
import models.lenet as lenet
import models.mlp as mlp
import models.resnet as resnet


def get_model(name):
    if name == "example":
        return example.Model
    elif name == "lenet":
        return lenet.Model
    elif name == "mlp":
        return mlp.Model
    # elif name == "resnet":
    #     return resnet.Model
