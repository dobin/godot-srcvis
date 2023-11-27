#!/usr/bin/env python

import unittest

from parsing.lineparser import *



class ParserTest(unittest.TestCase):

    def test_get_signal(self):
        tests = [
            {
                "line": 'signal s_player_death',
                "result": 'signal s_player_death',
            },
            { 
                "line": 'signal lets_spawn_this(enemy_definition)',
                "result": 'signal lets_spawn_this(enemy_definition)',
            },
        ]
        for test in tests:
            result = parse_line_signal(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_connect(self):
        tests = [
            {
                "line": 'WaveGenerator.level_finished.connect(_on_level_finished)',
                "result": 'WaveGenerator.level_finished.connect(_on_level_finished)',
                #"result": 'WaveGenerator.level_finished -> _on_level_finished()',
            },
            { 
                "line": 'Data.goto_state.connect(_on_lets_goto_state)',
                "result": 'Data.goto_state.connect(_on_lets_goto_state)',
                #"result": 'Data.goto_state -> _on_lets_goto_state',
            }, 
        ]
        for test in tests:
            result = parse_line_connect(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_dollar(self):
        tests = [
            {
                "line": '$hud/screen_game_selecting.hide()',
                "result": '$hud',
            },
            { 
                "line": '$attack.exec_tower_weapon(Data.keymap.mapping[tower_name])',
                "result": '$attack',
            }, 
            { 
                "line": '$CollisionShape2D.disabled = false',
                "result": '$CollisionShape2D',
            }
        ]
        for test in tests:
            result = parse_line_dollar(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_load(self):
        tests = [
            {
                "line": 'var error = image.load(sprite_sheet_path)',
                "result": 'sprite_sheet_path',
            },
            {
                "line": 'var level_generator = load(__source).new()',
                "result": '__source',
            },
        ]
        for test in tests:
            result = parse_line_load(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_preload(self):
        tests = [
            {
                "line": 'var mob = preload("res://enemies/mob.tscn").instantiate()',
                "result": 'res://enemies/mob.tscn',
            },
            { 
                "line": 'var update_select = preload("res://hud/hud_upgrade_select.tscn")',
                "result": 'res://hud/hud_upgrade_select.tscn',
            }, 
        ]
        for test in tests:
            result = parse_line_preload(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_new(self):
        tests = [
            {
                "line": 'level_generator = LevelGenerator.new()',
                "result": 'LevelGenerator',
            },
            { 
                "line": 'Wave.new(1, 3.0, 10.0, "random", {})',
                "result": 'Wave',
            }, 
            { 
                "line": 'var enemy_type = EnemyType.new(enemies_data[name_id], is_big, can_move)',
                "result": 'EnemyType',
            }
        ]
        for test in tests:
            result = parse_line_new(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_instantiate(self):
        tests = [
            {
                "line": 'var b = Bullet.instantiate()',
                "result": 'Bullet',
            },
            { 
                "line": 'var mob = preload("res://enemies/mob.tscn").instantiate()',
                "result": 'preload("res://enemies/mob.tscn")',
            }, 
        ]
        for test in tests:
            result = parse_line_instantiate(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_emit(self):
        tests = [

            { 
                "line": 's_player_death.emit()  # notify that we are dead',
                "result": 's_player_death',
            }, 
            { 
                "line": 'start_game.emit("debug")',
                "result": 'start_game',
            }
        ]
        for test in tests:
            result = parse_line_emit(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_nodesingroup(self):
        tests = [
            {
                "line": 'if get_tree().get_nodes_in_group("minions").size() > utils.get_weapon_minion_maxcount()',
                "result": 'minions',
            },
            { 
                "line": 'for weapon_icon in get_tree().get_nodes_in_group("weapon_icons"):',
                "result": 'weapon_icons',
            },
        ]
        for test in tests:
            result = parse_line_get_node_in_group(test["line"])
            self.assertEqual(result, test["result"])


    def test_get_exports(self):
        tests = [
            {
                "line": '@export var Bullet : PackedScene',
                "result": 'Bullet: PackedScene',
            },
        ]
        for test in tests:
            result = parse_line_export(test["line"])
            self.assertEqual(result, test["result"])



