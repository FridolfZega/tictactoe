# ⚡ Quick Start Guide - Tic Tac Toe Hand Vision

## 30-Detik Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run aplikasi
python main.py

# 3. Mulai bermain!
```

---

## 🎮 Bermain dalam 1 Menit

1. **Point Index Finger** ke cell yang ingin dipilih
2. **Hold 1 Detik** - lihat progress bar mengisi
3. **Lepaskan** - cell akan terisi dengan symbol
4. **Giliran berganti** otomatis
5. **Menang** - garis kemenangan akan highlighted

---

## 🎨 Quick Theme Switch

### Option 1: Edit theme_config.py
```python
# Line terakhir file:
ACTIVE_THEME = THEME_CYBERPUNK  # Ubah ke tema pilihan
```

### Option 2: Edit main.py
```python
# Di top file (setelah import):
from theme_config import get_theme_by_name
COLORS = get_theme_by_name('cyberpunk')  # cyberpunk, synthwave, matrix, dll
```

### Available Themes:
- `neon_dark` (default) - Modern gaming
- `cyberpunk` - Bold orange neon
- `minimalist` - Clean light theme
- `synthwave` - Retro 80s
- `matrix` - Green hacker theme

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **R** | Restart game |
| **ESC** | Quit |

---

## 🔧 Quick Troubleshooting

### Webcam tidak detected?
```python
# Ubah index di main.py line ~25:
cap = cv2.VideoCapture(1)  # Try 1, 2, 3, etc
```

### Hand detection tidak berfungsi?
```python
# Pastikan pencahayaan cukup
# Ensure hand visible di frame
# Try adjust confidence threshold
min_detection_confidence=0.5
```

### Performa lambat?
```python
# Kurangi resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
```

---

## 📊 Project Files

| File | Purpose |
|------|---------|
| `main.py` | Main application (rendering + logic) |
| `game.py` | Game logic (untouched) |
| `theme_config.py` | Color themes & animation config |
| `requirements.txt` | Python dependencies |
| `README.md` | Full documentation |
| `ENHANCEMENT_GUIDE.md` | Customization guide |

---

## 🎬 Demo Scenarios

### Scenario 1: Play Game
```
1. Start python main.py
2. Point to top-left cell → hold 1 sec → X appears
3. Point to center cell → hold 1 sec → O appears
4. Continue until winner
5. See animated overlay
6. Press R to play again
```

### Scenario 2: Change Theme
```
1. Edit theme_config.py
2. Change: ACTIVE_THEME = THEME_CYBERPUNK
3. Run: python main.py
4. See new colors immediately
```

### Scenario 3: Customize Colors
```python
# In theme_config.py, edit:
THEME_NEON_DARK['player_x'] = (255, 100, 0)  # Orange
THEME_NEON_DARK['player_o'] = (100, 255, 200)  # Cyan
```

---

## 📈 Performance Tips

- **30+ FPS** - Smooth gameplay
- **1280x720** - Default resolution (responsive)
- **1 sec hold** - Perfect timing for selection
- **Real-time rendering** - All effects smooth

---

## ✨ Unique Features

✅ **Futuristic Neon UI** - Modern gaming aesthetic  
✅ **Hand Gesture Control** - Touchless interaction  
✅ **Smooth Animations** - Professional effects  
✅ **Multiple Themes** - 5 designs ready-to-use  
✅ **Real-time Feedback** - Progress bar & indicators  
✅ **Professional Overlay** - Stunning winner display  
✅ **100% Game Logic Preserved** - Same gameplay  

---

## 🎯 Next Steps

1. **Play the game** - `python main.py`
2. **Read documentation** - Check `README.md`
3. **Customize theme** - Edit `theme_config.py`
4. **Learn more** - See `ENHANCEMENT_GUIDE.md`
5. **Share project** - Impress your friends! 🎉

---

**Ready? Let's play! 🚀**

```bash
python main.py
```

