# Deploy Pik-Cha to Render

## Quick Deployment Steps

### Backend Deployment (Flask)

1. **Sign up** at [render.com](https://render.com) (or log in)

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository

3. **Configure the Backend**
   
   **Basic Settings:**
   - **Name:** `pik-cha-backend` (or any name)
   - **Region:** Choose closest to you
   - **Branch:** `main` (or your default branch)
   - **Root Directory:** `server` ⚠️ **IMPORTANT**
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`

4. **Add Environment Variables**
   Click "Advanced" → "Environment Variables" and add:
   ```
   DATABASE_URL=sqlite:///../instance/pikcha.db
   FLASK_SECRET_KEY=<generate-random-key>
   JWT_SECRET_KEY=<generate-random-key>
   FLASK_ENV=production
   ```

5. **Deploy!**
   Click "Create Web Service"

6. **Get your Backend URL**
   After deployment, you'll get a URL like: `https://pik-cha-backend.onrender.com`
   ⚠️ **Copy this URL** - you'll need it for the frontend

### Frontend Deployment (React + Vite)

1. **Create New Static Site**
   - Click "New +" button
   - Select "Static Site"

2. **Configure the Frontend**
   
   **Basic Settings:**
   - **Name:** `pik-cha-frontend`
   - **Branch:** `main`
   - **Root Directory:** `client/pik-cha`
   - **Build Command:** `npm run build`
   - **Publish Directory:** `dist`

3. **Add Environment Variable**
   ```
   VITE_API_BASE_URL=<your-backend-url-from-above>
   ```
   Replace `<your-backend-url-from-above>` with the URL from step 6 above
   (e.g., `https://pik-cha-backend.onrender.com`)

4. **Deploy!**
   Click "Create Static Site"

## Generating Secret Keys

Run this in your terminal:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Run it twice to get two different keys for `FLASK_SECRET_KEY` and `JWT_SECRET_KEY`

## Important Notes

### Database
- Render provides free PostgreSQL databases
- To use PostgreSQL instead of SQLite:
  1. Create a PostgreSQL database in Render
  2. Update `DATABASE_URL` to use the PostgreSQL connection string
  3. Run migrations: `flask db upgrade`

### CORS
The current CORS settings should work, but you can restrict it in production by updating `config.py`:
```python
CORS(app, resources={r"/api/*": {"origins": "https://pik-cha-frontend.onrender.com"}})
```

### Free Tier Limitations
- Render free tier can "spin down" after 15 minutes of inactivity
- First request after spin-down takes ~30-60 seconds
- Consider upgrading for production use

## Cost
**Total: $0/month** (using free tier for both)

## Troubleshooting

**Build fails?**
- Check the logs in Render dashboard
- Make sure `requirements.txt` is in the `server` directory
- Ensure Gunicorn is in requirements.txt

**Frontend can't connect to backend?**
- Verify `VITE_API_BASE_URL` is set correctly
- Check backend is running (look at logs)
- Test backend URL directly in browser

**Database issues?**
- Make sure `DATABASE_URL` is set correctly
- If using SQLite, ensure path is correct
- Consider switching to PostgreSQL for better reliability

## Testing

1. Visit your frontend URL
2. Try signing up/logging in
3. Upload an image
4. Test transformations
