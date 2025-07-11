import winsound

def play_beep():
    try:
        winsound.Beep(1000, 500)
    except Exception as e:
        print(f"Beep failed: {e}")
