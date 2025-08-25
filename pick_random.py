import argparse
import random

already_done_books = []
already_done_movies = []

# Lists are formed by calling range() on the values of each list.
book_lists = {"NYT21st": (100,),
              "booker": (1969, 2025),
              "booker-international": (2005, 2024, 2),
              "national-book-award": (1965, 2024)}

# There are 1256 movies in criterion, but so it' more balanced if we
# pick a random stream of 100 of them
criterion_start = random.randint(0, 1156)
movie_lists = {"bfi": (100,), 
               "criterion": (criterion_start, criterion_start + 100),
               "variety": (100,),
               "NYT_movies21": (100,)}

def pick_random(media_type, number):
    if media_type == "book":
        lists = book_lists
        done_list = already_done_books
    elif media_type == "movie":
        lists = movie_lists
        done_list = already_done_movies

    full_list = []
    for list_name, numbers in lists.items():
        full_list.extend([f"{list_name}-{i}" for i in range(*numbers)])
    for done_thing in done_list:
        if done_thing in full_list:
            full_list.remove(done_thing)
    choices = random.choices(full_list, k=number)
    return choices


def main():
    parser = argparse.ArgumentParser(description='Pick next book club!')
    parser.add_argument("--media", choices = ["book", "movie"], required=True)
    parser.add_argument("--how-many", type=int, required=True)
    args = parser.parse_args()

    choices = pick_random(args.media, args.how_many)

    print("\n"*1)
    print(f"The {args.media} selections are....")
    print("\n"*1)
    print("\n".join(choices))
    print("\n".join(["!"*(i*3) for i in range(5)]))
    print("\n"*3)

if __name__ == "__main__":
    main()
