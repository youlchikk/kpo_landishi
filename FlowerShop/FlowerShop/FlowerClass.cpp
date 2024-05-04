#include "FlowerClass.h"

FlowerClass::FlowerClass(std::string name_new = "flower", double price_flower = 1, double mass_flower = 0.1, int quantity_flower = 10) {
	name = name_new;
	price = price_flower;
	mass = mass_flower;
	quantity = quantity_flower;
	std::cout << "Создан цветок " << name << " стоимостью " << price << " и массой " << mass << std::endl;
}

double FlowerClass::getPriceFlower() {
	return price;
}

double FlowerClass::getMassFlower() {
	return mass;
}

bool FlowerClass::checkQuantity() {
	return (quantity != 0);
}