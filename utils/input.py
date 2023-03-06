import pygame


class Input:
    def __init__(self, player, game, settings):
        self.player = player
        self.settings = settings
        self.game = game

        self.min_x = 0
        self.max_x = self.settings.width - self.player.width
        self.mouse_pressed = False

    def update(self):
        # Use variable to reduce for loops for both updating the button's hover effect and handling click
        self.mouse_pressed = False

        # Go through events and proceed to quit or set mouse_pressed to True for later use
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.game.buttons.selected_button = (self.game.buttons.selected_button + 1)\
                                                        % self.game.buttons.button_count
                elif event.key == pygame.K_UP:
                    self.game.buttons.selected_button -= 1
                    if self.game.buttons.selected_button < 0:
                        self.game.buttons.selected_button = self.game.buttons.button_count - 1
                elif event.key == pygame.K_RETURN and self.game.buttons.button_count > 0:
                    self.game.buttons.buttons[self.game.buttons.selected_button].click()

        # Get keyboard and mouse inputs
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        # Go through buttons and update hover / handle clicking
        for index, button in enumerate(self.game.buttons.buttons):
            if button.update_hovered(mouse[0], mouse[1]):
                self.game.buttons.selected_button = index
                if self.mouse_pressed:
                    button.click()

        # Check to exit with escape
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        # Update player position
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.x -= self.settings.__speed__ * self.game.modifier
            if self.player.x < self.min_x:
                self.player.x = self.min_x
                self.player.rot = 0
            else:
                self.player.rot = 10
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.x += self.settings.__speed__ * self.game.modifier

            if self.player.x > self.max_x:
                self.player.x = self.max_x
                self.player.rot = 0
            else:
                self.player.rot = -10
        else:
            self.player.rot = 0
