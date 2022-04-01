import tkinter as tk
from ttkthemes import themed_tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from mutagen.mp3 import MP3
import os
import time
import pygame

class MediaPlayer:
    def __init__(self, window):

        style = ttk.Style()
        style.theme_use("breeze")

        background = "grey"

        style.configure("TScale",background = background)

        self.root = window

        self.root.configure(bg="black")

        self.music_image = Image.open('images/bg.jpg')
        self.music_image = self.music_image.resize((370,300),Image.ANTIALIAS)
        self.music_image = ImageTk.PhotoImage(self.music_image)

        self.repeat_icon = Image.open('images/repeat.png')
        self.repeat_icon = self.repeat_icon.resize((40, 40), Image.ANTIALIAS)
        self.repeat_icon = ImageTk.PhotoImage(self.repeat_icon)

        self.repeat1_icon = Image.open('images/repeat1.png')
        self.repeat1_icon = self.repeat1_icon.resize((40, 40), Image.ANTIALIAS)
        self.repeat1_icon = ImageTk.PhotoImage(self.repeat1_icon)

        self.play_icon = Image.open('images/play.png')
        self.play_icon = self.play_icon.resize((90, 90), Image.ANTIALIAS)
        self.play_icon = ImageTk.PhotoImage(self.play_icon)

        self.pause_icon = Image.open('images/pause.png')
        self.pause_icon = self.pause_icon.resize((90, 90), Image.ANTIALIAS)
        self.pause_icon = ImageTk.PhotoImage(self.pause_icon)

        self.next_icon = Image.open('images/next.png')
        self.next_icon = self.next_icon.resize((70, 70), Image.ANTIALIAS)
        self.next_icon = ImageTk.PhotoImage(self.next_icon)

        self.previous_icon = Image.open('images/previous.png')
        self.previous_icon = self.previous_icon.resize((70, 70), Image.ANTIALIAS)
        self.previous_icon = ImageTk.PhotoImage(self.previous_icon)

        self.stop_icon = Image.open('images/stop.png')
        self.stop_icon = self.stop_icon.resize((90, 90), Image.ANTIALIAS)
        self.stop_icon = ImageTk.PhotoImage(self.stop_icon)

        self.speaker_icon = Image.open('images/speaker.png')
        self.speaker_icon = self.speaker_icon.resize((30, 30), Image.ANTIALIAS)
        self.speaker_icon = ImageTk.PhotoImage(self.speaker_icon)

        self.mute_icon = Image.open('images/mute.png')
        self.mute_icon = self.mute_icon.resize((30, 30), Image.ANTIALIAS)
        self.mute_icon = ImageTk.PhotoImage(self.mute_icon)

        self.delete_icon = Image.open('images/delete.png')
        self.delete_icon = self.delete_icon.resize((30, 30), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(self.delete_icon)

        self.delete_all_icon = Image.open('images/delete2.png')
        self.delete_all_icon = self.delete_all_icon.resize((30, 30), Image.ANTIALIAS)
        self.delete_all_icon = ImageTk.PhotoImage(self.delete_all_icon)

        self.add_song_icon = Image.open('images/song.png')
        self.add_song_icon = self.add_song_icon.resize((30, 30), Image.ANTIALIAS)
        self.add_song_icon = ImageTk.PhotoImage(self.add_song_icon)

        self.multiple_song_icon = Image.open('images/song2.png')
        self.multiple_song_icon = self.multiple_song_icon.resize((30, 30), Image.ANTIALIAS)
        self.multiple_song_icon = ImageTk.PhotoImage(self.multiple_song_icon)

        self.shuffle_icon = Image.open('images/shuffle.png')
        self.shuffle_icon = self.shuffle_icon.resize((40, 40), Image.ANTIALIAS)
        self.shuffle_icon = ImageTk.PhotoImage(self.shuffle_icon)

        self.auto_play_icon = Image.open('images/auto_play.png')
        self.auto_play_icon = self.auto_play_icon.resize((40, 50), Image.ANTIALIAS)
        self.auto_play_icon = ImageTk.PhotoImage(self.auto_play_icon)

        self.auto_play_not_icon = Image.open('images/auto_play_not.png')
        self.auto_play_not_icon = self.auto_play_not_icon.resize((40, 40), Image.ANTIALIAS)
        self.auto_play_not_icon = ImageTk.PhotoImage(self.auto_play_not_icon)


        self.song_photo = tk.Label(self.root,text="",image=self.music_image,bd=0)
        self.song_photo.place(x=80,y=78)

        self.heading = tk.Label(self.root, bg="black",text="Music Player",font="lucida 40 bold",fg="#F4B81A")
        self.heading.place(x=0,y=2,relwidth=1)

        tk.Label(self.root, text="",background=background,height=7,width=120).place(x=5,y=400)

        self.songs_list = tk.Listbox(self.root, width=30, height=18, bg="black", fg="blue", relief="flat",
                                     selectbackground="grey")
        self.songs_list.place(x=520, y=60)

        self.time_elapsed_label = tk.Label(self.root,text="00:00", fg="black",background=background,
                                           activebackground=background,padx=5)
        self.time_elapsed_label.place(x=10,y=400)

        self.music_duration_label = tk.Label(self.root,text="00:00",fg="black",background=background,
                                             activebackground=background,padx=15)
        self.music_duration_label.place(x=460,y=400)

        self.progress_scale = ttk.Scale(self.root,orient="horizontal",style='TScale',from_=0,length=380,
                                        command="command",cursor='hand2')
        self.progress_scale.place(x=80,y=400)

        self.play_button = tk.Button(self.root,image=self.play_icon,command=self.play_song,cursor='hand2',bd=0,
                                     background=background,activebackground=background)
        self.play_button.place(x=146,y=425)

        self.next_button = tk.Button(self.root, image=self.next_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.next_button.place(x=328, y=435)

        self.previous_button = tk.Button(self.root, image=self.previous_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.previous_button.place(x=73, y=435)

        self.stop_button = tk.Button(self.root, image=self.stop_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.stop_button.place(x=236, y=425)

        self.shuffle_button = tk.Button(self.root, image=self.shuffle_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.shuffle_button.place(x=10, y=425)

        self.speaker_button = tk.Button(self.root, image=self.speaker_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.speaker_button.place(x=390, y=420)

        self.repeat_button = tk.Button(self.root, image=self.repeat_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.repeat_button.place(x=10, y=470)

        self.auto_play_button = tk.Button(self.root, image=self.auto_play_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.auto_play_button.place(x=420, y=453)

        self.vol_scale = ttk.Scale(self.root, from_=0,to=100,orient="horizontal",command="simple",cursor="hand2")
        self.vol_scale.place(x=420,y=425)

        self.status = tk.Label(self.root,text="Playing : ---------- Song : 0 of 0",fg="black",anchor="w",background="grey",
                               font="lucida 9 bold",bd=5,relief="ridge")
        self.status.place(x=5,y=520,relwidth=1)

        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)

        m1 = tk.Menu(self.menu,background="grey",tearoff=False,bd=0,activebackground="black")
        self.menu.add_cascade(label="Actions",menu=m1)

        m1.add_command(label="Add Song",command=self.add_songs,image=self.add_song_icon,compound="left")

        m2 = tk.Menu(self.menu, background="grey", tearoff=False, bd=0, activebackground="black")
        self.menu.add_cascade(label="Delete", menu=m2)

        m2.add_command(label="Delete Selected", command="command", image=self.delete_icon, compound="left")
        m2.add_command(label="Delete All", command="command", image=self.delete_all_icon, compound="left")

        self.directory_list = []


    def add_songs(self):
        songs = filedialog.askopenfilenames(title="Select Music Folder", filetypes=(('mp3 files', '*.mp3'),))
        for song in songs:
            song_name = os.path.basename(song)
            directory_path = song.replace(song_name,"")
            self.directory_list.append({'path':directory_path,'song':song_name})
            self.songs_list.insert('end',song_name)

        self.songs_list.select_set('0')

    def play_song(self):
        self.progress_scale['value'] = 0
        self.time_elapsed_label['text'] = "00:00"

        song_name = self.songs_list.get('active')
        self.status.config(text=f"Playing : {song_name} Song : {self.songs_list.index('active')} of "
                                f"{self.songs_list.size()}")
        directory_path=None
        for dictio in self.directory_list:
            if dictio['song'] == song_name:
                directory_path = dictio['path']

        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        self.music_length = int(music_data.info.length)
        self.music_duration_label['text'] = time.strftime('%M:%S', time.gmtime(self.music_length))

        self.progress_scale['to'] = self.music_length
        self.play_button.config(image=self.pause_icon)
        pygame.mixer.music.load(song_with_path)
        pygame.mixer.music.play()


if __name__ == '__main__':

    window = themed_tk.ThemedTk()
    pygame.init()

    window.title("Music Player")
    window.maxsize(width=750,height=550)
    window.minsize(width=540,height=550)

    x = MediaPlayer(window)
    window.mainloop()
