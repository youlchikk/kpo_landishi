#pragma once

#include <vector>
#include <string>
#include "FlowerClass.h"
#include <iostream>

class BouquetClass
{
public:
	std::string name;
	double massBouquet;
	double price;


private:
	std::string buyer_name;
	std::vector <FlowerClass*> flowers_Bouquet;


public:
	BouquetClass(std::string name_Bouquet, std::string buyer, std::vector<FlowerClass*> flowers);
	double MinimumFlower();
	double MaximumFlower();
	double getMassBouquet();
	double getPriceBouquet();
};

