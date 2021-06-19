# -*- coding:utf-8 -*-
'''
Created on 2016. 12. 2.

@author: Jiwon
'''

# state 충돌할때 바뀌는걸로 (중력도) 고치기
# 공격, 슬라이드, 투척 모션
# 표창 컴퍼넌트 만들기
# 적만들기
# 맵만들기

import os, time
import sys

from pygame.locals import *

import Component.Block
import Component.Player_Ninja
import Data
import EventChecker
import Map.Level
import pygame as pg


def write(location, message, size=50, color=Data.Color.black):
    font = pg.font.Font(Data.Resource.font, size)
    font = font.render(message, True, color)
    rect = font.get_rect()
    rect.x = location[0]
    rect.y = location[1]
    return font, rect


def showLoading(display):
    # 로딩화면 재생
    loadimage = pg.image.load(Data.Resource.load)
    loadrect = loadimage.get_rect()
    loadrect.x += 200
    loadrect.y += 220
    display.fill(Data.Color.white)
    display.blit(loadimage, loadrect)
    pg.display.update()


def runGame():
    ## 0. pygame 초기화 ##
    display = pg.display.set_mode(Data.window, HWSURFACE | DOUBLEBUF)  # display 객체
    pg.display.set_caption("I DON'T AVOID - 2015642028 김지원")
    input = EventChecker.InputEvent()  # 이벤트 객체
    clock = pg.time.Clock()  # fps객체

    ## 1. player, block, map,기타등등 초기화 ##
    player = Component.Player_Ninja.Player_Ninja("player1", showChoice(input, display))  # 플레이어 생성
    pg.mixer.music.load(Data.Resource.bgm)

    # 로딩화면 재생
    showLoading(display)
    smokeimage = pg.image.load(Data.Resource.smoke).convert_alpha()
    smokerect = smokeimage.get_rect()
    winImage = pg.image.load(Data.Resource.win).convert_alpha()

    block_group = Component.Block.BlockGroup("level1")  # 블럭그룹 생성
    map = Map.Level.Level1(block_group)  # 맵 생성(블럭그룹 초기화)
    background = map.getBackground()

    selImage = []  # 선택창
    selImage.append(pg.image.load(Data.Resource.select1).convert_alpha())
    selImage.append(pg.image.load(Data.Resource.select2).convert_alpha())
    selImage.append(pg.image.load(Data.Resource.select3).convert_alpha())

    ## 2. sprite group으로 묶음 ##
    blockList = block_group.getList()  # 블럭들

    character_layer = pg.sprite.RenderPlain(*[player])
    block_layer = pg.sprite.RenderPlain(*blockList)

    # 배경위치 설정(카메라)
    background_start_x = -(background.get_size()[0] / 3)
    backgroundRect = [background_start_x, 0]
    display.blit(background, backgroundRect)  # 배경그리기

    player.updateCollide(block_layer)
    smokeStart = False

    smokeHigh = 0
    pg.mixer.music.play(-1, 0)
    time
    deadTime = 0
    ## 1. 게임 메인 루프 ##
    while (True):
        input.check()  # 이벤트 확인

        # 죽었다면 리스폰, 연기 초기화
        if (player.state.getName() == Data.Action.dead
                and input.getTime() - deadTime > 5000):  # 죽으면 개념세이브?
            player.setPlayerLocation(400, 400)
            player.state.setState(Data.Action.idle)
            player.state.setFrame(Data.Action.idle)
            pg.mixer.music.rewind()
            smokeHigh = 0
            smokeStart = False
            deadTime = 0

        if (input.isExit() or input.getKey() == K_ESCAPE):
            break;

        # Clear
        if (player.realLocation[0] < -1700):
            rect = winImage.get_rect()
            rect.x += 100
            rect.y += 100
            display.blit(winImage, rect)
            pg.display.update()
            time.sleep(3)
            break;

        # 카메라 업데이트

        cam_x, cam_y = updateCamera(player, blockList, block_layer)

        # 움직이는 배경그리기
        backgroundRect[0] -= cam_x / 10
        #         backgroundRect[1] -= cam_y/100 #그림이 작아서 못움직임
        display.blit(background, backgroundRect)

        # 업데이트

        player.updateCollide(block_layer)
        character_layer.update(input)

        # 나머지 그리기
        block_layer.draw(display)
        character_layer.draw(display)

        # 일정 높이 이하로 떨어지면 연기가 움직이기 시작(닿이면 죽어요..!)
        if (player.realLocation[1] < -6500 and smokeStart == False):
            smokeStart = True

        # 연기가 시작했는지 확인
        if (smokeStart):
            smokerect, smokeHigh = updateSmoke(player, smokeimage, smokerect, smokeHigh)
            display.blit(smokeimage, smokerect)
            display.blit(smokeimage, (smokerect.x - 300, smokerect.y))
            display.blit(smokeimage, (smokerect.x + 400, smokerect.y))
            # 연기가 플레이어 높이-50보다 높다면 사망
            if (smokerect.y < player.location[1] - 50):
                player.state.dead()
                font, rect = write((10, 200), "아래에서 나오는 연기는 위험합니다. 빠르게 올라가세요!", 40)
                display.blit(font, rect)
                if (deadTime == 0):
                    deadTime = input.getTime()
        # 전체 화면 및 FPS설정
        pg.display.update()
        clock.tick(Data.FPS)


def showChoice(input, display):
    sel = []
    sel.append(pg.image.load(Data.Resource.select1))
    sel.append(pg.image.load(Data.Resource.select2))
    sel.append(pg.image.load(Data.Resource.select3))

    number = 0
    clock = pg.time.Clock()
    display.fill(Data.Color.white)
    while (True):
        input.check()
        key = input.getKey()
        if (input.isExit() or key == K_ESCAPE):
            pg.quit()
            sys.exit()
        if (key == K_LEFT):
            number = 1
        elif (key == K_RIGHT):
            number = 2
        elif (key == K_RETURN):
            break;
        rect = sel[number].get_rect()
        rect.x += -70
        rect.y += 10
        display.blit(sel[number], rect)
        pg.display.update()
        clock.tick(30)

    if (number == 1):
        return True
    else:
        return False


def updateSmoke(player, smokeimage, smokerect, up):
    cam_y = 0
    new = [0, 0]  # 바뀔위치

    if (player.location[1] < Data.ground_y[0]):
        cam_y = Data.ground_y[0] - player.location[1]
        player.realLocation[1] += int(cam_y)
        player.location[1] = Data.ground_y[0]

    elif (player.location[1] > Data.ground_y[1]):
        cam_y = Data.ground_y[1] - player.location[1]
        player.realLocation[1] += int(cam_y)
        player.location[1] = Data.ground_y[1]

    new[1] = (130 * 64) - (player._startLocation[1] - player.realLocation[1])
    smokerect.y = new[1] + up
    up -= 0.2
    return smokerect, up


def updateCamera(player, blockList, blockLayer):
    cam_x = 0
    cam_y = 0
    new = [0, 0]  # 바뀔위치
    # x카메라
    if (player.location[0] < Data.ground_x[0]):
        cam_x = Data.ground_x[0] - player.location[0]
        player.realLocation[0] += int(cam_x)
        player.location[0] = Data.ground_x[0]
    elif (player.location[0] > Data.ground_x[1]):
        cam_x = Data.ground_x[1] - player.location[0]
        player.realLocation[0] += int(cam_x)
        player.location[0] = Data.ground_x[1]

    if (player.location[1] < Data.ground_y[0]):
        cam_y = Data.ground_y[0] - player.location[1]
        player.realLocation[1] += int(cam_y)
        player.location[1] = Data.ground_y[0]

    elif (player.location[1] > Data.ground_y[1]):
        cam_y = Data.ground_y[1] - player.location[1]
        player.realLocation[1] += int(cam_y)
        player.location[1] = Data.ground_y[1]

    # x축 블럭배치
    oneTime = True
    length = [0, 0]
    for com in blockList:

        new[0] = (com._location[1] * 64) - (player._startLocation[0] -\
                                            player.realLocation[0]) + com._edit[0]
        if (oneTime):
            length[0] = new[0] - com.rect.x
            oneTime = False

        com.rect.x = new[0]

    # x축 충돌해결
    collideList = pg.sprite.spritecollide(player.realRect, blockLayer, False)
    while (len(collideList) > 0):  # 블럭과 충돌했다면
        if (length[0] > 0):  # 오른쪽으로 갔다면
            player.pushPlayer(1, 0)
        else:  # 반대
            player.pushPlayer(-1, 0)
        collideList = pg.sprite.spritecollide(player.realRect, blockLayer, False)

    # y축 블럭배치
    oneTime = True
    for com in blockList:

        new[1] = (com._location[0] * 64) - (player._startLocation[1] -\
                                            player.realLocation[1]) + com._edit[1]
        if (oneTime):
            length[1] = new[1] - com.rect.y
            oneTime = False
        com.rect.y = new[1]

    # y축 충돌 해결
    collideList = pg.sprite.spritecollide(player.realRect, blockLayer, False)
    while (len(collideList) > 0):  # 블럭과 충돌했다면
        if (length[1] > 0):  # 아래로갔다면
            player.pushPlayer(0, 1)
        else:  # 반대
            player.pushPlayer(0, -1)
        collideList = pg.sprite.spritecollide(player.realRect, blockLayer, False)

    return (int(cam_x), int(cam_y))


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)  # 화면위치

    pg.init()  # pygame초기화
    runGame()

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
