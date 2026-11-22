import asyncio
import random
import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Racing Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

BLUE = (40, 130, 255)
RED = (240, 70, 70)
WHITE = (255, 255, 255)
GRAY = (70, 70, 70)
GREEN = (50, 140, 70)


def reset_game():
    player = pygame.Rect(175, 490, 50, 80)
    enemy = pygame.Rect(random.randint(75, 275), -80, 50, 80)
    return player, enemy, 0, False


player, enemy, score, game_over = reset_game()
running = True


async def main():
    global player, enemy, score, game_over, running

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    player, enemy, score, game_over = reset_game()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.left > 60:
                player.x -= 5
            if keys[pygame.K_RIGHT] and player.right < 340:
                player.x += 5

            enemy.y += 5 + min(score, 10)
            if enemy.top > HEIGHT:
                score += 1
                enemy.y = -80
                enemy.x = random.randint(75, 275)

            if player.colliderect(enemy):
                game_over = True

        screen.fill(GREEN)
        pygame.draw.rect(screen, GRAY, (50, 0, 300, HEIGHT))
        pygame.draw.line(screen, WHITE, (50, 0), (50, HEIGHT), 4)
        pygame.draw.line(screen, WHITE, (350, 0), (350, HEIGHT), 4)
        for y in range(0, HEIGHT, 80):
            pygame.draw.rect(screen, WHITE, (198, y, 4, 40))

        pygame.draw.rect(screen, BLUE, player, border_radius=8)
        pygame.draw.rect(screen, RED, enemy, border_radius=8)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (65, 15))

        if game_over:
            message = font.render("GAME OVER", True, WHITE)
            retry = font.render("SPACE TO RESTART", True, WHITE)
            screen.blit(message, message.get_rect(center=(200, 250)))
            screen.blit(retry, retry.get_rect(center=(200, 300)))

        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
