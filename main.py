import cv2
import mediapipe as mp
import time
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


def draw_grid(img):
    h, w, _ = img.shape
    line_color = (220, 220, 220)
    thickness = 6
    cv2.line(img, (w // 3, 0), (w // 3, h), line_color, thickness)
    cv2.line(img, (2 * w // 3, 0), (2 * w // 3, h), line_color, thickness)
    cv2.line(img, (0, h // 3), (w, h // 3), line_color, thickness)
    cv2.line(img, (0, 2 * h // 3), (w, 2 * h // 3), line_color, thickness)
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 0), (w, 92), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.44, img, 0.56, 0, img)


def draw_marks(img):
    h, w, _ = img.shape
    for i, mark in enumerate(board):
        if mark:
            row = i // 3
            col = i % 3
            cx = col * w // 3 + w // 6
            cy = row * h // 3 + h // 6
            color = (255, 100, 50) if mark == "X" else (50, 200, 255)
            cv2.putText(img, mark, (cx - 40, cy + 40), cv2.FONT_HERSHEY_SIMPLEX, 3, color, 8)


def draw_overlay(img):
    h, w, _ = img.shape
    if winner == "Draw":
        status = "Hasil: Seri"
    elif winner:
        status = f"Pemenang: {winner}"
    else:
        status = f"Giliran: {current_player}"

    cv2.putText(img, "Tic Tac Toe Kamera", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (240, 240, 240), 2)
    cv2.putText(img, status, (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (180, 255, 180), 2)
    cv2.putText(img, "Arahkan jari telunjuk ke kotak lalu tahan 1 detik", (20, h - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (220, 220, 220), 1)
    cv2.putText(img, "Tekan R untuk ulangi / ESC untuk keluar", (20, h - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (220, 220, 220), 1)


def draw_highlight(img, cell, color=(0, 180, 255)):
    if cell < 0 or cell > 8:
        return
    h, w, _ = img.shape
    row = cell // 3
    col = cell % 3
    x1 = col * w // 3 + 5
    y1 = row * h // 3 + 5
    x2 = (col + 1) * w // 3 - 5
    y2 = (row + 1) * h // 3 - 5
    overlay = img.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), color, -1)
    cv2.addWeighted(overlay, 0.15, img, 0.85, 0, img)
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 4)


def draw_win_line(img, combo):
    if not combo:
        return
    h, w, _ = img.shape
    start, _, end = combo
    row1, col1 = divmod(start, 3)
    row2, col2 = divmod(end, 3)
    x1 = col1 * w // 3 + w // 6
    y1 = row1 * h // 3 + h // 6
    x2 = col2 * w // 3 + w // 6
    y2 = row2 * h // 3 + h // 6
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 12)


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

    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    hover_cell = -1

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks and not game_over:
        hand = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
        lm = hand.landmark[8]
        x, y = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (x, y), 12, (0, 0, 255), -1)
        cell = get_cell(x, y, w, h)
        hover_cell = cell

        if cell == selected_cell:
            if time.time() - selection_start > 1.0:
                if make_move(board, cell, current_player):
                    winner, winning_line = check_winner(board)
                    if not winner:
                        current_player = "O" if current_player == "X" else "X"
                    game_over = winner is not None
                selected_cell = -1
                selection_start = 0.0
        else:
            selected_cell = cell
            selection_start = time.time()

    draw_grid(img)
    if hover_cell != -1 and not game_over:
        draw_highlight(img, hover_cell)
    draw_marks(img)
    draw_overlay(img)
    if game_over and winning_line:
        draw_win_line(img, winning_line)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord("r"):
        reset_game()

    cv2.imshow("Tic Tac Toe Kamera", img)

cap.release()
cv2.destroyAllWindows()
