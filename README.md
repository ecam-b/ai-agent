
# Proyecto Selenium POM con Pytest

Este proyecto implementa automatización de pruebas web usando Selenium, Pytest y el patrón Page Object Model (POM).

## Estructura

```
AIAgentMCP/
│   requirements.txt
│   README.md
│   conftest.py
│   pytest.ini
│
├───pages/
│       base_page.py
│       login_page.py
│       signup_page.py
│
└───tests/
        test_login.py
        test_signup.py
```

## Instalación

1. Crea y activa un entorno virtual (opcional pero recomendado):
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```

## Ejecución de tests

Para ejecutar todos los tests:
```powershell
pytest
```
Para ejecutar solo los tests marcados como `signup` (registro y login):
```powershell
pytest -m signup
```

## Escenarios automatizados

- Registro de usuario, validación de login y eliminación de cuenta.
- Login de usuario existente y eliminación de cuenta.

Todos los flujos usan localizadores robustos y métodos reutilizables en las pages.
