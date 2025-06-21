# Estructura del proyecto Selenium con POM y Pytest

```
AIAgentMCP/
│   requirements.txt
│   README.md
│   conftest.py
│
├───pages/
│       google_page.py
│
└───tests/
        test_google.py
```

- Usa un entorno virtual (venv) para aislar dependencias.
- Estructura POM: las páginas están en `pages/` y los tests en `tests/`.
- Ejecuta los tests con:
  ```powershell
  .venv\Scripts\pytest.exe
  ```
- Instala dependencias con:
  ```powershell
  .venv\Scripts\pip.exe install -r requirements.txt
  ```
