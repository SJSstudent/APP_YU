from tkinter import *
import psutil
import calendar
import tkinter.ttk
from datetime import datetime

# 기능 개인 정보 설명, 노트북 베터리, 학교 홈페이지 버튼 + 자주 사용하는 웹 사이트, 학점,
# 메모장 기능, 드래그 and 드롭, 캘린더(계획표 작성)

# 디자인은 기능을 다 만들고 나서 시작!

def Battery():
    battery=psutil.sensors_battery()
    percent=battery.percent
    lbl.config(text=f"{percent}%")
    
def list_box_active(event):
    selected=list_box.curselection()
    if selected:
        delete_list=main_frame.place_slaves()
        for i in delete_list: i.destroy()
        if selected[0]==(0):one_list_box()
        if selected[0]==(1):two_list_box(int(datetime.now().year),int(datetime.now().month))

def one_list_box():
    treeview = tkinter.ttk.Treeview(main_frame, 
    column=("name", "year", "grade"), 
    displaycolumns=("name", "year", "grade"),
    show='headings')
    treeview.place(x=10,y=10,width=610,height=460)
    
    input_treeview=(("name","교과목명"),
                    ("year","학기"),
                    ("grade","등급"),)
    
    input_value=(
        ("독서와 토론",1,"B+"),
        ("영화속의인공지능인문학",1,"B"),
        ("소프트웨어와인공지능",1,"A+"),
        ("실용영어",1,"C+"),
        ("행렬및행렬식",1,"A"))
    
    for i,j in input_treeview:
        treeview.column(i,width=20,anchor="center")
        treeview.heading(i,text=j,anchor="center")

    for i in range(len(input_value)):
        treeview.insert("","end",text="",values=input_value[i],iid=i)

def two_list_box(year,month):

    def isLeapYear(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def lastDay(year, month):
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        m[1] = 29 if isLeapYear(year) else 28
        return m[month - 1]

    def totalDay(year, month, day):
        total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
        for i in range(1, month):
            total += lastDay(year, i)
        return total + day

    def weekDay(year, month, day):
        return totalDay(year, month, day) % 7

    def A_plus_button():
        nonlocal month
        month+=1
        title_name.config(text=f"{year}년 {month}월")
        two_list_box(year,month)

    def A_minus_button():
        nonlocal month
        month-=1
        title_name.config(text=f"{year}년 {month}월")
        two_list_box(year,month)
        
    plus_button=Button(main_frame,text="+",command=A_plus_button)
    minus_button=Button(main_frame,text="-",command=A_minus_button)
    title_name=Label(main_frame, text=f"{year}년 {month}월")
    
    xp,yp=10,40
    day_data={
        i:"" if i<=weekDay(year, month, 1) or i%8==0 else i-weekDay(year, month, 1)
        for i in range(1,43)
    }
    
    for i in range(1,43):
        if type(day_data[i])==int and lastDay(year, month)<day_data[i]:
            break
        if i%8==0:
            xp,yp=10,yp+70
            continue
        F=Frame(main_frame,width=60,height=60)
        L=Label(F,text=f"{day_data[i]}")
        L.place(x=10,y=10)
        F.place(x=xp,y=yp)
        xp+=70

    title_name.place(x=250,y=10)
    plus_button.place(x=20,y=10)
    minus_button.place(x=50,y=10)
    

tk = Tk()
tk.geometry("900x500")
tk.resizable(False, False)
tk.title("YU")

profile_frame=Frame(tk, relief="solid", width=250,height=60,bg='#e3e3e3')
profile_frame.place(x=10,y=10)

battery_frame=Frame(tk, relief="solid", width=250,height=300,bg='#e3e3e3')
battery_frame.place(x=10,y=80)

list_frame=Frame(tk, relief="solid", width=250,height=100,bg='#e3e3e3')
list_frame.place(x=10,y=390)

main_frame=Frame(tk, relief="solid", width=620,height=480,bg='#e3e3e3')
main_frame.place(x=270,y=10)

#===========================================

name_lable=Label(tk,text="이름 : 주현준",bg='#e3e3e3')
age_lable=Label(tk,text="나이 : 20",bg='#e3e3e3')
major_lable=Label(tk,text="전공 : 컴퓨터학부",bg='#e3e3e3')

battery_png=PhotoImage(file="C:\\PP\\python\\P\\battery.png")
battery_lable=Label(tk,image=battery_png)
lbl=Label(tk,text="!123123123",bg='#e3e3e3')

# 홈페이지 활성화 되면 수정 ㄱㄱ
YU_homepage_button=Button(tk,text="영남대 홈페이지")
YU_major_homepage_button=Button(tk,text="영남대 컴퓨터학부 홈페이지")
YU_major_R_homepage_button=Button(tk,text="영남대 정보통신공학과 홈페이지")

list_scrollbar=Scrollbar(list_frame)
list_box=Listbox(list_frame,yscrollcommand=list_scrollbar.set,
    width=5,height=5)

list_box_value=["학점","달력","파일 확인하기"]
for i in list_box_value:
    list_box.insert(END,i)

main_not_label=Label(main_frame,text="없음",bg='#e3e3e3')

#============================================

name_lable.place(x=120,y=14)
age_lable.place(x=120,y=30)
major_lable.place(x=120,y=46)

battery_lable.place(x=90,y=100)
lbl.place(x=90,y=180)

YU_homepage_button.place(x=90,y=230)
YU_major_homepage_button.place(x=90,y=260)
YU_major_R_homepage_button.place(x=90,y=290)

Battery()

list_box.place(x=10, y=10, width=200, height=80)
list_scrollbar.place(x=215, y=10, height=80)

main_not_label.place(x=310,y=240)

list_box.bind("<<ListboxSelect>>", list_box_active)

tk.mainloop()