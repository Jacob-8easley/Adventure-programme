from item import Item
import pytest

from room import Room



def test_get_exits_valid_value():
    test_room = Room("test")
    test_room_1 = Room("test_1")
    test_room.exits["N"] = test_room_1
    test_room_1.exits["S"] = test_room
    expected_value = ["N"]
    actual_value = test_room.get_exits()
    assert expected_value == actual_value
    
    
    
    
def test_set_exits_valid_value():
    test_room = Room("test")
    test_room_1 = Room("test_1")
    expected_value = test_room.exits["N"] = test_room_1
    actual_value = test_room.set_exits("N",test_room_1)
    assert expected_value == actual_value
    
    
    
def test_remove_item_valid_value():
    test_room = Room("test")
    expected_value = None
    actual_value = test_room.remove_item()
    assert expected_value == actual_value
    
