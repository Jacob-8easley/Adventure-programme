from cgi import test
from enemy import Enemy
from item import Item
import pytest 
from player import Player
from weapon import Weapon

def test_update_health_valid_value():
    test_player = Player()
    expected_value = 105
    actual_value = test_player.update_health(5) 
    assert expected_value == actual_value
    
def test_attack_valid_value_no_weapon():
    test_player = Player()
    expected_value = 0
    actual_value =test_player.attack()
    assert expected_value == actual_value
    
    
def test_attack_valid_value_weapon():
    test_weapon = Weapon("test", equipable=True, quantity=1, weight=None, power=5, equip_state=True)
    test_player = Player()
    test_player.weapon = test_weapon
    expected_value = -5
    actual_value =test_player.attack()
    assert expected_value == actual_value
    
    
def test_get_weapon_valid_value_no_weapon():
    test_weapon = Weapon("test", equipable=True, quantity=1, weight=None, power=5, equip_state=False)
    test_player = Player()
    expected_value = None
    actual_value =test_player.get_weapon()
    assert expected_value == actual_value
    
def test_get_weapon_valid_value_weapon():
    test_weapon = Weapon("test", equipable=True, quantity=1, weight=None, power=5, equip_state=True)
    test_player = Player()
    test_player.weapon = test_weapon
    expected_value = "test"
    actual_value =test_player.get_weapon()
    assert expected_value == actual_value
    
def test_add_to_library_valid_value():
    test_item = Item("test",)
    test_player = Player()
    expected_value = {"test":id(test_item)}
    expected_value = test_player.library["test"]=test_item
    actual_value =test_player.add_to_library(test_item)
    assert expected_value == actual_value
    
def test_remove_from_library_valid_value():
    test_item = Item("test")
    test_player = Player()
    expected_value = None
    # expected_value = test_player.library["test"]=test_item
    actual_value =test_player.remove_from_library(test_item)
    assert expected_value == actual_value
    
    
def test_equip_weapon_valid_value_no_weapon():
    test_weapon = Weapon("test")
    test_player = Player()
    expected_value = None
    actual_value = test_player.equip_weapon(test_weapon)
    assert expected_value == actual_value
    
def test_equip_weapon_valid_value_weapon():
    test_weapon = Weapon("test")
    test_player = Player()
    test_player.library["test"]=test_weapon
    expected_value = test_weapon.name
    actual_value = test_player.equip_weapon(test_weapon.name)
    assert expected_value == actual_value