from cosmostat import Likelihood, get_dataset
from cosmostat.models.cpl import Params, model

params = Params(0, 0.3)


# TODO: Improve tests.


def test_wz():
    """"""
    wz = model.functions.wz
    wz_v = wz(0, params)
    assert wz_v == 0


def test_r_bao():
    """"""
    dataset = get_dataset("BAO")
    likelihood = Likelihood(model, dataset)
    chi_square_bao = likelihood.chi_square
    chi_square_bao_v = chi_square_bao(params)
    print(chi_square_bao_v)
    assert chi_square_bao_v == 0
