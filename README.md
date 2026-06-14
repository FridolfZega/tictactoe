# 🎮 TIC TAC TOE - Hand Vision Interactive Game

## 📌 Tentang Aplikasi

**Tic Tac Toe Hand Vision** adalah aplikasi permainan Tic Tac Toe interaktif yang menggunakan **Computer Vision** dan **Hand Detection** dengan MediaPipe. Pemain dapat bermain dengan menggerakkan tangan mereka - tidak perlu keyboard atau mouse!

### Fitur Utama
✅ **Real-time Hand Detection** menggunakan MediaPipe  
✅ **Gesture-based Gameplay** - arahkan jari ke cell untuk bermain  
✅ **Hold-to-Select Mechanic** - tahan jari 1 detik untuk memilih cell  
✅ **Professional Futuristic UI** dengan neon theme  
✅ **Smooth Animations** untuk visual appeal  
✅ **Live Player Status** dengan real-time update  
✅ **Win/Draw Detection** dengan animated overlay  
✅ **Customizable Themes** - 5 tema ready-to-use  

---

## 🚀 Instalasi & Setup

### Prerequisites
- Python 3.9+
- Webcam/Camera
- Windows, macOS, atau Linux

### Step 1: Clone atau Download Project
```bash
cd tictactoe
```

### Step 2: Setup Virtual Environment
```bash
python3 -m venv venv
```

### Step 3: Aktivasi Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Aplikasi
```bash
python main.py
```

---

## 🎮 Cara Bermain

### Kontrol Permainan

1. **Arahkan Jari Telunjuk** ke cell yang ingin dipilih
2. **Tahan Selama 1 Detik** - progress bar akan muncul
3. **Lepaskan** - cell akan terisi dengan simbol pemain
4. **Giliran Berganti** otomatis ke pemain lain

### Keyboard Shortcuts
| Tombol | Fungsi |
|--------|--------|
| **R** | Reset/Restart Game |
| **ESC** | Quit Aplikasi |

### Cara Menang
- **3 Berturut-turut Horizontal** ✓
- **3 Berturut-turut Vertikal** ✓
- **3 Berturut-turut Diagonal** ✓
- **Seri (Draw)** jika semua cell penuh, tidak ada pemenang

---

## 🎨 UI/UX Features

### Visual Elements

#### 1. **Top Panel - Game Status**
- Judul game: "TIC TAC TOE"
- Subtitle: "HAND VISION"
- Status real-time: Player turn / Win / Draw
- Glass morphism effect dengan neon border

#### 2. **Game Grid**
- Grid 3x3 dengan neon glow effects
- Dynamic highlighting untuk cell yang ditunjuk
- Smooth animations & transitions
- Corner effects untuk enhanced aesthetics

#### 3. **Right Panel - Player Info**
- Player X stats (moves count)
- Player O stats (moves count)
- Color-coded sesuai pemain
- Glass panel design

#### 4. **Bottom Panel - Instructions**
- Clear instructions untuk user
- Keyboard shortcuts
- Help text

#### 5. **Hold Progress Indicator**
- Visual progress bar saat hold cell
- Gradient color animation (cyan → pink)
- Percentage display
- Positioned di bawah selected cell

#### 6. **Finger Indicator**
- Green dot menunjukkan posisi jari
- Glow effect untuk better visibility
- Crosshair untuk precision
- Real-time tracking

#### 7. **Winner Overlay**
- Semi-transparent full-screen overlay
- Centered glass panel
- Animated winner text dengan scaling
- "Press R to Play Again" instruction
- Color-coded sesuai pemenang

---

## 🎨 Themes

Aplikasi menyediakan **5 tema siap pakai**. Edit di `theme_config.py`:

### 1. **Neon Dark** (Default)
```python
ACTIVE_THEME = THEME_NEON_DARK
```
- Dark background dengan cyan neon
- Modern gaming aesthetic
- Cocok untuk showcase & presentation

### 2. **Cyberpunk**
```python
ACTIVE_THEME = THEME_CYBERPUNK
```
- Orange & magenta neon
- Bold futuristic style
- High contrast

### 3. **Minimalist**
```python
ACTIVE_THEME = THEME_MINIMALIST
```
- Light background
- Clean & simple design
- Less glow effects

### 4. **Synthwave**
```python
ACTIVE_THEME = THEME_SYNTHWAVE
```
- Retro 80s style
- Magenta & cyan
- Nostalgic gaming feel

### 5. **Matrix**
```python
ACTIVE_THEME = THEME_MATRIX
```
- Green matrix theme
- Hacker aesthetic
- All-green color palette

### Cara Menggunakan Custom Theme

**Option 1: Edit main.py**
```python
# Di top main.py, ubah:
from theme_config import get_theme_by_name
COLORS = get_theme_by_name('cyberpunk')
```

**Option 2: Edit theme_config.py**
```python
ACTIVE_THEME = THEME_CYBERPUNK  # Change default theme
```

---

## 📁 Project Structure

```
tictactoe/
├── main.py                 # Main application dengan rendering baru
├── game.py                 # Game logic & algorithms (unchanged)
├── app.py                  # Flask web API (optional)
├── theme_config.py         # Theme & color configuration
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface (optional)
├── static/
│   └── style.css          # Web styling (optional)
├── UI_UPGRADE_SUMMARY.md  # Dokumentasi upgrade UI/UX
└── README.md              # File ini
```

---

## 🔧 Technical Details

### Dependencies

| Package | Versi | Fungsi |
|---------|-------|--------|
| OpenCV | ≥4.5 | Video capture & image processing |
| MediaPipe | 0.10.13 | Hand detection & tracking |
| Flask | ≥2.0 | Web API (optional) |
| NumPy | ≥2.0 | Numerical computing |

### Architecture

```
Input (Webcam)
    ↓
OpenCV Capture (1280x720)
    ↓
MediaPipe Hand Detection
    ↓
Get Cell Position
    ↓
Validate Move (game.py)
    ↓
Update Board State
    ↓
Check Winner
    ↓
Render Visualization (NEW!)
    ↓
Display Output
```

### Game Logic (Preserved 100%)

- `get_cell(x, y, w, h)` - Convert pixel coords to cell
- `check_winner(board)` - Check 8 winning combinations
- `make_move(board, cell, player)` - Validate & execute move
- `reset_board()` - Clear board state

**Semua fungsi tetap unchanged!**

---

## 🎯 Performance Optimization

### Frame Rate
- Target: 30 FPS untuk smooth rendering
- OpenCV waitKey: 1ms
- Animation updates per frame

### Memory Usage
- Image processing in-place (minimal copy)
- Hand detection caching
- Efficient rendering layers

### Rendering Pipeline
1. Dark background fill
2. Grid drawing dengan glow
3. Mark drawing dengan shadow
4. Highlights & indicators
5. UI panels
6. Overlays
7. Display output

---

## 🐛 Troubleshooting

### Issue: Webcam tidak terdeteksi
**Solution:**
```python
# Di main.py, ubah index:
cap = cv2.VideoCapture(0)  # 0 = default, coba 1, 2, etc
```

### Issue: Hand detection lambat
**Solution:**
```python
# Kurangi detection confidence:
min_detection_confidence=0.5  # default 0.6
```

### Issue: Grid tidak terlihat jelas
**Solution:**
```python
# Edit theme_config.py:
'grid': (0, 255, 255),  # Ubah BGR color value
```

### Issue: Performance rendah
**Solution:**
```python
# Resize input frame:
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)  # from 1280
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)  # from 720
```

---

## 📊 Key Statistics

| Metrik | Value |
|--------|-------|
| Resolution | 1280×720 |
| Target FPS | 30+ |
| Detection Model | MediaPipe Hands |
| Grid Size | 3×3 (9 cells) |
| Hold Duration | 1 second |
| Themes Available | 5 |
| Animation Effects | 12+ |
| UI Panels | 4 |

---

## 🎮 Game Examples

### Scenario 1: Normal Gameplay
1. Player X point ke top-left cell
2. Hold 1 second → cell filled dengan X
3. Player O point ke center cell
4. Hold 1 second → cell filled dengan O
5. Continue until winner detected

### Scenario 2: Win Detection
1. Player X completes 3-in-a-row
2. Winning overlay appears dengan animated text
3. Winning line highlighted dengan glow effect
4. "Press R to Play Again" instruction shown

### Scenario 3: Draw Game
1. All 9 cells filled, no winner
2. Draw overlay appears
3. Message: "GAME DRAW!"
4. Press R to restart

---

## 🎬 Demo & Showcase

Perfect untuk:
- ✨ **Presentasi Proyek** - Impressive modern UI
- 🎓 **Demo Kelas** - Engaging hand tracking
- 🏆 **Kompetisi** - Professional appearance
- 📹 **Video Demo** - Smooth animations
- 🎪 **Pameran** - Eye-catching visuals

---

## 📝 Development Notes

### Upgrade Highlights
- ✅ 14 new rendering functions added
- ✅ 5 complete themes designed
- ✅ Animation system implemented
- ✅ Glass morphism effects
- ✅ Neon glow layers
- ✅ Real-time progress tracking
- ✅ Professional overlay system
- ✅ Zero changes to game logic

### Code Quality
- 100% backward compatible
- Clean separation of concerns
- Modular theme system
- Well-commented code
- Follows Python conventions

---

## 📞 Support & Help

### Common Questions

**Q: Bisakah mengubah warna?**  
A: Ya, edit `theme_config.py` atau buat custom theme

**Q: Bagaimana mengubah detection sensitivity?**  
A: Edit `min_detection_confidence` di main.py line ~7

**Q: Apakah bisa run di macOS/Linux?**  
A: Ya, code cross-platform compatible

**Q: Apakah ada dependencies tambahan?**  
A: Semua sudah di `requirements.txt`

---

## 📜 License & Credits

- **OpenCV** - Image processing library
- **MediaPipe** - Hand detection framework
- **Python** - Programming language
- **Custom UI** - Original design

---

## 🚀 Future Enhancements

Possible additions (without affecting core game):
- [ ] Sound effects & background music
- [ ] Multiplayer networked mode
- [ ] AI opponent dengan computer vision
- [ ] Gesture-based menu navigation
- [ ] Recording & replay functionality
- [ ] Difficulty levels
- [ ] Leaderboard system
- [ ] Mobile app version

---

## ✅ Changelog

### v2.0 (Current - UI Upgrade)
- ✨ Complete UI/UX redesign
- 🎨 5 theme support
- 🎬 Animation system
- 📊 New panels & indicators
- 🌟 Professional overlay system
- 🔧 Theme configuration system

### v1.0 (Original)
- 🎮 Basic Tic Tac Toe gameplay
- 🖐️ Hand detection
- 🎯 Cell selection

---

## 📄 Additional Resources

- [MediaPipe Documentation](https://mediapipe.dev/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Computer Vision Basics](https://en.wikipedia.org/wiki/Computer_vision)

---

**Last Updated:** June 10, 2026  
**Status:** ✅ Production Ready  
**Version:** 2.0

**Enjoy your Tic Tac Toe Hand Vision Game! 🎮✨**

