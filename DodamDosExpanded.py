#AI사용기록
#전에 한거는 #AI 되어 있음
#파일/쓰기 읽기 문제-UTF-8



print("\033[37mDodam OS make by L.Doyun\033[37m")
import os, sys, subprocess, datetime, requests
from tempfile import TemporaryFile
from datetime import time

version = '--expandversion1.0--'
dir_ = os.path.dirname(os.path.realpath(__file__))  # dir
dir__ = dir_ + '\\'
sysdir = os.path.join(dir__, 'expandedfile.txt')  # ✅ 문자열 경로
pyver = sys.version[0:6]
temp = ''
templist = []
ifdeveloper = False

print('\033[32mDodamDosExpanded is loading system...\033[32m')

fp = TemporaryFile('w+t')
fp.write('|DodamDos Temp|\n')
fp.write('|load end|\n')

def plus(*a):
    temp = 0
    for i in range(0, len(a) + 1):
        temp = temp + i
    return temp

def modify_line_in_file(file_path, line_number, new_content):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if line_number < 1 or line_number > len(lines):
        print("error line defind")
        return

    lines[line_number - 1] = new_content + '\n'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# 개발자 모드 확인
try:
    f = open(os.path.join(dir_, 'expandedfile.txt'), "r", encoding="utf-8")
    templist = f.readlines()
    f.close()
    if templist[3].strip() == 'developer__True':
        print('developer mode True')
        ifdeveloper = True
except Exception as error:
    ifdeveloper = False
    pass

print('\033[37m완료\033[37m')
print()
print('한국어')
temp = os.path.isfile(os.path.join(dir_, 'expandedfile.txt'))
if temp:
    fp.write('|isfile expandedfile|\n')
else:
    f = open(os.path.join(dir_, 'expandedfile.txt'), 'w', encoding='utf-8')
    temp = input('이름을 입력하시오:')
    f.write(f'osname_____Dodam OS\nosversion__{version}\nname_______{temp}\ndeveloper__False\nPersinfor__False')
    print('installed')
    f.close()

# read ver
f = open(os.path.join(dir_, 'expandedfile.txt'), "r", encoding="utf-8")
templist = f.readlines()
f.close()
if templist[1][11:-1] != version:
    print(templist[1][11:-1])
    print('에러 코드100: 파일 버전 맞지 않음.')
else:
    pass

print(f'파이썬 버전:{sys.version[0:6]}')
fp.write(f'|Python Version: {sys.version[0:6]}|\n')

cmd = ''
while cmd != 'exit()':
    try:
        with open(os.path.join(dir_, 'expandedfile.txt'), "r", encoding="utf-8") as f:
            templist = f.readlines()
        if templist[4][11:].strip() == 'False':
            cmd = input(f"{dir_}\\")
        elif templist[4][11:].strip() == 'True':
            cmd = input(f">")
        else:
            cmd = input('error>')
        fp.write('user inputting...\n')
    except Exception as error:
        print(f"오류 발생: {error}")

    if cmd.startswith('help'):
        if cmd.startswith('help_help'):
            print('1.output([outputtext])')
            print('2.is_')
            print('->var([varname])')
            print('3.run_')
            print('->py_[filename]')
            print('->app_[appname]')
            print('4.dir_')
            print('->_app')
            print('5.store_[you_want_download_appname]')
            print('6.time')
            print('7.settings_')
            print('->settings_Persinfor_')
            print('->->True')
            print('->->False')
        elif cmd.startswith('help_system'):
            print('시스템 정보:')
            print('made by L.Doyun')
            print('\033[32mDodamDosExpanded\033[32m')
            f = open(os.path.join(dir_, 'expandedfile.txt'), "r", encoding="utf-8")
            templist = f.readlines()
            f.close()
            print(f'\033[37mDodamDosExpanded버전: {templist[1][11:-1]}\033[37m')
            print(f'파이썬 버전: {pyver}')
            print(f'사용자 이름: {templist[2][11:]}')

    elif cmd.startswith('output(') and cmd[-1] == ')':
        fp.write(f'user enter: {cmd}\n')
        print(f'{cmd[7:-1]}')

    elif cmd.startswith('is'):
        fp.write(f'user enter: {cmd}\n')
        if cmd[2:6] == 'var(' and cmd[-1] == ')':
            if cmd[6:-1] in locals():
                print(f'{cmd[6:-1]} 변수는 존재합니다.')
            else:
                print(f'{cmd[6:-1]} 변수는 존재하지 않습니다.')

    elif cmd.startswith('run_'):
        if cmd.startswith('run_py_'):
            subprocess.run(["python", f"{cmd[11:]}"])
        elif cmd.startswith('run_app_'):
            print(f'{dir_}\\app')
            subprocess.run(["python", f"{cmd[8:]}.py"], cwd=(f'{dir_}\\app'))

    elif cmd.startswith('dir_'):
        if cmd.startswith('dir_app'):
            print('app의 앱들')
            folder_path = f'{dir_}\\app'
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    file_name_without_ext = os.path.splitext(file_name)[0]
                    timestamp = os.path.getmtime(file_path)
                    formatted_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d")
                    print(f"앱 이름:{file_name_without_ext} 설치된 날짜:{formatted_date}")
        elif cmd.startswith('dir_'):
            print('main의 앱들')
            folder_path = dir_
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    file_name_without_ext = os.path.splitext(file_name)[0]
                    timestamp = os.path.getmtime(file_path)
                    formatted_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d")
                    print(f"{file_name_without_ext} 만든 날짜:{formatted_date}")

    elif cmd.startswith('store_'):
        github_raw_url = f"https://raw.githubusercontent.com/dodam2015/DodamDosApps/main/{cmd[6:]}.py"
        save_folder = os.path.join(dir_, "app")
        os.makedirs(save_folder, exist_ok=True)
        file_name = f"{cmd[6:]}.py"
        save_path = os.path.join(save_folder, file_name)

        response = requests.get(github_raw_url)

        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"파일 다운로드 완료:")
        else:
            print(f"다운로드 실패! 상태 코드: {response.status_code}")

    elif cmd == 'time':
        now = datetime.datetime.now()
        print(now.strftime("%Y%m%d"))

    elif cmd == 'developer':
        if ifdeveloper:
            print('app loading')
            subprocess.run(["python", f"{dir__}GrohnThERUfH\\wegjwrg.py"])
        else:
            pass

    elif cmd.startswith('settings_'):
        if cmd.startswith('settings_Persinfor_'):
            print(cmd[19:])
            if cmd[19:] == 'True':
                modify_line_in_file(sysdir, 5, 'Persinfor__True')
            elif cmd[19:] == 'False':
                modify_line_in_file(sysdir, 5, 'Persinfor__False')
    elif cmd.startswith('resave'):
        import tkinter as tk
        from tkinter import filedialog, messagebox
        import os

        def open_file_from_list(filename):
            """선택한 파일 내용을 텍스트 상자에 표시."""
            global file_path
            if filename.startswith("@부모@"):
                file_path = os.path.join(parent_dir, filename[5:])  # "@부모@" 제거 후 경로 설정
            else:
                file_path = os.path.join(dir_, filename)  # 파일 경로 설정

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text_area.delete("1.0", tk.END)  # 기존 내용 삭제
                    text_area.insert(tk.END, file.read())  # 파일 내용 삽입
            except Exception as e:
                messagebox.showerror("오류", f"파일을 여는 중 오류가 발생했습니다: {e}")

        def save_file(event=None):
            """텍스트 상자의 내용을 파일에 저장하고 창을 닫음."""
            global file_path
            if file_path:
                try:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(text_area.get("1.0", tk.END))  # 텍스트 상자 내용 파일에 쓰기
                    messagebox.showinfo("성공", "파일이 성공적으로 저장되었습니다.")
                    window.destroy()  # 창 닫기
                except Exception as e:
                    messagebox.showerror("오류", f"파일을 저장하는 중 오류가 발생했습니다: {e}")
            else:
                messagebox.showinfo("알림", "열린 파일이 없습니다.")

        # Tkinter 윈도우 생성
        window = tk.Tk()
        window.title("텍스트 파일 편집기")
        window.geometry("800x600")  # 창 크기 설정

        # 파일 경로 저장 변수 (전역 변수)
        file_path = None

        # 현재 스크립트 디렉토리
        dir_ = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(dir_)  # 부모 디렉토리

        # 파일 목록 생성
        file_list = []
        # 현재 디렉토리 파일 추가
        for filename in os.listdir(dir_):
            file_path_full = os.path.join(dir_, filename)
            if os.path.isfile(file_path_full):
                file_list.append(filename)

        # 부모 디렉토리 파일 추가 (앞에 "@부모@" prefix 붙임)
        for filename in os.listdir(parent_dir):
            file_path_full = os.path.join(parent_dir, filename)
            if os.path.isfile(file_path_full):
                file_list.append("@부모@" + filename)

        # 파일 목록 표시를 위한 Listbox 생성
        listbox = tk.Listbox(window)
        for filename in file_list:
            listbox.insert(tk.END, filename)
        listbox.pack(side=tk.LEFT, fill=tk.Y)

        # Listbox에서 파일 선택 시 이벤트 처리
        listbox.bind("<Double-Button-1>", lambda event: open_file_from_list(listbox.get(tk.ANCHOR)))

        # 텍스트 상자 생성
        text_area = tk.Text(window, wrap=tk.WORD, undo=True)
        text_area.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Ctrl+S 단축키 바인딩
        window.bind("<Control-s>", save_file)

        # Tkinter 이벤트 루프 시작
        window.mainloop()



    else:
        if cmd == '' or cmd == ' ':
            pass
        else:
            print(f'{cmd}는/은 유효한 명령어가 아닙니다.')
