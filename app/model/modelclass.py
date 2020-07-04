import syft as sy

class Classifier(sy.Plan):
    def __init__(self):
        super(Classifier, self).__init__(id='encrypted-model')
        # Unpickle model here

    def forward(self, x):
        return x
