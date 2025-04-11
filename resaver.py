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
