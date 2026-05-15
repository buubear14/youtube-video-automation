````markdown name=README.md
# 🎬 YouTube Video Automation

**Automated AI-powered YouTube video generation and upload system** - completely free, running 24/7 on GitHub Actions.

Created by: **buubear14**

---

## ✨ Features

- ✅ **Automated Script Generation** - Uses DeepSeek API for viral scripts
- ✅ **AI Voiceover** - ElevenLabs generates natural-sounding narration
- ✅ **Dual Video Generation** - Synthesia + D-ID with automatic fallback
- ✅ **Trending Topics** - Pulls from YouTube & News API
- ✅ **Auto Upload** - Directly uploads to your YouTube channel
- ✅ **Scheduled Automation** - Runs every 3 days via GitHub Actions
- ✅ **Completely Free** - No credit card required

---

## 🚀 Quick Start

### 1. Create Repository
Fork or clone this repo to your GitHub account.

### 2. Get API Keys (5 minutes)

| API | Where to Get | Free Tier |
|-----|-------------|-----------|
| **DeepSeek** | https://platform.deepseek.com/ | ✅ Generous free tier |
| **ElevenLabs** | https://elevenlabs.io/ | ✅ 330k chars/month |
| **Synthesia** | https://www.synthesia.io/ | ✅ Free tier available |
| **D-ID** | https://www.d-id.com/ | ✅ Free tier available |
| **YouTube API** | https://console.cloud.google.com/ | ✅ Unlimited free |
| **News API** | https://newsapi.org/ | ✅ 100 requests/day free |

### 3. Add GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these secrets:
```
DEEPSEEK_API_KEY = your_key_here
ELEVENLABS_API_KEY = your_key_here
SYNTHESIA_API_KEY = your_key_here
D_ID_API_KEY = your_key_here
NEWS_API_KEY = your_key_here
YOUTUBE_CREDENTIALS = your_json_credentials
```

### 4. Run First Test

Go to **Actions** → **YouTube Video Automation** → **Run workflow** → **Run workflow**

Watch your first video generate and upload! 🎉

---

## 📁 Project Structure

```
.
├── main.py                    # Main orchestrator
├── config.py                  # API configuration
├── trending.py                # Trending topics fetcher
├── script_generator.py         # DeepSeek script generation
├── audio_generator.py          # ElevenLabs voiceover
├── video_generator.py          # Synthesia + D-ID dual APIs
├── uploader.py                 # YouTube upload handler
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
└── .github/workflows/
    └── auto_upload.yml         # GitHub Actions workflow
```

---

## 🔄 How It Works

Every 3 days, the automation:

1. **Fetches trending topics** from YouTube & News API
2. **Generates a compelling script** using DeepSeek API
3. **Creates AI voiceover** with ElevenLabs
4. **Generates AI video** with Synthesia (fallback to D-ID)
5. **Uploads to YouTube** automatically
6. **Repeats** in 3 days

```
Trending Topic → Script → Voiceover → Video → Upload → YouTube
```

---

## ⚙️ Configuration

### Change Upload Schedule

Edit `.github/workflows/auto_upload.yml`:

```yaml
schedule:
  - cron: '0 2 */3 * *'  # Every 3 days at 2 AM UTC
```

**Common cron expressions:**
- `0 2 * * *` = Daily at 2 AM
- `0 2 * * 0` = Every Sunday at 2 AM  
- `0 2 */7 * *` = Every 7 days

### Adjust Video Settings

Edit `config.py`:
```python
VIDEO_DURATION = 60         # seconds
VOICE_GENDER = "male"       # male/female
VIDEO_LANGUAGE = "en"       # language code
```

---

## 💰 Cost Analysis

**Total Monthly Cost: $0**

| Service | Free Tier | Monthly Usage |
|---------|-----------|---------------|
| DeepSeek | Generous | ~60 requests |
| ElevenLabs | 330k chars | ~200k chars |
| Synthesia | Free tier | ~10 videos |
| D-ID | Free tier | Unlimited fallback |
| YouTube API | Unlimited | Unlimited |
| GitHub Actions | 2000 min/month | ~100 min |

✅ Everything stays within free limits!

---

## 🐛 Troubleshooting

### "API key not found"
→ Check that GitHub Secrets are named exactly as expected

### "Video generation failed"
→ Check API key validity; dual fallback will try D-ID

### "YouTube upload failed"
→ Ensure YouTube credentials JSON is properly formatted

### Check Workflow Logs
Go to **Actions** tab → Select workflow → View logs

---

## 🎯 Monetization Tips

1. **YouTube Partner Program**: 1000 subs + 4000 watch hours
2. **Affiliate Marketing**: Add links in descriptions
3. **Sponsored Content**: Once channel grows
4. **Patreon**: Build community and offer exclusives

---

## 📝 License

Free to use and modify for personal use.

---

## ❓ Support

- Check workflow logs in GitHub Actions
- Verify all API keys are correct
- Ensure YouTube account is eligible for uploads
- Test manually: `python main.py`

---

## 🎬 Next Steps

1. ✅ Add API keys to GitHub Secrets
2. ✅ Test the workflow manually
3. ✅ Wait for first automated run (3 days)
4. ✅ Monitor and optimize script generation
5. ✅ Scale to multiple channels as needed

**Happy automating! 🚀**
````
