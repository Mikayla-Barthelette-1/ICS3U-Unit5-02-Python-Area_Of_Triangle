#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program calculates the area of a triangle


def calculate_area(base, height):
    # calculate area

    # process

    area = height * base / 2
    print("The area of the triangle is {0} cm².".format(area))


def main():
    # this function gets base and height

    # input
    base_from_user = input("Enter the base length of a triangle (cm): ")
    height_from_user = input("Enter the height of a triangle (cm): ")
    print("")

    try:
        base = int(base_from_user)
        height = int(height_from_user)
    except (Exception):
        print("Invalid input.")
    finally:
        None

    # call functions
    calculate_area(base, height)
    print("\nDone.")


if __name__ == "__main__":
    main()
