import streamlit as st
import pygame
import random
from PIL import Image
import numpy as np
import os

def raceGame():
    st.title("🏎️ Race Game 🏎️")
    
    # Game constants
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    CAR_WIDTH = 40
    CAR_HEIGHT = 60
    OBSTACLE_WIDTH = 60
    OBSTACLE_HEIGHT = 60
    FPS = 60

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Load images
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(current_dir, 'img')
    
    player_car_img = pygame.image.load(os.path.join(img_dir, 'car.png'))
    enemy_car1_img = pygame.image.load(os.path.join(img_dir, 'enemy_car_1.png'))
    enemy_car2_img = pygame.image.load(os.path.join(img_dir, 'enemy_car_2.png'))

    # Scale images
    player_car_img = pygame.transform.scale(player_car_img, (CAR_WIDTH, CAR_HEIGHT))
    enemy_car1_img = pygame.transform.scale(enemy_car1_img, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    enemy_car2_img = pygame.transform.scale(enemy_car2_img, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Initialize game state
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'player_x' not in st.session_state:
        st.session_state.player_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
    if 'high_score' not in st.session_state:
        st.session_state.high_score = 0

    def reset_game():
        st.session_state.game_active = True
        st.session_state.game_over = False
        st.session_state.score = 0
        st.session_state.player_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2

    def draw_car(surface, x, y):
        surface.blit(player_car_img, (x, y))

    def draw_obstacle(surface, x, y, obstacle_type):
        if obstacle_type == 1:
            surface.blit(enemy_car1_img, (x, y))
        else:
            surface.blit(enemy_car2_img, (x, y))

    def race_game_loop():
        pygame.init()
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        
        player_y = SCREEN_HEIGHT - CAR_HEIGHT - 20
        player_speed = 7  # Increased speed for smoother movement
        obstacles = []
        obstacle_speed = 5
        
        game_frame = st.empty()
        score_display = st.empty()
        
        while True:
            screen.fill(GRAY)  # Changed background to gray for road-like appearance
            
            # Draw road lines
            for i in range(0, SCREEN_HEIGHT, 100):
                pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH//2 - 2, i, 4, 60))  # Thinner, more realistic lines
                pygame.draw.rect(screen, WHITE, (10, i, 4, 60))  # Left road boundary
                pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 14, i, 4, 60))  # Right road boundary
            
            # Player controls with smoother movement
            if st.session_state.game_active:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and st.session_state.player_x > 0:
                    st.session_state.player_x = max(0, st.session_state.player_x - player_speed)
                if keys[pygame.K_RIGHT] and st.session_state.player_x < SCREEN_WIDTH - CAR_WIDTH:
                    st.session_state.player_x = min(SCREEN_WIDTH - CAR_WIDTH, st.session_state.player_x + player_speed)
            
            # Draw player car
            draw_car(screen, st.session_state.player_x, player_y)
            
            # Spawn and move obstacles
            if random.randint(1, 50) == 1:
                obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
                obstacle_type = random.randint(1, 2)  # Randomly choose between two enemy car types
                obstacles.append([obstacle_x, -OBSTACLE_HEIGHT, obstacle_type])
            
            for obstacle in obstacles[:]:
                obstacle[1] += obstacle_speed
                draw_obstacle(screen, obstacle[0], obstacle[1], obstacle[2])
                
                # Collision detection
                if (obstacle[1] + OBSTACLE_HEIGHT > player_y and 
                    obstacle[1] < player_y + CAR_HEIGHT and 
                    obstacle[0] < st.session_state.player_x + CAR_WIDTH and 
                    obstacle[0] + OBSTACLE_WIDTH > st.session_state.player_x):
                    st.session_state.game_over = True
                    if st.session_state.score > st.session_state.high_score:
                        st.session_state.high_score = st.session_state.score
                    st.session_state.game_active = False
                    return
                
                # Update score
                if obstacle[1] > SCREEN_HEIGHT:
                    obstacles.remove(obstacle)
                    st.session_state.score += 1
            
            # Convert pygame surface to streamlit image
            frame = pygame.surfarray.array3d(screen)
            frame = frame.swapaxes(0, 1)
            image = Image.fromarray(frame.astype('uint8'))
            game_frame.image(image, use_column_width=True)
            
            # Display score with improved styling
            score_display.markdown(f"""
                <div style='text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px;'>
                    <h2 style='color: #1f1f1f;'>Score: {st.session_state.score} | High Score: {st.session_state.high_score}</h2>
                </div>
            """, unsafe_allow_html=True)
            
            clock.tick(FPS)

    # Game interface with improved styling
    if st.session_state.game_over:
        st.error("🏁 Game Over!")
        st.markdown(f"<h2 style='text-align: center;'>Final Score: {st.session_state.score}</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Play Again", use_container_width=True):
                reset_game()
                st.experimental_rerun()
    elif not st.session_state.game_active:
        st.markdown("""
            <div style='text-align: center; padding: 20px;'>
                <h3>🎮 Controls</h3>
                <p>Use the <kbd>←</kbd> and <kbd>→</kbd> arrow keys to move your car!</p>
                <p>Avoid the incoming vehicles and survive as long as possible!</p>
            </div>
        """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚦 Start Game", use_container_width=True):
                reset_game()
                race_game_loop()
    else:
        st.markdown("""
            <div style='text-align: center;'>
                <p>Use <kbd>←</kbd> and <kbd>→</kbd> arrow keys to avoid obstacles!</p>
            </div>
        """, unsafe_allow_html=True)
        race_game_loop()
