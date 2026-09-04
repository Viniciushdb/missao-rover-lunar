"""Inicializacao dos sistemas do Rover Lunar."""


def inicializar_sistemas() -> dict:
    """Liga os sistemas essenciais e devolve o status de cada um."""
    sistemas = {
        "energia": "online",
        "comunicacao": "online",
        "navegacao": "online",
        "sensores": "online",
    }
    print("Rover Lunar: sistemas inicializados.")
    for nome, status in sistemas.items():
        print(f"  - {nome}: {status}")
    return sistemas


def main() -> None:
    inicializar_sistemas()


if __name__ == "__main__":
    main()
