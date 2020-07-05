from app.utils.db.utils import connect_to_db
from app.utils.db.crud import authenticate_client
DB_URL = 'sqlite:///./syft-test.db'

from app.utils.pydantic_models.schemas import ClientBase

import syft as sy
from syft.grid.public_grid import PublicGridNetwork

import torch as th
hook = sy.TorchHook(th)
hook.local_worker.is_client_worker = False

from modelclass import Classifier

session = connect_to_db(DB_URL)

def get_inference(data, net):
    public_grid = PublicGridNetwork(hook, net)
    input_value = th.tensor(data['data'])
    model = Classifier()
    model.build(th.tensor([5., 3.]))

    public_grid.query_model_hosts(model.id, mpc=True)
    return {"result": public_grid.run_remote_inference(
        model.id,
        input_value,
        mpc=True
    )}

def login(username, password):
    client = ClientBase(username=username, password=password)
    if authenticate_client(session, client):
        return {"msg": "Success"}

    return {"msg": "Login Failed. Incorrect credentials"}
