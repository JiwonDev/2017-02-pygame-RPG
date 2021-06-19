# -*- coding:utf-8 -*-
'''
Created on 2016. 11. 29.
#-*-coding:utf-8-*-
@author: Jiwon
'''
import pygame as pg


class Component(pg.sprite.Sprite):
    '''
    classdocs
    컴포넌트 기본틀(인터페이스)
    '''
    _comType = None  # 컴포넌트 타입(부모)
    _comName = None  # 이름

    _comList = []

    def __init__(self, comType, name):
        pg.sprite.Sprite.__init__(self)
        self._comType = comType
        self._comName = name

    def addComponent(self, components):  # 컴퍼넌트 추가
        if (isinstance(components, list)):
            for com in components:
                self._addOne(com)
        else:
            self._addOne(components)

    def _addOne(self, component):
        assert (component.getType() != self._comType),\
            str(self) + " _ " + str(component) + " 자기자신과 같은타입은 컴포넌트로 등록 할 수없습니다."

        for com in self._comList:
            assert (str(component) != str(com)),\
                str(self) + " _ " + str(component) + "는 이미 존재하는 컴포넌트입니다."

        self._comList.append(component)

    def removeComponent(self, component):  # 컴퍼넌트 삭제
        deleteCheck = False
        for i in range(0, len(self._comList)):
            if (str(component) == str(self._comList[i])):
                deleteCheck = True
                del self._comList[i]
                break;
        if (deleteCheck == False):
            print(str(self) + " _ " + str(component) + "는 존재하지 않아 삭제불가능합니다.")

    def getList(self):
        return self._comList

    def getType(self):
        return self._comType

    def getName(self):
        return self._comName

    def __str__(self):
        return "(" + self._comType + "):" + self._comName
