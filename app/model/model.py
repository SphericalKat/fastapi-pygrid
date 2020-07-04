import syft as sy
from syft.grid.public_grid import PublicGridNetwork

import torch as th
hook = sy.TorchHook(th)
hook.local_worker.is_client_worker = False

from modelclass import Classifier

def get_inference(data, net):
    public_grid = PublicGridNetwork(hook, net)
    input_value = th.tensor(data)
    model = Classifier()
    model.build(th.tensor([5., 3.]))

    public_grid.query_model_hosts(model.id, mpc=True)
    return {"result": public_grid.run_remote_inference(
        model.id,
        input_value,
        mpc=True
    )}
