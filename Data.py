# -*- coding:utf-8 -*-
'''
Created on 2016. 11. 29.

@author: Jiwon
상수 데이터 파일
'''
import pygame
from pygame.locals import *
import os

# key


# 창
window_width = 1152
window_height = 864
window = [window_width, window_height]

# FPS
FPS = 30

# Key

showStatMessage = True

# Player basic state

# idle, *collide, dead, Immortal - collide는 모션중에 발생
# move, jump ,dash, fall, climb
# action, throw, attack, block, skill

# location[] , speed[] , speedRate[] , playerStat[]
# collideList[] , state , player(Component)

# ninjaImage - (58, 110)
player_HP = 100
player_SP = 100
player_moveSpeed = 8
player_runSpeed = 14
player_maxSpeed = 30
player_maxGravity = 20
player_jumpSpeed = -17  # 점프 높이
ground_x = [300, 750]
ground_y = [280, 600]

player_rect = [60, 110]
player_dashRect = [30, 110]

gravity = 1

# playerSize = (40,80)

west, left = "left", "left"
east, right = "right", "right"
north, up = "up", "up"
south, down = "down", "down"
overlap = "overlap"


class Key:
    LEFT = K_LEFT
    RIGHT = K_RIGHT
    UP = K_UP
    DOWN = K_DOWN
    JUMP = K_s
    DASH = K_d

    SHIFT = K_LSHIFT
    ATTACK = K_1
    THROW = K_2


def removeDirSuffix(sDir, suffixList):
    for suffix in suffixList:
        if (str(sDir).endswith(suffix)):
            sDir = sDir[0:len(sDir) - len(suffix)]
            break
    return sDir


class Action:
    dead = "dead"
    idle = "idle"
    attack = "attack"
    climb = "climb"
    run = "run"
    move = "move"
    dash = "dash"
    throw = "throw"
    jump = "jump"
    jump_attack = "jumpattack"
    jump_throw = "jumpthrow"

    skill = "skill"
    collide = "collide"
    fall = "fall"
    action = "action"
    attack = "attack"
    block = "block"
    Immortal = "Immortal"


class Block:
    bridge = "bridge"
    cloud = "cloud"
    grass = "grass"
    plant = "plant"
    temple = "temple"


ninja_all_frame = [Action.dead, Action.idle, Action.attack, Action.climb, Action.move, Action.dash, Action.throw,
                   Action.jump, Action.jump_attack, Action.jump_throw]
block_all = [Block.bridge, Block.cloud, Block.grass, Block.plant, Block.temple]


class Resource:
    startDir = removeDirSuffix(os.getcwd(), ["\\Component"])
    resDir = startDir + "\\resources"

    bgm = resDir + "\\sound\\music\\bgm.mp3"

    select1 = resDir + "\\graphic\\select1.png"
    select2 = resDir + "\\graphic\\select2.png"
    select3 = resDir + "\\graphic\\select3.png"
    win = resDir + "\\graphic\\win.png"
    font = resDir + "\\font.otf"
    load = resDir + "\\graphic\\loading.png"
    smoke = resDir + "\\graphic\\smoke.png"
    background = resDir + "\\graphic\\background.png"
    ninja_boy = resDir + "\\graphic\\player\\ninja_boy\\"
    ninja_girl = resDir + "\\graphic\\player\\ninja_girl\\"

    ninja_imgName = {}
    ninja_imgCount = {}
    ninja_imgType = {}

    ninja_imgCount[Action.dead] = 3

    ninja_imgName[Action.dead] = "Dead__"
    ninja_imgName[Action.idle] = "Idle__"
    ninja_imgName[Action.attack] = "Attack__"
    ninja_imgName[Action.climb] = "Climb__"
    ninja_imgName[Action.move] = "Run__"
    ninja_imgName[Action.dash] = "Slide__"
    ninja_imgName[Action.throw] = "Throw__"
    ninja_imgName[Action.jump] = "Jump__"
    ninja_imgName[Action.jump_attack] = "Jump_Attack__"
    ninja_imgName[Action.jump_throw] = "Jump_Throw__"

    for frame in ninja_all_frame:
        ninja_imgType[frame] = ".png"
        if (frame == Action.climb):
            ninja_imgCount[frame] = 2
        else:
            ninja_imgCount[frame] = 10

    block_imgName = {}
    block_imgDir = {}
    block_imgType = {}

    block_imgDir[Block.grass] = resDir + "\\graphic\\block\\grass\\"
    block_imgDir[Block.bridge] = resDir + "\\graphic\\block\\bridge\\"
    block_imgDir[Block.cloud] = resDir + "\\graphic\\block\\cloud\\"
    block_imgDir[Block.plant] = resDir + "\\graphic\\block\\plant\\"
    block_imgDir[Block.temple] = resDir + "\\graphic\\block\\temple\\"

    block_imgName[Block.bridge] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    block_imgName[Block.cloud] = ["0", "1", "2", "3", "4"]
    block_imgName[Block.grass] = ["0", "1", "2", "3", "4", "5", "6", "7", ]
    block_imgName[Block.plant] = ["0", "1", "2"]
    block_imgName[Block.temple] = ["0", "1", "2", "3", "4", "5", "6"]

    for type in block_all:
        block_imgType[type] = ".png"


class Event:
    userEventList = []

    resetPlayer = USEREVENT + 1
    userEventList.append(resetPlayer)


class Color:
    gameSky = (0, 87, 184)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 128, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    orange = (255, 165, 0)
    gold = (255, 215, 0)
    skyblue = (135, 206, 234)
    pink = (255, 105, 180)
    gray = (128, 128, 128)


class Type:
    character = "characterType"
    block = "blockType"
    blockGroup = "blockGroupType"
