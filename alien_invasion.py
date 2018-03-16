import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_function as gf 

def run_game():
	#初始化并创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("外星人入侵")
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	ship = Ship(ai_settings, screen)
	#子弹编组
	bullets = Group()
	aliens = Group()
	gf.creat_fleet(ai_settings, screen, ship, aliens)
	
	
	#游戏主循环
	while True:
		
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
			bullets)
		if stats.game_active ==True:
			ship.update()#每次检查完事件更新飞船位置
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)	
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
			bullets, play_button)
		
run_game()