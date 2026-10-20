# Penelope on Vercel (The Ithacans, PS-04)

## Get your Vercel link (about 5 minutes)
Option A, Vercel CLI:
    npm i -g vercel
    cd penelope-vercel
    vercel login
    vercel --prod          # prints https://your-app.vercel.app

Option B, GitHub: push this folder to a GitHub repo, then vercel.com -> Add New -> Project -> Import. Click Deploy.

It works immediately with the offline brain (no keys). Then add the optional upgrades below in
Vercel -> Project -> Settings -> Environment Variables, and redeploy (vercel --prod).

## Optional upgrades
1. Real Claude brain: add ANTHROPIC_API_KEY (and optionally PENELOPE_MODEL).
2. Shared live mode (needed for Telegram/WhatsApp): Vercel -> Storage / Marketplace -> add "Upstash Redis" (free) and connect it to the project.
   The env vars are added automatically. The dashboard then shows chats from every channel live.
   Without Redis the app runs in "Browser demo mode": the web demo still works, state lives in your browser.
3. Telegram bot: talk to @BotFather -> /newbot -> copy the token -> add TELEGRAM_BOT_TOKEN -> redeploy -> open once in a browser:
   https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-app.vercel.app/api/telegram
4. WhatsApp (Twilio sandbox): Twilio Console -> Messaging -> Try WhatsApp -> set "When a message comes in" to
   https://your-app.vercel.app/api/whatsapp  (POST).
Tune rules with env var REFUND_LIMIT (default 1000); other rules are at the top of api/_core.py.

## Layout
public/index.html  chat + seller dashboard      api/_core.py  store, 6 tools, guardrails, brains
api/chat|state|decide|reset.py  web endpoints   api/telegram.py, api/whatsapp.py  channel webhooks
