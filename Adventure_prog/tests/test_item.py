import pytest

from item import Item

def test_set_equiped_valid_value():
    test_item = Item("test", equipable=False, quantity=1, weight=None, equip_state=False)
    expected_value = True
    actual_value = test_item.set_equiped()
    assert expected_value == actual_value 
    
    
def test_set_unequipped_valid_value():
    test_item = Item("test", equipable=False, quantity=1, weight=None, equip_state= True)
    expected_value = False
    actual_value = test_item.set_unequipped()
    assert expected_value == actual_value