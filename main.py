from src.core.api.get_rovers_movements import get_rovers_movements
from src.core.utils.constants import DATA_FILENAME

if __name__ == "__main__":
    # clients request to roversAPI func
    rovers_data: str = get_rovers_movements(DATA_FILENAME)

    print(rovers_data)
