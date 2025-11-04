# Руководство по публикации в PyPI

## Подготовка к публикации

### 1. Регистрация на PyPI

1. Создайте аккаунт на [PyPI](https://pypi.org/account/register/)
2. Создайте аккаунт на [TestPyPI](https://test.pypi.org/account/register/) для тестирования

### 2. Настройка учетных данных

#### Для локальной публикации (старый способ):

```bash
# Создайте файл ~/.pypirc
[pypi]
username = __token__
password = pypi-xxxxxxxxxxxxx

[testpypi]
username = __token__
password = pypi-xxxxxxxxxxxxx
```

Или используйте переменные окружения:
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxxxxxxxxxxxx
```

#### Для автоматической публикации через GitHub Actions:

1. Перейдите в Settings → Secrets and variables → Actions
2. Добавьте новый секрет:
   - Name: `PYPI_API_TOKEN`
   - Value: ваш API токен из PyPI (начинается с `pypi-`)

### 3. Тестирование на TestPyPI

```bash
# Соберите пакет
python -m build

# Загрузите на TestPyPI
twine upload --repository testpypi dist/*

# Протестируйте установку
pip install --index-url https://test.pypi.org/simple/ zerotrue-sdk
```

## Публикация

### Способ 1: Автоматическая публикация через GitHub Releases

1. Обновите версию в `pyproject.toml`:
   ```toml
   version = "1.0.1"
   ```

2. Создайте коммит и тег:
   ```bash
   git add pyproject.toml
   git commit -m "chore: bump version to 1.0.1"
   git tag v1.0.1
   git push origin main --tags
   ```

3. Создайте релиз на GitHub:
   - Перейдите в Releases → Draft a new release
   - Выберите тег `v1.0.1`
   - Заполните описание релиза
   - Нажмите "Publish release"

4. GitHub Actions автоматически опубликует пакет в PyPI

### Способ 2: Ручная публикация

```bash
# Убедитесь, что у вас установлены инструменты
pip install build twine

# Очистите старые сборки
rm -rf dist/ build/ *.egg-info

# Соберите пакет
python -m build

# Проверьте пакет
twine check dist/*

# Загрузите на PyPI
twine upload dist/*
```

## Проверка после публикации

```bash
# Установите пакет из PyPI
pip install zerotrue-sdk

# Проверьте, что все работает
python -c "from zerotrue import ZeroTrue; print('OK')"
```

## Обновление версии

Используйте семантическое версионирование (SemVer):
- `MAJOR.MINOR.PATCH` (например, `1.0.0`)
- MAJOR - несовместимые изменения API
- MINOR - новая функциональность с обратной совместимостью
- PATCH - исправления ошибок с обратной совместимостью

## Полезные команды

```bash
# Просмотр информации о пакете
pip show zerotrue-sdk

# Обновление пакета
pip install --upgrade zerotrue-sdk

# Удаление пакета
pip uninstall zerotrue-sdk
```

