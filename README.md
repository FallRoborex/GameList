# GameList
GameList is a personal game-tracking web app where you log, rate, and organize the games you've played, are playing, or plan to play

# Game Tracker — Project Scaffold
 
## Setup
 
1. Have Postgres running locally (or update DATABASE_URL in app/database.py
   to point at wherever your DB lives).
2. Create a virtual environment and install dependencies:
```
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
```
3. Run the app:
```
   uvicorn app.main:app --reload
```
4. Visit http://localhost:8000/docs to see and test your endpoints interactively.
## What's already built vs. what you need to fill in
 
**Already built:**
- Project structure
- Database connection setup (app/database.py)
- User model (app/models.py)
- Route definitions and their expected behavior, as docstrings (app/main.py, app/auth.py)
**You need to implement (look for TODO comments):**
- app/auth.py: hash_password, verify_password, create_access_token,
  create_refresh_token, decode_token
- app/main.py: register, login, get_current_user route bodies
- app/models.py: RefreshToken model (once basic auth works)
## Suggested order to build in
 
1. Fill in `hash_password` and `verify_password` first — test these in
   isolation (even just a quick throwaway script) before touching routes.
2. Fill in `create_access_token` and `decode_token` — again, test these
   two together in isolation first (encode something, decode it back,
   confirm you get the original data).
3. Wire up the `/auth/register` route using what you built in step 1.
4. Wire up the `/auth/login` route using what you built in steps 1 and 2.
5. Wire up `/auth/me` as your first protected route.
6. Only once all of that works end-to-end, add the RefreshToken model
   and wire refresh-token issuance/rotation into login.
## Notes on the security decisions baked into this scaffold
 
- Argon2 for password hashing (not bcrypt) — currently the more modern
  recommended choice.
- JWT access tokens (short-lived, 15 min) + refresh tokens (longer-lived,
  7 days) — limits damage if a token leaks, while not forcing constant re-login.
- httpOnly cookies for token storage (not localStorage) — closes off XSS
  token theft, since JavaScript can't read httpOnly cookies at all.
- SameSite=Strict on cookies — closes off CSRF by refusing to send the
  cookie on any request that didn't originate from your own site.