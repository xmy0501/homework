import allure
import pytest

from test_pytest.core.calc import Calc
@allure.feature('乘法')
class TestCalcMul():

    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    # 乘法：乘数为整数
    @allure.feature('整数')
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
        [10000000000000000, 1, 10000000000000000],
        [5000000000000000, 2, 10000000000000000]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 乘数为浮点数
    @allure.feature('浮点数')
    @pytest.mark.parametrize('a, b, c',[
        [0.1, 1, 0.1],
        [-0.1, 1, -0.1],
        [0.1, -1, -0.1],
        [0.5, 0.2, 0.1],
        [1, 0.1, 0.1],
        [0, 0.5, 0],
        [0, -0.5, 0],
        [0.5, 0, 0],
        [-0.5, 0, 0],
        [0.00000000000001, 0.1, 0.000000000000001],
        [0.00000000000001, -0.1, -0.000000000000001],
        [-0.00000000000001, -0.1, 0.000000000000001]
    ])
    def test_mul2(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 乘法结果超出最多展示位数
    @allure.feature('运行结果超长')
    @pytest.mark.parametrize('a, b, c', [
        [10000000000000000, 10, 1e17],
        [0.1, 0.0000000000000001, 1e-17],
        [10000000000000000, -10, -1e17],
        [0.1, -0.0000000000000001, -1e-17],
        [-10000000000000000, -10, 1e17],
        [-0.1, -0.0000000000000001, 1e-17]
    ])
    def test_div(self, a, b, c):
        assert self.calc.mul(a, b) == c


    # 除法：除数和被除数为整数
    @allure.feature('除法')
    @allure.feature('整数')
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [-1, -1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [0, 1, 0],
        [10000000000000000, 1, 10000000000000000],
        [10000000000000000, -1, -10000000000000000],
        [-10000000000000000, 1, -10000000000000000],
        [-10000000000000000, -1, 10000000000000000]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 除数和被除数为小数
    @allure.feature('浮点数')
    @pytest.mark.parametrize('a, b, c',[
        [0.1, 1, 0.1],
        [0.1, 0.1, 1],
        [1, 0.1, 10],
        [0.1, -1, -0.1],
        [0.1, -0.1, -1],
        [1, -0.1, -10],
        [-0.1, 1, -0.1],
        [-0.1, 0.1, -1],
        [-1, 0.1, -10],
        [-0.1, -1, 0.1],
        [-0.1, -0.1, 1],
        [-1, -0.1, 10],
        [0, 0.5, 0],
        [0, -0.5, 0],
        [0.0000000000000001, 1, 0.0000000000000001],
        [1, 0.00000000000000001, 100000000000000000],
        [-0.0000000000000001, 1, -0.0000000000000001],
        [-1, 0.00000000000000001, -100000000000000000],
        [0.0000000000000001, -1, -0.0000000000000001],
        [1, -0.00000000000000001, -100000000000000000],
        [-0.0000000000000001, -1, 0.0000000000000001],
        [-1, -0.00000000000000001, 100000000000000000]
    ])
    def test_div2(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 除数结果超过最多展示位数
    @allure.feature('运行结果超长')
    @pytest.mark.parametrize('a, b, c', [
        [1000000000000000000, 10, 1e17],
        [0.1, 0.000000000000000001, 1e17],

        [1000000000000000000, -10, -1e17],
        [0.1, -0.000000000000000001, -1e17],

        [-1000000000000000000, 10, -1e17],
        [-0.1, 0.000000000000000001, -1e17],

        [-1000000000000000000, -10, 1e17],
        [-0.1, -0.000000000000000001, 1e17]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 除数为0时异常情况
    @allure.feature('除数为0')
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0],
        [-1, 0],
        [-0.1, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

