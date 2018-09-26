import tkinter

win = tkinter.Tk()

win.title("scoreball")
win.geometry("400x400+400+40")

score = tkinter.Scrollbar()

text = tkinter.Text(win, width=100, height=50)
score.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text.pack()
score.config(command=text.yview)
text.config(yscrollcommand=score.set)

str = """
Good morning everyone,
today is my turn to the speech. First of all, I would like to say that a quick test, we hope that the good preparation, good test for all, is the only way home for a good year. My English is not high, I wish I could within the next two years to learn English well. I hope you will be able to learn English after graduation to have a good future.
Finally, I wish the students and teachers a happy new year, further study and work. Well! I finished the speech. Thank you for listening.
Good afternoon, my dear friends. 　　

I am very happy to meet you here.It is my great honor to communicate with you at such a special occation.First of all,please allow me to express my appreciation to you all to listion to me.
I am proud of being a college student.The collegelife is fresh,new teachers, new classmates and new friends. I like the friendship, and their wide knowledge and opening mind. The grand library, school buildings and wide playground attrattde me very much.My college life is better than I expected, I can do anything I like. In the college we can not only learn the professional knowledge,but also develop our comprehensive abilities.If we can make full use of the period,we can learn many useful things.Besides,we should have the active attitude to our life,do a contributionto the society.Collegelife is the most precious time in our life.Most of us want to become an outstanding man. But there are some students still waste their time. They get together for eating, drinking or playing cards. They're busy in searching for a girlfriend or a boyfriend. They completely forget their task as college students. 　　
Finally, I hope everybody can try their best to become a worthy person to our country, and make great contrib
"""
text.insert(tkinter.INSERT, str)

# score = tkinter.Scrollbar()
win.mainloop()
