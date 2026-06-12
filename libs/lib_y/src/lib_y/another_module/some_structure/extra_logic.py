import tomllib

def load_config(file_path):
    """Loads a TOML configuration file and returns its contents as a dictionary."""
    with open(file_path, "rb") as f:
        config = tomllib.load(f)
    return config