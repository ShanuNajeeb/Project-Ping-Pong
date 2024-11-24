### Ping Pong Game in Python Using Turtle Graphics

This script is a simple **Ping Pong Game** built with the `turtle` module in Python. Two players can control the paddles, and the game keeps track of the score.

---

### **Features**
1. **Two-Player Controls**:
   - **Player A**: Use `W` (up) and `S` (down) keys.
   - **Player B**: Use `Up` and `Down` arrow keys.

2. **Dynamic Ball Movement**:
   - Ball bounces off the walls and paddles.
   - Resets position when a player scores.

3. **Scoring System**:
   - Score is displayed at the top.
   - Increments when the ball crosses the opponent's side.

4. **Real-Time Updates**:
   - Smooth game loop using `gs.update()`.

---

### **How to Play**
1. Run the script in a Python environment with the `turtle` library.
2. Use the specified keys to move paddles and prevent the ball from crossing your side.
3. The score updates automatically for each round.

---

### **Code Highlights**
1. **Paddles**:
   - Created as `Turtle` objects, shaped as rectangles.
   - Positioned on either side of the screen.

2. **Ball Mechanics**:
   - Moves diagonally with `ball.dx` and `ball.dy`.
   - Reverses direction upon collision with walls or paddles.

3. **Keyboard Bindings**:
   - Player inputs are linked to the paddle movement functions via `onkeypress`.

4. **Collision Detection**:
   - Paddles check if the ball is within their range for a realistic bounce.

---

### **Enhancements to Consider**
- Add sound effects for paddle hits and scoring.
- Include difficulty levels with increasing ball speed.
- Implement a "win condition" with a max score.
- Add AI for single-player mode where Player B is computer-controlled.
