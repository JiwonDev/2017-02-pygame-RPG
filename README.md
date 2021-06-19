# 2017-02-pygame-RPG
pygame을 이용한 2D RPG게임입니다.<br/>
맨날 콘솔창으로만 개발하다보니 심심해서 만들었던 게임입니다.<br/>
시작은 몬스터를 잡는 메#플스토리 같은 게임으로 기획했지만 개발하면서 생기는 수많은 오류들과 시간이 너무 많이들어가 점프맵으로 바뀐 슬픈 프로젝트<br/>
다음에 유니티를 배워서 제대로 한번 만들어볼까 생각해보고 있습니다.

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/26001202/122640134-baf62780-d138-11eb-952b-9547c14308ac.gif)

<br/>
<hr/>

# pygame?

파이썬 2D 게임을 만드는 라이브러리입니다. 상업적인 게임을 릴리즈하기에는 무리가 있고 (배포가 힘듬) 토이 프로젝트로 만들면 재밌습니다<br/>
리소스는 무료이미지, 사운드를 여기저기 모아서 사용했습니다.
파이게임은 기본적으로 아래와 같은 코드가 필요합니다.
```
0. 기본값 및 상수 설정
1. 라이브러리 초기화(initialize)
- (반복루프) -
- 2. 사용자 입력처리(event listen)
- 3. 게임 상태 업데이트(update)
- 4. 게임 상태 그리기(surface, draw)
- FPS 딜레이 (FPS Tick)
- - - - - - - - - -
5. 라이브러리 종료 및 시스템 종료(quit)
```
2017년 당시 pygame에 대해 공부했던 내용들입니다.

### 0. 기본값 및 상수 설정
- 특정 객체를 사용할 때,(소리,그림등) 초기화를 해야하는지 정도는 숙지하자. (안하면 나중에 빅엿먹는다)
- 되도록이면 문자열, 상수값들을 상수용 변수에 넣어서 사용하자.(안하면 추가,수정할때 매우 고통받을 것이다.)

### 1. 라이브러리 초기화(initialize)
python 라이브러리는 매-우 많다. 포기하지말고 갓 구글님께 한번 물어보고 라이브러리를 찾아쓰자.

## - (반복루프) -

### - 2. 사용자 입력처리(event listen)

pygame이 처리 할 수 있는 이벤트 종류는 상당히 많은데, 너무 많으니까 다음장에 알아보자.

### - 3. 게임 상태 업데이트(update)

우리가 그림그릴 판이다.
플레이어, 게임요소, 적등 원하는 것들을 객체를 만들고 서로 상호작용하도록 만들자.

### - 4. 게임 상태 그리기(surface, draw)

그리는 것도있고, 원래 있던것을 수면위로 띄우는(surface, 업데이트하는)것도 있다.
image파일은 불러오는데 오래걸리니까, 게임 시작하기 전에 미리 다 불러와놓고 시작하자.
충돌처리는 대부분 도형(ex 사각형 -> rect)을 덧씌워서 처리한다.
간혹 업데이트 잘 했는데 그림그리는걸 틀려서 애먹는 경우도 있으므로, 숙지하도록 하자.

### - FPS 딜레이 (FPS Tick)

tick이다. 이걸 안걸면 fps가 너무 빨라 렉걸린다.
pygame.time.Clock()로 받아서 쓸 수 있으니까 꼭 기억하자.

```python
''' 예시 (실제 코드 X) '''
#주의 : 실제코드가 아닙니다. 당연히 복붙하면 작동안되요.#
import pygame//pygame 라이브러리
import sys, os//필요한 라이브러리들

//#0. 기본값 설정
//       R  G  B 값
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

//게임용 변수
KeyDown = false;//키보드가 눌렸는지 확인
userHit = false;//user가 맞았는지 확인용
runCheck = false;//게임종료 확인용

//화면크기
screen_width = 700
screen_height = 400

//#1. 라이브러리 초기화
pygame.init() # pygame 초기화
screen = pygame.display.set_mode((scrren_width,screen_height)) // 화면객체 설정
clock = pygame.time.Clock() // fps tick용 객체 설정

screen.fill(white) // 배경을 흰색으로 채우기


//#- (반복루프) -
while(runCheck):
// #2) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runCheck = false
        if 사용자의 마우스클릭:
            keyDown = true
            userHit = true

// #3) 게임 상태 업데이트
    if 화면밖으로 나갔다면:
        error.update(player.Out)
    else 플레이어가 맞았다면
        hp.update(-10)

// #4) 게임 상태 그리기
    screen.display.filp() // 스크린에 덮어씌워진(반영안된) 배경그림 새로 그리기

    runner_img = pygame.image.load("runner.png")//이미지 파일 불러오기
    runner_rect = runner_img.get_rect()//해당 이미지 파일의 사각형(충돌확인)
    screen.blit(runner_img, runner_rect)
    //blit = bit block - image transfer, 이미지파일과 충돌확인용 사각형 합쳐서 그리기
    
    pygame.display.filp()// 업데이트 된 내용을 화면에 반영하기
    
// #FPS 딜레이
    clock.tick(60) //60프레임용 딜레이

//#5. 라이브러리 및 시스템 종료
pygame.quit()
sys.quit()

```

<br/>
<hr/>


# 0. 버그 죽여줘..

개발하면서 캐릭터의 상태변경 (이동->점프->대쉬 등)이나 속도에 관련된 버그가 많았습니다.
그래서 콘솔창을 이용해 실시간으로 현재좌표, 절대좌표, 캐릭터의 상태값, 충돌된 블럭, 속도, 가속도, 현재프레임(캐릭터 스프라이트)을 확인 할 수 있습니다.
콘솔창을 확인하시면 캐릭터를 어떤식으로 구현했는지 알 수 있으며 거슬린다면 Data.py 에서 끌 수 있습니다.
```python
# data.py #

# 창
window_width = 1152
window_height = 864
window = [window_width, window_height]

# FPS
FPS = 30

# stat on/off
showStatMessage = True # 여기를 False로 하면 콘솔이 꺼집니다.
...
```

<br/>
<hr/>


# 1. 캐릭터 선택창

캐릭터를 선택 할 수 있습니다. 참고로 초기기획에는 몬스터까지 다 구현할 생각이였어서 캐릭터에 공격모션과 체력 데이터가 있긴합니다. (사용X) <br/>

캐릭터 (Player_Ninja.py)에서는 각 캐릭터의 이미지 경로(Data.py와 연결), 상태 데이터값, 행동값을 가지고 있습니다.
캐릭터를 선택하는 코드는 다음과 같습니다.

```python
    ## 0. pygame 초기화 ##
    display = pg.display.set_mode(Data.window, HWSURFACE | DOUBLEBUF)  # display 객체
    pg.display.set_caption("I DON'T AVOID - 2015642028 김지원")
    input = EventChecker.InputEvent()  # 이벤트 객체
    clock = pg.time.Clock()  # fps객체

    ## 1. player, block, map,기타등등 초기화 ##
    player = Component.Player_Ninja.Player_Ninja("player1", showChoice(input, display))  
    # 플레이어 생성, showChoice는 선택한 캐릭터값을 반환합니다.
    
    pg.mixer.music.load(Data.Resource.bgm)
```

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/26001202/122640266-99497000-d139-11eb-8ae6-ed71aef604c1.gif)

<br/>
<hr/>

# 2. 캐릭터 행동
걷기, 달리기, 대쉬, 점프, 공격, 벽타기등 여러가지 동작을 만들었습니다.
각 행동값은 상하좌우 충돌블럭의 여부, 현재속도, 이전 상태값을 통해 구해 프레임 별로 갱신합니다.

![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/26001202/122640940-1c1ffa00-d13d-11eb-9372-bf72dbd973fd.gif)


```python
    #Player_ninja.py
    def stateHandler(self, input):
        press = input.getPress()
        funcKey = input.getFuncKey()
        key = input.getKey()

        idle = Data.Action.idle
        move = Data.Action.move
        jump = Data.Action.jump
        climb = Data.Action.climb
        dash = Data.Action.dash
        throw = Data.Action.throw
        attack = Data.Action.attack
        fall = Data.Action.fall
        dead = Data.Action.dead

        # climb 쿨타임 갱신
        if (self.state.getName() == climb):
            self.coolTime[climb] = 0

        # 방향 확인
        if (not self.state.getName() == dash):
            if (press[Data.Key.LEFT]):
                # 방금 벽을 탔다면 방향변경 불가능
                if (not (self.coolTime[climb] < 600 and self.state.getName() == jump)):
                    self.direction = 0
        ...
```

<br/>
<hr/>


# 3. 배경과 맵
배경은 큰 이미지를 캐릭터움직임에 맞춰 적당히 따라 움직여 동적인 배경화면을 구현했습니다.
맵은 Block 객체로 이루어져있으며, Block_group 객체에 각 블럭들을 등록하고 맵 생성기에 
맵은 초기 기획에서는 에디터창 (미구현)으로 블럭을 하나하나 그릴 수 있게 만들려고 했었습니다
하지만 시간이 너무 많이 투자되고, 힘들어서 코드상으로 그리는걸로 마무리지었습니다.

```python
# Map 생성방법
class LevelBasic:
    _background = None

    def __init__(self, blockGroupMgnt):
        self.blockGroup = blockGroupMgnt
        self.makeMap()
        self._background = pg.image.load(Data.Resource.background)  # 배경이미지
        '''
        Constructor
        '''
        # 위치,그림이름,그림인덱스,세부조정

    def getBackground(self):
        return self._background

    def draw(self, location, name, index, edit=None):
        str = "%d_%d" % (location[0], location[1])
        img = self.blockGroup.getBlockImage(name, index)
        block = Block(str, location, img)

        if (edit != None):  # 세부조정, 현재 위치에서 조금더함
            block.setRect([edit[0], edit[1]])

        self.blockGroup.addComponent(block)

    def makeMap(self):
        pass


class Level1(LevelBasic):
    '''
    classdocs
    1단계
    '''

    def makeMap(self):
        cloud = Data.Block.cloud
        grass = Data.Block.grass
        bridge = Data.Block.bridge
        plant = Data.Block.plant
        temple = Data.Block.temple
        # 가시
        for i in range(0, 43):
            self.draw([131, i], temple, 6)

        # 왼쪽벽
        for i in range(0, 130):
            self.draw([i, 0], temple, 1)
        # 0.0 구름
        self.draw([1, 1], cloud, 0, [10, 10])
        self.draw([1, 2], cloud, 1)
        self.draw([1, 3], cloud, 2)
  ...
```

Block과 BlockGroup코드는 다음과 같습니다.

```python
#Block 과 BlockGroup
class Block(ComponentBasic.Component):
    _size = None
    _location = None
    _edit = None

    def __init__(self, name, location, image):
        super().__init__(Data.Type.block, name)
        self.image = image
        self.rect = self.image.get_rect()
        self.setLocation(location)
        self._size = self.image.get_size()
        self._edit = [0, 0]

    def setLocation(self, location):
        self._location = location
        self.rect.x = location[1] * 64
        self.rect.y = location[0] * 64

    def setRect(self, addRect):
        self._edit = addRect
        self.rect.x += addRect[0]
        self.rect.y += addRect[1]

    def getLocation(self):  # 상대위치
        return self._location

    def getRect(self):  # 절대위치
        self._size = self.image.get_size()
        return [self.rect.x, self.rect.y, self._size[0], self._size[1]]

    def getSize(self):
        return self._size


class BlockGroup(ComponentBasic.Component):
    '''
    classdocs
    '''
    allBlock = {}

    def __init__(self, name):
        super().__init__(Data.Type.blockGroup, name)
        self.frameInit()

    def getBlockImage(self, name, index):
        return self.allBlock[name][index]

    def frameInit(self):
        for name in Data.block_all:
            self.allBlock[name] = []
            for i in range(0, len(Data.Resource.block_imgName[name])):
                dir = Data.Resource.block_imgDir[name]\
                      + Data.Resource.block_imgName[name][i]\
                      + Data.Resource.block_imgType[name]
                image = pg.image.load(dir)
                self.allBlock[name].append(image)
```

<br/>
<hr/>

# 4. main코드
각 컴포넌트 (캐릭터, 블럭, 맵, 이벤트리스너, 리소스)가 파일로 나누어져있습니다.<br/>
메인코드에서는 여러 컴포넌트의 초기값을 지정해주고, pygame을 이용해서 게임을 실행합니다.
맵 끝까지 간다면 클리어할 수 있고, 아래쪽에서 올라오는 연기에 닿이면 캐릭터가 죽습니다. (시작위치로 리스폰)<br/>

```python
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
    
    '''...중략...'''
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
    
```
