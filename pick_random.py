import argparse
import random

already_done_books = []
already_done_movies = []

# Lists are formed by calling range() on the values of each list.
book_lists = {"NYT21st": ((100,), "https://www.nytimes.com/interactive/2025/movies/best-movies-21st-century.html"),
              "booker": ((1969, 2025), "https://en.wikipedia.org/wiki/Booker_Prize#Winners"),
              "booker-international": ((2005, 2024, 2), "https://en.wikipedia.org/wiki/International_Booker_Prize"),
              "national-book-award": ((1965, 2024), "https://en.wikipedia.org/wiki/National_Book_Award_for_Fiction#Honorees,_general_fiction")
              }

# There are 1256 movies in criterion, but so it' more balanced if we
# pick a random stream of 100 of them
criterion_start = random.randint(0, 1206)
movie_lists = {"bfi": ((100,), "https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time"), 
               "criterion": ((criterion_start, criterion_start + 100), "https://www.criterion.com/shop/browse/list?sort=spine_number&direction=asc"),
               "variety": ((100,), "https://variety.com/lists/best-movies-of-all-time/"),
               "NYT_movies21": ((100,), "https://www.nytimes.com/interactive/2025/movies/best-movies-21st-century.html")
               }

def pick_random(media_type, number):
    if media_type == "book":
        lists = book_lists
    elif media_type == "movie":
        lists = movie_lists

    full_list = []
    for list_name, (numbers, link) in lists.items():
        full_list.extend([f"{list_name}-{i}" for i in range(*numbers)])
    choices = random.choices(full_list, k=number)
    return choices


def links_list(media_type):
    link_lines = []
    if media_type == "book":
        lists = book_lists
    elif media_type == "movie":
        lists = movie_lists

    for list_name, (numbers, link) in lists.items():
        link_lines.append(f'{list_name}: \033]8;;{link}\033\\{link}\033]8;;\033\\')
    return link_lines

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
    print("\n".join(links_list(args.media)))
    print("\n"*4)


if __name__ == "__main__":
    main()
