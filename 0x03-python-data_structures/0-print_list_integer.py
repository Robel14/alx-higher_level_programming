#!/bin/bash

print_list_integer() {
    for num in "${@}"; do
        printf "%d\n" "${num}"
    done
}

# Example usage:
my_list=(1 2 3 4 5)
print_list_integer "${my_list[@]}"
