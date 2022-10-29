"""
    This is the code of guess number game.
    Using random model to generate the interger between 0 and 1024. Larger or smaller will be hinted.
    The times will be recorded.
"""

import random
import tkinter
number=random.randint(0,1024) #the number need to guess, randomly generate
num=0 # the times playing
# the scope to hint
maxn=1024
minn=0
running=True

# "close" button issue
def eBtoClose(event):
    root.destroy()

# modify the label text
def labelqval(vText):
    label_val_q.config(label_val_q,text=vText)

def labelqval_times(vText):
    label_val_times.config(label_val_times,text=vText)

# "guess" button issue
def eBtoGuess(event):
    global maxn  # global variables
    global minn
    global num
    global running
    if running:
        val_a=int(entry_a.get()) #turn entry type into int tpye
        if val_a==number:
            num += 1
            labelqval("恭喜答对了")
        elif val_a<number:   # guess smaller
            if val_a>minn:   # change val_a into minn
                minn=val_a
                num+=1
                labelqval("输入小了，请输入"+str(minn)+"到"+str(maxn)+"之间的任意整数：")
            else:
                num += 1
                labelqval("输入小了，请输入" + str(minn) + "到" + str(maxn) + "之间的任意整数：")
        else:
            if val_a<maxn:
                maxn=val_a
                num+=1
                labelqval("输入大了，请输入" + str(minn) + "到" + str(maxn) + "之间的任意整数：")
            else:
                num+=1
                labelqval("输入大了，请输入" + str(minn) + "到" + str(maxn) + "之间的任意整数：")

    else:
        labelqval("你已经答对了")
    labelqval_times('您尝试的次数为：' + str(num))

# the times of guessing
def guess_times():
    labelqval_times('您尝试的次数为：'+str(num))


# main
root=tkinter.Tk(className='Guessing Number') #create the windows object
root.geometry('400x90+200+200')
# size:400x90 ;  position:200,200
label_val_q=tkinter.Label(root,width="80")
label_val_q.pack(side='top') # location

label_val_times=tkinter.Label(root,width="80")
label_val_times.pack(side='top') # location

entry_a=tkinter.Entry(root,width="40") # entry a single line of the text
# button guess
btnGuess=tkinter.Button(root,text='Guess')
entry_a.pack(side='left')
entry_a.bind('<Return>',eBtoGuess) # trigger event
btnGuess.bind('<1>',eBtoGuess)
btnGuess.pack(side='left')
#button clsoe
btnClose=tkinter.Button(root,text='CLose')
btnClose.bind('<1>',eBtoClose)
btnClose.pack(side='left')

labelqval('Please enter the integer range 0 to 1024:')
entry_a.focus_get() #将焦点设置在所需的小部件上
print(number)
root.mainloop()

