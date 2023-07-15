/* returns an incorrect value :( */

#include <iostream>
#include <string>
#include <list>
#include <cmath>

std::list <double> data = {};

double maths(std::string size) {
    double total = 0.0;
    double mean = 0.0;
    for (double i : data) {
        mean += i;
    }
    mean /= data.size();
    std::cout << "mean = ";
    std::cout << mean << "\n";
    for (double i : data) { /* this the error i tihnk coz mean works as intended and produces desired outcome (tested with dataset [1,2,3,4,5,6,7,8,9,10] on an online mean calculator and python code i wrote)*/
        std::cout << "item = " << i << "\n";
        i -= mean;
        std::cout << "i - mean = ";
        std::cout << i << "\n";
        i = pow(i, 2);
        std::cout << "(i - mean) ^ 2 = ";
        std::cout << i << "\n";
        total += i;
    }
    if (size == "sample") {
        return sqrt(total / data.size());
    }
    else {
        return sqrt(total / data.size() -1);
    }
}

void setup() {
    std::string input;
    while (input != "end") {
        std::cout << "\ninput a value ";
        std::cin >> input;
        if (input == "end") {
            std::cout << "\ndata development process ended";
            while (input != "sample" && input != "population") {
                std::cout << "\nis this a sample or a population? ";
                std::cin >> input;
                if (input == "sample") {
                    std::cout << "\n" << maths("sample");
                }
                else if (input == "population") {
                    std::cout << "\n" << maths("population");
                }
                else {
                    std::cout << "\ninvalid response";
                }
            }
        }
        else {
            try {
                data.push_back(std::stof(input));
            }
            catch (...) {
                std::cout << "\ninvalid input";
            }
        }
    }
}

int main() {
    std::string input;
    std::cout << "welcome, please remember that this is a WIP and returns an incorrect value";
    while (input != "yes") {
        std::cout << "\ndo you wish to start ";
        std::cin >> input;
        if (input == "yes") {
            std::cout << "\nstarting...";
            setup();
            return 0;
        }
        else if (input == "no") {
            std::cout << "\nok... why?\nending program...";
            return 1;
        }
        else {
            std::cout << "\ninvalid response";
        }
    }
}
