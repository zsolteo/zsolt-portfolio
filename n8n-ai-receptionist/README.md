# n8n AI receptionist and concierge

An AI-based automated telephone receptionist and concierge built on the n8n automation platform. It started as my research paper at Dunaújvárosi Egyetem (University of Dunaújváros).

The example in this folder is set up for a hotel: the fictional **Grand Danube Hotel**, a 4-star city hotel. The same design fits large hotel chains and independent hotels alike. Swap the hotel name, FAQ and booking API for your own.

## What it does

- Answers the phone in English or Hungarian, in short spoken replies
- Answers hotel questions: check-in and check-out times, parking, breakfast, spa, airport transfer
- Checks room availability and prices
- Takes a booking, but only after reading every detail back to the caller and getting a clear yes
- Hands over to a human for complaints, payments and group bookings
- Never takes card numbers on the phone and never invents prices or policies

## How it works

```
caller -> voice provider (speech-to-text) -> n8n webhook
       -> Receptionist agent (Claude + call memory)
            tools: Hotel FAQ · Check availability · Create booking · Transfer to front desk
       -> reply text -> voice provider (text-to-speech) -> caller
```

## Setup

1. In n8n, choose **Import from file** and pick `workflows/hotel-receptionist.json`.
2. Add your Anthropic API key as a credential on the **Claude** node.
3. Replace the `YOUR-HOTEL-API.example.com` URLs in the four tool nodes with your booking system or a Google Sheet API.
4. Point your voice provider (for example Twilio, Vapi or Retell) at the webhook URL. It should send `call_id` and `transcript`, and read `reply` back to the caller.

## Author

Csepecz Zsolt
