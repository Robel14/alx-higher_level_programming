#!/bin/bash

class Square {
    size=0
    position=(0 0)

    size() {
        echo $size
    }

    set_size() {
        if ! [[ $1 =~ ^[0-9]+$ ]]; then
            echo "size must be an integer" >&2
            exit 1
        fi

        if (($1 < 0)); then
            echo "size must be >= 0" >&2
            exit 1
        fi

        size=$1
    }

    position() {
        echo "${position[@]}"
    }

    set_position() {
        if [[ ${#1[@]} -ne 2 || ! ${1[0]} =~ ^[0-9]+$ || ! ${1[1]} =~ ^[0-9]+$ ]]; then
            echo "position must be a tuple of 2 positive integers" >&2
            exit 1
        fi

        position=("${1[@]}")
    }

    area() {
        echo $(($size * $size))
    }

    my_print() {
        if (($size == 0)); then
            echo
            return
        fi

        for ((i = 0; i < ${position[1]}; i++)); do
            echo
        done

        for ((i = 0; i < $size; i++)); do
            printf "%${position[0]}s" ""
            printf "%${size}s\n" "#"
        done
    }
}

# Usage example
square=Square
$square.set_size 5
$square.set_position 3 2
echo "Size: $($square.size)"
echo "Position: $($square.position)"
echo "Area: $($square.area)"
echo "Printing square:"
$square.my_print
