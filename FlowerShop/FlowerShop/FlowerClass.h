#pragma once

#include <string>
#include <iostream>

class FlowerClass
{
public:
	std::string name;
	double price;
	double mass;

protected:
	int quantity;


public:
	FlowerClass(std::string name, double price_flower, double mass_flower, int quantity_flower);
	double getPriceFlower();
	double getMassFlower();
	bool checkQuantity();
};

