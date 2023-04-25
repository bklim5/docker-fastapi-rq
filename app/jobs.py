import time
import random

# a dictionary of dishes and its corresponding emoji
dishes = {
    'pizza': '🍕',
    'pasta': '🍝',
    'salad': '🥗',
    'milkshake': '🥤',
    'coke': '🥤',
}

def process_order(dish_name: str):
    """A function that takes a dish name, "cook" it with randomized timing
       and return the dish emoji with the time it took to prepare

    Args:
        dish_name (str): name of the dish/drink

    Returns:
        if the dish_name is not in the dishes dictionary, return a string response with the sorry message
        if the dish_name is in the dishes dictionary, return a string response with the dish emoji and the time it took to cook
    """
    time_lapsed = random.randint(1, 10)
    time.sleep(time_lapsed)
    cooked_dish = dishes.get(dish_name)
    if not cooked_dish:
        return 'Sorry, after checking with the kitchen we do not have that dish today'

    return f'Your {cooked_dish} is ready! It took {time_lapsed}s'