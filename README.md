# 🎓 School Members System

A small Python OOP practice project simulating a school membership system — built to practice **inheritance**, **`super()`**, and **method overriding**.

---

## 🛠️ Concepts Practiced

- Class inheritance (`User → Student → OnlineStudent`, `User → Teacher`)
- Using `super()` in constructors and overridden methods
- Method overriding (`show_profile()`)
- Simple business logic (`status()`, `calculate_salary()`)

---

## 📦 Classes

- **`User`** — base class with `name` and `phone`, and a `show_profile()` method
- **`Student`** (inherits `User`) — adds `course` and `score`; has a `status()` method that returns `"Accepted"` or `"Need for greater effort"` based on the score
- **`Teacher`** (inherits `User`) — adds `specialty` and `hourly_rate`; has a `calculate_salary(hours)` method
- **`OnlineStudent`** (inherits `Student`) — adds `platform`, without repeating any code from `Student`

---

## ▶️ Run It

```bash
python Mini_project_1.py
```

---

## 👤 Author

**Kourosh**
🚀 Frontend Developer | Learning Python & Django

- 📧 abasikourosh72@gmail.com
- 💬 [Telegram](https://t.me/kourosh2087)
