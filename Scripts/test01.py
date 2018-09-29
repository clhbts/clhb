import allure
import pytest


class Test01():
    @allure.step("执行学院添加操作")
    def test01(self):
        print("执行学院添加操作")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step("执行学院更新操作")
    def test02(self):
        allure.attach("断言开始","学院更新是否成功")
        print("执行学院更新操作")
        allure.attach("断言结束","学员更新成功")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        print("test03执行成功")
        assert 0