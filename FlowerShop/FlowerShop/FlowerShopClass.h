#pragma once

#include <string>
#include <vector>
#include <iostream>
#include "FlowerClass.h"

class FlowerShopClass
{
public:
	std::string name;
	std::vector <FlowerClass*> flowers;

private:
	double stars;

public:
	FlowerShopClass(std::string name, double stars);
	void Add_Flower(FlowerClass* flower);
	void Print_Flower();
	std::vector <FlowerClass*> Array_of_flowers_creat(std::vector <int> numbers);
};

