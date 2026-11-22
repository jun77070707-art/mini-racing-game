# Mini Racing Game

A beginner-friendly Python car-dodging game for a programming fundamentals class.

## Local play

Install Python 3.12, then run:

```bash
python -m pip install pygame-ce
python main.py
```

Use left/right arrow keys. Avoid the red car. Press Space after crashing to restart.

## GitHub Pages

Upload `main.py`, `requirements.txt`, `README.md` and `.github/workflows/deploy.yml` to a public GitHub repository on its `main` branch. In Settings > Pages, select **GitHub Actions** as the source. Check the Actions tab for the build and deployment result. Your URL will be `https://YOUR_USERNAME.github.io/REPOSITORY_NAME/`.

The browser version requires Pygbag and may need testing across browsers. The local desktop version is keyboard-controlled.

## Programming concepts

- Variables: positions and score
- `if`: movement, collision, restart
- `while`: game loop
- `for`: drawing road markings
- `random.randint`: obstacle position
- Function: `reset_game`
- `asyncio.sleep(0)`: allows the browser build to update smoothly
