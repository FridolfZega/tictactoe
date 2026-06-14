import cv2
import mediapipe as mp
import time
import numpy as np
from game import get_cell, check_winner, reset_board, make_move

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6, min_tracking_confidence=0.6)
mp_draw = mp.solutions.drawing_utils

# Board Tic Tac Toe
board = reset_board()
current_player = "X"
selected_cell = -1
selection_start = 0.0
winner = None
winning_line = None
game_over = False

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Color Palette - Futuristic Neon Theme
COLORS = {
    'background': (10, 12, 20),
    'grid': (0, 255, 255),  # Cyan
    'grid_light': (100, 255, 255),
    'neon_pink': (255, 0, 127),
    'neon_purple': (200, 0, 255),
    'neon_blue': (0, 150, 255),
    'neon_green': (0, 255, 100),
    'player_x': (0, 150, 255),  # Blue
    'player_o': (255, 0, 127),  # Pink
    'text_primary': (255, 255, 255),
    'text_secondary': (180, 180, 180),
    'highlight': (0, 255, 255),
    'win_line': (0, 255, 150),
    'glass_bg': (30, 40, 60),
}

# Animation frame counter
frame_count = 0


def create_glass_panel(img, x1, y1, x2, y2, alpha=0.3):
    """Buat efek glassmorphism panel"""
    overlay = img.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), COLORS['glass_bg'], -1)
    cv2.rectangle(overlay, (x1, y1), (x2, y2), COLORS['neon_purple'], 2)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)


def draw_neon_line(img, pt1, pt2, color, thickness=3, glow=True):
    """Gambar garis dengan efek neon glow"""
    if glow:
        # Glow effect (thicker, semi-transparent)
        overlay = img.copy()
        cv2.line(overlay, pt1, pt2, color, thickness + 6)
        cv2.addWeighted(overlay, 0.3, img, 0.7, 0, img)
    # Main line
    cv2.line(img, pt1, pt2, color, thickness)


def draw_grid(img):
    """Gambar grid 3x3 dengan efek neon elegan"""
    h, w, _ = img.shape
    
    # Grid dimensions
    cell_w = w // 3
    cell_h = h // 3
    
    grid_color = COLORS['grid']
    glow_color = (50, 200, 200)
    
    # Vertical lines dengan glow effect
    for i in range(1, 3):
        x = i * cell_w
        # Glow layer
        overlay = img.copy()
        cv2.line(overlay, (x, 100), (x, h - 100), glow_color, 12)
        cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)
        # Main line
        cv2.line(img, (x, 100), (x, h - 100), grid_color, 4)
    
    # Horizontal lines dengan glow effect
    for i in range(1, 3):
        y = i * cell_h
        # Glow layer
        overlay = img.copy()
        cv2.line(overlay, (50, y), (w - 50, y), glow_color, 12)
        cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)
        # Main line
        cv2.line(img, (50, y), (w - 50, y), grid_color, 4)
    
    # Border dengan efek neon corner
    border_thickness = 3
    cv2.rectangle(img, (50, 100), (w - 50, h - 100), COLORS['grid'], border_thickness)
    
    # Corner glow effects
    corner_pts = [(50, 100), (w - 50, 100), (50, h - 100), (w - 50, h - 100)]
    for pt in corner_pts:
        overlay = img.copy()
        cv2.circle(overlay, pt, 15, COLORS['neon_purple'], -1)
        cv2.addWeighted(overlay, 0.4, img, 0.6, 0, img)


def draw_marks(img):
    """Gambar X dan O dengan efek 3D dan shadow"""
    h, w, _ = img.shape
    cell_w = w // 3
    cell_h = h // 3
    
    for i, mark in enumerate(board):
        if mark:
            row = i // 3
            col = i % 3
            cx = col * cell_w + cell_w // 2
            cy = row * cell_h + cell_h // 2
            
            if mark == "X":
                color = COLORS['player_x']
                draw_x_mark(img, cx, cy, color)
            else:
                color = COLORS['player_o']
                draw_o_mark(img, cx, cy, color)


def draw_x_mark(img, cx, cy, color):
    """Gambar X dengan efek shadow dan glow"""
    offset = 50
    thickness = 8
    
    # Shadow effect
    shadow_offset = 3
    shadow_color = (20, 20, 40)
    cv2.line(img, (cx - offset + shadow_offset, cy - offset + shadow_offset), 
             (cx + offset + shadow_offset, cy + offset + shadow_offset), shadow_color, thickness + 2)
    cv2.line(img, (cx + offset + shadow_offset, cy - offset + shadow_offset), 
             (cx - offset + shadow_offset, cy + offset + shadow_offset), shadow_color, thickness + 2)
    
    # Glow effect
    overlay = img.copy()
    cv2.line(overlay, (cx - offset, cy - offset), (cx + offset, cy + offset), color, thickness + 4)
    cv2.line(overlay, (cx + offset, cy - offset), (cx - offset, cy + offset), color, thickness + 4)
    cv2.addWeighted(overlay, 0.3, img, 0.7, 0, img)
    
    # Main mark
    cv2.line(img, (cx - offset, cy - offset), (cx + offset, cy + offset), color, thickness)
    cv2.line(img, (cx + offset, cy - offset), (cx - offset, cy + offset), color, thickness)


def draw_o_mark(img, cx, cy, color):
    """Gambar O dengan efek shadow dan glow"""
    radius = 50
    thickness = 8
    
    # Shadow effect
    shadow_offset = 3
    shadow_color = (20, 20, 40)
    cv2.circle(img, (cx + shadow_offset, cy + shadow_offset), radius, shadow_color, thickness + 2)
    
    # Glow effect
    overlay = img.copy()
    cv2.circle(overlay, (cx, cy), radius, color, thickness + 4)
    cv2.addWeighted(overlay, 0.3, img, 0.7, 0, img)
    
    # Main mark
    cv2.circle(img, (cx, cy), radius, color, thickness)


def draw_hold_progress(img, cell, progress):
    """Gambar progress bar hold detection dengan animasi"""
    if cell < 0 or cell > 8:
        return
    
    h, w, _ = img.shape
    cell_w = w // 3
    cell_h = h // 3
    
    row = cell // 3
    col = cell % 3
    
    # Progress bar position
    bar_x1 = col * cell_w + 20
    bar_y1 = (row + 1) * cell_h - 25
    bar_x2 = (col + 1) * cell_w - 20
    bar_y2 = (row + 1) * cell_h - 15
    
    # Background bar
    overlay = img.copy()
    cv2.rectangle(overlay, (bar_x1, bar_y1), (bar_x2, bar_y2), COLORS['glass_bg'], -1)
    cv2.addWeighted(overlay, 0.6, img, 0.4, 0, img)
    cv2.rectangle(img, (bar_x1, bar_y1), (bar_x2, bar_y2), COLORS['neon_purple'], 2)
    
    # Progress fill dengan gradient color
    fill_width = int((bar_x2 - bar_x1) * progress)
    if fill_width > 0:
        # Gradient dari cyan ke pink
        gradient_color = (
            int(0 + (255 - 0) * progress),      # B
            int(255 - (255 - 0) * progress),    # G
            int(255 - (255 - 127) * progress)   # R
        )
        cv2.rectangle(img, (bar_x1, bar_y1), (bar_x1 + fill_width, bar_y2), gradient_color, -1)
    
    # Percentage text
    percentage = int(progress * 100)
    cv2.putText(img, f"{percentage}%", (bar_x1 + 5, bar_y1 - 5), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, COLORS['neon_green'], 1)


def draw_overlay(img):
    """Gambar overlay informasi dengan panel glassmorphism"""
    h, w, _ = img.shape
    
    # Top panel - Game title dan status
    create_glass_panel(img, 10, 10, w - 10, 95, alpha=0.5)
    
    cv2.putText(img, "TIC TAC TOE", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, 
                COLORS['neon_green'] if 'neon_cyan' not in COLORS else COLORS['neon_cyan'], 2)
    cv2.putText(img, "HAND VISION", (20, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                COLORS['text_secondary'], 1)
    
    # Status text
    if winner == "Draw":
        status_text = "GAME DRAW!"
        status_color = COLORS['neon_purple']
    elif winner:
        status_text = f"PLAYER {winner} WIN!"
        status_color = COLORS['neon_green']
    else:
        status_text = f"PLAYER {current_player} TURN"
        status_color = COLORS['player_x'] if current_player == "X" else COLORS['player_o']
    
    cv2.putText(img, status_text, (w - 360, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                status_color, 2)
    
    # Bottom panel - Instructions
    create_glass_panel(img, 10, h - 100, w - 10, h - 10, alpha=0.5)
    
    cv2.putText(img, "Point index finger to cell and hold 1 second to play", 
                (20, h - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.65, COLORS['text_primary'], 1)
    cv2.putText(img, "[ R ] Reset Game     [ ESC ] Quit", 
                (20, h - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.65, COLORS['neon_green'], 1)
    
    # Player indicator panels
    draw_player_panel(img, w)


def draw_player_panel(img, w):
    """Gambar panel pemain aktif dan skor"""
    h, _, _ = img.shape
    
    panel_x = w - 280
    panel_y = 120
    panel_w = 260
    panel_h = 120
    
    # Background panel
    create_glass_panel(img, panel_x, panel_y, panel_x + panel_w, panel_y + panel_h, alpha=0.6)
    
    # Player X info
    x_color = COLORS['player_x']
    x_count = board.count('X')
    cv2.putText(img, "PLAYER X", (panel_x + 20, panel_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                x_color, 2)
    cv2.circle(img, (panel_x + 230, panel_y + 25), 8, x_color, -1)
    cv2.putText(img, f"Moves: {x_count}", (panel_x + 20, panel_y + 65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
                x_color, 1)
    
    # Player O info
    o_color = COLORS['player_o']
    o_count = board.count('O')
    cv2.putText(img, "PLAYER O", (panel_x + 20, panel_y + 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                o_color, 2)
    cv2.circle(img, (panel_x + 230, panel_y + 90), 8, o_color, -1)
    cv2.putText(img, f"Moves: {o_count}", (panel_x + 20, panel_y + 130), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
                o_color, 1)


def draw_highlight(img, cell, color=None):
    """Highlight cell yang ditunjuk dengan animasi dan efek"""
    if cell < 0 or cell > 8 or board[cell] != "":
        return
    
    if color is None:
        color = COLORS['highlight']
    
    h, w, _ = img.shape
    cell_w = w // 3
    cell_h = h // 3
    
    row = cell // 3
    col = cell % 3
    x1 = col * cell_w + 5
    y1 = row * cell_h + 100
    x2 = (col + 1) * cell_w - 5
    y2 = (row + 1) * cell_h - 5
    
    # Animated glow dengan pulsing effect
    glow_intensity = 0.2 + 0.15 * abs(np.sin(frame_count * 0.1))
    
    # Multiple glow layers
    for i in range(3):
        overlay = img.copy()
        intensity = glow_intensity * (0.3 - i * 0.1)
        cv2.rectangle(overlay, (x1 - i, y1 - i), (x2 + i, y2 + i), color, 2)
        cv2.addWeighted(overlay, intensity, img, 1 - intensity, 0, img)
    
    # Main highlight border
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
    
    # Fill dengan transparency
    overlay = img.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), color, -1)
    cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)


def draw_win_line(img, combo):
    """Gambar garis kemenangan dengan efek neon spectacular"""
    if not combo:
        return
    
    h, w, _ = img.shape
    cell_w = w // 3
    cell_h = h // 3
    
    start, _, end = combo
    row1, col1 = divmod(start, 3)
    row2, col2 = divmod(end, 3)
    
    x1 = col1 * cell_w + cell_w // 2
    y1 = row1 * cell_h + cell_h // 2 + 100
    x2 = col2 * cell_w + cell_w // 2
    y2 = row2 * cell_h + cell_h // 2 + 100
    
    # Animated line dengan pulsing glow
    pulse = abs(np.sin(frame_count * 0.15)) * 0.5 + 0.5
    glow_color = COLORS['win_line']
    
    # Thick glow layer
    overlay = img.copy()
    cv2.line(overlay, (x1, y1), (x2, y2), glow_color, 30)
    cv2.addWeighted(overlay, pulse * 0.4, img, 1 - pulse * 0.4, 0, img)
    
    # Medium glow layer
    cv2.line(img, (x1, y1), (x2, y2), glow_color, 20)
    
    # Main bright line
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 8)


def draw_winner_overlay(img):
    """Gambar overlay kemenangan dengan efek spektakuler"""
    h, w, _ = img.shape
    
    if winner and winner != "Draw":
        # Semi-transparent overlay
        overlay = img.copy()
        cv2.rectangle(overlay, (0, 0), (w, h), (10, 10, 30), -1)
        cv2.addWeighted(overlay, 0.4, img, 0.6, 0, img)
        
        # Winner panel
        panel_h = 200
        panel_y = (h - panel_h) // 2
        
        create_glass_panel(img, 100, panel_y, w - 100, panel_y + panel_h, alpha=0.9)
        
        # Animated text dengan scaling
        pulse = abs(np.sin(frame_count * 0.12)) * 0.3 + 0.85
        font_scale = 1.8 * pulse
        
        winner_text = f"PLAYER {winner} WINS!"
        winner_color = COLORS['player_x'] if winner == "X" else COLORS['player_o']
        
        text_size = cv2.getTextSize(winner_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 3)[0]
        text_x = (w - text_size[0]) // 2
        text_y = panel_y + 80
        
        cv2.putText(img, winner_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 
                   font_scale, winner_color, 4)
        cv2.putText(img, "Press R to Play Again", (w // 2 - 120, panel_y + 150), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLORS['neon_green'], 2)
    
    elif winner == "Draw":
        # Draw overlay
        overlay = img.copy()
        cv2.rectangle(overlay, (0, 0), (w, h), (10, 10, 30), -1)
        cv2.addWeighted(overlay, 0.4, img, 0.6, 0, img)
        
        panel_h = 180
        panel_y = (h - panel_h) // 2
        
        create_glass_panel(img, 100, panel_y, w - 100, panel_y + panel_h, alpha=0.9)
        
        pulse = abs(np.sin(frame_count * 0.12)) * 0.3 + 0.85
        font_scale = 1.6 * pulse
        
        text_size = cv2.getTextSize("GAME DRAW!", cv2.FONT_HERSHEY_SIMPLEX, font_scale, 3)[0]
        text_x = (w - text_size[0]) // 2
        text_y = panel_y + 70
        
        cv2.putText(img, "GAME DRAW!", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 
                   font_scale, COLORS['neon_purple'], 4)
        cv2.putText(img, "Press R to Play Again", (w // 2 - 120, panel_y + 130), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLORS['neon_green'], 2)


def draw_finger_indicator(img, x, y):
    """Gambar indikator jari dengan efek glow"""
    # Main circle
    cv2.circle(img, (x, y), 12, COLORS['neon_green'], -1)
    
    # Glow effect
    overlay = img.copy()
    cv2.circle(overlay, (x, y), 20, COLORS['neon_green'], 3)
    cv2.addWeighted(overlay, 0.3, img, 0.7, 0, img)
    
    # Crosshair
    cv2.line(img, (x - 20, y), (x + 20, y), COLORS['neon_green'], 1)
    cv2.line(img, (x, y - 20), (x, y + 20), COLORS['neon_green'], 1)


def reset_game():
    global board, current_player, winner, winning_line, game_over, selected_cell, selection_start
    board = reset_board()
    current_player = "X"
    winner = None
    winning_line = None
    game_over = False
    selected_cell = -1
    selection_start = 0.0


while True:
    ret, img = cap.read()
    if not ret:
        break
    
    frame_count += 1
    
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    
    # Apply dark tint to camera background
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 0), (w, h), COLORS['background'], -1)
    cv2.addWeighted(overlay, 0.5, img, 0.5, 0, img)
    hover_cell = -1
    finger_x, finger_y = -1, -1

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # Hand detection dan cell selection logic
    if result.multi_hand_landmarks and not game_over:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark[8]  # Index finger tip
        finger_x, finger_y = int(lm.x * w), int(lm.y * h)
        cell = get_cell(finger_x, finger_y, w, h)
        hover_cell = cell

        if cell == selected_cell and board[cell] == "":
            current_time = time.time()
            hold_duration = current_time - selection_start
            
            if hold_duration > 1.0:
                # Make move - logic tetap sama
                if make_move(board, cell, current_player):
                    winner, winning_line = check_winner(board)
                    if not winner:
                        current_player = "O" if current_player == "X" else "X"
                    game_over = winner is not None
                selected_cell = -1
                selection_start = 0.0
            else:
                # Show progress
                progress = hold_duration
                draw_hold_progress(img, cell, progress)
        else:
            selected_cell = cell
            selection_start = time.time()

    # Render layers
    draw_grid(img)
    draw_marks(img)
    
    # Highlight selected cell
    if hover_cell != -1 and not game_over and board[hover_cell] == "":
        draw_highlight(img, hover_cell, COLORS['highlight'])
    
    # Draw finger indicator
    if finger_x != -1 and finger_y != -1:
        draw_finger_indicator(img, finger_x, finger_y)
    
    # Draw game status
    draw_overlay(img)
    
    # Draw winning line
    if game_over and winning_line:
        draw_win_line(img, winning_line)
    
    # Draw winner overlay
    draw_winner_overlay(img)

    # Keyboard input
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break
    elif key == ord("r") or key == ord("R"):
        reset_game()

    cv2.imshow("TIC TAC TOE - HAND VISION", img)

cap.release()
cv2.destroyAllWindows()
