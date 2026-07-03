from tkinter import *

## 변수 ##
window = None
canvas = None

# 이전 마우스 좌표를 저장할 변수
x1, y1 = None, None


## 함수 ##

# 마우스를 처음 클릭했을 때 실행되는 함수
def mouseClick(event):
    global x1, y1

    # 마우스를 누른 현재 위치를 저장한다.
    x1 = event.x
    y1 = event.y

    print("마우스 클릭 좌표:", x1, y1)


# 마우스를 누른 상태로 움직일 때 실행되는 함수
def mouseDrag(event):
    global x1, y1

    # 현재 마우스 위치를 가져온다.
    x2 = event.x
    y2 = event.y

    print("마우스 드래그 좌표:", x2, y2)

    # 이전 좌표(x1, y1)에서 현재 좌표(x2, y2)까지 짧은 선을 그린다.
    canvas.create_line(
        x1, y1,
        x2, y2,
        fill="red",
        width=5
    )

    # 현재 좌표를 다시 이전 좌표로 저장한다.
    # 그래야 다음 드래그 때 이어서 선이 그려진다.
    x1 = x2
    y1 = y2


# 메인 코드
window = Tk()
window.title("그림판 비슷한 프로그램 - 자유곡선")

canvas = Canvas(window, height=500, width=500, bg="white")

# 마우스 왼쪽 버튼을 처음 눌렀을 때
canvas.bind("<Button-1>", mouseClick)

# 마우스 왼쪽 버튼을 누른 상태로 움직일 때
canvas.bind("<B1-Motion>", mouseDrag)

canvas.pack()

window.mainloop()