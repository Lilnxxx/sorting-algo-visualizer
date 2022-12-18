import pygame
import random
import math
import time

pygame.init()
pygame.display.set_caption('Sorting Algo. Visualizer')
n=80
speed=30
min_val=500
max_val=1
sorting =False
ascending =True

tick=int(0)
minutes=00
seconds=00
FONT = pygame.font.SysFont('comicsans', 18)
LARGE_FONT = pygame.font.SysFont('comicsans', 28)
clock = pygame.time.Clock()
GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]


surface = pygame.display.set_mode((1000,600))
surface.fill((0))
BLACK = 255, 255, 255#0, 0, 0
WHITE = 0, 0, 0#255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0,255,255



def rand_lst(n):
    global min_val,max_val
    lst=[]
    for _ in range(n):
        r=random.randint(1,500)
        if(r<min_val):min_val=r
        if(r>max_val):max_val=r
        lst.append(r)
    return lst

def draw( algo_name,ascending):
    surface.fill(WHITE)
    spe_siz = FONT.render(f" Speed - {speed}  Size - {n}", 1, BLACK)
    surface.blit(spe_siz, (5 , 5))

    stop_watch = FONT.render(f"Time - 0{minutes} : {seconds}0 : 00", 1, BLACK)
    surface.blit(stop_watch, (800 , 5))

    title = LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, GREEN)
    surface.blit(title, (500 - (title.get_width()/2) , 5))

    controls = FONT.render("R - Reset | SPACE - Sort | A - Ascending | D - Descending | UP/DOWN -Speed | RIGHT/LEFT - Size", 1,BLACK)
    surface.blit(controls, (500 - controls.get_width()/2 , 45))

    sorting = FONT.render("I - Insertion Sort | B - Bubble Sort | Q - Quick Sort | S - Selection Sort", 1,BLACK)
    surface.blit(sorting, (500 - sorting.get_width()/2 , 75))

    draw_list()
    pygame.display.update()

def draw_list(color_positions={},clear_bg=False):
    global seconds,tick,minutes
    width=math.floor(880/n)
    padx=(1000-(width*n))//2
    if not sorting:
        minutes=seconds=tick=0
    if clear_bg:
        clear_rect = (padx, 100,1000-padx-padx,500)
        pygame.draw.rect(surface, (0,0,0), clear_rect)
        tick=tick+1
    if clear_bg and sorting:
        clear_rect = (800, 0,1000-padx-padx,30)
        pygame.draw.rect(surface,WHITE, clear_rect)
        stop_watch = FONT.render(f"Time - 0{minutes} : {seconds} : {tick}", 1, BLACK)
        surface.blit(stop_watch, (800 , 5))
        if(tick==speed):
            seconds=seconds+1
            if seconds==60:
                minutes=minutes+1
                seconds=0
            tick=0

    for val,i in enumerate(lst1):
        color = GRADIENTS[val % 3]
        if val in color_positions:
            color = color_positions[val]
        pygame.draw.rect(surface, color, pygame.Rect(padx,600-i, width, i))
        padx=padx+width    
    if clear_bg:
        pygame.display.update()

def bubble_sort( ascending=True):
    for i in range(len(lst1) - 1):
        for j in range(len(lst1) - 1 - i):
            num1 = lst1[j]
            num2 = lst1[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
                draw_list( {j: RED, j + 1: GREEN},True)
                yield True

def insertion_sort( ascending=True):
	for i in range(1, len(lst1)):
		current = lst1[i]

		while True:
			ascending_sort = i > 0 and lst1[i - 1] > current and ascending
			descending_sort = i > 0 and lst1[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			lst1[i] = lst1[i - 1]
			i = i - 1
			lst1[i] = current
			draw_list( {i - 1: GREEN, i: RED}, True)
			yield True

def quick_sort( l=0, h=n-1):
    stack = [0] * (n)
    stack[0] = 0
    stack[1] = n-1
    top=1
    # print(ascending," ",n," ",h," l ",l)
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        i = ( l - 1 )
        x = lst1[h]
        for j in range(l, h):
            draw_list({h:BLUE},True)
            yield True
            draw_list( {i : GREEN, j: RED}, True)
            if (lst1[j] >= x and ascending ):
                i = i + 1
                lst1[i], lst1[j] = lst1[j], lst1[i]
                draw_list( {i : RED, j: GREEN}, True)
            if (lst1[j] <= x and not ascending ):
                # print("desending qksort")
                i = i + 1
                lst1[i], lst1[j] = lst1[j], lst1[i]
                draw_list( {i : RED, j: GREEN}, True)
            
            yield True

        lst1[i + 1], lst1[h] = lst1[h], lst1[i + 1]
        draw_list( {i+1 : GREEN, h: RED}, True)
        yield True
        p=i + 1
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return lst1

def selection_sort(smal=0):
    sizz=len(lst1)
    start=0
    smal=0
    for m in range(len(lst1)):
        smal=start
        for i in range(start,sizz):
            if(ascending):
                if(lst1[smal]>lst1[i]):
                    smal=i
            else:
                if(lst1[smal]<lst1[i]):
                    smal=i
            draw_list( {i: BLUE,smal:GREEN,start:RED},True)
            yield True
        lst1[start],lst1[smal]=lst1[smal],lst1[start]
        start=start+1



sorting_algorithm = bubble_sort
sorting_algo_name = "Bubble Sort"
sorting_algorithm_generator = None
lst1=rand_lst(n)

# draw(ascending)
running =True
while(running):
    # print("hh") 
    clock.tick(speed)
    if sorting:
        try:
            next(sorting_algorithm_generator)
        except StopIteration:
            sorting = False
    else:
        # print("if")
        draw( sorting_algo_name,ascending)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_r:
            lst1=rand_lst(n)
            sorting=False
        elif event.key == pygame.K_SPACE and sorting==False:
            sorting = True
            sorting_algorithm_generator = sorting_algorithm( ascending)
        elif event.key == pygame.K_a and not sorting:
            ascending=True
        elif event.key == pygame.K_d and not sorting:
            ascending=False
        elif event.key == pygame.K_b and not sorting:
            sorting_algorithm = bubble_sort
            sorting_algo_name = "Bubble Sort"
        elif event.key == pygame.K_i and not sorting:
            sorting_algorithm = insertion_sort
            sorting_algo_name = "Insertion Sort"
        elif event.key == pygame.K_q and not sorting:
            sorting_algorithm = quick_sort
            sorting_algo_name = "Quick Sort"
        elif event.key == pygame.K_s and not sorting:
            sorting_algorithm = selection_sort
            sorting_algo_name = "Selection Sort"      
        elif event.key == pygame.K_RIGHT and not sorting and n<220:
            n=n+10
            lst1=rand_lst(n)
        elif event.key == pygame.K_LEFT and not sorting and n>10:
            n=n-10
            lst1=rand_lst(n)
        elif event.key == pygame.K_UP and not sorting and speed<150:
            speed=speed+5
        elif event.key == pygame.K_DOWN and not sorting and speed>5:
            speed=speed-5



pygame.quit()