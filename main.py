from src.utils.validate import validate_name

def main():
    name = "Nafistha"
    if validate_name(name):
        print(f"Nama valid: {name}")
    else:
        print("Nama tidak boleh kosong!")

if __name__ == "__main__":
    main()