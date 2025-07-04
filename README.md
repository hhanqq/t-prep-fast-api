Проект реализован в рамках интенсива от компании Т-Банк, кейс: T-prep.

Этот проект представляет собой **мини-систему аутентификации и управления тестами/вопросами (T-prep)** с использованием FastAPI, PostgreSQL и Alembic для миграций. Также реализованы модели пользователей, вопросы, группы вопросов и тесты.

---

# 🧩 Проект: Система управления тестами

## 📌 Описание
Проект реализует REST API для регистрации и авторизации пользователей, а также создания и управления тестами и вопросами. Поддерживает:
- Регистрацию и вход через JWT токены.
- Управление тестами (создание, хранение, уникальные ссылки).
- Управление вопросами и группами вопросов.
- Валидацию данных через Pydantic.
- Асинхронную работу с базой данных.

---

## 🛠 Стек технологий

| Категория       | Используемые технологии |
|----------------|-------------------------|
| **Backend**     | Python 3.12, FastAPI    |
| **База данных** | PostgreSQL              |
| **ORM**         | SQLAlchemy + AsyncAttrs |
| **Миграции**    | Alembic                 |
| **Аутентификация** | JWT, Bcrypt           |
| **Веб-фреймворк** | FastAPI                |
| **Контейнеризация** | Docker, Docker Compose |
| **Логирование** | logging                 |

---

## 🧠 Архитектура backend

### 1. **FastAPI**
- Реализованы следующие эндпоинты:
  - `/register` — регистрация пользователя
  - `/login` — получение JWT токена
  - `/create-test` — создание нового теста
  - `/test/{unique_url}` — просмотр теста по ссылке
  - `/questions` — получение списка вопросов
  - `/questions/add` — добавление новых вопросов

### 2. **JWT Аутентификация**
- Реализовано токенное аутентификационное окружение:
  - Логин через OAuth2 (`/login`)
  - Защита эндпоинтов через `Depends(get_current_user)`
  - Токены живут 30 минут

### 3. **Пользователи**
- Модель пользователя содержит поля:
  - `id`, `username`, `email`, `hashed_password`
- Регистрация проверяет уникальность email

### 4. **Тесты**
- Каждый тест имеет:
  - Заголовок, описание, код теста
  - Уникальный URL для доступа
- Генерация URL через `uuid.uuid4()`

### 5. **Вопросы**
- Вопросы связаны с тестами и группируются в группы
- Поддержка правильного и неправильных ответов

---

## 🗃️ Структура базы данных

```python
class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class QuestionModel(Base):
    __tablename__ = "Question"
    id = Column(Integer, primary_key=True)
    qstn = Column(String, nullable=False)               # Вопрос
    correct_answer = Column(String)                     # Правильный ответ
    wr_answer1 = Column(String)                         # Неверный 1
    wr_answer2 = Column(String)                         # Неверный 2
    wr_answer3 = Column(String)                         # Неверный 3

class QGroupModel(Base):
    __tablename__ = "Question_group"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)              # Название группы
    user_id = Column(Integer, ForeignKey("User.id"))     # Владелец группы
```

---

## 🔁 Миграции (Alembic)

- Автоматическое управление версиями БД
- Пример миграции:
  ```bash
  alembic revision --autogenerate -m "Initial migration"
  alembic upgrade head
  ```
- Поддержка downgrade/upgrade

---

## 🐳 Инфраструктура (Docker)

### `docker-compose.yml` содержит:
- `postgres`: PostgreSQL 15
- `pgadmin`: Для удобного просмотра БД
- `app`: FastAPI приложение

### `Dockerfile`:
- Основан на `python:3.12-slim`
- Установка зависимостей через `requirements.txt`
- Выполнение миграций перед запуском приложения:
  ```bash
  python -m alembic upgrade head
  ```

---

## 🚀 Установка и запуск

### 1. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 2. Настройте `.env` или измените `config.py`:
```python
DATABASE_URL = postgresql://SU:SU_passw@localhost:5433/postgres_db
```

### 3. Запустите проект через Docker:
```bash
docker-compose up --build
```

