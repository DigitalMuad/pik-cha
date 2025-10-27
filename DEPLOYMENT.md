# Pik-Cha Deployment Guide

## Quick Deployment Overview

This guide covers deploying both the backend (Flask) and frontend (React) separately.

---

## Backend Deployment (Flask)

### Option 1: Railway (Recommended)

1. **Sign up** at [railway.app](https://railway.app)
2. **Create a new project** and connect your GitHub repository
3. **Create a new service** from your repository
4. **Configure the service:**
   - **Root Directory:** `server`
   - **Build Command:** `pipenv install`
   - **Start Command:** `pipenv run gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Port:** Use environment variable `$PORT`

5. **Add Environment Variables:**
   ```
   DATABASE_URL=<your-database-url>
   FLASK_SECRET_KEY=<your-secret-key>
   JWT_SECRET_KEY=<your-jwt-secret-key>
   FLASK_ENV=production
   ```

6. **Deploy** and Railway will build and deploy your app
7. **Copy your backend URL** (e.g., `https://your-backend.railway.app`)

### Option 2: Render

1. **Sign up** at [render.com](https://render.com)
2. **Create a new Web Service** from your GitHub repository
3. **Configure:**
   - **Environment:** Python 3
   - **Build Command:** `cd server && pipenv install`
   - **Start Command:** `cd server && pipenv run gunicorn app:app --bind 0.0.0.0:$PORT`
4. **Add environment variables** (same as Railway above)
5. **Deploy** and get your backend URL

---

## Frontend Deployment (React + Vite)

### Option 1: Vercel (Recommended)

1. **Sign up** at [vercel.com](https://vercel.com)
2. **Import your GitHub repository**
3. **Configure:**
   - **Root Directory:** `client/pik-cha`
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`

4. **Add Environment Variables:**
   ```
   VITE_API_BASE_URL=<your-backend-url>
   ```
   (Replace with your deployed backend URL from Railway/Render)

5. **Deploy**

### Option 2: Netlify

1. **Sign up** at [netlify.com](https://netlify.com)
2. **Import your GitHub repository**
3. **Configure:**
   - **Base directory:** `client/pik-cha`
   - **Build command:** `npm run build`
   - **Publish directory:** `dist`

4. **Add Environment Variables:**
   ```
   VITE_API_BASE_URL=<your-backend-url>
   ```

5. **Deploy**

---

## Important Notes

### Environment Variables Summary

**Backend (Railway/Render):**
```
DATABASE_URL=<database-url>
FLASK_SECRET_KEY=<random-secret-key>
JWT_SECRET_KEY=<random-jwt-secret>
FLASK_ENV=production
```

**Frontend (Vercel/Netlify):**
```
VITE_API_BASE_URL=https://your-backend-url.railway.app
```

### Database Options

For production, consider using:
- **Railway PostgreSQL** (automatic with Railway)
- **Render PostgreSQL** (add as a service)
- **Supabase** (free PostgreSQL hosting)
- **Neon** (serverless PostgreSQL)

Update your `DATABASE_URL` to use PostgreSQL instead of SQLite:
```
DATABASE_URL=postgresql://user:password@host:port/database
```

### CORS Configuration

Make sure your backend's CORS settings allow your frontend domain. The current config in `config.py` should work, but you can restrict it in production:

```python
# In config.py
CORS(app, resources={r"/api/*": {"origins": "https://your-frontend.vercel.app"}})
```

---

## Deployment Checklist

- [ ] Backend deployed (Railway/Render)
- [ ] Backend URL copied
- [ ] Frontend configured with backend URL
- [ ] Environment variables set in both platforms
- [ ] Database configured (PostgreSQL)
- [ ] CORS settings updated
- [ ] Frontend deployed (Vercel/Netlify)
- [ ] Testing the deployed app

---

## Quick Start Commands

**To add Gunicorn to your backend:**
```bash
cd server
pipenv install gunicorn
```

**To test build locally:**
```bash
# Backend
cd server
pipenv run gunicorn app:app --bind 0.0.0.0:5000

# Frontend
cd client/pik-cha
npm run build
npm run preview
```

---

## Cost Overview

**Free Tier Options:**
- **Railway:** Free tier available with limited resources
- **Render:** Free tier with some limitations
- **Vercel:** Free tier with excellent performance
- **Netlify:** Free tier with generous limits

**Recommended Combo (All Free):**
- Backend: Railway (Free tier)
- Frontend: Vercel (Free tier)
- Total: $0/month

---

## Support

If you encounter issues:
1. Check platform logs for error messages
2. Verify environment variables are set correctly
3. Ensure database migrations have run
4. Test the API endpoints with Postman or curl
