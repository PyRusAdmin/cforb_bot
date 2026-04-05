# Правила участия в проекте / Contributing Guidelines

## 🇷🇺 На русском

Спасибо за ваш интерес к проекту! Мы рады любому вкладу. Пожалуйста, ознакомьтесь с этими правилами, чтобы участие было комфортным для всех.

### 📋 Содержание

- [Сообщения об ошибках](#сообщения-об-ошибках)
- [Предложения улучшений](#предложения-улучшений)
- [Pull-запросы](#pull-запросы)
- [Стиль кода](#стиль-кода)
- [Структура проекта](#структура-проекта)
- [Коммиты](#коммиты)

---

### 🐛 Сообщения об ошибках

Если вы нашли ошибку:

1. Проверьте, не создана ли уже похожая задача в [Issues](https://gitverse.ru/pyadminru/cforb_bot/issues)
2. Создайте новый Issue, указав:
   - **Описание** — краткое и понятное название проблемы
   - **Шаги воспроизведения** — подробно опишите, как воспроизвести ошибку
   - **Ожидаемое поведение** — что должно было произойти
   - **Фактическое поведение** — что произошло на самом деле
   - **Окружение** — версия Python, ОС, зависимости
   - **Скриншоты/логи** — если применимо

---

### 💡 Предложения улучшений

Если у вас есть идея по улучшению:

1. Проверьте существующие [Issues](https://gitverse.ru/pyadminru/cforb_bot/issues)
2. Создайте новый Issue с меткой `enhancement`
3. Опишите:
   - Какую проблему решает предложение
   - Как вы видите реализацию
   - Какие могут быть побочные эффекты

---

### 🔧 Pull-запросы

Перед отправкой PR:

1. **Создайте ветку** от `main`:
   ```bash
   git checkout -b feature/ваше-название
   ```

2. **Внесите изменения** и убедитесь, что всё работает

3. **Обновите зависимости**, если добавили новые

4. **Сделайте коммит** с понятным сообщением (см. раздел [Коммиты](#коммиты))

5. **Отправьте ветку** и создайте Merge Request:
   ```bash
   git push origin feature/ваше-название
   ```

6. **Заполните описание** в MR:
   - Что изменилось
   - Зачем это нужно
   - Как протестировать

---

### 💻 Стиль кода

**Python:**
- Следуйте [PEP 8](https://peps.python.org/pep-0008/)
- Используйте `snake_case` для функций и переменных
- Используйте `PascalCase` для классов
- Добавляйте docstring для функций и классов
- Максимальная длина строки — 120 символов

**Пример:**
```python
async def handle_start(message: Message) -> None:
    """Обработка команды /start."""
    await message.answer("Добро пожаловать!")
```

---

### 📁 Структура проекта

```
├── database/        # Работа с базой данных
├── handlers/        # Обработчики сообщений
│   ├── admin/       # Админ-панель
│   ├── user/        # Пользовательские хендлеры
│   └── services_prices/  # Услуги и цены
├── keyboards/       # Клавиатуры (inline, reply)
├── media/           # Медиа-файлы (фото, документы)
├── states/          # FSM-состояния
├── system/          # Основные модули (dispatcher, utils)
├── main.py          # Точка входа
├── requirements.txt # Зависимости
└── .env             # Переменные окружения (не коммитить!)
```

---

### 📝 Коммиты

**Формат сообщения:**
```
тип: краткое описание

подробное описание (если нужно)
```

**Типы:**
- `feat` — новая функция
- `fix` — исправление ошибки
- `docs` — изменение документации
- `style` — форматирование, без изменения логики
- `refactor` — рефакторинг
- `test` — добавление/изменение тестов
- `chore` — рутинные задачи (обновление зависимостей и т.д.)

**Примеры:**
```
feat: добавить обработку команды оплаты
fix: исправить ошибку с пагинацией
docs: обновить README
refactor: вынести валидацию в отдельную функцию
```

---

### 📞 Контакты

Если у вас есть вопросы, напишите в Telegram: [@pyadminru](https://t.me/pyadminru)

---

## 🇬🇧 In English

Thank you for your interest in the project! We welcome any contributions. Please review these guidelines to ensure a smooth experience for everyone.

### 🐛 Bug Reports

If you find a bug:

1. Check if a similar issue already exists in [Issues](https://gitverse.ru/pyadminru/cforb_bot/issues)
2. Create a new Issue including:
   - **Title** — short and descriptive
   - **Steps to reproduce** — how to trigger the bug
   - **Expected behavior** — what should happen
   - **Actual behavior** — what actually happens
   - **Environment** — Python version, OS, dependencies
   - **Screenshots/logs** — if applicable

---

### 💡 Feature Requests

If you have an improvement idea:

1. Check existing [Issues](https://gitverse.ru/pyadminru/cforb_bot/issues)
2. Create a new Issue with `enhancement` label
3. Describe:
   - What problem it solves
   - How you envision the implementation
   - Any potential side effects

---

### 🔧 Pull Requests

Before submitting a PR:

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes** and ensure everything works

3. **Update dependencies** if you added new ones

4. **Commit** with a clear message (see [Commits](#-commits))

5. **Push and create a Merge Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Fill in the MR description**:
   - What changed
   - Why it's needed
   - How to test it

---

### 💻 Code Style

**Python:**
- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use `snake_case` for functions and variables
- Use `PascalCase` for classes
- Add docstrings for functions and classes
- Maximum line length — 120 characters

---

### 📝 Commits

**Message format:**
```
type: short description

detailed description (if needed)
```

**Types:**
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation changes
- `style` — formatting, no logic changes
- `refactor` — code refactoring
- `test` — adding/modifying tests
- `chore` — maintenance tasks

**Examples:**
```
feat: add payment command handler
fix: fix pagination bug
docs: update README
refactor: extract validation to separate function
```

---

### 📞 Contact

If you have questions, reach out via Telegram: [@pyadminru](https://t.me/pyadminru)
