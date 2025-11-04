# Быстрый старт: Публикация Python SDK в PyPI

## Структура проекта

```
zerotrue-sdk/
├── zerotrue/              # Основной пакет
│   ├── __init__.py        # Экспорт публичного API
│   ├── client.py          # Главный клиент
│   ├── http_client.py     # HTTP клиент с retry логикой
│   ├── exceptions.py      # Исключения
│   ├── types.py           # Типы данных
│   └── resources/         # Ресурсы API
│       └── checks.py      # Ресурс для проверок
├── tests/                 # Тесты
├── examples/              # Примеры использования
├── pyproject.toml         # Конфигурация пакета (современный стандарт)
├── setup.py               # Для совместимости
├── MANIFEST.in            # Файлы для включения в пакет
└── README.md              # Документация
```

## Как публиковать в PyPI

### Шаг 1: Подготовка PyPI аккаунта

1. Зарегистрируйтесь на [PyPI](https://pypi.org/account/register/)
2. Создайте API токен:
   - Settings → Account settings → API tokens
   - Create API token
   - Scope: "Entire account" или конкретный проект
   - Скопируйте токен (начинается с `pypi-`)

### Шаг 2: Настройка GitHub Secrets (для автоматической публикации)

1. В репозитории: Settings → Secrets and variables → Actions
2. New repository secret:
   - Name: `PYPI_API_TOKEN`
   - Secret: ваш токен из PyPI (начинается с `pypi-`)

### Шаг 3: Автоматическая публикация через GitHub Releases

**Это самый простой способ:**

1. Обновите версию в `pyproject.toml`:
   ```toml
   version = "1.0.0"
   ```

2. Создайте коммит:
   ```bash
   git add pyproject.toml
   git commit -m "chore: prepare release v1.0.0"
   git push origin main
   ```

3. Создайте тег и релиз:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

4. На GitHub:
   - Перейдите в Releases → Draft a new release
   - Выберите тег `v1.0.0`
   - Заполните название и описание
   - Нажмите "Publish release"

5. GitHub Actions автоматически:
   - Соберет пакет
   - Опубликует в PyPI
   - Пакет будет доступен через `pip install zerotrue-sdk`

### Шаг 4: Ручная публикация (альтернатива)

Если нужно опубликовать вручную:

```bash
# Установите инструменты
pip install build twine

# Соберите пакет
python -m build

# Проверьте пакет
twine check dist/*

# Загрузите на PyPI (потребуется токен)
twine upload dist/*
```

## Как работают GitHub Releases

1. **При создании релиза** GitHub отправляет событие `release` с типом `created`
2. **GitHub Actions workflow** (`.github/workflows/publish.yml`) запускается автоматически
3. **Workflow:**
   - Проверяет код
   - Устанавливает Python
   - Собирает пакет через `python -m build`
   - Публикует в PyPI используя токен из секретов

## Важные моменты

### Имя пакета

Текущее имя в `pyproject.toml`: `zerotrue-sdk`

⚠️ **Проверьте доступность имени:**
- Перейдите на https://pypi.org/project/zerotrue-sdk/
- Если имя занято, измените в `pyproject.toml`:
  ```toml
  name = "zerotrue-python-sdk"  # или другое доступное имя
  ```

### Версионирование

Используйте [Semantic Versioning](https://semver.org/):
- `1.0.0` - первый релиз
- `1.0.1` - исправления ошибок
- `1.1.0` - новая функциональность
- `2.0.0` - несовместимые изменения

### Тестирование перед публикацией

Рекомендуется сначала протестировать на TestPyPI:

```bash
# Загрузите на TestPyPI
twine upload --repository testpypi dist/*

# Протестируйте установку
pip install --index-url https://test.pypi.org/simple/ zerotrue-sdk
```

## После публикации

Пакет будет доступен через:

```bash
pip install zerotrue-sdk
```

И использование:

```python
from zerotrue import ZeroTrue

client = ZeroTrue(api_key="your_key")
```

## Проверка статуса

- PyPI: https://pypi.org/project/zerotrue-sdk/
- GitHub Actions: Actions → Publish to PyPI
- Релизы: Releases в репозитории

## Troubleshooting

### Ошибка: "Package already exists"
- Увеличьте версию в `pyproject.toml`
- PyPI не позволяет перезаписывать существующие версии

### Ошибка: "Invalid API token"
- Проверьте правильность токена в GitHub Secrets
- Убедитесь, что токен имеет права на публикацию

### Ошибка: "Build failed"
- Проверьте логи GitHub Actions
- Убедитесь, что все зависимости указаны в `pyproject.toml`

