#### Computational Numerical Methods

Assignments, exercises, and other materials related to the Computational Numerical Methods.

# Python Project Setup

This guide explains how to initialize the project environment and run the notebooks.

---

# 1. Install UV

This project uses **uv** for dependency and environment management.

Install uv:

### Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

---

# 2. Initialize the Project

Clone the repository and enter the project folder:

```bash
git clone <repository-url>
cd <project-folder>
```

Initialize the environment:

```bash
uv venv
```

---

# 3. Activate the Virtual Environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

# 4. Install Dependencies

Install project dependencies:

```bash
uv sync
```

If the project is being created from scratch, install the required packages:

```bash
uv add notebook ipykernel
```

---

# 5. Register the Jupyter Kernel

Register the virtual environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name project-env
```

---

# 6. Running Jupyter

Start Jupyter Notebook:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

---

# 7. Using the Project in VSCode

Open the project folder in VSCode.

1. Install the **Python** and **Jupyter** extensions.
2. Open a `.ipynb` file.
3. Click **Select Kernel** in the top-right corner.
4. Choose the environment:

```
.venv (project-env)
```

---

# Project Structure

Suggested project structure:

```
project/
│
├── .venv/
├── pyproject.toml
├── notebooks/
│   └── example.ipynb
├── src/
└── README.md
```

---

# Quick Start

```bash
uv venv
source .venv/bin/activate
uv sync
jupyter notebook
```

---

# Troubleshooting

If the kernel does not appear in Jupyter or VSCode:

```bash
uv add ipykernel
python -m ipykernel install --user --name project-env
```

Then restart Jupyter or VSCode.
