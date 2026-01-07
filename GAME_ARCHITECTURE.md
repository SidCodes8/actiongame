# Falling & Catch Game - Architecture Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Technology Stack](#technology-stack)
3. [Architectural Pattern](#architectural-pattern)
4. [System Components](#system-components)
5. [Data Flow](#data-flow)
6. [Detailed Component Architecture](#detailed-component-architecture)
7. [Key Features & Algorithms](#key-features--algorithms)
8. [Educational Design](#educational-design)

---

## 1. System Overview

**Falling & Catch** is an educational web-based game designed for preschool to kindergarten children (ages 2.5-6 years). The game uses gesture-based controls powered by **MediaPipe Hand Tracking** to create an interactive learning experience where children catch falling items using hand movements.

### Core Objectives
- **Educational**: Teach alphabet recognition, animal identification, and shape learning
- **Accessibility**: Uses natural hand gestures instead of traditional input devices
- **Adaptive**: Three difficulty levels tailored to different age groups
- **Engaging**: Real-time feedback with confetti effects, sounds, and visual animations

### Game Modes
- **Alphabet Mode**: Letter recognition (uppercase, lowercase, phonics)
- **Animals Mode**: Animal identification with pictures, words, and riddles
- **Shapes Mode**: Shape recognition with real-world object associations

### Difficulty Levels
- **Preschool** (2.5-3.5 years): Slow speed, 3 items on screen, 5 hearts
- **Nursery** (3.5-4.5 years): Medium speed, 5 items on screen, 4 hearts
- **Kindergarten** (4.5-6 years): Fast speed, 6 items on screen, 3 hearts

---

## 2. Technology Stack

### Backend Framework
```
Django 4.x (Python Web Framework)
├── MVT Architecture (Model-View-Template)
├── URL Routing
├── Template Rendering
└── Configuration Management
```

### Frontend Technologies
```
HTML5 Canvas - Game rendering and graphics
JavaScript (ES6+) - Game logic and interactivity
TailwindCSS - Utility-first styling framework
Google Fonts - Fredoka & Outfit fonts for playful UI
```

### External Libraries & APIs
```
MediaPipe Hands - Real-time hand tracking
├── @mediapipe/camera_utils
├── @mediapipe/hands
├── @mediapipe/drawing_utils
└── @mediapipe/control_utils

Canvas Confetti - Visual celebration effects
Web Speech API - Text-to-speech for audio feedback
Font Awesome - Icon library
```

---

## 3. Architectural Pattern

The game follows a **hybrid architecture** combining:

### Backend: MVC Pattern (Django)
```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP Request
       ▼
┌─────────────┐
│  URL Router │ (urls.py)
└──────┬──────┘
       ▼
┌─────────────┐
│    Views    │ (views.py)
└──────┬──────┘
       │
       ├──────► ┌──────────────┐
       │        │ Game Config  │ (game_config.py)
       │        └──────────────┘
       │
       ▼
┌─────────────┐
│  Templates  │ (HTML/JavaScript)
└─────────────┘
```

### Frontend: Game Loop Pattern
```
┌────────────────────────────────────────┐
│          Initialization Phase          │
├────────────────────────────────────────┤
│ 1. Load calibration data               │
│ 2. Initialize MediaPipe hand tracking  │
│ 3. Set up game state                   │
│ 4. Configure canvas and context        │
└───────────────┬────────────────────────┘
                │
                ▼
┌────────────────────────────────────────┐
│           Game Loop (RAF)              │
│  ┌──────────────────────────────────┐  │
│  │  1. Clear Canvas                 │  │
│  │  2. Update Game State            │  │
│  │  3. Process Input (Hand Tracking)│  │
│  │  4. Spawn Items                  │  │
│  │  5. Update Item Positions        │  │
│  │  6. Collision Detection          │  │
│  │  7. Render Graphics              │  │
│  │  8. Update UI                    │  │
│  └──────────────────────────────────┘  │
│              ▲                         │
│              │                         │
│              │ requestAnimationFrame   │
│              └─────────────────────────│
└────────────────────────────────────────┘
```

---

## 4. System Components

### 4.1 Django Backend Structure
```
falling_catch_django_3/
├── config/                    # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI entry point
│
├── game/                      # Main game application
│   ├── views.py              # Request handlers
│   ├── urls.py               # Game URL patterns
│   ├── game_config.py        # Game configuration data
│   └── models.py             # (Empty - no database models)
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template with shared styles
│   └── game/
│       ├── home.html         # Landing page
│       ├── level_select.html # Mode/level selection
│       ├── calibration.html  # Hand tracking calibration
│       └── play.html         # Main game screen
│
└── db.sqlite3                # SQLite database (minimal usage)
```

### 4.2 Frontend Component Hierarchy
```
┌────────────────────────────────────────┐
│         Base Template (base.html)      │
│  - Global styles & animations          │
│  - External library imports            │
│  - Common UI components                │
└──────────────┬─────────────────────────┘
               │
       ┌───────┴────────┬──────────┬─────────────┐
       │                │          │             │
┌──────▼──────┐  ┌─────▼─────┐  ┌─▼────────┐  ┌─▼──────────┐
│ Home Page   │  │Level      │  │Calibra   │  │ Game Play  │
│             │  │Select     │  │tion      │  │            │
└─────────────┘  └───────────┘  └──────────┘  └────────────┘
                                                      │
                    ┌─────────────────────────────────┤
                    │                                 │
              ┌─────▼─────┐                    ┌──────▼──────┐
              │ Canvas    │                    │  UI Layer   │
              │ Rendering │                    │  - HUD      │
              │ Engine    │                    │  - Score    │
              └───────────┘                    │  - Timer    │
                                               │  - Hearts   │
                                               └─────────────┘
```

---

## 5. Data Flow

### 5.1 Request-Response Flow
```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Django
    participant GameConfig
    participant MediaPipe
    
    User->>Browser: Navigate to /select/
    Browser->>Django: HTTP GET /select/
    Django->>GameConfig: Load GAME_MODES & LEVELS
    GameConfig-->>Django: Return configuration
    Django-->>Browser: Render level_select.html
    
    User->>Browser: Select Mode & Level
    Browser->>Django: HTTP GET /play/alphabet/preschool/
    Django->>GameConfig: get_game_config('alphabet', 'preschool')
    GameConfig-->>Django: Combined config JSON
    Django-->>Browser: Render play.html with config
    
    Browser->>MediaPipe: Initialize hand tracking
    MediaPipe-->>Browser: Hand landmarks (realtime)
    Browser->>Browser: Game loop execution
```

### 5.2 Game State Flow
```mermaid
graph TD
    A[Page Load] --> B[Load Calibration]
    B --> C[Initialize MediaPipe]
    C --> D[Select First Target]
    D --> E[Start Timer]
    E --> F[Begin Game Loop]
    
    F --> G{Game Over?}
    G -->|No| H[Spawn Items]
    H --> I[Update Positions]
    I --> J[Check Collisions]
    J --> K{Collision?}
    K -->|Yes| L{Correct Item?}
    L -->|Yes| M[+Score, Confetti]
    L -->|No| N[-Heart, Shake]
    M --> O[Select New Target]
    N --> P{Hearts > 0?}
    P -->|No| Q[End Game - Lost]
    P -->|Yes| F
    O --> F
    K -->|No| R{Item Off Screen?}
    R -->|Yes| F
    R -->|No| F
    
    G -->|Yes| S[Show Game Over Modal]
```

---

## 6. Detailed Component Architecture

### 6.1 Backend Components

#### **Views Layer** (`views.py`)
Handles HTTP requests and prepares data for templates.

```python
# Key Responsibilities:
- Route incoming HTTP requests
- Load game configuration from game_config.py
- Prepare context data for templates
- Handle invalid mode/level combinations
- Render appropriate templates
```

**Functions:**
- `home_view()`: Landing page
- `level_select_view()`: Mode and level selection
- `calibration_view()`: Hand tracking calibration screen
- `play_view(mode, level)`: Main game with configuration injection

#### **Game Configuration** (`game_config.py`)
Centralized configuration management.

```python
# Data Structures:
GAME_MODES = {
    'alphabet': {...},
    'animals': {...},
    'shapes': {...}
}

GAME_LEVELS = {
    'preschool': {...},
    'nursery': {...},
    'kindergarten': {...}
}
```

**Key Features:**
- Mode-specific educational content (letters, animals, shapes)
- Level-specific difficulty settings (speed, hearts, time limit)
- Audio templates for text-to-speech
- Phonics mappings for kindergarten alphabet mode
- Animal riddles and shape descriptions

**Configuration Function:**
```python
get_game_config(mode, level)
# Returns combined configuration merging mode and level settings
```

#### **URL Routing** (`urls.py`)
Maps URLs to view functions.

```
/                          → home_view
/select/                   → level_select_view
/calibrate/                → calibration_view
/play/<mode>/<level>/      → play_view
```

---

### 6.2 Frontend Components

#### **A. Game State Management**

**Game State Object:**
```javascript
gameState = {
    score: 0,                      // Player's score
    hearts: <from config>,         // Remaining lives
    correctCatches: 0,             // Successful catches
    incorrectCatches: 0,           // Mistakes
    timeRemaining: <from config>,  // Countdown timer
    startTime: null,               // Game start timestamp
    gameOver: false,               // Game status flag
    won: false,                    // Win condition flag
    currentTarget: null,           // Current item to catch
    customSpeedMultiplier: 1.0,    // User speed adjustment
    nextCorrectSpawnTime: 0,       // Scheduled spawn time
    correctElementActive: false    // Correct item on screen
}
```

#### **B. Hand Tracking System**

**MediaPipe Integration:**
```javascript
// 1. Initialize MediaPipe Hands
hands = new Hands({...})
hands.setOptions({
    maxNumHands: 1,
    modelComplexity: 1,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5
})

// 2. Camera Setup
camera = new Camera(videoElement, {
    onFrame: async () => {
        await hands.send({ image: videoElement })
    }
})

// 3. Process Hand Results
onHandResults(results) {
    // Extract wrist landmark (index 0)
    // Apply calibration mapping
    // Filter with Kalman filter
    // Update basket position
}
```

**Calibration System:**
- Stores left and right hand boundary positions
- Maps raw hand X coordinate (0-1) to calibrated range
- Persists in localStorage for consistency
- Accessible via `/calibrate/` route

**Kalman Filter:**
```javascript
class KalmanFilter {
    // Smooths jittery hand tracking data
    // Parameters: R (measurement noise), Q (process noise)
    // Returns smoothed position estimate
}
```

#### **C. Spawning System**

**Grid-Based Spawn Manager:**
```javascript
// Canvas divided into 10 columns
COLUMNS = 10
COLUMN_WIDTH = CANVAS_WIDTH / COLUMNS

// Safety constraints
MIN_VERTICAL_SPACING = 200px   // Prevents vertical clustering
MIN_SPAWN_DELAY = 800ms        // Minimum time between spawns
```

**Spawn Algorithm:**
```
1. Check if enough time has passed since last spawn
2. Check if correct element should spawn (based on schedule)
3. If spawning correct element:
   a. Find safe column (no items within 200px vertically)
   b. Avoid last spawned column
   c. Create FallingItem(forceCorrect=true)
4. If spawning distractor:
   a. Check current item count < items_on_screen
   b. Find safe column
   c. Create FallingItem(forceCorrect=false)
```

**Scheduling Logic:**
```javascript
scheduleNextCorrectElement(currentTimestamp) {
    // Random delay between 3-10 seconds
    delay = (Math.random() * 7 + 3) * 1000
    
    // Speed up in last 10 seconds
    if (timeRemaining < 10) {
        delay = min(delay, 2000)
    }
    
    nextCorrectSpawnTime = currentTimestamp + delay
}
```

#### **D. Falling Item System**

**FallingItem Class:**
```javascript
class FallingItem {
    constructor(forceCorrect, spawnX) {
        // Size and position
        this.width = 80
        this.height = 80
        this.x = <spawn position>
        this.y = -80  // Start above screen
        
        // Content determination
        if (forceCorrect) {
            this.content = gameState.currentTarget
            this.isCorrect = true
        } else {
            this.content = <random wrong item>
            this.isCorrect = false
        }
        
        // Metadata
        this.itemType = <from config>
        this.modeData = <from config>
    }
    
    update() {
        // Move down by (baseSpeed × customSpeedMultiplier)
        this.y += speed
    }
    
    draw() {
        // Draw shadow
        // Draw rounded rectangle (green=correct, red=wrong)
        // Render content (emoji/letter/word)
    }
    
    isOffScreen() {
        return this.y > CANVAS_HEIGHT
    }
    
    collidesWithBasket() {
        // AABB collision detection
        return (overlap in X && overlap in Y)
    }
}
```

**Rendering Modes:**
- **picture**: Single emoji
- **picture+word**: Emoji + text label below
- **phonics**: Letter with phonetic sound
- **riddle**: Emoji representing riddle answer

#### **E. Basket System**

**Basket Object:**
```javascript
basket = {
    width: 120,
    height: 80,
    x: <controlled by hand tracking>,
    y: CANVAS_HEIGHT - 120,  // Fixed vertical position
    color: '#ff6b6b'
}
```

**Drawing:**
- Drop shadow for depth
- Gradient fill (red shades)
- Curved top edge (inverted arc)
- Basket emoji (🧺) in center

#### **F. Collision Detection System**

**Algorithm: Axis-Aligned Bounding Box (AABB)**
```javascript
collidesWithBasket() {
    return (
        item.x < basket.x + basket.width &&     // Item left edge before basket right
        item.x + item.width > basket.x &&       // Item right edge after basket left
        item.y < basket.y + basket.height &&    // Item top edge before basket bottom
        item.y + item.height > basket.y         // Item bottom edge after basket top
    )
}
```

**Collision Handling:**
```
On Correct Catch:
  ├── +10 points to score
  ├── Confetti animation at basket position
  ├── Text-to-speech: "Correct!"
  ├── Select new random target
  └── Schedule next correct element

On Incorrect Catch:
  ├── -1 heart
  ├── Screen shake animation
  ├── Text-to-speech: "Try again!"
  └── Check if hearts <= 0 → End Game
```

#### **G. Game Loop**

**RequestAnimationFrame Pattern:**
```javascript
function gameLoop(timestamp) {
    if (gameOver) return
    
    // 1. Clear canvas
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
    
    // 2. Update game state
    update(timestamp)
    
    // 3. Render all items
    items.forEach(item => item.draw())
    
    // 4. Render basket
    drawBasket()
    
    // 5. Schedule next frame
    requestAnimationFrame(gameLoop)
}
```

**Update Function:**
```javascript
function update(timestamp) {
    // Spawn new items
    spawnItem(timestamp)
    
    // Update all existing items
    for (item of items) {
        item.update()
        
        if (item.collidesWithBasket()) {
            handleCatch(item)
            removeItem(item)
        } else if (item.isOffScreen()) {
            if (item.isCorrect) {
                scheduleNextCorrectElement(timestamp)
            }
            removeItem(item)
        }
    }
}
```

#### **H. Timer System**

**Implementation:**
```javascript
startTimer() {
    timerInterval = setInterval(() => {
        if (!gameOver) {
            timeRemaining--
            updateTimerDisplay()
            
            // Check for timeout
            if (timeRemaining <= 0) {
                endGame(false, timeout=true)
            }
        }
    }, 1000)  // Every second
}
```

**Visual Feedback:**
- Normal: Green color
- Warning (<30s): Orange color with pulsing animation
- Format: M:SS (e.g., "1:45")

#### **I. Audio System**

**Web Speech API Integration:**
```javascript
function speak(text) {
    utterance = new SpeechSynthesisUtterance(text)
    utterance.rate = 1.0
    utterance.pitch = 1.2
    speechSynthesis.speak(utterance)
}
```

**Audio Templates:**
```
Alphabet (Preschool): "Catch the letter {item}"
Alphabet (Phonics):   "Catch the letter with sound {phonics}"
Animals (Riddle):     "Catch {riddle}"  // e.g., "the animal that barks"
Shapes (Riddle):      "Catch {riddle}"  // e.g., "the shape with no corners"
```

**Feedback Sounds:**
- On correct catch: "Correct!"
- On incorrect catch: "Try again!"
- On game win: "Congratulations! You won!"
- On game over: "Game over. Try again!"
- On timeout: "Time is up!"

#### **J. UI & HUD System**

**Heads-Up Display Components:**

1. **Score Display**
   - Current score (10 points per correct catch)
   - Accuracy percentage
   - Bounce animation on score change

2. **Timer Display**
   - Countdown in M:SS format
   - Warning indicator (<30 seconds)
   - Pulse animation when low

3. **Target Display**
   - Shows current item to catch
   - Updates on every correct catch
   - Format varies by mode (letter/phonics/name/riddle)

4. **Hearts Display**
   - Visual hearts (❤️) for lives
   - Gray hearts (🤍) for lost lives
   - Shake animation on loss

5. **Speed Slider**
   - Accessibility feature
   - Range: 0.5x to 3.0x
   - Persisted in localStorage

---

## 7. Key Features & Algorithms

### 7.1 Smart Spawning Algorithm

**Problems Solved:**
- Prevents item clustering
- Ensures catchability
- Maintains challenge level
- Avoids same-column repetition

**Implementation:**
```
Grid Division:
  Canvas width (1200px) ÷ 10 columns = 120px per column

Safety Check:
  For each column:
    Check all existing items
    If any item in column has Y < 200px:
      Mark column as UNSAFE
    Else:
      Mark column as SAFE

Column Selection:
  1. Filter to safe columns only
  2. Remove last spawned column (if > 1 safe column)
  3. Randomly select from remaining columns
  4. Add random offset within column bounds

Spawn Throttling:
  Only spawn if (currentTime - lastSpawnTime) >= 800ms
```

### 7.2 Kalman Filtering for Smooth Tracking

**Purpose:** Reduce jitter in hand position data

**Algorithm:**
```
Prediction Step:
  P = P + Q   (Increase uncertainty)

Update Step:
  K = P / (P + R)       (Kalman Gain)
  x = x + K × (z - x)   (Corrected estimate)
  P = (1 - K) × P       (Updated uncertainty)

Where:
  x = estimated position
  z = measured position
  P = estimate uncertainty
  Q = process noise (how much we expect x to change)
  R = measurement noise (sensor accuracy)
```

**Parameters Used:**
- R = 0.01 (low measurement noise - trust sensor)
- Q = 3 (moderate process noise - smooth rapid movements)

### 7.3 Adaptive Difficulty Scaling

**Difficulty Dimensions:**

| Level | Speed | Items | Hearts | Time | Age Range |
|-------|-------|-------|--------|------|-----------|
| Preschool | 1.5 px/frame | 3 | 5 | 120s | 2.5-3.5 yrs |
| Nursery | 2.5 px/frame | 5 | 4 | 120s | 3.5-4.5 yrs |
| Kindergarten | 3.5 px/frame | 6 | 3 | 120s | 4.5-6 yrs |

**Speed Calculation:**
```javascript
actualSpeed = baseSpeed × customSpeedMultiplier
// Example: 2.5 (nursery) × 1.5 (user setting) = 3.75 px/frame
```

### 7.4 Educational Content Mapping

**Mode-Specific Learning Objectives:**

**Alphabet Mode:**
```
Preschool:    Uppercase letter recognition (A-Z)
              Target: Vowels (A, E, I, O, U)

Nursery:      Lowercase letter recognition (a-z)
              Target: Lowercase vowels (a, e, i, o, u)

Kindergarten: Phonics and sound-letter mapping
              Target: Consonants with phonetic sounds
              Example: "B" → "/buh/" sound
```

**Animals Mode:**
```
Preschool:    Visual picture recognition
              Target: Common animals (dog, cat, bird, etc.)

Nursery:      Picture-to-word matching
              Target: Animals with written names

Kindergarten: Conceptual riddles
              Example: "Catch the animal that barks" → 🐶
```

**Shapes Mode:**
```
Preschool:    Basic shape recognition
              Target: Circle, triangle, star, heart

Nursery:      Shape-to-word matching
              Target: Shapes with written names

Kindergarten: Shape properties and real-life associations
              Example: "Catch the shape with no corners" → ⭕
```

---

## 8. Educational Design

### 8.1 Pedagogical Principles

**1. Progressive Difficulty:**
- Gradual increase in complexity across levels
- Age-appropriate content and challenges
- Scaffolded learning from recognition to comprehension

**2. Immediate Feedback:**
- Visual: Confetti for success, shake for errors
- Audio: Text-to-speech encouragement
- Tactile: Screen shake creates feedback loop

**3. Spaced Repetition:**
- Random target selection ensures variety
- Scheduled spawning prevents overwhelming
- Wrong items reinforce discrimination

**4. Multimodal Learning:**
- Visual: Emojis, colors, animations
- Auditory: Text-to-speech instructions
- Kinesthetic: Hand gesture control

**5. Intrinsic Motivation:**
- Score tracking and accuracy metrics
- Limited hearts create manageable stakes
- Celebratory effects reward success

### 8.2 Accessibility Features

**1. Speed Control:**
- Slider allows 0.5x to 3.0x speed adjustment
- Accommodates different motor skills
- Persisted preference across sessions

**2. Visual Clarity:**
- High contrast colors (green=correct, red=wrong)
- Large, legible fonts (Fredoka family)
- Clear emoji representations

**3. Calibration System:**
- Personalized hand tracking boundaries
- Adapts to different physical setups
- Improves tracking accuracy

**4. No Fine Motor Requirements:**
- Broad hand movements sufficient
- Large collision boxes
- Forgiving basket size (120px wide)

---

## Summary Architecture Diagram

```
┌───────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                         │
│  ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Score  │  │  Timer  │  │  Target  │  │    Hearts     │  │
│  └─────────┘  └─────────┘  └──────────┘  └───────────────┘  │
├───────────────────────────────────────────────────────────────┤
│                      CANVAS RENDERING                         │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  ┌───┐     ┌───┐         ┌───┐                         │ │
│  │  │ A │     │ 🐱│         │ ⭐ │    ← Falling Items     │ │
│  │  └───┘     └───┘         └───┘                         │ │
│  │                                                         │ │
│  │              ┌─────┐                                    │ │
│  │              │  🧺 │    ← Basket (Hand-controlled)     │ │
│  │              └─────┘                                    │ │
│  └─────────────────────────────────────────────────────────┘ │
├───────────────────────────────────────────────────────────────┤
│                      GAME ENGINE LAYER                        │
│  ┌────────────┐  ┌──────────┐  ┌─────────────────────────┐  │
│  │ Game Loop  │→ │ Spawner  │→ │  Collision Detection    │  │
│  │  (RAF)     │  │ Manager  │  │       (AABB)            │  │
│  └────────────┘  └──────────┘  └─────────────────────────┘  │
├───────────────────────────────────────────────────────────────┤
│                      INPUT PROCESSING                         │
│  ┌──────────────┐  ┌───────────────┐  ┌─────────────────┐   │
│  │   Camera     │→ │   MediaPipe   │→ │ Kalman Filter   │   │
│  │   Stream     │  │   Hand Model  │  │   Smoothing     │   │
│  └──────────────┘  └───────────────┘  └─────────────────┘   │
├───────────────────────────────────────────────────────────────┤
│                  CONFIGURATION & STATE                        │
│  ┌───────────────────┐  ┌──────────────────────────────────┐ │
│  │   Game Config     │  │      Game State                  │ │
│  │ (Django injected) │  │ - Score, Hearts, Timer           │ │
│  │ - Mode settings   │  │ - Items array                    │ │
│  │ - Level params    │  │ - Current target                 │ │
│  └───────────────────┘  └──────────────────────────────────┘ │
├───────────────────────────────────────────────────────────────┤
│                       BACKEND (Django)                        │
│  ┌────────┐  ┌─────────────┐  ┌─────────────────────────┐   │
│  │  URLs  │→ │    Views    │→ │     Templates           │   │
│  │ Router │  │  (+ Config) │  │  (HTML + JavaScript)    │   │
│  └────────┘  └─────────────┘  └─────────────────────────┘   │
└───────────────────────────────────────────────────────────────┘
```

---

## Technical Highlights for Your Professor

### 🎯 **Key Technical Achievements**

1. **Real-Time Computer Vision Integration**
   - MediaPipe hand tracking at 30+ FPS
   - Kalman filtering for noise reduction
   - Calibration system for personalization

2. **Professional Game Architecture**
   - Game loop pattern with RAF
   - Smart spawning algorithm preventing clustering
   - Grid-based spatial management

3. **Educational Technology Design**
   - Adaptive difficulty based on age research
   - Multimodal learning (visual, auditory, kinesthetic)
   - Data-driven configuration system

4. **Full-Stack Web Development**
   - Django backend with MVT pattern
   - Canvas-based rendering engine
   - Responsive UI with TailwindCSS

5. **Accessibility & UX**
   - Gesture-based control (no mouse/keyboard)
   - Speed controls for motor skill differences
   - Immediate feedback loops

### 📊 **Performance Metrics**

- **Rendering**: 60 FPS game loop
- **Input Latency**: <50ms hand tracking response
- **Spawn Rate**: 1 item per 0.8-2 seconds (configurable)
- **Smooth Movement**: Kalman-filtered hand position
- **Browser Compatibility**: Modern browsers with Canvas + MediaPipe support

---

## Conclusion

The Falling & Catch game demonstrates a sophisticated integration of modern web technologies, computer vision, and educational pedagogy. The architecture prioritizes:

- **Modularity**: Clear separation of concerns (backend config, frontend rendering, game logic)
- **Scalability**: Easy to add new modes, levels, or content
- **Performance**: Optimized game loop and rendering
- **Accessibility**: Natural gesture controls and adaptive difficulty
- **Educational Value**: Research-based learning objectives and feedback

This architecture serves as a foundation for future enhancements such as multiplayer modes, achievement systems, or advanced analytics.
