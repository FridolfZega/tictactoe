"""
Theme Configuration untuk Tic Tac Toe Hand Vision
Mudah di-customize tanpa mengubah main game logic
"""

# ============================================================================
# TEMA COLORS - FUTURISTIC NEON
# ============================================================================
THEME_NEON_DARK = {
    'name': 'Futuristic Neon Dark',
    'background': (10, 12, 20),
    'grid': (0, 255, 255),
    'grid_light': (100, 255, 255),
    'neon_pink': (255, 0, 127),
    'neon_purple': (200, 0, 255),
    'neon_blue': (0, 150, 255),
    'neon_green': (0, 255, 100),
    'player_x': (0, 150, 255),
    'player_o': (255, 0, 127),
    'text_primary': (255, 255, 255),
    'text_secondary': (180, 180, 180),
    'highlight': (0, 255, 255),
    'win_line': (0, 255, 150),
    'glass_bg': (30, 40, 60),
}

# ============================================================================
# TEMA ALTERNATIF - CYBERPUNK ORANGE
# ============================================================================
THEME_CYBERPUNK = {
    'name': 'Cyberpunk Orange',
    'background': (15, 20, 35),
    'grid': (255, 140, 0),
    'grid_light': (255, 165, 0),
    'neon_pink': (255, 0, 255),
    'neon_purple': (138, 43, 226),
    'neon_blue': (0, 100, 255),
    'neon_green': (50, 205, 50),
    'player_x': (255, 100, 0),
    'player_o': (255, 0, 255),
    'text_primary': (255, 255, 255),
    'text_secondary': (200, 150, 100),
    'highlight': (255, 200, 0),
    'win_line': (255, 150, 0),
    'glass_bg': (50, 30, 60),
}

# ============================================================================
# TEMA ALTERNATIF - MINIMALIST LIGHT
# ============================================================================
THEME_MINIMALIST = {
    'name': 'Minimalist Light',
    'background': (240, 240, 245),
    'grid': (50, 50, 150),
    'grid_light': (100, 100, 200),
    'neon_pink': (200, 50, 100),
    'neon_purple': (150, 100, 200),
    'neon_blue': (100, 150, 255),
    'neon_green': (50, 150, 100),
    'player_x': (50, 100, 200),
    'player_o': (200, 100, 50),
    'text_primary': (30, 30, 50),
    'text_secondary': (100, 100, 120),
    'highlight': (100, 150, 255),
    'win_line': (100, 200, 100),
    'glass_bg': (200, 200, 220),
}

# ============================================================================
# TEMA ALTERNATIF - RETRO SYNTHWAVE
# ============================================================================
THEME_SYNTHWAVE = {
    'name': 'Retro Synthwave',
    'background': (20, 10, 40),
    'grid': (255, 0, 255),
    'grid_light': (255, 100, 255),
    'neon_pink': (255, 0, 100),
    'neon_purple': (200, 100, 255),
    'neon_blue': (0, 200, 255),
    'neon_green': (100, 255, 200),
    'player_x': (0, 255, 255),
    'player_o': (255, 0, 255),
    'text_primary': (255, 255, 255),
    'text_secondary': (200, 200, 255),
    'highlight': (255, 100, 200),
    'win_line': (100, 255, 200),
    'glass_bg': (40, 20, 60),
}

# ============================================================================
# TEMA ALTERNATIF - MATRIX GREEN
# ============================================================================
THEME_MATRIX = {
    'name': 'Matrix Green',
    'background': (5, 15, 5),
    'grid': (0, 255, 0),
    'grid_light': (100, 255, 100),
    'neon_pink': (255, 0, 127),
    'neon_purple': (100, 200, 100),
    'neon_blue': (0, 150, 100),
    'neon_green': (0, 255, 0),
    'player_x': (100, 255, 100),
    'player_o': (0, 200, 0),
    'text_primary': (0, 255, 0),
    'text_secondary': (100, 200, 100),
    'highlight': (0, 255, 0),
    'win_line': (200, 255, 100),
    'glass_bg': (10, 40, 10),
}

# ============================================================================
# KONFIGURASI RENDERING
# ============================================================================
ANIMATION_CONFIG = {
    'glow_intensity_base': 0.2,
    'glow_intensity_pulse': 0.15,
    'pulsing_speed': 0.1,
    'highlight_fill_alpha': 0.2,
    'glass_alpha': 0.5,
    'progress_bar_update_speed': 1.0,
    'winner_text_scale_multiplier': 1.8,
}

# ============================================================================
# FONT & TEXT CONFIGURATION
# ============================================================================
TEXT_CONFIG = {
    'font': 3,  # cv2.FONT_HERSHEY_SIMPLEX
    'title_scale': 1.2,
    'subtitle_scale': 0.8,
    'status_scale': 1.0,
    'panel_scale': 0.7,
    'instruction_scale': 0.65,
    'default_thickness': 2,
}

# ============================================================================
# SELECTED THEME (dapat diubah di sini)
# ============================================================================
ACTIVE_THEME = THEME_NEON_DARK

# ============================================================================
# HELPER FUNCTION
# ============================================================================
def get_theme_by_name(theme_name):
    """Mendapatkan tema berdasarkan nama"""
    themes = {
        'neon_dark': THEME_NEON_DARK,
        'cyberpunk': THEME_CYBERPUNK,
        'minimalist': THEME_MINIMALIST,
        'synthwave': THEME_SYNTHWAVE,
        'matrix': THEME_MATRIX,
    }
    return themes.get(theme_name.lower(), THEME_NEON_DARK)

def list_available_themes():
    """Menampilkan semua tema yang tersedia"""
    themes = [
        'neon_dark',
        'cyberpunk',
        'minimalist',
        'synthwave',
        'matrix',
    ]
    return themes

# ============================================================================
# Cara Menggunakan:
# ============================================================================
# 1. Di main.py, import:
#    from theme_config import ACTIVE_THEME as COLORS
#
# 2. Atau untuk memilih tema spesifik:
#    from theme_config import get_theme_by_name
#    COLORS = get_theme_by_name('cyberpunk')
#
# 3. Untuk mengganti tema global, ubah:
#    ACTIVE_THEME = THEME_CYBERPUNK  # atau tema lain
#
# ============================================================================
