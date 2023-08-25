#create status and song frame
    song_status_frame = TK.Frame(root)
    song_status_frame.pack(side =TK.TOP)
    

    #create player status label
    status_label = LabelFrame(song_status_frame,text = "MP3 Player Status")
    status_label.grid(row=0,column =0)

    #create current song label
    song_label = Label(song_status_frame,text="Song Playing")
    song_label.grid(row = 1,column=0,)

    #create player status
    root_player_status = TK.StringVar()
    status_label2 =Label(song_status_frame,textvariable = root.player_status)
    status_label2.grid(row=0,column =3)
    root.player_status.set(play)
