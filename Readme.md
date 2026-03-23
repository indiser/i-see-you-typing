# 🔐 KeyLogger: Because Privacy is Overrated™

> *"I spent 3 hours building a keylogger when I could've just asked people what they're typing. But where's the fun in that?"* - Me, probably

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Questionable Life Choices](https://img.shields.io/badge/Life%20Choices-Questionable-red.svg)]()
[![Works on My Machine](https://img.shields.io/badge/Works%20on-My%20Machine-success.svg)]()

## 📖 What Fresh Hell is This?

A Python keylogger that records every keystroke with the enthusiasm of a nosy neighbor and the subtlety of a freight train. Started as `first.py` (creative naming, I know), evolved into `main.py` (even more creative), and now features enough enterprise-grade buzzwords to make a startup founder weep with joy.

**Current Status:** It works! (Narrator: *It mostly works*)

## 🎯 Features That Actually Exist

- ✅ **Logs keystrokes** - Shocking, I know
- ✅ **Timestamps** - Because knowing *when* you typed "password123" is crucial
- ✅ **Batch writing** - Pretending to care about I/O performance
- ✅ **File rotation** - When 5MB of your typing is too much
- ✅ **JSON config** - Making it look professional since 2026
- ✅ **Threading** - Because one thread wasn't enough to spy on you
- ✅ **Special key filtering** - Excludes shift/ctrl/alt (they know what they did)

## 🚀 Quick Start (AKA How to Incriminate Yourself)

```bash
# Install dependencies (just one, we're minimalists here)
pip install keyboard

# Run the basic version (for nostalgic purposes)
python first.py

# Run the "enterprise" version (same thing, more code)
python main.py
```

**Warning:** Running this on someone else's computer is illegal. Running it on your own computer is just sad. Choose wisely.

## 📁 Project Structure (It's Organized Chaos)

```
keylogger/
├── first.py                    # The OG - Simple, naive, beautiful
├── main.py                     # The "I learned about design patterns" version
├── keylogger_config.json       # Settings for people who like settings
├── keylog.txt                  # Your secrets (the old ones)
├── logs/                       # Your secrets (the new ones)
│   └── keylog_2026-02-05.txt  # Today's embarrassment
└── README.md                   # You are here (congrats!)
```

## 🎭 The Evolution Story

### `first.py` - The Innocent Days
*"I just learned about the keyboard library!"*
- 15 lines of pure, unadulterated simplicity
- No error handling (YOLO)
- Logs everything to one file forever
- Will it crash? Maybe. Will it work? Also maybe.

### `main.py` - The "I Read Clean Code" Phase
*"What if we added... EVERYTHING?"*
- 200+ lines of overengineering
- Classes! Threading! Deques! JSON!
- Handles errors like a responsible adult
- Still just logs keystrokes (but with *style*)

## 🔮 Future Improvements (AKA My TODO List That'll Never Get Done)

### 🎨 High Priority (I Might Actually Do These)

- [ ] **Encryption** - Because plaintext passwords in logs are *chef's kiss* terrible
- [ ] **GUI Dashboard** - Real-time keystroke visualization (for the voyeur in you)
- [ ] **Email Reports** - Daily summaries of your typos
- [ ] **Machine Learning** - Predict what you'll type next (spoiler: it's "password123")
- [ ] **Multi-language Support** - Spy on people globally!

### 🛠️ Medium Priority (Probably Not Happening)

- [ ] **Cloud Sync** - Upload your keystrokes to someone else's computer
- [ ] **Mobile App** - Because your phone doesn't spy on you enough
- [ ] **Browser Extension** - For when the desktop app isn't invasive enough
- [ ] **Autocorrect Integration** - Fix typos before logging them (we have standards)
- [ ] **Sentiment Analysis** - Detect when you're rage-typing
- [ ] **Stealth Mode** - Hide from Task Manager (and your conscience)

### 🎪 Low Priority (Fever Dream Territory)

- [ ] **Blockchain Integration** - Because why not ruin this too?
- [ ] **NFT Support** - Mint your keystrokes as NFTs (each typo is unique!)
- [ ] **AI Chatbot** - Responds to what you type before you finish typing it
- [ ] **VR Mode** - Watch your keystrokes in immersive 3D
- [ ] **Smart Home Integration** - "Alexa, what did I type at 3 AM?"
- [ ] **Quantum Encryption** - Logs exist in superposition until observed
- [ ] **Time Travel Feature** - Log keystrokes from the future

### 🔧 Technical Debt (The Stuff I Should Fix But Won't)

- [ ] **Unit Tests** - What are those? (I know what they are, I just choose violence)
- [ ] **Type Hints** - Python 3.5+ called, they want their features back
- [ ] **Proper Logging** - Using `print()` is a lifestyle choice
- [ ] **Documentation** - This README counts, right?
- [ ] **Code Comments** - The code is self-documenting (it's not)
- [ ] **Virtual Environment** - We install globally like savages
- [ ] **CI/CD Pipeline** - Continuous Integration? More like Continuous Procrastination

### 🎯 Performance Optimizations (For When I Care About Speed)

- [ ] **Async I/O** - Because threading is so 2020
- [ ] **Memory Profiling** - Find out why it uses 2GB to log "hello"
- [ ] **Database Backend** - SQLite for your keystrokes (overkill? never heard of it)
- [ ] **Caching Layer** - Cache keystrokes in Redis (I'm not joking, this would be hilarious)
- [ ] **Load Balancing** - Distribute keystroke logging across multiple cores
- [ ] **Microservices Architecture** - One service per key on the keyboard

### 🔒 Security Improvements (Ironic, I Know)

- [ ] **Password Protection** - Protect the app that steals passwords
- [ ] **2FA** - Two-factor auth to access your keystroke logs
- [ ] **Audit Logs** - Logs for your logs (logception)
- [ ] **Penetration Testing** - Hire hackers to hack the hacking tool
- [ ] **GDPR Compliance** - "We value your privacy" (we don't)

## 🤔 FAQ (Frequently Avoided Questions)

**Q: Is this legal?**  
A: On your own computer? Yes. On anyone else's? Absolutely not. Don't be that person.

**Q: Why did you make this?**  
A: To learn Python! And because my therapist said I need hobbies.

**Q: Should I use this in production?**  
A: If by "production" you mean "producing evidence for a lawsuit," then no.

**Q: Can I contribute?**  
A: Sure! I accept PRs, bug reports, and emotional support.

**Q: What's with all the jokes?**  
A: Coping mechanism for the existential dread of modern software development.

## 🐛 Known Issues (Features, Really)

- Logs your password when you type it (working as intended)
- Doesn't work when computer is off (investigating)
- May log your existential crisis at 3 AM (not a bug, a feature)
- Config file doesn't validate input (trust issues)
- No uninstall script (you're stuck with me now)

## 📜 License

MIT License - Because I'm not responsible for what you do with this.

**Disclaimer:** This is for educational purposes only. Don't be evil. Or do, but don't blame me.

## 🙏 Acknowledgments

- **Stack Overflow** - For teaching me everything
- **Coffee** - For keeping me awake during debugging sessions
- **Rubber Duck** - Best debugging partner, never judges
- **Past Me** - For writing `first.py` and thinking it was good enough
- **Future Me** - Sorry about the technical debt, buddy

## 📞 Contact

Found a bug? Have a feature request? Want to tell me my code is terrible?

Open an issue! Or don't. I'm not your boss.

---

<div align="center">

**⭐ Star this repo if you found it useful!**  
*(Or if you feel bad for me)*

*Made with ❤️, Python, and questionable decisions*

</div>

---

### 🎬 Epilogue

This project started as a simple 15-line script and evolved into a 200+ line monument to feature creep. It's a beautiful reminder that sometimes the simplest solution is the best solution, but where's the fun in that?

Remember: With great power comes great responsibility. And with keyloggers comes great legal liability.

**Stay curious, stay ethical, and may your logs be ever in your favor.** 🚀
