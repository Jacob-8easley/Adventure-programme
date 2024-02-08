# from health import Health
import pytest
from enemy import Enemy
# import monkeypatch 


# def test_get_attack_value_valid():
#     test_enemy = Enemy("test",health=10,attack=5,dead=False)
#     expected_value = 10
#     actual_value = test_enemy.get_attack_value()
#     assert expected_value == actual_value
    
def test_get_health_value_valid():
    test_enemy = Enemy("test",health=10,attack=5,dead=False)
    expected_value = 10
    actual_value = test_enemy.get_health()
    assert expected_value == actual_value
    
def test_update_health_value_valid():
    test_enemy = Enemy("test", health=10, attack=5, dead=False)
    expected_value = 15
    actual_value = test_enemy.update_health(5)
    assert expected_value == actual_value
    
def test_get_name_value_valid():
    test_enemy = Enemy("test", health=10, attack=5, dead=False)
    expected_value = "test"
    actual_value = test_enemy.get_name()
    assert expected_value == actual_value