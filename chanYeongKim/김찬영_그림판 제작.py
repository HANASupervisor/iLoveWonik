from tkinter import *  # Tkinter 내장에서 특정 기능을 담당하는 하위 모듈들 불러오기
from tkinter import colorchooser  # 기본 색상 선택창을 띄우는 모듈
from tkinter import filedialog  # 파일 저장/열기 탐색기 창을 띄우는 모듈
from tkinter import messagebox  # 팝업 안내창/경고창을 띄우는 모듈
import json  # 선의 좌표 데이터를 파일로 저장하고 읽기 위한 표준 라이브러리

##전역 변수 초기 설정
window = None  # 메인 창 객체를 담을 변수
canvas = None  # 그림이 그려질 캔버스
width_scale = None  # 선 굵기를 조절하는 슬라이더 위젯
color_indicator = None  # 현재 선택된 색상을 보여주는 라벨 위젯

x1 = None  # 마우스 클릭/이동 시 선이 시작될 X 좌표
y1 = None  # 마우스 클릭/이동 시 선이 시작될 Y 좌표
line_width = 5  # 선 굵기 초기값

# 스페이스바 색상 순환 및 상단 기본 색상 목록
color_list = ['black', 'red', 'blue', 'yellow', 'green', 'purple']
color_index = 0  # 현재 선택된 색상이 color_list의 몇 번째인지 추적하는 인덱스
current_color = color_list[color_index]  # 현재 펜 색상
bg_color = 'white'  # 배경색 및 지우개 색상

# 실행 취소(Ctrl+Z) 및 파일 저장을 위한 기록 보관소
history = []  # 전체 그림 기록(여러 개의 획들을 담는 리스트)
current_stroke = []  # 마우스를 드래그하는 동안 그려진 1개의 획을 임시로 담는 리스트



##색상 및 도구 제어 함수
# 지정된 색상으로 현재 펜 색상을 변경하고 UI를 동기화하는 함수
def set_color(new_color):
    global current_color, color_index
    current_color = new_color  # 실제로 칠해질 펜 색상 업데이트

    # 만약 선택한 색상이 color_list 안에 있다면, 스페이스바 색 인덱스도 함께 업데이트
    if new_color in color_list:
        color_index = color_list.index(new_color)

    # 도구 모음의 '색상 표시기' 라벨 배경색을 즉시 변경하여 사용자에게 시각적 피드백 제공
    color_indicator.config(bg=current_color)

# 기본 색상 선택창을 열어 사용자 지정 색상을 가져오는 함수
def open_color_chooser():
    global current_color, color_index
    # askcolor()는 ((R, G, B), '#HEX코드') 형태를 반환함. 창을 취소하면 (None, None) 반환
    color = colorchooser.askcolor(title="사용자 지정 색상")

    # 사용자가 취소를 누르지 않고 색상을 선택했을 때만 실행
    if color[1] is not None:
        new_color = color[1]  # '#HEX코드' 형태의 문자열 추출
        current_color = new_color
        color_indicator.config(bg=current_color)

        # 목록에 없는 새로운 색상이라면 color_list 끝에 추가하여 스페이스바로도 순환되게 만듦
        if new_color not in color_list:
            color_list.append(new_color)

        # 인덱스를 새로 추가된(또는 기존에 있던) 색상의 위치로 갱신
        color_index = color_list.index(new_color)

# 펜 버튼 클릭 시 펜을 사용할 수 있는 함수
def use_pen():
    global current_color
    # 지우개를 쓰다가 돌아올 때, color_index가 기억하는 색상으로 복구
    current_color = color_list[color_index]
    color_indicator.config(bg=current_color)

# 지우개 버튼 클릭 시 지우개 모드로 전환하는 함수
def use_eraser():
    global current_color
    # 지우개는 캔버스 배경색(흰색)과 똑같은 색으로 덧칠
    current_color = bg_color
    color_indicator.config(bg=bg_color)

# 인터페이스 슬라이더를 움직일 때마다 선 굵기를 바꾸는 함수
def update_width(val):
    global line_width
    line_width = int(val)  # 슬라이더는 문자열을 전달하므로 정수(int)로 변환 필수

# 마우스 휠을 굴렸을 때 선 굵기와 슬라이더 위치를 조절하는 함수
def change_width(event):
    global line_width, width_scale
    # event.delta 값이 양수면 위로 굴림(굵게), 음수면 아래로 굴림(가늘게)
    if event.delta > 0:
        line_width += 1
    elif event.delta < 0:
        line_width -= 1

    # 굵기가 슬라이더의 하한선(1)과 상한선(50)을 벗어나지 않도록 제한
    if line_width < 1:
        line_width = 1
    elif line_width > 50:
        line_width = 50

    # 변수값 변화를 화면 상단의 슬라이더 바 위치에도 동기화 반영
    width_scale.set(line_width)

# 스페이스바를 누를 때마다 목록의 다음 색상으로 순환하는 함수
def change_color_space(event):
    global current_color, color_index
    # 나머지 연산자(%)를 이용해 인덱스가 리스트 끝에 도달하면 다시 0으로 돌아가도록 만듦
    color_index = (color_index + 1) % len(color_list)
    set_color(color_list[color_index])

##마우스 그리기 및 실행 취소 이벤트 함수
# 마우스 왼쪽 버튼을 처음 눌렀을 때 점 지정 함수
def mouse_click(event):
    global x1, y1, current_stroke
    x1 = event.x  # 마우스가 누른 지점의 X 좌표 저장
    y1 = event.y  # 마우스가 누른 지점의 Y 좌표 저장
    current_stroke = []  # 새로운 획이 시작되므로 임시 바구니 초기화

# 마우스를 누른 채 움직일 때 호출 (선 그리기)
def mouse_draw(event):
    global x1, y1, line_width, current_stroke, current_color
    x2 = event.x  # 이동한 현재 지점의 X 좌표
    y2 = event.y  # 이동한 현재 지점의 Y 좌표

    # 이전 지점(x1,y1)부터 현재 지점(x2,y2)까지 아주 짧은 선 조각 생성
    # capstyle=ROUND는 선 조각 끝을 둥글게 만들어 빠르게 그릴 때 선 끊김을 방지함
    line_id = canvas.create_line(x1, y1, x2, y2, width=line_width, fill=current_color, capstyle=ROUND)

    # 생성된 선 조각의 ID뿐만 아니라 좌표, 굵기, 색상 등 속성 전체를 딕셔너리로 묶어 저장
    # (추후 파일 저장 및 불러오기를 완벽하게 구현하기 위함)
    current_stroke.append({
        'id': line_id,
        'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
        'width': line_width,
        'color': current_color
    })

    # 다음 선 조각이 자연스럽게 이어지도록 현재 지점을 다음 시작 지점으로 교체
    x1 = x2
    y1 = y2

# 마우스 왼쪽 버튼을 뗐을 때 호출 (획의 완성)
def mouse_release(event):
    global current_stroke, history
    # 전체 획을 history 기록장 리스트에 추가
    if current_stroke:
        history.append(current_stroke)
        current_stroke = []

# Ctrl+Z 단축키 입력 시 마지막으로 그린 획을 지우는 함수
def undo(event=None):
    global history
    # history에 기록이 남아있을 때만 작동
    if history:
        last_stroke = history.pop()  # 가장 마지막에 그린 획(딕셔너리들의 리스트)을 꺼냄
        for segment in last_stroke:
            canvas.delete(segment['id'])  # 캔버스에서 해당 선 조각 ID들을 찾아 모두 삭제

# 화면과 메모리의 모든 그림 기록을 지우는 함수
def clear_canvas(event=None):
    global history, current_stroke
    canvas.delete('all')  # 도화지에 있는 모든 그래픽 요소를 삭제
    history.clear()  # 실행 취소 기록도 모두 비움
    current_stroke = []


##파일 입출력(JSON 저장/불러오기) 함수
# 현재까지 그린 모든 선 데이터를 JSON 파일로 저장하는 함수
def save_file():
    # 저장할 경로와 이름을 지정하는 윈도우 탐색기 창 호출
    file_path = filedialog.asksaveasfilename(
        title="그림 저장",
        defaultextension=".json",
        filetypes=[("그림판 프로젝트 파일", "*.json")]
    )
    # 사용자가 취소를 누르지 않고 경로를 선택했을 때만 실행
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(history, f)  # history 2차원 리스트 데이터를 텍스트 형태로 변환해 파일에 작성
            messagebox.showinfo("저장 완료", "파일이 성공적으로 저장되었습니다.")
        except Exception as e:
            # 권한 문제 등으로 저장 실패 시 알림창 띄우기
            messagebox.showerror("오류", f"파일을 저장하는 중 오류가 발생했습니다:\n{e}")

# 저장된 JSON 프로젝트 파일을 읽어와 캔버스에 복원하는 함수
def load_file():
    global history
    # 불러올 파일을 선택하는 윈도우 탐색기 창 호출
    file_path = filedialog.askopenfilename(
        title="그림 불러오기",
        filetypes=[("그림판 프로젝트 파일", "*.json")]
    )
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f: #'r' = 리드모드
                loaded_history = json.load(f)  # 파일 내용을 파이썬 리스트/딕셔너리 형태로 읽어옴

            clear_canvas()  # 불러오기 전 기존 도화지를 깨끗이 비움

            # 저장되어 있던 데이터 좌표대로 캔버스에 선 조각들을 다시 그림
            for stroke in loaded_history:
                new_stroke = []
                for segment in stroke:
                    # 저장되어 있던 x1, y1, x2, y2, width, color를 그대로 가져와 다시 선을 생성
                    line_id = canvas.create_line(
                        segment['x1'], segment['y1'], segment['x2'], segment['y2'],
                        width=segment['width'], fill=segment['color'], capstyle=ROUND
                    )
                    # 이전 실행 때의 객체 ID는 유효하지 않으므로, 새롭게 발급받은 line_id로 업데이트
                    segment['id'] = line_id
                    new_stroke.append(segment)
                history.append(new_stroke)  # 불러온 그림도 Ctrl+Z로 지울 수 있도록 history에 등록

        except Exception as e:
            messagebox.showerror("오류", f"파일을 불러오는 중 오류가 발생했습니다:\n{e}")

## 메인 윈도우 및 UI 구성
window = Tk()
window.title('그림판 프로그램')

# 상단 메뉴바 (파일 -> 불러오기/저장/종료)
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)  # tearoff=0은 점선 분리바를 제거하는 옵션
file_menu.add_command(label="불러오기 (Load)", command=load_file)
file_menu.add_command(label="저장하기 (Save)", command=save_file)
file_menu.add_separator()  # 메뉴 사이에 구분선 추가
file_menu.add_command(label="종료", command=window.destroy)  # 창 닫기
menu_bar.add_cascade(label="파일", menu=file_menu)  # 상위 메뉴바에 붙이기
window.config(menu=menu_bar)

# 도구 모음 영역 (화면 최상단)
toolbar = Frame(window, bd=1, relief=SUNKEN)  # 약간 안으로 들어간 느낌(SUNKEN)의 프레임
toolbar.pack(side=TOP, fill=X, pady=5, padx=5)  # 창 맨 위에 가로로 꽉 차게 배치

# 펜/지우개/전체 지우기 버튼 생성 및 왼쪽부터 차례대로 배치
pen_btn = Button(toolbar, text="펜", command=use_pen, width=5)
pen_btn.pack(side=LEFT, padx=2)

eraser_btn = Button(toolbar, text="지우개", command=use_eraser, width=6)
eraser_btn.pack(side=LEFT, padx=2)

clear_btn = Button(toolbar, text="전체 지우기", command=clear_canvas, width=8)
clear_btn.pack(side=LEFT, padx=2)

# 현재 선택된 펜 색상을 네모납게 시각적으로 보여주는 라벨 위젯
color_indicator = Label(toolbar, bg=current_color, width=2, relief=SUNKEN)
color_indicator.pack(side=LEFT, padx=(10, 5))

# 색상 팔레트 영역 (도구 모음 내부의 프레임)
color_frame = Frame(toolbar)
color_frame.pack(side=LEFT, padx=5)

# color_list에 있는 색상들을 반복문으로 돌면서 조그만 색상 버튼들을 횡으로 나열
for col in color_list:
    # command에 lambda를 써서 데이터를 가지고 있으며 c=col로 지워지지 않게 버그 방지
    btn = Button(color_frame, bg=col, width=2, command=lambda c=col: set_color(c))
    btn.pack(side=LEFT, padx=1)

# 사용자 지정 색상을 여는 팔레트 버튼
custom_color_btn = Button(toolbar, text="색상 지정", command=open_color_chooser, width=8)
custom_color_btn.pack(side=LEFT, padx=5)

# 선 굵기를 마우스로 끌어서 조절하는 슬라이더 위젯
width_scale = Scale(toolbar, from_=1, to=50, orient=HORIZONTAL, label="선 굵기", command=update_width, length=150)
width_scale.set(line_width)  # 슬라이더 위치를 현재 line_width 값(5)에 동기화
width_scale.pack(side=LEFT, padx=15)

## 캔버스 생성 및 이벤트 바인딩

canvas = Canvas(window, width=900, height=600, bg=bg_color)
canvas.pack()

# 마우스 동작과 함수를 연결(바인딩)
canvas.bind('<Button-1>', mouse_click)  # 마우스 좌클릭 시
canvas.bind('<B1-Motion>', mouse_draw)  # 마우스 좌클릭 후 드래그 시
canvas.bind('<ButtonRelease-1>', mouse_release)  # 마우스 클릭을 뗄 때

# 키보드 및 마우스 휠 동작을 윈도우 창 전체에 바인딩
window.bind('<Delete>', clear_canvas)  # Delete 키 누르면 화면 비우기
window.bind('<Control-z>', undo)  # 소문자 z 단축키
window.bind('<Control-Z>', undo)  # CapsLock 켜진 상태 대비 대문자 Z 단축키
window.bind('<MouseWheel>', change_width)  # 마우스 휠 조작 시 선 굵기 변경
window.bind('<space>', change_color_space)  # 스페이스바 누르면 색상 순환

## 프로그램 이벤트 루프 실행
# 창이 닫힐 때까지 사용자의 마우스/키보드 입력을 무한히 감지하고 화면을 갱신함
window.mainloop()