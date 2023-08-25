# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
# 
#   DESIGNER NAME:  Chaddarrly Brown
# 
#       FILE NAME:  myplayer
#  
#            DATE:  05/08/2021
#
# DESCRIPTION
#   This program is a MP3 Music Player that will allow the user the ability to
# select a folder of MP3s to make a playlist from , from that playlist the user
# will be able to play , stop , pause, go to next song and also previous song 
#
# *****************************************************************************
#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------

DIRECTORY = 0
FILE      = 1

#---------------------------------------------------------------------
#---------------------------------------------------------------------

#import modules needed

import pygame
from tkinter import *
import tkinter as TK
import tkinter.filedialog as tk_file
import os

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will call other functions , and run the main program task
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------
def main():
    
    #initialize pygame
    pygame.init()
    
    #initialize mixer
    pygame.mixer.init()

    #display muic player graphics
    make_gui()

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will create the graphical user interface for the user to
#   interact with the mp3 music player
#
# INPUT PARAMETERS:
#    none
#
# OUTPUT PARAMETERS:
#   gui of a MP3 player
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------    
def make_gui():
    
    #create main window
    root = TK.Tk()
    root.title("My MP3 Player ")
    root.geometry("500x200")
    
    #create button control frame
    control_frame = TK.Frame(root)
    control_frame.pack()

#---------------------------------------------------
# Variables to be used in program
#---------------------------------------------------
    root.play_list     = []
    root.play_index    = 0
    root.player_status = "stop"
    root.track         = []
    root.volume_slider = 0

    
    #create control buttons image
    back_button_image    = PhotoImage(file = r"C:\Users\chaddy waddy\Desktop\python\mp3 player buttons\backbutton.png")
    forward_button_image = PhotoImage(file = r"C:\Users\chaddy waddy\Desktop\python\mp3 player buttons\forwardbutton.png")
    play_button_image    = PhotoImage(file = r"C:\Users\chaddy waddy\Desktop\python\mp3 player buttons\playbutton.jpg")
    pause_button_image   = PhotoImage(file = r"C:\Users\chaddy waddy\Desktop\python\mp3 player buttons\pausebutton.png")
    stop_button_image    = PhotoImage(file = r"C:\Users\chaddy waddy\Desktop\python\mp3 player buttons\stopbutton.png")

    
    #create control buttons
    back_button    = TK.Button(control_frame,image =back_button_image, borderwidth = 0,command = lambda root = root: previous_song(root) )
    forward_button = TK.Button(control_frame,image=forward_button_image, borderwidth = 0,command = lambda root = root: next_song(root))
    play_button    = TK.Button(control_frame,image=play_button_image, borderwidth = 0,command = lambda root = root: play_song(root))
    pause_button   = TK.Button(control_frame,image=pause_button_image, borderwidth = 0,command = lambda root = root: pause_song(root))
    stop_button    = TK.Button(control_frame,image=stop_button_image, borderwidth = 0,command = lambda root = root: stop_song(root))

    back_button.grid(row = 0, column = 0, padx = 10)
    forward_button.grid(row = 0, column = 1, padx = 10)
    play_button.grid(row = 0, column = 2, padx = 10)
    pause_button.grid(row = 0, column = 3,padx = 10)
    stop_button.grid(row = 0, column = 4, padx = 10)

    #create a quit button
    quit_button = TK.Button(root,text = "Quit",command = root.destroy)
    quit_button.place(x = 70,y = 165)


    #create status and song frame
    song_status_frame = TK.Frame(root)
    song_status_frame.pack(side = TK.TOP)

    
    #create player status label
    status_label = Label(song_status_frame,text = "MP3 Player Status :")
    status_label.grid(row = 0,column = 0)

    #create player status
    root.player_status = TK.StringVar()
    status_label2 = TK.Label(song_status_frame, textvariable = root.player_status,relief = "groove")
    status_label2.grid(row = 0, column = 1, padx = 10)
    root.player_status.set("stop")

    #create current song label
    song_label = Label(song_status_frame,text = "Now Playing :")
    song_label.grid(row = 1, column = 0)

    #create current song playing
    root.track = TK.StringVar()
    song_label2 = TK.Label(song_status_frame, textvariable = root.track, relief ="groove")
    song_label2.grid(row = 1,column = 1, padx = 10)
    root.track.set("None")

    #create volume label frame
    #volume_frame = LabelFrame(control_frame,text = "Volume")
    #volume_frame.grid(row = 0,column = 5, padx = 10)
    
    
    #create volume slider
    #volume_slider = TK.Scale(volume_frame, from_ = 0, to = 100, orient = VERTICAL, resolution = 1,command = lambda root = root: volume_control(root),length = 100)
    #volume_slider.pack()
    

    #create menu
    player_menu = TK.Menu(root)
    root.config(menu=player_menu)

    #add song menu
    add_song_menu = Menu(player_menu)
    player_menu.add_cascade(label = "Add Songs", menu = add_song_menu)
    add_song_menu.add_command(label = "Add Songs To Playlist", command = lambda root = root: make_playlist(root))

    #run main loop
    check_status(root)
    root.mainloop()
    
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will play the selected songthen button is pressed or if the
#   song is paused it will unpause the song when button is pressed
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def play_song(root):
    #if playlist not empty
    if len(root.play_list) != 0:
        
        #if player is stopped
        if root.player_status.get() == "stop":
            
            #change directory and select song
            os.chdir(root.play_list[root.play_index][DIRECTORY]) 
            song = root.play_list[root.play_index][FILE]
            
            #load song to be played
            pygame.mixer.music.load(song)
            root.track.set(song)

            #play song
            pygame.mixer.music.play()
            root.player_status.set("play")

            #if the song is selected but paused
        elif root.player_status.get() =="paused":
            
            #unpause song
            pygame.mixer.music.unpause()
            root.player_status.set("play")

        
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will pause the song when button is pressed if music is playing
#   or if the song is already paused it will unpause the song when button is pressed
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def pause_song(root):
    
    #if mixer is busy, and song is not paused
    if pygame.mixer.music.get_busy():
        if not root.player_status.get() =="paused":
        
            #pause song
            pygame.mixer.music.pause()
            root.player_status.set("paused")
            
    #if song is paused
    elif root.player_status.get()=="paused":
        
        #unpause song
        pygame.mixer.music.unpause()
        root.player_status.set("play")
        
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will stop the song when button is pressed
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def stop_song(root):
    
    #stop the song
    pygame.mixer.music.stop()
    root.player_status.set("stop")

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will check the status of the playlist and song , if song is over
# but not the last song in playlist it will go to the next song , if it is the last
# song it will wrap around back to the first song of the playlist
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def check_status(root):
    #if playlist is not empty 
    if len(root.play_list) != 0:
        
        #if player ready to play 
        if root.player_status.get() == "play":
            
            #if no music is playing
            if not pygame.mixer.music.get_busy():
                
                #if it is the last song in playlist
                if root.play_index == len(root.play_list)-1:
                    
                    #set playlist back to begining
                    root.play_index=0

                else:
                    #go to the next song
                    root.play_index+=1
                    
                #change directory and select song to be played
                os.chdir(root.play_list[root.play_index][DIRECTORY]) 
                song = root.play_list[root.play_index][FILE]
                
                #load song to be played
                pygame.mixer.music.load(song)
                root.track.set(song)
            
                #play song
                pygame.mixer.music.play()

    #check to see if song is done playing
    root.after(500,check_status,root)
           
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will go to the next song when button is pressed, if it is the
# last song in the playlist when button is pressed then playlist will wrap around
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def next_song(root):
    try:
        
        #if playlist is not empty
        if len(root.play_list) != 0:
            
            #if the song is the last song of playlist
            if root.play_index == len(root.play_list)-1:
                
                #set the playlist back to beginning
                root.play_index=0

            else:
                #go to the next song
                root.play_index+=1
                
            #stop the music
            pygame.mixer.music.stop()
            
            #change directory and select song
            os.chdir(root.play_list[root.play_index][DIRECTORY])    
            song = root.play_list[root.play_index][FILE]

            #load song
            pygame.mixer.music.load(song)
            root.track.set(song)

            #play song
            if root.player_status.get()=="play":
                pygame.mixer.music.play()
                
    # in case of index error let user know they have reached end of playlist       
    except IndexError:
        
        root.play_index =0
        print('End of Playlist')
    
# -----------------------------------------------------------------------------
# DESCRIPTION
#    This function will go to the previous song when button is pressed, if it is the
# first song in the playlist when button is pressed then playlist will wrap around
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def previous_song(root):

    try:
        #if playlist is not empty
        if len(root.play_list) != 0:
            
            #if it is the first song in playlist
            if root.play_index == 0:
                
                #set song to last song in playlist
                root.play_index=len(root.play_list)-1

            else:
                #go to previous song
                root.play_index-=1
                
            #stop mixer
            pygame.mixer.music.stop()
            
            #change directory and select song
            os.chdir(root.play_list[root.play_index][DIRECTORY])    
            song = root.play_list[root.play_index][FILE]
            
            #load the song
            pygame.mixer.music.load(song)
            root.track.set(song)
            
            #play the song
            if root.player_status.get()=="play":
                pygame.mixer.music.play()
                
    # in case of index error let user know they have reached beginning of playlist        
    except IndexError:
        root.play_index =0
        print('End of Playlist')
        
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will ask for a directory of songs, and create a playlist from
#  those files that end with mp3
#
# INPUT PARAMETERS:
#   directory
#
# OUTPUT PARAMETERS:
#    none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------

def make_playlist(root):
    
    #ask for file location
    directory =tk_file.askdirectory()
    
    # file location is not empty
    if directory !="":
        
        #change to that location
        os.chdir(directory)

        #create list of files 
        song_list = os.listdir()

        #add mp3 files to playlist
        for song in song_list:
            if song.endswith("mp3"):
                root.play_list.append([directory,song])

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will control the volume of the mp3 music player
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#    none
#
# RETURN:
#   none
#
#-----------------------------------------------------------------------------
#def volume_control(root):
    #pygame.mixer.music.set_volume(volume_slider)
    
    
            
# Call the main function. 
main() 

