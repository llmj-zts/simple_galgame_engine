import pygame


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if menu == 1:
        MessageBox("GALGAME模板", 500, 100, 70, center=True)
        game_start_btn.blit()
        b_continue.blit()
        if game_start_btn.pressed():
            getting_started()
        elif b_continue.pressed():
            getting_started(True)

    elif menu == 3:
        # 游戏
        if step == 1:
            blit_bg(new_bg)
            if show_text[0] == "@E":
                set_step(5)
                old_bg = new_bg
                new_bg = "black"
                load_image(["@B", new_bg])
            elif show_text[0] == "@L":
                set_step(4)
                old_bg = new_bg
                new_bg = "black"
                load_image(["@B", new_bg])
            elif show_text[0] == "@S":
                set_step(6)
            elif show_text[0] == "@B":
                if new_bg != show_text[1]:
                    set_step(2)
                    old_bg = new_bg
                    new_bg = show_text[1]
                    load_image(show_text)
                else:
                    next()
            elif show_text[0] == "@T":
                set_step(3)
                old_bg = new_bg
                new_bg = "".join(show_text)
                load_image(show_text)
            else:
                if pengz(
                    pygame.mouse.get_pos(), (0, 0), (1450, 20), image["exit"].get_size()
                ):
                    image["exit"].set_alpha(100)
                    if pygame.mouse.get_pressed()[0] and not avoidmouse:
                        save()
                        set_menu(1)
                        continue
                else:
                    image["exit"].set_alpha(50)
                screen.blit(image["exit"], (1450, 20))
                if show_text[0] != None:
                    if show_text[0] + str(show_text[1]) in image:
                        screen.blit(
                            image[show_text[0] + str(show_text[1])], (800, 130)
                        )  # 立绘
                    screen.blit(image["text-bg"], (150, 550))
                    MessageBox(
                        show_text[0], 300, 580, 45, color=(232, 242, 252), center=True
                    )
                else:
                    screen.blit(image["text-bg"], (150, 550))
                line = 0
                for i in show_text[2][:show_length].split("\n"):
                    MessageBox(i, 200, 620 + line * 41, s=40, color=(0, 0, 0))
                    line += 1
                if show_length < len(show_text[2]):
                    show_length += 1
                    if pygame.mouse.get_pressed()[0] and not avoidmouse:
                        show_length = len(show_text[2])
                elif show_length == len(show_text[2]):
                    uia += 1
                    if uia > 50:
                        uia = 0
                    # 在这里可以添加樱花放大或旋转的效果,看你喜欢了
                    screen.blit(image["next"], (1298, 765))
                    if pygame.mouse.get_pressed()[0] and not avoidmouse:
                        next()
        elif step == 2:
            if alpha <= 255:
                alpha += 5
                blit_bg(old_bg)
                blit_bg(new_bg, alpha)
            else:
                blit_bg(new_bg)
                set_step(1)
                del image[old_bg]
                old_bg = None
                next()
        elif step == 3:
            if alpha <= 255:
                alpha += 5
                blit_bg(old_bg)
                blit_bg(new_bg, alpha)
            else:
                blit_bg(new_bg)
            if time.time() - start_time > 1.5:
                del image[old_bg]
                old_bg = None
                next()
                if show_text[0] == "@B":
                    set_step(2)
                    old_bg = new_bg
                    new_bg = show_text[1]
                    load_image(show_text)
                else:
                    set_step(1)
        elif step == 4:
            if alpha <= 255:
                alpha += 3
                blit_bg(old_bg)
                blit_bg("black", alpha)
                MessageBox("失败", 750, 250, 300, (250, 10, 10), alpha, True)
            else:
                blit_bg("black")
                MessageBox("失败", 750, 250, 300, (250, 10, 10), center=True)
                b_restart.blit()
                if b_restart.pressed():
                    del image[old_bg]
                    getting_started(c=show_text[1])
        elif step == 5:
            if alpha <= 255:
                alpha += 3
                blit_bg(old_bg)
                blit_bg("black", alpha)
                MessageBox("完", 750, 250, 400, alpha=alpha, center=True)
            else:
                blit_bg("black")
                MessageBox("完", 750, 250, 400, center=True)
                if time.time() - start_time > 8:
                    del image[old_bg]
                    del image["black"]
                    set_menu(1)
                    if os.path.exists("save.sav"):
                        os.remove("save.sav")
        elif step == 6:
            blit_bg(new_bg)
            n = 0
            for i in show_text[1:]:
                b_sel.reset(i[0], (400, 200 + 200 * n))
                b_sel.blit()
                if b_sel.pressed():
                    game_process = [i[1], -1]
                    next()
                    set_step(1)
                n += 1

    if pygame.mouse.get_pressed()[0]:
        avoidmouse = True
    else:
        avoidmouse = False
        # -----------------------------------------------------------------------------------------
# class Button:
#     def __init__(self, msg=None, pos=None, text_size=40):
#         self.msg = msg
#         self.pos = pos
#         self.text_size = text_size
#
#     def blit(self):
#         if pengz(pygame.mouse.get_pos(), (0, 0), self.pos, image["button"].get_size()):
#             image["button"].set_alpha(240)
#         else:
#             image["button"].set_alpha(180)
#         screen.blit(image["button"], self.pos)
#         message(
#             self.msg,
#             self.pos[0] + image["button"].get_size()[0] / 2,
#             self.pos[1] + image["button"].get_size()[1] / 2,
#             center=True,
#             s=self.text_size,
#         )
#
#     def pressed(self):
#         return (
#             pengz(pygame.mouse.get_pos(), (0, 0), self.pos, image["button"].get_size())
#             and pygame.mouse.get_pressed()[0]
#             and not avoidmouse
#         )
#
#     def reset(self, msg, pos):
#         self.msg = msg
#         self.pos = pos


def set_step(s):
    global step, alpha, start_time
    step = s
    alpha = 0
    start_time = time.time()


def set_menu(m):
    global menu
    menu = m


def load_bg(bg):
    image[bg] = pygame.image.load(f"bg/{bg}.png").convert_alpha()


def load_image(n):
    global image
    if n[0] == "@B": if n[1] == "black":
            image["black"] = pygame.Surface((WIDTH, HEIGHT))
        else:
            load_bg(n[1])
    elif n[0] == "@T":
        title_surface = pygame.Surface((WIDTH, HEIGHT))
        message(n[1], 250, 200, 100, surface=title_surface, center=True)  # 章节标题
        message(n[2], 250, 350, 70, surface=title_surface, center=True)  # 章节名称
        title_surface.blit(
            pygame.image.load(f"title/{n[3]}.png").convert_alpha(), (750, 200)
        )  # 章节图片
        image["".join(n)] = title_surface


def insert_str(original_string, position, substring):
    return original_string[:position] + substring + original_string[position:]


def char_width(char):
    if char in FONT_WIDTH_FIX:
        return FONT_WIDTH_FIX[char]
    if unicodedata.east_asian_width(char) in ["W", "F"]:
        return 2
    elif unicodedata.east_asian_width(char) in ["N", "Na"]:
        return 1
    elif unicodedata.east_asian_width(char) == "H":
        return 0.5
    else:
        return 0


def adapt_text_width(text, max_length):
    text_list = text.split("\n")
    for item_num in range(len(text_list)):
        l = 0
        n = 0
        string = text_list[item_num]
        for i in string:
            if i == "\n":
                l = 0
            else:
                l += char_width(i)
            if l > max_length:
                string = insert_str(string, n, "\n")
                l = char_width(i)
                n += 1
            n += 1
        text_list[item_num] = string
    return "\n".join(text_list)


def next():
    global show_text, show_length, game_process
    show_length = 0
    game_process[1] += 1
    if text[game_process[0]][game_process[1]][0] == "@P":
        game_process = [text[game_process[0]][game_process[1]][1], 0]
    show_text = text[game_process[0]][game_process[1]]
    if not show_text[0] in ("@E", "@L", "@S", "@B", "@T", "@P"):
        show_text[2] = adapt_text_width(show_text[2], 56)


def blit_bg(bg, a=255):
    if bg != None:
        # if bg not in image: load_bg(bg) #保底
        image[bg].set_alpha(a)
        screen.blit(image[bg], (0, 0))


def save():
    s = {}
    s["process"] = game_process.copy()
    s["bg"] = new_bg
    with open("save.sav", "wb") as pickle_file:
        pickle.dump(s, pickle_file)


def getting_started(load_save=False, c=1):
    global game_process, old_bg, new_bg, image

    old_bg = "screenshot"
    temp_screen = pygame.Surface((WIDTH, HEIGHT))
    temp_screen.blit(screen, (0, 0))
    image["screenshot"] = temp_screen
    set_menu(3)
    if load_save and os.path.exists("save.sav"):
        with open("save.sav", "rb") as pickle_file:
            s = pickle.load(pickle_file)
        game_process = s["process"].copy()
        game_process[1] -= 1
        new_bg = s["bg"]
        load_image(["@B", new_bg])
        set_step(2)
    else:
        if os.path.exists("save.sav"):
            os.remove("save.sav")
        game_process = [c, -1]
        next()
        new_bg = "".join(show_text)
        load_image(show_text)
        set_step(3)


# 变量
step = 0
menu = 1
show_text = []
show_length = 0
alpha = 0
image = {}
start_time = 0
avoidmouse = False
uia = 0
game_process = [0, 0]

old_bg = None
new_bg = None

message("加载中......", 500, 500, 50, (200, 200, 200))
pygame.display.flip()


# 加载图像
for i in glob.glob("ui/*.png"):
    image[os.path.basename(i).split(".")[0]] = pygame.image.load(i).convert_alpha()
for i in glob.glob("title/*.png"):
    image[os.path.basename(i).split(".")[0]] = pygame.image.load(i).convert_alpha()
# 创建按钮
b_continue = Button("继续游戏", (150, 350), 60)
btn_start_game = Button("从头开始", (150, 550), 60)
b_sel = Button()
b_restart = Button("继续", (600, 600))
