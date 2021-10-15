#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program calculates the area of a triangle


def calculate_area(base_from_user, height_from_user):
    # calculate area

    # process & output
    try:
        base = int(base_from_user)
        height = int(height_from_user)
        area = height * base / 2
        print("The area of the triangle is {0} cm².".format(area))
    except (Exception):
        print("Invalid input.")
    finally:
        print("\nDone.")


def main():
    # this function gets base and height

    # input
    base_from_user = input("Enter the base length of a triangle (cm): ")
    height_from_user = input("Enter the height of a triangle (cm): ")
    print("")

    # call functions
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
