def validate_name(name: str) -> bool:
    if not name or len(name.strip()) == 0:
        return False
    return True