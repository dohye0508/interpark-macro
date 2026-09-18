import os
import sys
import pygame

# 음악 재생을 위한 클래스
class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        # PyInstaller 및 상대 경로 대응
        if getattr(sys, 'frozen', False):
            base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        else:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            
        self.mp3_file = os.path.join(base_dir, "resource", "alarm.mp3")
        
    def play_music(self):
        try:
            if os.path.exists(self.mp3_file):
                pygame.mixer.music.load(self.mp3_file)
                pygame.mixer.music.play(loops=-1)  # 음악 무한 반복 재생
            else:
                # 파일이 없을 경우 기본 비프음 출력
                import winsound
                winsound.Beep(1000, 1000)
        except Exception as e:
            print(f"Music error: {e}")
        
    def stop_music(self):
        try:
            pygame.mixer.music.stop()  # 음악 정지
        except Exception:
            pass