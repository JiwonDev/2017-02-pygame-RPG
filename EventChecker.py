# -*- coding:utf-8 -*-
'''
Created on 2016. 11. 29.

@author: Jiwon
'''
import pygame as pg
from pygame import *
import Data as value
import time


class InputEvent(object):
    '''
    classdocs
    사용자 입력확인 클래스
    사용하기 전 pygame.init() 을 실행시켜주어야 합니다.
    '''
    K_ALT = K_LALT
    K_CTRL = K_LCTRL
    K_SHIFT = K_LSHIFT

    _currentTime = None
    # 키보드 정보
    _currentKey = None
    _functionKey = {K_SHIFT: False, K_ALT: False, K_CTRL: False}
    _currentPress = None

    # 마우스 정보
    _mousePos = [0, 0]
    _mouseClick = False
    _mouseVisible = True

    # 종료 이벤트 정보
    _exitEvent = False

    # 사용자 이벤트 정보
    _userEvent = []

    # 입력가능한 키 목록
    valid_functionKey_list = set([K_LSHIFT, K_LCTRL, K_LALT])
    valid_specialKey_list = set([K_INSERT, K_HOME, K_PAGEDOWN, K_PAGEUP, K_END, K_DELETE])
    valid_key_list = set([K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_s, K_d, K_f, K_SPACE, K_RETURN])

    valid_key_list.update(valid_specialKey_list)

    def __init__(self):
        pass

    def check(self):
        self._currentTime = time.time() * 1000
        for event in pg.event.get():
            # 윈도우 종료 이벤트
            if (event.type == QUIT):
                self._exitEvent = True
                break;

            # 특수키 press 확인
            pressKey = pg.key.get_pressed()
            self._currentPress = pressKey
            for fkey in self._functionKey.keys():
                if (pressKey[fkey] == 0):
                    self._functionKey[fkey] = False
                else:
                    self._functionKey[fkey] = True

            # 일반키 상태 업데이트
            if (event.type == KEYDOWN and (event.key in self.valid_key_list)):
                self._currentKey = event.key

            # 일반키 Press 해제
            elif (event.type == KEYUP and event.key == self._currentKey):
                self._currentKey = None

                # 마우스 클릭 상태 업데이트
            elif (event.type == MOUSEBUTTONUP):
                self._mousePos = pg.mouse.get_pos()
                self._mouseClick = True

            # 사용자 이벤트
            elif (event.type in value.Event.userEventList):
                self._userEvent.append(event.type)

    def setMouseVisible(self, bool=True):
        # 마우스 드러내기/숨기기
        self._mouseVisible = bool
        pg.mouse.set_visible(bool)

    def getKey(self):
        # 현재 입력된 키
        return self._currentKey

    def getFuncKey(self):
        # 현재 입력된 기능키
        return self._functionKey

    def getShift(self):
        return self._functionKey[self.K_SHIFT]

    def getAlt(self):
        return self._functionKey[self.K_ALT]

    def getCtrl(self):
        return self._functionKey[self.K_CTRL]

    def getPos(self):
        # 현재 마우스 위치
        self._mousePos = pg.mouse.get_pos()
        return self._mousePos

    def getClick(self):
        click = self._mouseClick
        self._mouseClick = False
        # 현재 마우스 클릭상태
        return click

    def removeValidKey(self, key):
        # 유효키 삭제하기
        try:
            self.valid_key_list.remove(key)
        except:
            print("InputEvent - (removeValidKey) 존재하지 않는 키를 삭제요청하였습니다.")

    def getEvent(self):  # 이벤트 리스트를 반환
        event = self._userEvent
        self._userEvent = []
        return event

    def getPress(self):
        return self._currentPress

    def addVaildKey(self, key):
        # 유효키 추가하기
        self.valid_key_list.add(key)

    def getValidKeyList(self):
        # 유효한 키 목록
        return tuple(self.valid_key_list)

    def getTime(self):
        return self._currentTime

    def isExit(self):
        return self._exitEvent
