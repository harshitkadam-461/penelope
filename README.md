Penelope (The Ithacans). Flask app on Vercel: app.py + core.py + public/index.html.
Env vars (optional): ANTHROPIC_API_KEY, PENELOPE_MODEL, REFUND_LIMIT, TELEGRAM_BOT_TOKEN, and Upstash Redis (UPSTASH_REDIS_REST_URL / _TOKEN or KV_REST_API_URL / _TOKEN).
Telegram webhook: https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://<your-app>.vercel.app/api/telegram
WhatsApp (Twilio) webhook: https://<your-app>.vercel.app/api/whatsapp
