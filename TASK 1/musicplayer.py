import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        master.geometry("400x200")

        self.music_list = []
        self.current_index = 0
        self.paused = False
        self.playing = False

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.master, text="Select a folder with music files")
        self.label.pack()

        self.select_button = tk.Button(self.master, text="Select Folder", command=self.select_folder)
        self.select_button.pack()

        self.play_button = tk.Button(self.master, text="Play", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack()

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack()

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.music_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp3')]
            if self.music_list:
                self.label.config(text="Selected folder: " + folder_path)
                self.play_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.NORMAL)
                self.pause_button.config(state=tk.NORMAL)
            else:
                self.label.config(text="No music files found in the selected folder")

    def play_music(self):
        if not self.playing:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_list[self.current_index])
            pygame.mixer.music.play()
            self.playing = True
        else:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.load(self.music_list[self.current_index])
                pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False

    def pause_music(self):
        if self.playing:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
