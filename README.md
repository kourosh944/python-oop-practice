# 🐍 Python OOP Practice — Inheritance & super()

A collection of Python exercises and a mini-project, all focused on practicing **class inheritance**, **`super()`**, and **method overriding**.

---

## 📂 Exercises (`/exercises`)

| File | Topic |
|---|---|
| `train_1.py` | First child class — basic inheritance (`Animal → Dog`) |
| `train_2.py` | Inherited attributes without a new `__init__` |
| `train_3.py` | First use of `super()` in a constructor |
| `train_4.py` | Overriding a method (`Vehicle → Car`) |
| `train_5.py` | Using `super()` inside a regular (non-constructor) method |
| `train_6.py` | Combining inheritance, `super()`, and overriding (`BankAccount`) |
| `train_7.py` | Fixing broken code — a common `super()` mistake |
| `train_8.py` | Predicting output — constructor execution order |
| `train_9.py` | Designing a child class with calculation (`DiscountedProduct`) |

---

## 🎓 Mini Project — School Members System (`school_members.py`)

A small system simulating school members, combining everything practiced in the exercises above:

- **`User`** — base class (`name`, `phone`)
- **`Student`** (inherits `User`) — adds `course`, `score`, and a `status()` method
- **`Teacher`** (inherits `User`) — adds `specialty`, `hourly_rate`, and `calculate_salary()`
- **`OnlineStudent`** (inherits `Student`) — adds `platform`, built entirely with `super()` (no repeated code)

---

## ▶️ Run Any File

```bash
python exercises/train_1.py
python school_members.py
```

---

## 👤 Author

**Kourosh**
🚀 Frontend Developer | Learning Python & Django

- 📧 abasikourosh72@gmail.com
- 💬 [Telegram](https://t.me/kourosh2087)
