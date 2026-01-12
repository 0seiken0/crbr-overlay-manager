import dolphin_memory_engine as dolphin
import tkinter as tk
from tkinter import ttk
from os import path
from configparser import ConfigParser
import shutil
from pathlib import Path
import pandas as pd
import datetime

vanillaParts = [
    {
        0: ["Ray 01", "レイ０１"],
        1: ["Splendor", "スプレンダー"],
        2: ["Glory", "ラーバ"],
        3: ["Milky Way", "ミルキーウェイ"],
        4: ["Earth", "スピカ"],
        5: ["Sol", "アース"],
        6: ["Metal Ape", "メタルコング"],
        7: ["Metal Bear", "メタルベア"],
        8: ["Metal Ox", "メタルオックス"],
        9: ["Swift", "リトルチック"],
        10: ["Shrike", "ペキンダック"],
        11: ["Peregrine", "ペリグリン"],
        12: ["Javelin", "ジャベリン"],
        13: ["Glaive", "ブローバ"],
        14: ["Halberd", "ハルベルト"],
        15: ["Criminal", "クリミナル"],
        16: ["Buggy", "バギー"],
        17: ["Juggler", "ジャグラー"],
        18: ["Defender", "ディフェンダー"],
        19: ["Seeker", "ベリアス"],
        20: ["Breaker", "ブレイカー"],
        21: ["Seal Head", "シールヘッド"],
        22: ["Dour Head", "プレジャーヘッド"],
        23: ["Tank Head", "ホバーヘッド"],
        24: ["Rakansen", "ラカンセン"],
        25: ["Ruhiel", "ルヒエル"],
        26: ["Athena", "アルテミス"],
        27: ["Ray Legend", "レイレジェンド"],
        28: ["Ray Warrior", "レイウォーリア"],
        29: ["Oil Can", "ドラムカン"],
        30: ["Rahu I", "アール第1形態"],
        31: ["Rahu II", "アール第2形態"],
        32: ["Rahu III", "アール第3形態"],
        33: ["Chickenheart", "チキンハート"]
    },
    {
        0: ["Basic", "ベーシック"],
        1: ["3-Way", "３ウェイ"],
        2: ["Gatling", "ガトリング"],
        3: ["Vertical", "バーティカル"],
        4: ["Sniper", "スナイパー"],
        5: ["Stun", "スタン"],
        6: ["Hornet", "ホーネット"],
        7: ["Flame", "フレイム"],
        8: ["Dragon", "ドラゴン"],
        9: ["Splash", "スプラッシュ"],
        10: ["Left Arc", "レフトアーク"],
        11: ["Right Arc", "ライトアーク"],
        12: ["Shotgun", "ショットガン"],
        13: ["Rayfall", "レイフォール"],
        14: ["Bubble", "バブル"],
        15: ["Eagle", "イーグル"],
        16: ["V Laser", "Vレーザー"],
        17: ["Magnum", "マグナム"],
        18: ["Needle", "ニードル"],
        19: ["Starshot", "スターレイヤー"],
        20: ["Glider", "グライダー"],
        21: ["Homing Star", "マルチプル"],
        22: ["Trap", "トラップ"],
        23: ["Drill", "ドリル"],
        24: ["Titan", "ジャイアント"],
        25: ["Claw", "キャッチ"],
        26: ["Knuckle", "ナックル"],
        27: ["Afterburner", "アクセル"],
        28: ["Blade", "ブレード"],
        29: ["Meteor Storm", "スターダスト"],
        30: ["Twin Fang", "ファング"],
        31: ["Gravity", "グラビティ"],
        32: ["Phoenix", "フェニックス"],
        33: ["Left Pulse", "レフトループ"],
        34: ["Right Pulse", "ライトループ"],
        35: ["Sword Storm", "サークルソード"],
        36: ["Ion", "サンダー"],
        37: ["Flare", "フレアキャノン"],
        38: ["Left 5-Way", "レフト５ウェイ"],
        39: ["Right 5-Way", "ライト５ウェイ"],
        40: ["Halo", "エンジェルリング"],
        41: ["Wave Laser", "リップルレーザー"],
        42: ["X Laser", "Xレーザーガン"],
        43: ["Crystal Strike", "メテオフリッカー"],
        44: ["Wyrm", "オロチ"],
        45: ["Raptor", "ガルーダ"],
        46: ["Waxing Arc", "ディアナビート"],
        47: ["Waning Arc", "ルナビート"],
        48: ["Rahu I", "ラグナロク1st"],
        49: ["Rahu II", "ラグナロク2nd"],
        50: ["Rahu III", "ラグナロク3rd"],
        51: ["Can", "ドラムカン"]
    },
    {
        0: ["Standard", "スタンダード"],
        1: ["Standard F", "スタンダードF"],
        2: ["Standard S", "スタンダードS"],
        3: ["Standard K", "スタンダードK"],
        4: ["Standard X", "スタンダードX"],
        5: ["Wave", "ウェーブ"],
        6: ["Straight G", "ストレートG"],
        7: ["Straight S", "ストレートS"],
        8: ["Straight T", "ストレートT"],
        9: ["Left Flank H", "レフトシュートH"],
        10: ["Right Flank H", "ライトシュートH"],
        11: ["Left Wave", "レフトウェーブ"],
        12: ["Right Wave", "ライトウェーブ"],
        13: ["Burrow D", "アイドリングD"],
        14: ["Burrow P", "アイドリングP"],
        15: ["Freeze", "フリーズ"],
        16: ["Tomahawk B", "トマホークB"],
        17: ["Tomahawk G", "トマホークG"],
        18: ["Gemini B", "ジェミニB"],
        19: ["Gemini P", "ジェミニP"],
        20: ["Submarine D", "サブマリンD"],
        21: ["Submarine P", "サブマリンP"],
        22: ["Submarine K", "サブマリンK"],
        23: ["Crescent P", "クレセントP"],
        24: ["Crescent C", "クレセントC"],
        25: ["Crescent K", "クレセントK"],
        26: ["Dual", "ディレイ"],
        27: ["Dual C", "ディレイC"],
        28: ["Acrobat", "アクロバット"],
        29: ["Delta", "デルタ"],
        30: ["Wall", "ウォール"],
        31: ["Smash", "スマッシュ"],
        32: ["Double Mine", "ダブルマイン"],
        33: ["Geo Trap", "ジオトラップ"],
        34: ["Titan", "ジャイアント"],
        35: ["Treble", "ゴウカ"],
        36: ["Wyvern", "ワイバーン"],
        37: ["Waxing Arc", "ルナヒート"],
        38: ["Waning Arc", "ディアナヒート"],
        39: ["Grand Cross", "グランドクロス"],
        40: ["Can", "ドラムカン"]
    },
    {
        0: ["Standard", "スタンダード"],
        1: ["Standard F", "スタンダードF"],
        2: ["Seeker F", "シーカーF"],
        3: ["Seeker G", "シーカーG"],
        4: ["Speed D", "スピードD"],
        5: ["Speed P", "スピードP"],
        6: ["Cockroach G", "コックローチG"],
        7: ["Cockroach H", "コックローチH"],
        8: ["Dolphin", "ドルフィン"],
        9: ["Dolphin G", "ドルフィンG"],
        10: ["Spider", "スパイダー"],
        11: ["Spider G", "スパイダーG"],
        12: ["Sky Freeze", "スカイフリーズ"],
        13: ["Ground Freeze", "グランドフリーズ"],
        14: ["Feint F", "フェイントF"],
        15: ["Feint G", "フェイントG"],
        16: ["Float F", "フロートF"],
        17: ["Jumping B", "ジャンピングB"],
        18: ["Jumping G", "ジャンピングG"],
        19: ["Diving", "ダイビング"],
        20: ["Wave", "ウェーブ"],
        21: ["Satellite", "サテライト"],
        22: ["Satellite H", "サテライトH"],
        23: ["Beast F", "ヤジューF"],
        24: ["Trio H", "トリプルH"],
        25: ["Wall", "ウォール"],
        26: ["Reflection", "リフレクション"],
        27: ["Caboose C", "リアシュートC"],
        28: ["Caboose T", "リアシュートT"],
        29: ["Caboose X", "リアシュートX"],
        30: ["Twin Flank F", "サイドウェイF"],
        31: ["Twin Flank G", "サイドウェイG"],
        32: ["Umbrella", "アンブレラ"],
        33: ["Throwing D", "スローイングD"],
        34: ["Throwing P", "スローイングP"],
        35: ["Double Wave", "ダブルウェーブ"],
        36: ["Titan", "ジャイアント"],
        37: ["Cheetah", "ハヤテ"],
        38: ["Wolf Spider", "グリフォン"],
        39: ["Orca", "ムーンライト"],
        40: ["Penumbra I", "カタストロフィ1st"],
        41: ["Penumbra II", "カタストロフィ2nd"],
        42: ["Penumbra III", "カタストロフィ3rd"],
        43: ["Can", "ドラムカン"]
    },
    {
        0: ["Standard", "スタンダード"],
        1: ["High Jump", "ハイジャンプ"],
        2: ["Ground", "グランダー"],
        3: ["Formula", "フォーミュラー"],
        4: ["Stabilizer", "スタビライザー"],
        5: ["Short Thrust", "ショートバーニア"],
        6: ["Long Thrust", "ロングバーニア"],
        7: ["Quick Jump", "クイックジャンプ"],
        8: ["Feather", "フェザー"],
        9: ["Wide Jump", "ワイドジャンプ"],
        10: ["Booster", "ブースター"],
        11: ["Swallow", "ヒエン"],
        12: ["Raven", "レイブン"],
        13: ["Eclipse", "イクリプス"],
        14: ["Ultimate", "アルティメット"],
        15: ["Can", "ドラムカン"]
    }
]

ph3Parts = [
    {
        0: ["Ray 01", "レイ０１"],
        1: ["Splendor", "スプレンダー"],
        2: ["Glory", "ラーバ"],
        3: ["Milky Way", "ミルキーウェイ"],
        4: ["Earth", "スピカ"],
        5: ["Sol", "アース"],
        6: ["Metal Ape", "メタルコング"],
        7: ["Metal Bear", "メタルベア"],
        8: ["Metal Ox", "メタルオックス"],
        9: ["Swift", "リトルチック"],
        10: ["Shrike", "ペキンダック"],
        11: ["Peregrine", "ペリグリン"],
        12: ["Javelin", "ジャベリン"],
        13: ["Glaive", "ブローバ"],
        14: ["Halberd", "ハルベルト"],
        15: ["Criminal", "クリミナル"],
        16: ["Buggy", "バギー"],
        17: ["Juggler", "ジャグラー"],
        18: ["Defender", "ディフェンダー"],
        19: ["Seeker", "ベリアス"],
        20: ["Breaker", "ブレイカー"],
        21: ["Seal Head", "シールヘッド"],
        22: ["Dour Head", "プレジャーヘッド"],
        23: ["Tank Head", "ホバーヘッド"],
        24: ["Chickenheart", "チキンハート"],
        25: ["Rahubeast", "アールビースト"],
        26: ["Ruhiel", "ルヒエル"],
        27: ["Lancer", "ランサー"],
        28: ["Gladiator", "グラディエーター"],
        29: ["Ray Soldier", "レイソルジャー"],
        30: ["Athena", "アルテミス"],
        31: ["Rebecca", "レベッカ"],
        32: ["May", "メイ"],
        33: ["Lumen", "ルーメン"],
        34: ["Pepper", "ペッパー"],
        35: ["Nybble", "ニブル"],
        36: ["Vulcan", "ウゥルカーヌス"],
        37: ["Spitfire", "スピットファイア"],
        38: ["Albatross", "アルバトロス"]
    },
    {
        0: ["Basic", "ベーシック"],
        1: ["Needle", "ニードル"],
        2: ["Sniper", "スナイパー"],
        3: ["Gatling", "ガトリング"],
        4: ["Ion", "サンダー"],
        5: ["V Laser", "Vレーザー"],
        6: ["Dragon", "ドラゴン"],
        7: ["Hydra", "ヒュドラー"],
        8: ["Bubble", "バブル"],
        9: ["Splash", "スプラッシュ"],
        10: ["Stun", "スタン"],
        11: ["Shotgun", "ショットガン"],
        12: ["Magnum", "マグナム"],
        13: ["Drill", "ドリル"],
        14: ["Knuckle", "ナックル"],
        15: ["Quickshot", "クイックショット"],
        16: ["Surge", "サージ"],
        17: ["Flame", "フレイム"],
        18: ["Hornet", "ホーネット"],
        19: ["Vertical", "バーティカル"],
        20: ["Buster", "バスター"],
        21: ["Meteor Storm", "スターダスト"],
        22: ["Left Pulse", "レフトループ"],
        23: ["Right Pulse", "ライトループ"],
        24: ["Twin Fang", "ファング"],
        25: ["Flare", "フレアキャノン"],
        26: ["Rahu I", "ラグナロク1st"],
        27: ["Slicer", "スライサー"],
        28: ["Gravity", "グラビティ"],
        29: ["3-Way", "３ウェイ"],
        30: ["Left Arc", "レフトアーク"],
        31: ["Right Arc", "ライトアーク"],
        32: ["Starshot", "スターレイヤー"],
        33: ["Homing Star", "マルチプル"],
        34: ["Glider", "グライダー"],
        35: ["Halo", "エンジェルリング"],
        36: ["Afterburner", "アクセル"],
        37: ["Rayfall", "レイフォール"],
        38: ["Eagle", "イーグル"],
        39: ["Trap", "トラップ"],
        40: ["Sword Storm", "サークルソード"],
        41: ["Vulture", "ハゲタカ"],
        42: ["Pursuit", "パースート"],
        43: ["Titan", "ジャイアント"],
        44: ["Left 5-Way", "レフト５ウェイ"],
        45: ["Right 5-Way", "ライト５ウェイ"],
        46: ["Claw", "キャッチ"],
        47: ["Blade", "ブレード"],
        48: ["Phoenix", "フェニックス"]
    },
    {
        0: ["Standard R", "スタンダードR"],
        1: ["Standard F", "スタンダードF"],
        2: ["Standard S", "スタンダードS"],
        3: ["Standard K", "スタンダードK"],
        4: ["Standard X", "スタンダードX"],
        5: ["Straight R", "ストレートR"],
        6: ["Straight G", "ストレートG"],
        7: ["Straight S", "ストレートS"],
        8: ["Straight T", "ストレートT"],
        9: ["Left Flank F", "レフトシュートF"],
        10: ["Right Flank F", "ライトシュートF"],
        11: ["Left Flank H", "レフトシュートH"],
        12: ["Right Flank H", "ライトシュートH"],
        13: ["Left Flank X", "レフトシュートX"],
        14: ["Right Flank X", "ライトシュートX"],
        15: ["Burrow D", "アイドリングD"],
        16: ["Burrow P", "アイドリングP"],
        17: ["Tomahawk R", "トマホークR"],
        18: ["Tomahawk B", "トマホークB"],
        19: ["Tomahawk G", "トマホークG"],
        20: ["Tomahawk S", "トマホークS"],
        21: ["Gemini D", "ジェミニD"],
        22: ["Gemini P", "ジェミニP"],
        23: ["Dual R", "ディレイR"],
        24: ["Dual D", "ディレイD"],
        25: ["Dual C", "ディレイC"],
        26: ["Submarine D", "サブマリンD"],
        27: ["Submarine P", "サブマリンP"],
        28: ["Submarine K", "サブマリンK"],
        29: ["Submarine X", "サブマリンX"],
        30: ["Crescent R", "クレセントR"],
        31: ["Crescent P", "クレセントP"],
        32: ["Crescent C", "クレセントC"],
        33: ["Crescent K", "クレセントK"],
        34: ["Freeze", "フリーズ"],
        35: ["Wave", "ウェーブ"],
        36: ["Left Wave", "レフトウェーブ"],
        37: ["Right Wave", "ライトウェーブ"],
        38: ["Acrobat", "アクロバット"],
        39: ["Delta", "デルタ"],
        40: ["Wall", "ウォール"],
        41: ["Smash", "スマッシュ"],
        42: ["Double Mine", "ダブルマイン"],
        43: ["Geo Trap", "ジオトラップ"],
        44: ["Titan", "ジャイアント"],
        45: ["Solar Pillar", "ソーラーピラー"],
        46: ["Rapid", "ラピッド"],
        47: ["Grand Cross", "グランドクロス"],
        48: ["Cluster", "クラスター"],
        49: ["Drake R", "ドレークR"],
        50: ["Drake G", "ドレークG"],
        51: ["Drake X", "ドレークX"],
        52: ["Heavy R", "ヘヴィーR"],
        53: ["Heavy D", "ヘヴィーD"],
        54: ["Heavy H", "ヘヴィーH"],
        55: ["Heavy K", "ヘヴィーK"]
    },
    {
        0: ["Standard R", "スタンダードR"],
        1: ["Standard D", "スタンダードD"],
        2: ["Twin Flank F", "サイドウェイF"],
        3: ["Twin Flank G", "サイドウェイG"],
        4: ["Speed R", "スピードR"],
        5: ["Speed D", "スピードD"],
        6: ["Speed P", "スピードP"],
        7: ["Cockroach G", "コックローチG"],
        8: ["Cockroach H", "コックローチH"],
        9: ["Dolphin R", "ドルフィンR"],
        10: ["Dolphin G", "ドルフィンG"],
        11: ["Dolphin X", "ドルフィンX"],
        12: ["Jumping B", "ジャンピングB"],
        13: ["Jumping G", "ジャンピングG"],
        14: ["Caboose C", "リアシュートC"],
        15: ["Caboose T", "リアシュートT"],
        16: ["Caboose X", "リアシュートX"],
        17: ["Wave", "ウェーブ"],
        18: ["Double Wave", "ダブルウェーブ"],
        19: ["Wall", "ウォール"],
        20: ["Umbrella", "アンブレラ"],
        21: ["Trio F", "トリプルF"],
        22: ["Trio H", "トリプルH"],
        23: ["Titan", "ジャイアント"],
        24: ["Throwing D", "スローイングD"],
        25: ["Throwing P", "スローイングP"],
        26: ["Reflection", "リフレクション"],
        27: ["Float F", "フロートF"],
        28: ["Feint F", "フェイントF"],
        29: ["Feint G", "フェイントG"],
        30: ["Seeker R", "シーカーR"],
        31: ["Seeker F", "シーカーF"],
        32: ["Seeker G", "シーカーG"],
        33: ["Diving", "ダイビング"],
        34: ["Spider R", "スパイダーR"],
        35: ["Spider H", "スパイダーH"],
        36: ["Spider G", "スパイダーG"],
        37: ["Sky Freeze", "スカイフリーズ"],
        38: ["Ground Freeze", "グランドフリーズ"],
        39: ["Satellite", "サテライト"],
        40: ["Satellite H", "サテライトH"],
        41: ["Beast F", "ヤジューF"],
    },
    {
        0: ["Standard", "スタンダード"],
        1: ["Formula", "フォーミュラー"],
        2: ["Stabilizer", "スタビライザー"],
        3: ["Precision", "プレシジョン"],
        4: ["Wide Jump", "ワイドジャンプ"],
        5: ["Aerial", "エアリアル"],
        6: ["Eclipse", "イクリプス"],
        7: ["Ultimate", "アルティメット"],
        8: ["High Jump", "ハイジャンプ"],
        9: ["Ground", "グランダー"],
        10: ["Quick Jump", "クイックジャンプ"],
        11: ["Feather", "フェザー"],
        12: ["Short Thrust", "ショートバーニア"],
        13: ["Long Thrust", "ロングバーニア"],
        14: ["Swallow", "ヒエン"],
        15: ["Plus One", "プラスワン"],
        16: ["Booster", "ブースター"],
        17: ["Overhaul", "オーバーホール"],
        18: ["Raven", "レイブン"],
        19: ["Prowler", "プロウラー"]
    }
]

ph3dot1Parts = [
    {
        0: ["Ray 01", "レイ０１"],
        1: ["Splendor", "スプレンダー"],
        2: ["Glory", "ラーバ"],
        3: ["Milky Way", "ミルキーウェイ"],
        4: ["Earth", "スピカ"],
        5: ["Sol", "アース"],
        6: ["Metal Ape", "メタルコング"],
        7: ["Metal Bear", "メタルベア"],
        8: ["Metal Ox", "メタルオックス"],
        9: ["Swift", "リトルチック"],
        10: ["Shrike", "ペキンダック"],
        11: ["Peregrine", "ペリグリン"],
        12: ["Javelin", "ジャベリン"],
        13: ["Glaive", "ブローバ"],
        14: ["Halberd", "ハルベルト"],
        15: ["Criminal", "クリミナル"],
        16: ["Buggy", "バギー"],
        17: ["Juggler", "ジャグラー"],
        18: ["Defender", "ディフェンダー"],
        19: ["Seeker", "ベリアス"],
        20: ["Breaker", "ブレイカー"],
        21: ["Seal Head", "シールヘッド"],
        22: ["Dour Head", "プレジャーヘッド"],
        23: ["Tank Head", "ホバーヘッド"],
        24: ["Chickenheart", "チキンハート"],
        25: ["Lionmane", "ライオンメーン"],
        26: ["Wolfclaw", "ウルフクロー"],
        27: ["Gannicus", "ガンニクス"],
        28: ["Spartacus", "スパルタクス"],
        29: ["Crixus", "クリクスス"],
        30: ["Athena", "アルテミス"],
        31: ["Hestia", "ヘスティアー"],
        32: ["Nike", "ニーケー"],
        33: ["Blitz", "ブリッツ"],
        34: ["Turbo", "ターボ"],
        35: ["Zoom", "ズーム"],
        36: ["Tempest", "テンペスト"],
        37: ["Cyclone", "サイクロン"],
        38: ["Hurricane", "ハリケーン"]
    },
    {
        0: ["Basic", "ベーシック"],
        1: ["Needle", "ニードル"],
        2: ["Sniper", "スナイパー"],
        3: ["Gatling", "ガトリング"],
        4: ["Ion", "サンダー"],
        5: ["V Laser", "Vレーザー"],
        6: ["Dragon", "ドラゴン"],
        7: ["Hydra", "ヒュドラー"],
        8: ["Bubble", "バブル"],
        9: ["Splash", "スプラッシュ"],
        10: ["Stun", "スタン"],
        11: ["Shotgun", "ショットガン"],
        12: ["Magnum", "マグナム"],
        13: ["Drill", "ドリル"],
        14: ["Knuckle", "ナックル"],
        15: ["Quickshot", "クイックショット"],
        16: ["Surge", "サージ"],
        17: ["Flame", "フレイム"],
        18: ["Hornet", "ホーネット"],
        19: ["Vertical", "バーティカル"],
        20: ["Buster", "バスター"],
        21: ["Meteor Storm", "スターダスト"],
        22: ["Left Pulse", "レフトループ"],
        23: ["Right Pulse", "ライトループ"],
        24: ["Twin Fang", "ファング"],
        25: ["Flare", "フレアキャノン"],
        26: ["Rahu I", "ラグナロク1st"],
        27: ["Slicer", "スライサー"],
        28: ["Gravity", "グラビティ"],
        29: ["3-Way", "３ウェイ"],
        30: ["Left Arc", "レフトアーク"],
        31: ["Right Arc", "ライトアーク"],
        32: ["Starshot", "スターレイヤー"],
        33: ["Homing Star", "マルチプル"],
        34: ["Glider", "グライダー"],
        35: ["Halo", "エンジェルリング"],
        36: ["Afterburner", "アクセル"],
        37: ["Rayfall", "レイフォール"],
        38: ["Eagle", "イーグル"],
        39: ["Trap", "トラップ"],
        40: ["Sword Storm", "サークルソード"],
        41: ["Vulture", "ハゲタカ"],
        42: ["Pursuit", "パースート"],
        43: ["Titan", "ジャイアント"],
        44: ["Left 5-Way", "レフト５ウェイ"],
        45: ["Right 5-Way", "ライト５ウェイ"],
        46: ["Claw", "キャッチ"],
        47: ["Blade", "ブレード"],
        48: ["Phoenix", "フェニックス"]
    },
    {
        0: ["Standard R", "スタンダードR"],
        1: ["Standard F", "スタンダードF"],
        2: ["Standard S", "スタンダードS"],
        3: ["Standard K", "スタンダードK"],
        4: ["Standard X", "スタンダードX"],
        5: ["Straight R", "ストレートR"],
        6: ["Straight G", "ストレートG"],
        7: ["Straight S", "ストレートS"],
        8: ["Straight T", "ストレートT"],
        9: ["Left Flank F", "レフトシュートF"],
        10: ["Right Flank F", "ライトシュートF"],
        11: ["Left Flank H", "レフトシュートH"],
        12: ["Right Flank H", "ライトシュートH"],
        13: ["Left Flank X", "レフトシュートX"],
        14: ["Right Flank X", "ライトシュートX"],
        15: ["Burrow D", "アイドリングD"],
        16: ["Burrow P", "アイドリングP"],
        17: ["Tomahawk R", "トマホークR"],
        18: ["Tomahawk B", "トマホークB"],
        19: ["Tomahawk G", "トマホークG"],
        20: ["Gemini D", "ジェミニD"],
        21: ["Gemini P", "ジェミニP"],
        22: ["Dual R", "ディレイR"],
        23: ["Dual D", "ディレイD"],
        24: ["Dual C", "ディレイC"],
        25: ["Submarine D", "サブマリンD"],
        26: ["Submarine P", "サブマリンP"],
        27: ["Submarine K", "サブマリンK"],
        28: ["Submarine X", "サブマリンX"],
        29: ["Crescent R", "クレセントR"],
        30: ["Crescent P", "クレセントP"],
        31: ["Crescent C", "クレセントC"],
        32: ["Crescent K", "クレセントK"],
        33: ["Freeze", "フリーズ"],
        34: ["Wave", "ウェーブ"],
        35: ["Left Wave", "レフトウェーブ"],
        36: ["Right Wave", "ライトウェーブ"],
        37: ["Acrobat", "アクロバット"],
        38: ["Delta", "デルタ"],
        39: ["Wall", "ウォール"],
        40: ["Smash", "スマッシュ"],
        41: ["Double Mine", "ダブルマイン"],
        42: ["Geo Trap", "ジオトラップ"],
        43: ["Titan", "ジャイアント"],
        44: ["Solar Pillar", "ソーラーピラー"],
        45: ["Rapid", "ラピッド"],
        46: ["Grand Cross", "グランドクロス"],
        47: ["Cluster", "クラスター"],
        48: ["Heavy R", "ヘヴィーR"],
        49: ["Heavy D", "ヘヴィーD"],
        50: ["Heavy H", "ヘヴィーH"],
        51: ["Heavy K", "ヘヴィーK"]
    },
    {
        0: ["Standard R", "スタンダードR"],
        1: ["Standard D", "スタンダードD"],
        2: ["Twin Flank F", "サイドウェイF"],
        3: ["Twin Flank G", "サイドウェイG"],
        4: ["Speed R", "スピードR"],
        5: ["Speed D", "スピードD"],
        6: ["Speed P", "スピードP"],
        7: ["Cockroach G", "コックローチG"],
        8: ["Cockroach H", "コックローチH"],
        9: ["Dolphin R", "ドルフィンR"],
        10: ["Dolphin G", "ドルフィンG"],
        11: ["Dolphin X", "ドルフィンX"],
        12: ["Jumping B", "ジャンピングB"],
        13: ["Jumping G", "ジャンピングG"],
        14: ["Caboose C", "リアシュートC"],
        15: ["Caboose T", "リアシュートT"],
        16: ["Caboose X", "リアシュートX"],
        17: ["Wave", "ウェーブ"],
        18: ["Double Wave", "ダブルウェーブ"],
        19: ["Wall", "ウォール"],
        20: ["Umbrella", "アンブレラ"],
        21: ["Trio F", "トリプルF"],
        22: ["Trio H", "トリプルH"],
        23: ["Titan", "ジャイアント"],
        24: ["Throwing D", "スローイングD"],
        25: ["Throwing P", "スローイングP"],
        26: ["Reflection", "リフレクション"],
        27: ["Float F", "フロートF"],
        28: ["Feint F", "フェイントF"],
        29: ["Feint G", "フェイントG"],
        30: ["Seeker R", "シーカーR"],
        31: ["Seeker F", "シーカーF"],
        32: ["Seeker G", "シーカーG"],
        33: ["Diving", "ダイビング"],
        34: ["Spider R", "スパイダーR"],
        35: ["Spider H", "スパイダーH"],
        36: ["Spider G", "スパイダーG"],
        37: ["Sky Freeze", "スカイフリーズ"],
        38: ["Ground Freeze", "グランドフリーズ"],
        39: ["Satellite", "サテライト"],
        40: ["Satellite H", "サテライトH"],
        41: ["Beast F", "ヤジューF"],
    },
    {
        0: ["Standard", "スタンダード"],
        1: ["Formula", "フォーミュラー"],
        2: ["Stabilizer", "スタビライザー"],
        3: ["Precision", "プレシジョン"],
        4: ["Wide Jump", "ワイドジャンプ"],
        5: ["Aerial", "エアリアル"],
        6: ["Eclipse", "イクリプス"],
        7: ["Ultimate", "アルティメット"],
        8: ["High Jump", "ハイジャンプ"],
        9: ["Ground", "グランダー"],
        10: ["Quick Jump", "クイックジャンプ"],
        11: ["Feather", "フェザー"],
        12: ["Short Thrust", "ショートバーニア"],
        13: ["Long Thrust", "ロングバーニア"],
        14: ["Swallow", "ヒエン"],
        15: ["Plus One", "プラスワン"],
        16: ["Booster", "ブースター"],
        17: ["Overhaul", "オーバーホール"],
        18: ["Raven", "レイブン"],
        19: ["Prowler", "プロウラー"]
    }
]

global configs
configs = ConfigParser()
configs.read("config.ini")
dirname = "OBS Sources"
pImgPath = "Player Images"
pWinsImgPath = "Victory Images"
langDict = {
    "English": "0",
    "日本語": "1"
}

def loadClearLoop():
    state = configs.get("status", "state")
    dolphin.un_hook()
    dolphin.hook()
    if dolphin.is_hooked():
        if (configs.getboolean("configurations", "autoload") and configs.getboolean("configurations", "autoclear")):
            if state != "loaded" and int.from_bytes(dolphin.read_bytes(0x8024FCF8, 2)) != 0: # robo bytes loaded
                loadParts()
            if state != "cleared" and int.from_bytes(dolphin.read_bytes(0x8024FCF8, 2)) == 0: # robo bytes unloaded
                clearParts()
        elif (configs.getboolean("configurations", "autoload") and int.from_bytes(dolphin.read_bytes(0x8024FCF8, 2)) != 0): # robo bytes loaded
            loadParts()
        elif (configs.getboolean("configurations", "autoclear") and int.from_bytes(dolphin.read_bytes(0x8024FCF8, 2)) == 0):
            clearParts()


    if configs.getboolean("configurations", "autoload") or configs.getboolean("configurations", "autoclear"):
        window.after(500, loadClearLoop)


def loadParts():
    dolphin.hook()

    byteList = [
        0x8040bab7, 0x8040bab9, 0x8040babb, 0x8040babd, 0x8040babf,
        0x8041044b, 0x8041044d, 0x8041044f, 0x80410451, 0x80410453,
        0x80414ddf, 0x80414de1, 0x80414de3, 0x80414de5, 0x80414de7,
        0x80419773, 0x80419775, 0x80419777, 0x80419779, 0x8041977b
    ]
    parts = []
    lang = int(configs.get("configurations", "language"))

    if dolphin.is_hooked():
        
        for byte in byteList:
            value = dolphin.read_byte(byte)
            match configs.get("configurations", "version"):
                case "Vanilla":
                    bodyDict = vanillaParts[0]
                    gunDict = vanillaParts[1]
                    bombDict = vanillaParts[2]
                    podDict = vanillaParts[3]
                    legDict = vanillaParts[4]
                case "Project Hive 3":
                    bodyDict = ph3Parts[0]
                    gunDict = ph3Parts[1]
                    bombDict = ph3Parts[2]
                    podDict = ph3Parts[3]
                    legDict = ph3Parts[4]
                case "Project Hive 3.1":
                    bodyDict = ph3dot1Parts[0]
                    gunDict = ph3dot1Parts[1]
                    bombDict = ph3dot1Parts[2]
                    podDict = ph3dot1Parts[3]
                    legDict = ph3dot1Parts[4]
                    

            if byte in [0x8040bab7, 0x8041044b, 0x80414ddf, 0x80419773]:
                part = bodyDict.get(value)[lang]
            elif byte in [0x8040bab9, 0x8041044d, 0x80414de1, 0x80419775]:
                part = gunDict.get(value)[lang]
            elif byte in [0x8040babb, 0x8041044f, 0x80414de3, 0x80419777]:
                part = bombDict.get(value)[lang]
            elif byte in [0x8040babd, 0x80410451, 0x80414de5, 0x80419779]:
                part = podDict.get(value)[lang]
            elif byte in [0x8040babf, 0x80410453, 0x80414de7, 0x8041977b]:
                part = legDict.get(value)[lang]
            parts.append(part)

        partsChanged = False
        s = [parts[0] + "\n", parts[1] + "\n", parts[2] + "\n", parts[3] + "\n", parts[4]]
        with open(path.join(dirname, "red.txt"), "r", encoding="utf-8") as rf:
            if ("".join(s) != "".join(rf.readlines())):
                partsChanged = True
                with open(path.join(dirname, "red.txt"), "w", encoding="utf-8") as wf:
                    wf.writelines(s)

        s = [parts[5] + "\n", parts[6] + "\n", parts[7] + "\n", parts[8] + "\n", parts[9]]
        with open(path.join(dirname, "blue.txt"), "r", encoding="utf-8") as rf:
            if ("".join(s) != "".join(rf.readlines())):
                partsChanged = True
                with open(path.join(dirname, "blue.txt"), "w", encoding="utf-8") as wf:
                    wf.writelines(s)

        s = [parts[10] + "\n", parts[11] + "\n", parts[12] + "\n", parts[13] + "\n", parts[14]]
        with open(path.join(dirname, "green.txt"), "r", encoding="utf-8") as rf:
            if ("".join(s) != "".join(rf.readlines())):
                partsChanged = True
                with open(path.join(dirname, "green.txt"), "w", encoding="utf-8") as wf:
                    wf.writelines(s)

        s = [parts[15] + "\n", parts[16] + "\n", parts[17] + "\n", parts[18] + "\n", parts[19]]
        with open(path.join(dirname, "yellow.txt"), "r", encoding="utf-8") as rf:
            if ("".join(s) != "".join(rf.readlines())):
                partsChanged = True
                with open(path.join(dirname, "yellow.txt"), "w", encoding="utf-8") as wf:
                    wf.writelines(s)

        currentStatus = statusQueue.cget("text")
        if "Loaded parts to sources" not in currentStatus and partsChanged:
            addStatusText("Loaded parts to sources")

        configs.set("status", "state", "loaded")
    
        with open("config.ini", "w") as configFile:
            configs.write(configFile)


def clearParts():
    with open(path.join(dirname, "red.txt"), "r", encoding="utf-8") as f:
        if f.read() != configs.get("configurations", "cleartext"):

            with open(path.join(dirname, "red.txt"), "w", encoding="utf-8") as f:
                f.write(configs.get("configurations", "cleartext"))

            with open(path.join(dirname, "blue.txt"), "w", encoding="utf-8") as f:
                f.write(configs.get("configurations", "cleartext"))

            with open(path.join(dirname, "green.txt"), "w", encoding="utf-8") as f:
                f.write(configs.get("configurations", "cleartext"))

            with open(path.join(dirname, "yellow.txt"), "w", encoding="utf-8") as f:
                f.write(configs.get("configurations", "cleartext"))

            currentStatus = statusQueue.cget("text")
            if "Cleared parts from sources" not in currentStatus:
                addStatusText("Cleared parts from sources")

            configs.set("status", "state", "cleared")
    
            with open("config.ini", "w") as configFile:
                configs.write(configFile)


def updateSB():
    p1nameStr = p1nameRaw = p1name.get()
    if p1nameStr.endswith(" [L]"):
        p1nameStr = p1nameStr[:-4]
    with open(path.join(dirname, "p1name.txt"), "w") as f:
        f.write(p1nameRaw)
        p1imagePath = path.join(pImgPath, p1nameStr + " - p1.png")
        p1winsImagePath = path.join(pWinsImgPath, p1nameStr + " wins.png")

        p1imageFile = Path(p1imagePath)
        if p1imageFile.is_file():
            shutil.copy(p1imagePath, path.join(pImgPath, "p1.png"))
        else: 
            shutil.copy(path.join(pImgPath, "p1unknown.png"), path.join(pImgPath, "p1.png"))

        p1winsImageFile = Path(p1winsImagePath)
        if p1winsImageFile.is_file():
            shutil.copy(p1winsImagePath, path.join(pWinsImgPath, "p1 wins.png"))
        else:
            shutil.copy(path.join(pWinsImgPath, "unknown wins.png"), path.join(pWinsImgPath, "p1 wins.png"))


    with open(path.join(dirname, "p1wins.txt"), "w") as f:
        f.write(p1nameStr.upper() + " WINS ")

    with open(path.join(dirname, "p1score.txt"), "w") as f:
        f.write(p1score.get())

    p2nameStr = p2nameRaw = p2name.get()
    if p2nameStr.endswith(" [L]"):
        p2nameStr = p2nameStr[:-4]
    with open(path.join(dirname, "p2name.txt"), "w") as f:
        f.write(p2nameRaw)
        p2imagePath = path.join(pImgPath, p2nameStr + " - p2.png")
        p2winsImagePath = path.join(pWinsImgPath, p2nameStr + " wins.png")

        p2imageFile = Path(p2imagePath)
        if p2imageFile.is_file():
            shutil.copy(p2imagePath, path.join(pImgPath, "p2.png"))
        else: 
            shutil.copy(path.join(pImgPath, "p2unknown.png"), path.join(pImgPath, "p2.png"))

        p2winsImageFile = Path(p2winsImagePath)
        if p2winsImageFile.is_file():
            shutil.copy(p2winsImagePath, path.join(pWinsImgPath, "p2 wins.png"))
        else:
            shutil.copy(path.join(pWinsImgPath, "unknown wins.png"), path.join(pWinsImgPath, "p2 wins.png"))
        
    with open(path.join(dirname, "p2wins.txt"), "w") as f:
        f.write(p2nameStr.upper() + " WINS ")

    with open(path.join(dirname, "p2score.txt"), "w") as f:
        f.write(p2score.get())

    addStatusText("Updated scoreboard")


def incDecScore(component):
    if component == "p1plus1":
        curScore = p1score.get()
        p1score.delete(0, 'end')
        p1score.insert(0, int(curScore) + 1)
        with open(path.join(dirname, "p1score.txt"), "w") as f:
            f.write(p1score.get())
    elif component == "p1minus1":
        curScore = p1score.get()
        p1score.delete(0, 'end')
        p1score.insert(0, int(curScore) - 1)
        with open(path.join(dirname, "p1score.txt"), "w") as f:
            f.write(p1score.get())
    elif component == "p2plus1":
        curScore = p2score.get()
        p2score.delete(0, 'end')
        p2score.insert(0, int(curScore) + 1)
        with open(path.join(dirname, "p2score.txt"), "w") as f:
            f.write(p2score.get())
    elif component == "p2minus1":
        curScore = p2score.get()
        p2score.delete(0, 'end')
        p2score.insert(0, int(curScore) - 1)
        with open(path.join(dirname, "p2score.txt"), "w") as f:
            f.write(p2score.get())


def switchSB():
    temp = p1name.get()
    p1name.delete(0, 'end')
    p1name.insert(0, p2name.get())
    p2name.delete(0, 'end')
    p2name.insert(0, temp)
    temp = p1score.get()
    p1score.delete(0, 'end')
    p1score.insert(0, p2score.get())
    p2score.delete(0, 'end')
    p2score.insert(0, temp)
    updateSB()


def updateClearText():
    #read file, compare to clearText, if same then update robo files
    updateRobos = False
    clearText = clearEntry.get(1.0, "end-1c")
    with open(path.join(dirname, "red.txt"), "r") as f:
        if (f.read() == configs.get("configurations", "cleartext")):
            updateRobos = True

    configs.set("configurations", "cleartext", clearText)
    
    with open("config.ini", "w") as configFile:
        configs.write(configFile)

    if updateRobos:
        with open(path.join(dirname, "red.txt"), "w") as f:
            f.write(clearText)
        with open(path.join(dirname, "blue.txt"), "w") as f:
            f.write(clearText)
        with open(path.join(dirname, "green.txt"), "w") as f:
            f.write(clearText)
        with open(path.join(dirname, "yellow.txt"), "w") as f:
            f.write(clearText)


def show(b):
    match b.config("text")[-1]:
        case "Load Parts":
            b.grid(row=1, column=0, columnspan=2)
        case "Clear Parts":
            b.grid(row=1, column=2, columnspan=3)


def hide(b):
    b.grid_forget()


def checkTick(tickVar, tickBox, partsButton):
    if (tickVar.get()):
        s = "true"
        hide(partsButton)
        if not (configs.getboolean("configurations", "autoload") or configs.getboolean("configurations", "autoclear")):
           window.after(500, loadClearLoop)
    else:
        s = "false"
        show(partsButton)
    match tickBox.config("text")[-1]:
        case "Auto Load Parts":
            configs.set("configurations", "autoload", s)
        case "Auto Clear Parts":
            configs.set("configurations", "autoclear", s)
    with open("config.ini", "w") as configFile:
        configs.write(configFile)


def comboBoxConfigUpdate(comboBox, setting):
    if (setting == "language"):
        value = langDict[comboBox.get()]
    else:
        value = comboBox.get()
    configs.set("configurations", setting, value)
    with open("config.ini", "w") as configFile:
        configs.write(configFile)


def addStatusText(newStatus):
    currentStatus = statusQueue.cget("text").split("\n")
    currentStatus.append(newStatus)
    statusQueue.configure(text="\n".join(currentStatus))
    window.after(3000, lambda:popStatusQueue(newStatus))


def popStatusQueue(text):
    currentStatus = statusQueue.cget("text").split("\n")
    currentStatus.remove(text)
    statusQueue.configure(text="\n".join(currentStatus))


def updatePlayerNameList(playerNames, p1name, p2name):
    playerNameString = playerNames.get(1.0, "end-1c")
    playerNameList = playerNameString.split("\n")
    playerNameList = sorted(playerNameList, key=str.casefold)
    for i in range(int(configs.get("playernames", "numplayers"))):
        configs.remove_option("playernames", "player" + str(i))
    configs.set("playernames", "numplayers", str(len(playerNameList)))
    for i in range(len(playerNameList)):
        configs.set("playernames", "player" + str(i), playerNameList[i])
    with open("config.ini", "w") as configFile:
        configs.write(configFile)
    playerNameString = "\n".join(playerNameList)
    playerNames.delete(1.0, "end-1c")
    playerNames.insert(1.0, playerNameString)
    p1name["values"] = playerNameList
    p2name["values"] = playerNameList


def updateTourneyInfo(tourneyName, tourneyRound):
    with open(path.join(dirname, "tourney.txt"), "w") as f:
        f.write(tourneyName.get())
    with open(path.join(dirname, "round.txt"), "w") as f:
        f.write(tourneyRound.get())
    addStatusText("Updated tourney info")


def saveBuilds(p1name, p2name, tourneyName):
    p1nameStr, p2nameStr = p1name.get(), p2name.get()
    if (p1nameStr.endswith(" [L]")):
        p1nameStr = p1nameStr[:-4]
    if (p2nameStr.endswith(" [L]")):
        p2nameStr = p2nameStr[:-4]
    redParts = []
    blueParts = []
    greenParts = []
    yellowParts = []
    with open(path.join(dirname, "red.txt"), "r") as f:
        redParts = f.readlines()
    with open(path.join(dirname, "blue.txt"), "r") as f:
        blueParts = f.readlines()
    with open(path.join(dirname, "green.txt"), "r") as f:
        greenParts = f.readlines()[:-1]
    with open(path.join(dirname, "yellow.txt"), "r") as f:
        yellowParts = f.readlines()[:-1]
    for parts in redParts, blueParts, greenParts, yellowParts:
        for i in range(len(parts)):
            parts[i] = parts[i].replace("\n", "")
    filename = "builds.xlsx"
    curSheetname = tourneyName.get() + " " + str(datetime.date.today())
    df = pd.DataFrame([[p1nameStr] + redParts + blueParts, [p2nameStr] + greenParts + yellowParts], columns=["Player", "Robo1", "Gun1", "Bomb1", "Pod1", "Legs1", "Robo2", "Gun2", "Bomb2", "Pod2", "Legs2"])
    if Path(filename).is_file():
        xl = pd.ExcelFile(filename)
        existingDfs = {sheet_name: xl.parse(sheet_name).drop(columns="Unnamed: 0") for sheet_name in xl.sheet_names}
        with pd.ExcelWriter(filename) as writer:
            for sheetname in existingDfs:
                existingDf = existingDfs[sheetname]
                if sheetname == curSheetname:
                    existingDf = existingDf._append(df)
                existingDf.to_excel(writer, sheet_name=sheetname)
            if curSheetname not in existingDfs:
                df.to_excel(writer, sheet_name=curSheetname)
    else:
        df.to_excel(filename, sheet_name=curSheetname)
    addStatusText("Saved builds to '" + filename + "'")



window = tk.Tk()
window.title("CRBR Overlay Manager")
window.iconbitmap(path.join("..", "assets", "crom.ico"))

### tabs
tabs = ttk.Notebook(window)
mainTab = ttk.Frame(tabs)
configTab = ttk.Frame(tabs)
tabs.add(mainTab, text="Main")
tabs.add(configTab, text="Config")
tabs.grid(row=0, column=0)

### main tab
## parts components
loadPartsButton = ttk.Button(mainTab, text="Load Parts", command=loadParts)
if not configs.getboolean("configurations", "autoload"):
    loadPartsButton.grid(row=1, column=0, columnspan=2)

clearPartsButton = ttk.Button(mainTab, text="Clear Parts", command=clearParts)
if not configs.getboolean("configurations", "autoclear"):
    clearPartsButton.grid(row=1, column=2, columnspan=3)

savePartsButton = ttk.Button(mainTab, text="Save Parts", command=lambda:saveBuilds(p1name, p2name, tourneyName))
savePartsButton.grid(row=0, column=5, columnspan=2)

## scoreboard components
playerNameList = []
for i in range(int(configs.get("playernames", "numplayers"))):
    playerNameList.append(configs.get("playernames", "player" + str(i)))
playerNameList = sorted(playerNameList, key=str.casefold)
p1label = ttk.Label(mainTab, text="P1:")
p1label.grid(row=3, column=0)
p1nameVar = tk.StringVar()
p1name = ttk.Combobox(mainTab, width=16, textvariable=p1nameVar)
p1name.grid(row=4, column=0, columnspan=3, padx=7)
p1name["values"] = playerNameList

p2label = ttk.Label(mainTab, text="P2:")
p2label.grid(row=3, column=4)
p2nameVar = tk.StringVar()
p2name = ttk.Combobox(mainTab, width=16, textvariable=p2nameVar)
p2name.grid(row=4, column=4, columnspan=3, padx=7)
p2name["values"] = playerNameList

p1score = ttk.Entry(mainTab, width=4)
p1score.grid(row=5, column=1)
p1score.insert(0, "0")

p1minus1 = ttk.Button(mainTab, text="-1", width=3, command=lambda:incDecScore("p1minus1"))
p1minus1.grid(row=5, column=0)
p1plus1 = ttk.Button(mainTab, text="+1", width=3, command=lambda:incDecScore("p1plus1"))
p1plus1.grid(row=5, column=2)

p2score = ttk.Entry(mainTab, width=4)
p2score.grid(row=5, column=5)
p2score.insert(0, "0")

p2minus1 = ttk.Button(mainTab, text="-1", width=3, command=lambda:incDecScore("p2minus1"))
p2minus1.grid(row=5, column=4)
p2plus1 = ttk.Button(mainTab, text="+1", width=3, command=lambda:incDecScore("p2plus1"))
p2plus1.grid(row=5, column=6)

switch = ttk.Button(mainTab, text="<->", width=4, command=switchSB)
switch.grid(row=4, rowspan=2, column=3)

updateSbButton = ttk.Button(mainTab, text="Update SB", command=updateSB)
updateSbButton.grid(row=0, column=0, columnspan=2, padx=10, pady=7)

## tourney info
tnLabel = ttk.Label(mainTab, text="Event:")
tnLabel.grid(row=7, column=0)
tourneyName = ttk.Entry(mainTab)
tourneyName.grid(row=8, column=0, columnspan=3)
trLabel = ttk.Label(mainTab, text="Round:")
trLabel.grid(row=7, column=4)
tourneyRound = ttk.Entry(mainTab)
tourneyRound.grid(row=8, column=4, columnspan=3)
tourneyInfoButton = ttk.Button(mainTab, text="Update Tourney", command=lambda:updateTourneyInfo(tourneyName, tourneyRound))
tourneyInfoButton.grid(row=0, column=2, columnspan=3)


## status queue
statusQueue = ttk.Label(mainTab, justify="center")
statusQueue.grid(row=9, column=0, columnspan=7)

### config
## clear text
ceLabel = ttk.Label(configTab, text="Clear Text:")
ceLabel.grid(row=0, column=0)
clearEntry = tk.Text(configTab, width=16, height=4, font=("Arial", 9))
clearEntry.grid(row=1, rowspan=2, column=0, columnspan=2)
clearEntry.insert(1.0, configs.get("configurations", "cleartext"))

saveClearText = ttk.Button(configTab, text="Save", width=5, command=updateClearText)
saveClearText.grid(row=0, column=1)

## player names
pnLabel = ttk.Label(configTab, text="Player Names:")
pnLabel.grid(row=0, column=2)
playerNames = tk.Text(configTab, width=16, height=4, font=("Arial", 9))
playerNames.grid(row=1, rowspan=2, column=2, columnspan=2)
playerNameList = []
for i in range(int(configs.get("playernames", "numplayers"))):
    playerNameList.append(configs.get("playernames", "player" + str(i)))
playerNameString = "\n".join(playerNameList)
playerNames.insert(1.0, playerNameString)
savePlayerNames = ttk.Button(configTab, text="Save", width=5, command=lambda:updatePlayerNameList(playerNames, p1name, p2name))
savePlayerNames.grid(row=0, column=3)

## patch
patchLabel = ttk.Label(configTab, text="Version")
patchLabel.grid(row=3, column=0)
patchVar = tk.StringVar()
patchComboBox = ttk.Combobox(configTab, width=15, textvariable=patchVar, state="readonly")
patchComboBox.grid(row=4, column=0, columnspan=2, padx=10)
patchComboBox["values"] = ("Vanilla", "Project Hive 3", "Project Hive 3.1")
patchComboBox.bind("<<ComboboxSelected>>", lambda _:comboBoxConfigUpdate(patchComboBox, "version"))
patchComboBox.set(configs.get("configurations", "version"))

## language
langLabel = ttk.Label(configTab, text="Language/言語")
langLabel.grid(row=5, column=0)
langVar = tk.StringVar()
langComboBox = ttk.Combobox(configTab, width=15, textvariable=langVar, state="readonly")
langComboBox.grid(row=6, column=0, columnspan=2, padx=10)
langComboBox["values"] = ("English", "日本語")
langComboBox.bind("<<ComboboxSelected>>", lambda _:comboBoxConfigUpdate(langComboBox, "language"))
tar = configs.get("configurations", "language")
for key, val in langDict.items():
    if val == tar:
        configLang = key
langComboBox.set(configLang)

## autoload
loadTickVar = tk.BooleanVar()
loadTickVar.set(configs.getboolean("configurations", "autoload"))
loadTickBox = ttk.Checkbutton(configTab, text="Auto Load Parts", variable=loadTickVar, command=lambda:checkTick(loadTickVar, loadTickBox, loadPartsButton))
loadTickBox.grid(row=3, rowspan=2, column=2, columnspan=2, padx=10, pady=7)
clearTickVar = tk.BooleanVar()
clearTickVar.set(configs.getboolean("configurations", "autoclear"))
clearTickBox = ttk.Checkbutton(configTab, text="Auto Clear Parts", variable=clearTickVar, command=lambda:checkTick(clearTickVar, clearTickBox, clearPartsButton))
clearTickBox.grid(row=5, rowspan=2, column=2, columnspan=2, padx=10, pady=7)

if configs.getboolean("configurations", "autoload") or configs.getboolean("configurations", "autoclear"):
    loadClearLoop()
window.mainloop()